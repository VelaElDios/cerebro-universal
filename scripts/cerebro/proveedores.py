"""
Adaptadores de IA: cada proveedor sabe hablar con su API y nada más.

Para añadir una IA nueva:
- Si su API es compatible con OpenAI (OpenRouter, NVIDIA NIM, Groq... casi todas),
  NO hay que tocar código: se añade en config/ias.json con "tipo": "openai" y su URL.
- Opciones por proveedor en config/ias.json:
    "max_tokens": tope de lo que puede escribir la IA (algunas APIs cortan pronto si no se dice)
    "tiempo_max": segundos de espera por respuesta (por defecto 180; los modelos grandes tardan más)
    "esperas": segundos antes de cada intento con el mismo modelo (por defecto [0, 30, 90])
    "extra": campos que se añaden tal cual a la petición (opciones propias de cada API)
    "stream": true → la respuesta llega a trozos. Con mensajes muy largos algunas APIs (NVIDIA) cortan
              la conexión si tardan minutos en contestar de golpe; a trozos, la conexión no se queda parada
- Si no lo es, se añade aquí una clase nueva con el método _llamar() y se registra en TIPOS.
"""

import http.client
import json
import os
import time
import urllib.error
import urllib.request

ESPERAS = [0, 30, 90]  # segundos antes de cada intento con el mismo modelo
TIEMPO_MAX_RESPUESTA = 180  # segundos máximos esperando a que una IA conteste (si no, se salta el modelo)

# Hora límite (time.monotonic) para todo el paso. La pone proyecto.py con fijar_limite().
# Así ninguna llamada ni espera se pasa del tiempo que GitHub Actions deja al job.
_LIMITE = None


def fijar_limite(segundos_desde_ahora: float):
    global _LIMITE
    _LIMITE = time.monotonic() + segundos_desde_ahora


def tiempo_restante() -> float:
    return float("inf") if _LIMITE is None else _LIMITE - time.monotonic()


class TiempoAgotado(Exception):
    """Se acaba el tiempo del paso: no se empieza ninguna llamada ni espera más."""


class Saturado(Exception):
    """El servidor está ocupado: merece la pena esperar y reintentar el mismo modelo."""


class SaltarModelo(Exception):
    """Modelo inexistente, sin cupo o petición demasiado grande: pasar al siguiente."""


class Proveedor:
    def __init__(self, nombre: str, cfg: dict):
        self.nombre = nombre
        self.cfg = cfg
        self.clave = os.environ.get(cfg["clave_env"], "").strip()

    @property
    def disponible(self) -> bool:
        return bool(self.clave)

    @property
    def tiempo_max(self) -> float:
        """Lo que se espera a una respuesta: el del proveedor, pero nunca más de lo que queda de paso."""
        return max(30, min(self.cfg.get("tiempo_max", TIEMPO_MAX_RESPUESTA), tiempo_restante() - 30))

    def modelos(self) -> list[str]:
        return list(self.cfg.get("modelos", []))

    def _llamar(self, modelo: str, sistema: str, mensaje: str) -> str:
        raise NotImplementedError

    def pedir(self, sistema: str, mensaje: str) -> tuple[str, str]:
        """Prueba cada modelo con reintentos. Devuelve (texto, modelo que respondió)."""
        esperas = self.cfg.get("esperas", ESPERAS)   # p. ej. [0, 20]: menos espera con un 503
        for modelo in self.modelos():
            for intento, espera in enumerate(esperas, start=1):
                # Hace falta tiempo para la espera y para una respuesta completa
                if tiempo_restante() < espera + 60:
                    raise TiempoAgotado(f"Sin tiempo para llamar a {self.nombre} ({modelo})")
                if espera:
                    print(f"  Esperando {espera}s...")
                    time.sleep(espera)
                print(f"[{self.nombre}] {modelo} · intento {intento}/{len(esperas)}")
                try:
                    texto = self._llamar(modelo, sistema, mensaje)
                    if texto and texto.strip():
                        return texto, modelo
                    print("  Respuesta vacía")
                except Saturado as e:
                    print(f"  Ocupado: {e}")
                except SaltarModelo as e:
                    print(f"  {e} → paso al siguiente modelo")
                    break
        raise SaltarModelo(f"Ningún modelo de {self.nombre} ha respondido")


