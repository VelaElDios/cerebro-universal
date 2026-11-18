"""
Control del conocimiento: Javier decide qué sabe el cerebro. Órdenes sencillas, en una nota de
proyectos/control/ (se ejecutan en la siguiente ejecución, sin IA) o al momento en su PC con
`py scripts/control.py "olvidar tema: ac"`:

  olvidar tema: ac                     borra todas las notas de ese tema
  olvidar fuente: temarios/AC/Tema2    borra lo aprendido de esa carpeta o archivo (si una nota viene también
                                       de otras fuentes, solo se le quita esa fuente)
  olvidar nota: título o nombre        borra una nota concreta
  olvidar proyecto: memoria-procesos   borra lo que se aprendió en ese proyecto
  no aprender: temarios/AC/examenes    a partir de ahora, eso no se aprende (proyectos/aprendizaje/ignorar.txt)
  reaprender: temarios/AC/Tema2        olvida eso y lo vuelve a aprender en la próxima tanda
  aprender:                            todo lo que vaya debajo se guarda como nota, tal cual, con confianza
  tipo: receta | concepto | decision | dato     «verificado» (lo dice Javier). Opcionales: tipo, temas,
  temas: ac, cache                     privado: si (solo en el repo privado). El título es el de la nota
  privado: si                          de control (o «titulo: …»).
  (texto del conocimiento)

Antes de borrar se puede probar con «simular» en la primera línea: dice qué haría sin tocar nada.
Lo borrado sigue en el historial de git (GitHub), así que se puede recuperar.
"""

import json
import re
from pathlib import Path

from . import conocimiento, nucleo, privado

MARCA = "## Hecho por el cerebro"
NO_SON_ORDENES = {"bitacora.md", "spec.md", "estado.md", "leeme.md", "readme.md"}


# ---------- olvidar ----------

def _coincide(n: dict, criterio: str, valor: str) -> str | None:
    """None si no coincide; «borrar» si la nota entera es de eso; «quitar» si solo en parte."""
    v = valor.strip().lower()
    if criterio == "tema":
        return "borrar" if conocimiento.nombre_de(v) in [conocimiento.nombre_de(t) for t in n.get("temas", [])] else None
    if criterio == "nota":
        return "borrar" if n["nombre"] == conocimiento.nombre_de(v) or conocimiento.normalizar(
            n.get("titulo", "")) == conocimiento.normalizar(valor) else None
    if criterio == "fuente":
        fuentes = n.get("fuentes", [])
        si = [f for f in fuentes if v in f.lower()]
        if not si:
            return None
        return "borrar" if len(si) == len(fuentes) else "quitar"
    if criterio == "proyecto":
        proys = n.get("proyectos", [])
        if v not in [p.lower() for p in proys]:
            return None
        return "borrar" if len(proys) == 1 else "quitar"
    return None


def _quitar_enlaces(nombres: dict[str, str]):
    """Cambia [[nota-borrada|texto]] por «texto» en todo el vault y en lo privado (sin enlaces rotos)."""
    if not nombres:
        return
    patron = re.compile(r"\[\[(?:[^\]|]*/)?(" + "|".join(re.escape(n) for n in nombres) + r")(?:\|([^\]]*))?\]\]")
    sitios = [nucleo.RAIZ / "memoria", privado.carpeta_conocimiento()] + list((nucleo.RAIZ / "proyectos").glob("*"))
    for base in sitios:
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            if any(x in p.parts for x in ("borrador", "final", ".repos")):
                continue
            t = p.read_text(encoding="utf-8", errors="replace")
            if not any(n in t for n in nombres):
                continue
            t2 = patron.sub(lambda m: m.group(2) or nombres.get(m.group(1), m.group(1)), t)
            # Líneas «Relacionado:» que se han quedado sin enlaces
            t2 = re.sub(r"\nRelacionado: (?:[^\[\n]*)\n", "\n", t2)
            if t2 != t:
                p.write_text(t2, encoding="utf-8")


