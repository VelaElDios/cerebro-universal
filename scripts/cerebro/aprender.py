"""
Aprender: el cerebro lee documentos (temarios, documentación de los proyectos...) y guarda lo que saca de
ellos como conocimiento (ver conocimiento.py), con una cita literal de cada cosa para no inventar.

Un proyecto de tipo "aprender" (proyectos/aprendizaje/proyecto.json):

  "tipo": "aprender",
  "cada_horas": 4,                        no se ejecuta más a menudo (deja paso a los demás proyectos)
  "repos": {"saas": "https://github.com/...",
            "datos": {"url": "https://github.com/VelaElDios/cerebro-datos", "token_env": "DATOS_TOKEN",
                      "opcional": true}},  repo privado: los temarios no se suben al vault público
  "aprender_de": [
      {"entrada": "repo:saas/docs/documentacion-tecnica.md", "temas": ["saas"], "proyecto": "memoria-procesos"},
      {"entrada": "repo:datos/temarios/**/*", "temas": []}
  ]

Cada archivo se trocea (unos 14.000 caracteres por trozo) y una IA saca de cada trozo las notas útiles.
procesados.json recuerda qué trozos de qué archivo (por su huella md5) están hechos: si el archivo
cambia, se vuelve a aprender. Al acabar un archivo se crea su nota de «fuente», que enlaza todo lo sacado.
"""

import hashlib
import json
import os
import re
from pathlib import Path

from . import conocimiento, dataset, mapas, medios, nucleo, repos
from . import proveedores as prov

TROZO = 14_000
MIN_PARA_TROZO = 5 * 60

SISTEMA = """Eres el APRENDIZ de "Cerebro Universal", la memoria compartida de varias IAs. Lees un trozo de un
documento y guardas lo que otra IA necesitaría saber en el futuro para trabajar sin volver a leerlo:
conceptos, recetas (cómo se hace algo, con su código), decisiones (qué se eligió y por qué) y datos
concretos (cifras, fechas, nombres).

Reglas:
- Cada nota es útil por sí sola: otra IA la lee sin el documento delante.
- Cada nota lleva una «cita» copiada LITERALMENTE del trozo (una frase entera). Sin cita literal, no vale.
- No inventes nada que no esté en el trozo. No hagas notas de relleno ni de cosas obvias.
- Si una nota ya existe en el MAPA DEL CEREBRO con el mismo título, usa ese título exacto: se ampliará.
- Enlaza en «relacionado» los títulos del mapa que tengan que ver.
- Entre 3 y 10 notas por trozo, según lo que dé de sí.

Responde EXACTAMENTE con estos bloques:

<<<RESUMEN>>>
2-4 frases: de qué trata este trozo.
""" + conocimiento.FORMATO


def _md5(ruta: Path) -> str:
    return hashlib.md5(ruta.read_bytes()).hexdigest()


def trocear(texto: str, tam: int = TROZO) -> list[str]:
    """Trozos de ~tam caracteres cortando por párrafos (o por líneas si un párrafo es enorme)."""
    parrafos = re.split(r"\n\s*\n", texto)
    trozos, actual = [], ""
    for p in parrafos:
        while len(p) > tam:
            corte = p.rfind("\n", 0, tam)
            corte = corte if corte > tam // 2 else tam
            if actual:
                trozos.append(actual)
                actual = ""
            trozos.append(p[:corte])
            p = p[corte:]
        if len(actual) + len(p) + 2 > tam and actual:
            trozos.append(actual)
            actual = ""
        actual += ("\n\n" if actual else "") + p
    if actual.strip():
        trozos.append(actual)
    return [t for t in trozos if t.strip()]


def preparar_repos(carpeta: Path, cfg: dict) -> list[str]:
    """Descarga los repos. Los opcionales (p. ej. el privado, si aún no hay token) se saltan sin error."""
    info, a_bajar, tokens = [], {}, []
    for nombre, dato in cfg.get("repos", {}).items():
        if isinstance(dato, dict) and dato.get("token_env"):
            token = os.environ.get(dato["token_env"])
            if not token:
                if dato.get("opcional"):
                    info.append(f"{nombre}: sin {dato['token_env']}, se salta")
                    continue
                raise RuntimeError(f"falta {dato['token_env']} para el repo {nombre}")
            tokens.append(token)
            dato = {**dato, "url": dato["url"].replace("https://", f"https://x-access-token:{token}@")}
        a_bajar[nombre] = dato
    try:
        info += repos.preparar(carpeta, {**cfg, "repos": a_bajar})
    except repos.RepoNoDisponible as e:
        mensaje = str(e)
        for t in tokens:
            mensaje = mensaje.replace(t, "***")
        raise RuntimeError(mensaje)
    return info