class Gemini(Proveedor):
    def _llamar(self, modelo, sistema, mensaje):
        from google import genai
        from google.genai import errors, types

        espera = int(self.tiempo_max)
        if getattr(self, "_espera_cliente", None) != espera:
            # Sin timeout, una llamada colgada esperaba para siempre (pasó: 26 min parada)
            self._cliente = genai.Client(api_key=self.clave,
                                         http_options=types.HttpOptions(timeout=espera * 1000))
            self._espera_cliente = espera
        try:
            r = self._cliente.models.generate_content(
                model=modelo,
                contents=mensaje,
                config=types.GenerateContentConfig(
                    system_instruction=sistema,
                    temperature=0.4,
                    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
                ),
            )
            return r.text
        except errors.ServerError as e:
            raise Saturado(f"{e.code} {e.message}")
        except errors.ClientError as e:
            if e.code in (400, 404, 429):
                raise SaltarModelo(f"{e.code} {e.message}")
            raise  # 401/403: key mal puesta, no tiene sentido reintentar
        except Exception as e:
            # Timeout (httpx.ReadTimeout...) o conexión cortada: este modelo no contesta, al siguiente
            if "timeout" in type(e).__name__.lower() or "timeout" in str(e).lower():
                raise SaltarModelo(f"no contestó en {espera}s")
            raise


class CompatibleOpenAI(Proveedor):
    """Cualquier API con el formato de OpenAI: /models y /chat/completions."""

    def modelos(self):
        lista = super().modelos()
        if self.cfg.get("autodescubrir_gratis") and self.disponible:
            lista += [m for m in self._modelos_gratis() if m not in lista]
        return lista

    def _modelos_gratis(self) -> list[str]:
        """Los modelos gratis cambian a menudo: los pedimos a la API en cada ejecución."""
        try:
            datos = self._http("GET", "/models")
        except Exception as e:
            print(f"  No pude listar modelos de {self.nombre}: {e}")
            return []
        gratis = [m for m in datos.get("data", []) if str(m.get("id", "")).endswith(":free")]
        gratis.sort(key=lambda m: m.get("context_length") or 0, reverse=True)
        elegidos = [m["id"] for m in gratis[: self.cfg.get("max_autodescubiertos", 4)]]
        print(f"  Modelos gratis encontrados en {self.nombre}: {elegidos}")
        return elegidos

    def _http(self, metodo: str, ruta: str, cuerpo: dict | None = None, espera: float = 60) -> dict:
        peticion = urllib.request.Request(
            self.cfg["url"].rstrip("/") + ruta,
            method=metodo,
            data=json.dumps(cuerpo).encode() if cuerpo is not None else None,
            headers={
                "Authorization": f"Bearer {self.clave}",
                "Content-Type": "application/json",
                "X-Title": "cerebro-universal",
            },
        )
        with urllib.request.urlopen(peticion, timeout=espera) as r:
            return json.loads(r.read().decode("utf-8"))

    def _llamar(self, modelo, sistema, mensaje):
        cuerpo = {
            "model": modelo,
            "temperature": 0.4,
            "messages": [
                {"role": "system", "content": sistema},
                {"role": "user", "content": mensaje},
            ],
        }
        if self.cfg.get("max_tokens"):
            cuerpo["max_tokens"] = self.cfg["max_tokens"]
        cuerpo.update(self.cfg.get("extra", {}))
        espera = self.tiempo_max
        try:
            if self.cfg.get("stream"):
                return self._llamar_a_trozos(cuerpo, espera)
            datos = self._http("POST", "/chat/completions", cuerpo, espera=espera)
        except urllib.error.HTTPError as e:
            detalle = e.read().decode("utf-8", errors="replace")[:300]
            # 403 aquí suele ser "este modelo tiene restricciones", no "tu key está mal" (eso es 401)
            if e.code in (400, 402, 403, 404, 413, 429):
                raise SaltarModelo(f"{e.code} {detalle}")
            if e.code >= 500:
                raise Saturado(f"{e.code} {detalle}")
            raise RuntimeError(f"{self.nombre} respondió {e.code}: {detalle}")
        except TimeoutError:
            raise SaltarModelo(f"no contestó en {espera:.0f}s")
        except urllib.error.URLError as e:
            if "timed out" in str(e).lower():
                raise SaltarModelo(f"no contestó en {espera:.0f}s")
            raise Saturado(str(e))
        except (http.client.HTTPException, ConnectionError, OSError) as e:
            # «Remote end closed connection without response»: la API cortó (pasa con NVIDIA y mensajes
            # muy largos). Se salta este modelo, no el proveedor entero.
            raise SaltarModelo(f"la conexión se cortó: {type(e).__name__}: {e}")

        if "error" in datos:  # algunos proveedores devuelven 200 con un error dentro
            raise Saturado(str(datos["error"])[:300])
        try:
            eleccion = datos["choices"][0]
            texto = eleccion["message"]["content"]
        except (KeyError, IndexError, TypeError):
            raise SaltarModelo(f"Respuesta con formato inesperado: {str(datos)[:200]}")
        if eleccion.get("finish_reason") == "length":
            # Se quedó sin espacio para escribir: un archivo cortado a medias rompe el proyecto
            raise SaltarModelo("la respuesta se cortó por max_tokens (sube max_tokens en config/ias.json)")
        return texto


    def _llamar_a_trozos(self, cuerpo: dict, espera: float) -> str:
        """Petición con "stream": la respuesta llega en eventos «data: {...}» (formato SSE de OpenAI)."""
        cuerpo = {**cuerpo, "stream": True}
        peticion = urllib.request.Request(
            self.cfg["url"].rstrip("/") + "/chat/completions",
            method="POST",
            data=json.dumps(cuerpo).encode(),
            headers={
                "Authorization": f"Bearer {self.clave}",
                "Content-Type": "application/json",
                "Accept": "text/event-stream",
                "X-Title": "cerebro-universal",
            },
        )
        limite = time.monotonic() + espera
        partes, fin = [], None
        with urllib.request.urlopen(peticion, timeout=espera) as r:
            for linea in r:
                if time.monotonic() > limite:
                    raise SaltarModelo(f"no terminó de contestar en {espera:.0f}s")
                linea = linea.decode("utf-8", errors="replace").strip()
                if not linea.startswith("data:"):
                    continue   # líneas vacías y comentarios «: keep-alive»
                dato = linea[5:].strip()
                if dato == "[DONE]":
                    break
                try:
                    evento = json.loads(dato)
                except ValueError:
                    continue
                if "error" in evento:
                    raise Saturado(str(evento["error"])[:300])
                for eleccion in evento.get("choices") or []:
                    trozo = (eleccion.get("delta") or {}).get("content")
                    if trozo:
                        partes.append(trozo)
                    if eleccion.get("finish_reason"):
                        fin = eleccion["finish_reason"]
        if fin == "length":
            raise SaltarModelo("la respuesta se cortó por max_tokens (sube max_tokens en config/ias.json)")
        return "".join(partes)