def olvidar(criterio: str, valor: str, simular: bool = False) -> tuple[list[str], list[str]]:
    """Devuelve (títulos borrados, títulos a los que solo se les quitó esa fuente o proyecto)."""
    borradas, recortadas, nombres = [], [], {}
    for n in conocimiento.todas():
        accion = _coincide(n, criterio, valor)
        if not accion:
            continue
        titulo = n.get("titulo", n["nombre"]) + (" 🔒" if n.get("privada") else "")
        ruta = nucleo.RAIZ / n["ruta"]
        if accion == "borrar":
            borradas.append(titulo)
            nombres[n["nombre"]] = n.get("titulo", n["nombre"])
            if not simular:
                ruta.unlink()
        else:
            recortadas.append(titulo)
            if not simular:
                v = valor.lower()
                campo = "fuentes" if criterio == "fuente" else "proyectos"
                n[campo] = [x for x in n.get(campo, []) if v not in x.lower()]
                datos = {k: x for k, x in n.items() if k not in ("nombre", "ruta", "privada")}
                conocimiento._escribir(ruta, datos)
    if not simular:
        _quitar_enlaces(nombres)
    return borradas, recortadas


# ---------- aprendizaje: ignorar y reaprender ----------

def _carpeta_aprendizaje() -> Path:
    return nucleo.RAIZ / "proyectos" / "aprendizaje"


def no_aprender(patron: str, simular: bool = False) -> str:
    f = _carpeta_aprendizaje() / "ignorar.txt"
    actuales = f.read_text(encoding="utf-8").splitlines() if f.exists() else [
        "# Lo que contenga cualquiera de estas líneas no se aprende (lo escribe scripts/cerebro/control.py)"]
    if patron in actuales:
        return f"«{patron}» ya se ignoraba"
    if not simular:
        f.write_text("\n".join(actuales + [patron]) + "\n", encoding="utf-8")
    return f"a partir de ahora no se aprende nada que contenga «{patron}»"


