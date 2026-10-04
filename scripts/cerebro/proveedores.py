"""
Adaptadores de IA: cada proveedor sabe hablar con su API y nada más.

Para añadir una IA nueva:
- Si su API es compatible con OpenAI (Groq, OpenRouter, Mistral, Cerebras... casi todas),
  NO hay que tocar código: se añade en config/ias.json con "tipo": "openai" y su URL.
- Si no lo es, se añade aquí una clase nueva con el método _llamar() y se registra en TIPOS.
"""

import json
import os
import time
import urllib.error
import urllib.request

ESPERAS = [0, 30, 90]  # segundos antes de cada intento con el mismo modelo


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

    def modelos(self) -> list[str]:
        return list(self.cfg.get("modelos", []))

    def _llamar(self, modelo: str, sistema: str, mensaje: str) -> str:
        raise NotImplementedError

    def pedir(self, sistema: str, mensaje: str) -> tuple[str, str]:
        """Prueba cada modelo con reintentos. Devuelve (texto, modelo que respondió)."""
        for modelo in self.modelos():
            for intento, espera in enumerate(ESPERAS, start=1):
                if espera:
                    print(f"  Esperando {espera}s...")
                    time.sleep(espera)
                print(f"[{self.nombre}] {modelo} · intento {intento}/{len(ESPERAS)}")
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

        if not hasattr(self, "_cliente"):
            self._cliente = genai.Client(api_key=self.clave)
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

    def _http(self, metodo: str, ruta: str, cuerpo: dict | None = None) -> dict:
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
        with urllib.request.urlopen(peticion, timeout=300) as r:
            return json.loads(r.read().decode("utf-8"))

    def _llamar(self, modelo, sistema, mensaje):
        try:
            datos = self._http("POST", "/chat/completions", {
                "model": modelo,
                "temperature": 0.4,
                "messages": [
                    {"role": "system", "content": sistema},
                    {"role": "user", "content": mensaje},
                ],
            })
        except urllib.error.HTTPError as e:
            detalle = e.read().decode("utf-8", errors="replace")[:300]
            if e.code in (400, 402, 404, 413, 429):
                raise SaltarModelo(f"{e.code} {detalle}")
            if e.code >= 500:
                raise Saturado(f"{e.code} {detalle}")
            raise RuntimeError(f"{self.nombre} respondió {e.code}: {detalle}")
        except (urllib.error.URLError, TimeoutError) as e:
            raise Saturado(str(e))

        if "error" in datos:  # algunos proveedores devuelven 200 con un error dentro
            raise Saturado(str(datos["error"])[:300])
        try:
            return datos["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            raise SaltarModelo(f"Respuesta con formato inesperado: {str(datos)[:200]}")


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
        except SaltarModelo as e:
            print(f"[{nombre}] {e}")
    raise RuntimeError(f"Ninguna IA ha podido hacer de {rol}. Se reintentará en la próxima ejecución.")