def _huella_texto(texto: str) -> str:
    return hashlib.md5(texto.encode("utf-8")).hexdigest()


def pendientes(carpeta: Path, cfg: dict, registro: dict) -> list[tuple[dict, str, Path | str, str, str]]:
    """[(regla, etiqueta, origen, huella, tipo)] de lo que queda por aprender: archivos de cualquier tipo
    y cada URL de los archivos de enlaces (enlaces*.txt, *.url)."""
    res = []

    def anadir(regla, etiqueta, origen, huella, tipo):
        r = registro.get(etiqueta)
        if r and r.get("md5") == huella and (r.get("hechos", 0) >= r.get("total", 1) or r.get("error_fijo")):
            return
        res.append((regla, etiqueta, origen, huella, tipo))

    for regla in cfg.get("aprender_de", []):
        for etiqueta, ruta in repos.resolver(carpeta, regla["entrada"]):
            if ruta.name.startswith(".") or ruta.name.lower() in ("leeme.md", "readme.md") and "temarios" in etiqueta:
                continue
            tipo = medios.tipo_de(ruta.name)
            if tipo == "enlaces":
                for url in medios.enlaces_de(ruta):
                    anadir(regla, url, url, _huella_texto(url), medios.tipo_de(url))
            elif tipo != "desconocido":
                anadir(regla, etiqueta, ruta, _md5(ruta), tipo)
    return res


def _clave_transcripcion(etiqueta: str) -> str:
    return "transcripciones/" + conocimiento.nombre_de(etiqueta)[:80] + ".md"


def leer(carpeta: Path, etiqueta: str, origen, tipo: str, huella: str) -> tuple[str, bool]:
    """Texto de cualquier cosa. Las transcripciones de una IA se guardan en el repo privado y se reutilizan."""
    cache = carpeta / repos.CARPETA_REPOS / "datos" / _clave_transcripcion(etiqueta)
    if cache.exists():
        texto = cache.read_text(encoding="utf-8")
        if f"huella: {huella}" in texto[:400]:
            return texto.split("\n---\n", 1)[-1], True
    texto, es_ia = medios.extraer(origen, tipo)
    if es_ia:
        dataset.adjuntar(_clave_transcripcion(etiqueta),
                         f"origen: {etiqueta}\nhuella: {huella}\ntipo: {tipo}\nfecha: {nucleo.ahora():%Y-%m-%d}\n---\n{texto}")
    return texto, es_ia