def reaprender(patron: str, simular: bool = False) -> tuple[list[str], int]:
    borradas, _ = olvidar("fuente", patron, simular)
    quitadas = 0
    for reg in (_carpeta_aprendizaje() / "procesados.json", privado.ruta() / "procesados.json"):
        if not reg.exists():
            continue
        datos = json.loads(reg.read_text(encoding="utf-8"))
        fuera = [k for k in datos if patron.lower() in k.lower()]
        quitadas += len(fuera)
        if fuera and not simular:
            for k in fuera:
                del datos[k]
            reg.write_text(json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
    # Si estaba en ignorar.txt, deja de ignorarse
    f = _carpeta_aprendizaje() / "ignorar.txt"
    if f.exists() and not simular:
        lineas = [l for l in f.read_text(encoding="utf-8").splitlines() if l.strip() != patron]
        f.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return borradas, quitadas


# ---------- aprender algo concreto ----------

def aprender(texto: str, titulo: str, tipo: str = "concepto", temas: str = "", privada: bool = False) -> list[str]:
    """Lo que dice Javier se guarda tal cual y como verificado (la fuente es él)."""
    texto = texto.strip()
    if len(texto) < 20:
        return []
    primera = re.split(r"(?<=[.!?])\s|\n", texto, maxsplit=1)[0][:300]
    bloque = (f"tipo: {tipo}\ntitulo: {titulo}\ntemas: {temas}\nfuente: Javier\ncita: {primera}\n"
              f"contenido:\n{texto}")
    return conocimiento.guardar(bloque, "", verificacion=texto, fuente_por_defecto="Javier", privada=privada)


# ---------- órdenes ----------

def ejecutar_orden(texto: str, titulo: str = "") -> str:
    """Ejecuta las órdenes de una nota (o de la línea de comandos). Devuelve el informe en Markdown."""
    lineas = texto.strip().splitlines()
    simular = bool(lineas) and lineas[0].strip().lower().startswith("simular")
    informe = ["*(simulación: no se ha tocado nada)*"] if simular else []
    i = 0
    while i < len(lineas):
        l = lineas[i].strip()
        i += 1
        if not l or l.lower().startswith(("simular", "#")):
            continue
        m = re.match(r"^olvidar\s+(tema|fuente|nota|proyecto)\s*:\s*(.+)$", l, re.I)
        if m:
            borradas, recortadas = olvidar(m.group(1).lower(), m.group(2).strip(), simular)
            informe.append(f"**Olvidar {m.group(1).lower()} «{m.group(2).strip()}»:** {len(borradas)} notas borradas"
                           + (f", {len(recortadas)} recortadas (venían también de otro sitio)" if recortadas else "")
                           + ("".join(f"\n  - {b}" for b in borradas[:200])))
            continue
        m = re.match(r"^no\s+aprender\s*:\s*(.+)$", l, re.I)
        if m:
            informe.append(f"**No aprender:** {no_aprender(m.group(1).strip(), simular)}")
            continue
        m = re.match(r"^reaprender\s*:\s*(.+)$", l, re.I)
        if m:
            borradas, quitadas = reaprender(m.group(1).strip(), simular)
            informe.append(f"**Reaprender «{m.group(1).strip()}»:** {len(borradas)} notas borradas y {quitadas} archivos "
                           "marcados para volver a aprenderse en la próxima tanda")
            continue
        if re.match(r"^aprender\s*:?\s*$", l, re.I) or re.match(r"^aprender\s*:\s*\S", l, re.I):
            resto = [re.sub(r"^aprender\s*:\s*", "", l, flags=re.I)] + lineas[i:]
            i = len(lineas)
            meta, cuerpo = {}, []
            for r in resto:
                mm = re.match(r"^\s*(tipo|temas|privado|titulo|título)\s*:\s*(.*)$", r, re.I)
                if mm and not any(c.strip() for c in cuerpo):
                    meta[mm.group(1).lower().replace("í", "i")] = mm.group(2).strip()
                elif r.strip() or cuerpo:
                    cuerpo.append(r)
            tipo = meta.get("tipo", "concepto").lower()
            if tipo not in ("concepto", "receta", "decision", "decisión", "dato"):
                tipo = "concepto"
            tipo = tipo.replace("ó", "o")
            es_priv = meta.get("privado", "").lower().startswith("s")
            if es_priv and not privado.disponible():
                informe.append("**Aprender:** no guardado: el modo privado no está disponible aquí")
                continue
            nombre_nota = meta.get("titulo") or titulo or "Nota de Javier"
            if simular:
                informe.append(f"**Aprender:** guardaría «{nombre_nota}» ({tipo}{', privada' if es_priv else ''})")
            else:
                g = aprender("\n".join(cuerpo), nombre_nota, tipo, meta.get("temas", ""), es_priv)
                informe.append(f"**Aprender:** " + (f"guardada [[{g[0]}]] como {tipo} verificado"
                                                    + (" (privada 🔒)" if es_priv else "") if g else
                                                    "no guardado (el texto es demasiado corto)"))
            continue
        informe.append(f"No entiendo esta línea: «{l}» (mira proyectos/control/LEEME.md)")
    return "\n\n".join(informe) or "No había ninguna orden."


def pendientes(carpeta: Path) -> list[Path]:
    return [p for p in sorted(carpeta.rglob("*.md")) if p.name.lower() not in NO_SON_ORDENES
            and MARCA not in p.read_text(encoding="utf-8", errors="replace")]


def ejecutar(carpeta: Path, cfg: dict, cfg_ruta: Path, bitacora: Path) -> str:
    """Proyecto de tipo "control": ejecuta las notas de órdenes pendientes (sin IA)."""
    hechas = []
    for ruta in pendientes(carpeta):
        texto = re.sub(r"^---\n.*?\n---\n", "", ruta.read_text(encoding="utf-8", errors="replace"), flags=re.S)
        informe = ejecutar_orden(texto, ruta.stem)
        with ruta.open("a", encoding="utf-8") as f:
            f.write(f"\n\n{MARCA} ({nucleo.ahora():%Y-%m-%d %H:%M})\n\n{informe}\n")
        hechas.append(ruta.stem)
    if hechas:
        nucleo.anotar(bitacora, "🎛️ Órdenes ejecutadas", "\n".join(f"- [[{h}]]" for h in hechas))
    return f"Órdenes ejecutadas: {len(hechas)}"
