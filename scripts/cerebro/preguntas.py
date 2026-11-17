"""
Pregúntale al cerebro: Javier (o cualquiera) escribe una nota en proyectos/preguntas/ con su pregunta y,
en la siguiente ejecución, el cerebro contesta debajo usando SOLO lo que sabe (notas del vault con sus
fuentes), diciendo de qué notas sale cada cosa y qué no sabe. Proyecto de tipo "preguntas": solo se
ejecuta cuando hay alguna sin contestar (ver elegir_proyecto.py).

  proyectos/preguntas/¿Cómo se despliega en Cloud Run.md   ← la pregunta (el título o el texto)
  ...
  ## Respuesta del cerebro (2026-11-17 · nvidia-revisor)   ← lo que añade el cerebro

Cada pregunta con su respuesta se guarda también en los datos de entrenamiento.
"""

import re
from pathlib import Path

from . import conocimiento, dataset, memoria, nucleo
from . import proveedores as prov

MARCA = "## Respuesta del cerebro"
NO_SON_PREGUNTAS = {"bitacora.md", "spec.md", "estado.md", "leeme.md", "readme.md"}

SISTEMA = """Eres el CEREBRO: la memoria compartida de las IAs que trabajan para Javier. Contestas su pregunta usando
SOLO el CONOCIMIENTO DEL CEREBRO que te paso (notas con su fuente) y las fichas de los proyectos.

Reglas:
- Cada afirmación lleva la nota de la que sale entre dobles corchetes, con su nombre exacto: [[nombre-de-la-nota]].
- Si las notas no bastan para contestar algo, dilo claro («El cerebro no tiene información sobre…») y di qué
  documento habría que darle para que lo aprenda. No rellenes con lo que tú sabes por tu cuenta sin avisar:
  si añades algo de conocimiento general, márcalo como «(conocimiento general, no está en el cerebro)».
- Si dos notas se contradicen, dilo.
- Directo y claro, en español, en Markdown. Primero la respuesta corta y luego el detalle."""


def pendientes(carpeta: Path) -> list[Path]:
    res = []
    for p in sorted(carpeta.rglob("*.md")):
        if p.name.lower() in NO_SON_PREGUNTAS or "/." in p.as_posix():
            continue
        texto = p.read_text(encoding="utf-8", errors="replace")
        if MARCA not in texto:
            res.append(p)
    return res


def _pregunta(ruta: Path) -> str:
    texto = re.sub(r"^---\n.*?\n---\n", "", ruta.read_text(encoding="utf-8", errors="replace"), flags=re.S).strip()
    return f"{ruta.stem}\n\n{texto}".strip()


def _contexto(pregunta: str) -> str:
    fichas = []
    for estado in sorted((nucleo.RAIZ / "proyectos").glob("*/estado.md")):
        fichas.append(f"### Ficha de {estado.parent.name}\n{conocimiento.leer_estado(estado.parent)[:1500]}")
    return (f"# CONOCIMIENTO DEL CEREBRO (lo más relacionado con la pregunta)\n"
            f"{conocimiento.seleccionar([], pregunta, '', max_chars=14000)}\n\n"
            f"# LECCIONES (errores ya resueltos)\n{memoria.seleccionar([], pregunta, max_chars=3000)}\n\n"
            f"# FICHAS DE LOS PROYECTOS\n" + "\n\n".join(fichas) + "\n\n"
            f"# MAPA DEL CEREBRO\n{conocimiento.mapa_textual()}")


def enlazar_titulos(texto: str) -> str:
    """Las IAs enlazan por título ([[Arquitectura en capas…]]) y Obsidian necesita el nombre del archivo:
    [[titulo]] → [[nombre-del-archivo|titulo]] cuando el título es de una nota que existe."""
    por_titulo = {}
    for n in conocimiento.todas():
        por_titulo[conocimiento.normalizar(n.get("titulo", ""))] = n["nombre"]
        por_titulo[conocimiento.normalizar(n["nombre"])] = n["nombre"]

    def cambiar(m):
        dentro = m.group(1)
        if "|" in dentro:
            return m.group(0)
        nombre = por_titulo.get(conocimiento.normalizar(dentro))
        if not nombre:
            return m.group(0)
        return f"[[{nombre}]]" if nombre == dentro else f"[[{nombre}|{dentro}]]"
    return re.sub(r"\[\[([^\]]+)\]\]", cambiar, texto)


def ejecutar(carpeta: Path, cfg: dict, cfg_ruta: Path, bitacora: Path) -> str:
    config, proveedores = prov.cargar(nucleo.RAIZ / "config" / "ias.json")
    roles = config.get("roles", {})
    config = {**config, "roles": {**roles, "cerebro": cfg.get("roles", {}).get("cerebro")
                                  or roles.get("cerebro") or roles.get("revisor", [])}}
    hechas = []
    for ruta in pendientes(carpeta):
        if prov.tiempo_restante() < 4 * 60:
            break
        pregunta = _pregunta(ruta)
        mensaje = f"# PREGUNTA DE JAVIER\n{pregunta}\n\n{_contexto(pregunta)}"
        try:
            respuesta, ia, modelo = prov.pedir_rol("cerebro", config, proveedores, SISTEMA, mensaje)
        except (RuntimeError, prov.TiempoAgotado) as e:
            nucleo.anotar(bitacora, "⚠️ Pregunta sin contestar", f"`{ruta.name}`: {e}")
            break
        usadas = conocimiento.ultimas_usadas()
        respuesta = enlazar_titulos(respuesta)
        dataset.registrar(carpeta.name, "cerebro", "pregunta", ia, modelo, SISTEMA, mensaje, respuesta)
        with ruta.open("a", encoding="utf-8") as f:
            f.write(f"\n\n{MARCA} ({nucleo.ahora():%Y-%m-%d %H:%M} · {ia} · {modelo})\n\n{respuesta.strip()}\n\n"
                    f"*Notas consultadas: {len(usadas)}. Para otra pregunta, crea otra nota en esta carpeta.*\n")
        hechas.append(ruta.name)
    if hechas:
        nucleo.anotar(bitacora, "💬 Preguntas contestadas", "\n".join(f"- [[{h[:-3]}]]" for h in hechas))
    return f"Preguntas contestadas: {len(hechas)}"