def ejecutar(carpeta: Path, cfg: dict, cfg_ruta: Path, bitacora: Path) -> str:
    """Aprende todo lo que pueda en el tiempo del paso. Devuelve un resumen."""
    config, proveedores = prov.cargar(nucleo.RAIZ / "config" / "ias.json")
    roles = config.get("roles", {})
    config = {**config, "roles": {**roles, "aprendiz": cfg.get("roles", {}).get("aprendiz")
                                  or roles.get("aprendiz") or roles.get("revisor", [])}}
    info = preparar_repos(carpeta, cfg)
    ruta_reg = carpeta / "procesados.json"
    registro = json.loads(ruta_reg.read_text(encoding="utf-8")) if ruta_reg.exists() else {}
    cola = pendientes(carpeta, cfg, registro)
    if not cola:
        return "Nada nuevo que aprender."

    hechas_total, trozos_total, apuntes = 0, 0, []
    for regla, etiqueta, origen, huella, tipo in cola:
        try:
            texto, es_ia = leer(carpeta, etiqueta, origen, tipo, huella)
        except medios.NoSePuede as e:
            registro[etiqueta] = {"md5": huella, "hechos": 0, "total": 1, "notas": [], "error": str(e)[:300],
                                  "error_fijo": "no sé leer" in str(e)}
            apuntes.append(f"- ⚠️ `{etiqueta}`: {str(e)[:200]}")
            ruta_reg.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
            continue
        except prov.TiempoAgotado as e:
            apuntes.append(f"- ⏳ `{etiqueta}`: {e}")
            break
        except Exception as e:   # una web caída, un archivo roto...: se reintenta la próxima vez
            apuntes.append(f"- ⚠️ `{etiqueta}`: no se pudo leer ({type(e).__name__}: {str(e)[:150]})")
            continue
        fuente_nota = f"{etiqueta} (transcripción de IA)" if es_ia else etiqueta
        trozos = trocear(texto)
        r = registro.get(etiqueta)
        if not r or r.get("md5") != huella:
            r = {"md5": huella, "hechos": 0, "total": len(trozos), "notas": []}
        temas = list(regla.get("temas", []))
        # En temarios/, la subcarpeta es el tema (temarios/redes/tema1.pdf → «redes»)
        m = re.search(r"temarios/([^/]+)/", str(etiqueta))
        if m and conocimiento.nombre_de(m.group(1)) not in temas:
            temas.append(conocimiento.nombre_de(m.group(1)))
        proyecto = regla.get("proyecto", "")
        while r["hechos"] < len(trozos):
            if prov.tiempo_restante() < MIN_PARA_TROZO:
                break
            i = r["hechos"]
            mensaje = (f"# DOCUMENTO\n{etiqueta} (trozo {i + 1} de {len(trozos)})\n\n"
                       f"# MAPA DEL CEREBRO (lo que ya se sabe, por temas)\n{conocimiento.mapa_textual()}\n\n"
                       f"# TEMAS SUGERIDOS\n{', '.join(temas) or '(elígelos tú)'}\n\n"
                       f"# TROZO\n{trozos[i]}")
            try:
                respuesta, ia, modelo = prov.pedir_rol("aprendiz", config, proveedores, SISTEMA, mensaje)
            except (RuntimeError, prov.TiempoAgotado) as e:
                apuntes.append(f"- {etiqueta}: sin IA disponible ({e})")
                break
            idx = dataset.registrar(cfg_ruta.parent.name, "aprendiz", "aprender", ia, modelo, SISTEMA, mensaje, respuesta)
            secciones = nucleo.parsear(respuesta)["secciones"]
            guardadas = conocimiento.guardar(secciones.get("CONOCIMIENTO", ""), proyecto, verificacion=trozos[i],
                                             fuente_por_defecto=fuente_nota, temas_extra=temas)
            dataset.resultado(idx, notas_guardadas=len(guardadas))
            r["notas"] = sorted(set(r["notas"]) | set(guardadas))
            r.setdefault("resumenes", []).append(secciones.get("RESUMEN", "").strip()[:600])
            r["hechos"] += 1
            hechas_total += len(guardadas)
            trozos_total += 1
            registro[etiqueta] = r
            ruta_reg.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
        registro[etiqueta] = r
        if r["hechos"] >= len(trozos):
            titulo = (etiqueta if tipo in ("web", "youtube")
                      else Path(etiqueta.split("/", 1)[-1]).stem.replace("-", " ").replace("_", " "))
            if not es_ia and tipo not in ("web", "youtube") and "/" in etiqueta.split(":", 1)[-1]:
                carpeta_doc = Path(etiqueta.split(":", 1)[-1]).parent.name.strip(".")   # para que no choquen dos README
                titulo = f"{titulo} ({carpeta_doc})" if carpeta_doc else titulo
            fuente = conocimiento.guardar_fuente(titulo, fuente_nota, temas, r["notas"], proyecto,
                                                 resumen="\n".join(r.get("resumenes", []))[:3000])
            apuntes.append(f"- ✅ `{etiqueta}` aprendido entero: {len(r['notas'])} notas → [[{fuente}]]")
        else:
            apuntes.append(f"- ⏳ `{etiqueta}`: trozo {r['hechos']} de {len(trozos)}")
        ruta_reg.write_text(json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
        if prov.tiempo_restante() < MIN_PARA_TROZO:
            break

    mapas.generar()
    resumen = (f"Trozos leídos: {trozos_total} · notas nuevas o ampliadas: {hechas_total}\n\n"
               + ("**Repos:** " + " · ".join(info) + "\n\n" if info else "") + "\n".join(apuntes))
    nucleo.anotar(bitacora, "📚 Aprendizaje", resumen)
    return resumen