TIPOS = {"gemini": Gemini, "openai": CompatibleOpenAI}


def cargar(ruta_config) -> tuple[dict, dict]:
    """Lee config/ias.json y crea un adaptador por proveedor."""
    config = json.loads(ruta_config.read_text(encoding="utf-8"))
    proveedores = {
        nombre: TIPOS[cfg["tipo"]](nombre, cfg)
        for nombre, cfg in config["proveedores"].items()
    }
    return config, proveedores


def pedir_rol(rol: str, config: dict, proveedores: dict, sistema: str, mensaje: str) -> tuple[str, str, str]:
    """Pide al primer proveedor disponible del rol. Devuelve (texto, proveedor, modelo)."""
    for nombre in config["roles"][rol]:
        p = proveedores[nombre]
        if not p.disponible:
            print(f"[{nombre}] sin key configurada, lo salto")
            continue
        try:
            texto, modelo = p.pedir(sistema, mensaje)
            return texto, nombre, modelo
        except TiempoAgotado:
            raise  # no tiene sentido probar otro proveedor: se acabó el tiempo del paso
        except SaltarModelo as e:
            print(f"[{nombre}] {e}")
        except Exception as e:  # cualquier otro fallo de este proveedor: probar el siguiente
            print(f"[{nombre}] Error inesperado, paso al siguiente proveedor: {e}")
    raise RuntimeError(f"Ninguna IA ha podido hacer de {rol}. Se reintentará en la próxima ejecución.")
