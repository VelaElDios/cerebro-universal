"""
Mapas del Cerebro: todo lo que saben las IAs, enlazado para verlo (Obsidian) y para recorrerlo (máquinas).

Se regenera al final de cada paso (generar()):

  memoria/CEREBRO.md           puerta de entrada para CUALQUIER IA: cómo está organizado y qué leer
  memoria/indice.md            lecciones y conocimiento, con lo pendiente de confirmar
  memoria/temas/<tema>.md      un nodo por tema que enlaza lecciones, conocimiento y proyectos (hubs del grafo)
  memoria/mapas/grafo.json     el grafo entero en JSON (nodos y aristas) para IAs, scripts o una IA local
  memoria/mapas/cerebro.canvas el mapa visual completo (Canvas de Obsidian)
  memoria/mapas/<proyecto>.canvas  el mapa de cada proyecto
"""

import json
import math
import re
from pathlib import Path

from . import conocimiento, nucleo
from . import memoria as lecciones

MARCA = "(este archivo se genera solo)"
# Colores del Canvas de Obsidian: 1 rojo, 2 naranja, 3 amarillo, 4 verde, 5 cian, 6 morado
COLORES = {"proyecto": "6", "tema": "5", "leccion": "1", "concepto": "4", "receta": "3",
           "decision": "2", "dato": "5", "fuente": "6"}
ICONOS = {"proyecto": "📁", "tema": "🔵", "leccion": "⚠️", "concepto": "💡", "receta": "🧪",
          "decision": "⚖️", "dato": "📊", "fuente": "📚"}


def _raiz() -> Path:
    return nucleo.RAIZ


def proyectos() -> list[dict]:
    res = []
    for cfg_ruta in sorted((_raiz() / "proyectos").glob("*/proyecto.json")):
        carpeta = cfg_ruta.parent
        if carpeta.name.startswith("_"):
            continue
        try:
            cfg = json.loads(cfg_ruta.read_text(encoding="utf-8-sig"))
        except Exception:
            continue
        nota = "estado.md" if (carpeta / "estado.md").exists() else "bitacora.md"
        res.append({"nombre": carpeta.name, "estado": cfg.get("estado", "?"), "temas": cfg.get("temas", []),
                    "ruta": f"proyectos/{carpeta.name}/{nota}", "tipo_proyecto": cfg.get("tipo", "construir")})
    return res


def nodos_y_aristas() -> tuple[list[dict], list[dict]]:
    nodos, aristas = [], []
    temas: dict[str, int] = {}

    def tema(t):
        t = t.lower()
        temas[t] = temas.get(t, 0) + 1
        return f"tema:{t}"

    for p in proyectos():
        nodos.append({"id": f"proyecto:{p['nombre']}", "tipo": "proyecto", "titulo": p["nombre"],
                      "estado": p["estado"], "temas": p["temas"], "ruta": p["ruta"]})
        for t in p["temas"]:
            aristas.append({"de": f"proyecto:{p['nombre']}", "a": tema(t), "tipo": "usa"})
    for l in lecciones.todas():
        nid = f"leccion:{l['nombre']}"
        nodos.append({"id": nid, "tipo": "leccion", "titulo": l.get("titulo", l["nombre"]),
                      "temas": l["temas"], "proyectos": l.get("proyectos", []),
                      "confianza": "verificado" if l.get("estado") == "confirmada" else "propuesto",
                      "ruta": f"memoria/lecciones/{l['nombre']}.md"})
        for t in l["temas"]:
            aristas.append({"de": nid, "a": tema(t), "tipo": "trata"})
        for p in l.get("proyectos", []):
            aristas.append({"de": nid, "a": f"proyecto:{p}", "tipo": "aprendido_en"})
    notas = conocimiento.todas()
    por_nombre = {n["nombre"]: n for n in notas}
    for n in notas:
        nid = f"{n['tipo']}:{n['nombre']}"
        nodos.append({"id": nid, "tipo": n["tipo"], "titulo": n.get("titulo", n["nombre"]),
                      "temas": n.get("temas", []), "proyectos": n.get("proyectos", []),
                      "confianza": n.get("confianza", "propuesto"), "ruta": n["ruta"]})
        for t in n.get("temas", []):
            aristas.append({"de": nid, "a": tema(t), "tipo": "trata"})
        for p in n.get("proyectos", []):
            aristas.append({"de": nid, "a": f"proyecto:{p}", "tipo": "de_proyecto"})
        for destino in re.findall(r"\[\[([^\]|#]+)", n["cuerpo"]):
            destino = destino.strip().split("/")[-1]
            if destino in por_nombre and destino != n["nombre"]:
                d = por_nombre[destino]
                aristas.append({"de": nid, "a": f"{d['tipo']}:{destino}", "tipo": "enlaza"})
    for t, veces in temas.items():
        nodos.append({"id": f"tema:{t}", "tipo": "tema", "titulo": t, "peso": veces, "ruta": f"memoria/temas/{t}.md"})
    ids = {n["id"] for n in nodos}
    aristas = [a for a in aristas if a["de"] in ids and a["a"] in ids]
    return nodos, aristas


# ---------- Notas de Obsidian ----------

def _enlace(n: dict) -> str:
    destino = n["ruta"][:-3] if n["ruta"].endswith(".md") else n["ruta"]
    aviso = "" if n.get("confianza", "verificado") == "verificado" else " · ⚠️ propuesto"
    return f"- {ICONOS.get(n['tipo'], '')} [[{destino}|{n['titulo']}]]{aviso}"


def escribir_temas(nodos: list[dict], aristas: list[dict]):
    carpeta = _raiz() / "memoria" / "temas"
    carpeta.mkdir(parents=True, exist_ok=True)
    por_id = {n["id"]: n for n in nodos}
    vecinos: dict[str, list[dict]] = {}
    for a in aristas:
        if a["a"].startswith("tema:"):
            vecinos.setdefault(a["a"], []).append(por_id[a["de"]])
    temas = [n for n in nodos if n["tipo"] == "tema"]
    validos = {n["titulo"] for n in temas}
    for nota in carpeta.glob("*.md"):
        if nota.stem not in validos and ("se genera solo" in nota.read_text(encoding="utf-8")):
            nota.unlink()
    orden = ["proyecto", "receta", "decision", "concepto", "dato", "leccion", "fuente"]
    nombres = {"proyecto": "Proyectos", "receta": "Recetas (cómo lo hacemos)", "decision": "Decisiones (y por qué)",
               "concepto": "Conceptos", "dato": "Datos", "leccion": "Lecciones (errores ya resueltos)",
               "fuente": "Documentos aprendidos"}
    for t in temas:
        lista = vecinos.get(t["id"], [])
        # temas que comparten notas con este: enlaces entre hubs (el grafo queda conectado)
        cercanos: dict[str, int] = {}
        ids_vecinos = {v["id"] for v in lista}
        for a in aristas:
            if a["de"] in ids_vecinos and a["a"].startswith("tema:") and a["a"] != t["id"]:
                cercanos[a["a"][5:]] = cercanos.get(a["a"][5:], 0) + 1
        partes = [f"---\ntipo: \"tema\"\ntitulo: \"{t['titulo']}\"\nnotas: {len(lista)}\n---\n",
                  f"# {t['titulo']}\n\nNodo del mapa del Cerebro con todo lo que se sabe de «{t['titulo']}» {MARCA}.\n"]
        for tipo in orden:
            del_tipo = sorted((v for v in lista if v["tipo"] == tipo), key=lambda v: v["titulo"].lower())
            if del_tipo:
                partes.append(f"\n## {nombres[tipo]}\n\n" + "\n".join(_enlace(v) for v in del_tipo) + "\n")
        if cercanos:
            top = sorted(cercanos.items(), key=lambda x: -x[1])[:12]
            partes.append("\n## Temas relacionados\n\n" + " · ".join(f"[[{c}]]" for c, _ in top) + "\n")
        (carpeta / f"{t['titulo']}.md").write_text("".join(partes), encoding="utf-8")


def escribir_indice(nodos: list[dict]):
    pendientes = [n for n in nodos if n.get("confianza") == "propuesto"]
    temas = sorted((n for n in nodos if n["tipo"] == "tema"), key=lambda n: -n.get("peso", 0))
    cuenta = {t: sum(1 for n in nodos if n["tipo"] == t) for t in ICONOS}
    texto = (f"# Índice del Cerebro\n\nTodo lo que saben las IAs, por tipo {MARCA}. La puerta de entrada es "
             f"[[CEREBRO]] y el mapa visual, [[mapas/cerebro.canvas|cerebro.canvas]].\n\n"
             "Para confirmar algo propuesto: abrir la nota, revisarla y cambiar `confianza` a `verificado` "
             "(o `estado` a `confirmada` en las lecciones).\n\n"
             "## Temas\n\n" + " · ".join(f"[[{t['titulo']}]] ({t.get('peso', 0)})" for t in temas) + "\n")
    for tipo in ["proyecto", "receta", "decision", "concepto", "dato", "fuente", "leccion"]:
        del_tipo = sorted((n for n in nodos if n["tipo"] == tipo), key=lambda n: n["titulo"].lower())
        if del_tipo:
            texto += f"\n## {ICONOS[tipo]} {tipo.capitalize()} ({cuenta[tipo]})\n\n" + "\n".join(_enlace(n) for n in del_tipo) + "\n"
    texto += f"\n## Pendientes de confirmar ({len(pendientes)})\n\n" + ("\n".join(_enlace(n) for n in pendientes) or "Ninguno.") + "\n"
    (_raiz() / "memoria" / "indice.md").write_text(texto, encoding="utf-8")


CEREBRO = """---
tipo: "guia"
titulo: "CEREBRO: cómo usar esta memoria"
---

# CEREBRO — léeme primero (para IAs)

Este vault es la **memoria compartida** de todas las IAs que trabajan para Javier: da igual qué modelo o qué
empresa esté conectada, aquí está lo que ya se sabe, cómo se hacen las cosas y por qué. Sirve también para
buscar con RAG y, en el futuro, para entrenar una IA local. {marca}

## Cómo encontrar algo

1. **Por proyecto:** `proyectos/<nombre>/estado.md` es la ficha corta (qué es, decisiones, convenciones,
   estado y siguiente). La bitácora entera está al lado.
2. **Por tema:** `memoria/temas/<tema>.md` enlaza todo lo de ese tema: recetas, decisiones, conceptos,
   datos, lecciones y proyectos.
3. **Por tipo:** `memoria/conocimiento/<tipo>/` y `memoria/lecciones/` (todo listado en [[indice]]).
4. **Máquinas:** `memoria/mapas/grafo.json` tiene todas las notas (nodos) y sus relaciones (aristas).

## Tipos de nota

| Tipo | Carpeta | Para qué |
|---|---|---|
| 💡 concepto | `conocimiento/conceptos/` | Qué es algo (término, pieza de la arquitectura, tema del temario) |
| 🧪 receta | `conocimiento/recetas/` | **Cómo lo hacemos** en nuestros proyectos: pasos y código que funcionó. Si existe, se hace igual |
| ⚖️ decisión | `conocimiento/decisiones/` | Qué se eligió y por qué: no se vuelve a discutir sin motivo nuevo |
| 📊 dato | `conocimiento/datos/` | Hechos concretos de un proyecto (cifras, fechas, nombres), con su fuente |
| 📚 fuente | `conocimiento/fuentes/` | Un documento aprendido (temario, documentación) y todo lo que se sacó de él |
| ⚠️ lección | `lecciones/` | Errores que ya se resolvieron: no repetirlos |

## Reglas para usarla

- `confianza: "verificado"` → la cita está comprobada literalmente en su fuente: úsalo sin volver a deducirlo.
  `"propuesto"` → probablemente bien, pero compruébalo antes de dar nada por cierto.
- Si lo que necesitas no está, **apréndelo y guárdalo** (bloque `<<<CONOCIMIENTO>>>`) con su fuente y una cita
  literal. Nunca inventes datos: lo que no está en una fuente no se escribe.
- Reglas fijas de Javier: [[reglas-tfg]] (memorias con formato de TFG).

## Ahora mismo

{estadisticas}

## Temas principales

{temas}
"""


def escribir_cerebro(nodos: list[dict], aristas: list[dict]):
    cuenta = {t: sum(1 for n in nodos if n["tipo"] == t) for t in ICONOS}
    estad = (f"{len(nodos)} nodos y {len(aristas)} relaciones: " + ", ".join(
        f"{v} {ICONOS[k]} {k}" for k, v in cuenta.items() if v) + f" · actualizado {nucleo.ahora():%Y-%m-%d %H:%M}")
    temas = sorted((n for n in nodos if n["tipo"] == "tema"), key=lambda n: -n.get("peso", 0))[:30]
    (_raiz() / "memoria" / "CEREBRO.md").write_text(CEREBRO.format(
        marca=MARCA, estadisticas=estad,
        temas=" · ".join(f"[[{t['titulo']}]] ({t.get('peso', 0)})" for t in temas) or "(ninguno)"), encoding="utf-8")


# ---------- Canvas (el mapa visual) ----------

TAMANOS = {"tema": (340, 110), "proyecto": (380, 130), "fuente": (320, 100)}


def _posiciones(nodos: list[dict], aristas: list[dict], previas: dict[str, tuple[float, float]]) -> dict:
    """Disposición por fuerzas (Fruchterman-Reingold, en Python puro para no depender de nada): los nodos
    enlazados se atraen y todos se repelen, así salen racimos por tema como un mapa mental. Se parte de
    las posiciones del canvas anterior para que el mapa crezca sin recolocarse entero cada vez."""
    import hashlib
    ids = [n["id"] for n in nodos]
    if not ids:
        return {}
    k = 900.0                                   # distancia ideal entre nodos
    pos = {}
    for i in ids:
        if i in previas:
            pos[i] = list(previas[i])
        else:
            h = hashlib.md5(i.encode()).digest()
            pos[i] = [(h[0] * 256 + h[1]) / 65535 * 8000 - 4000, (h[2] * 256 + h[3]) / 65535 * 8000 - 4000]
    pares = [(a["de"], a["a"]) for a in aristas if a["de"] in pos and a["a"] in pos]
    nuevos = sum(1 for i in ids if i not in previas)
    iteraciones = 60 if nuevos < len(ids) * 0.2 else (180 if len(ids) < 500 else 80)
    temp = 600.0 if nuevos >= len(ids) * 0.2 else 150.0
    for _ in range(iteraciones):
        disp = {i: [0.0, 0.0] for i in ids}
        for x in range(len(ids)):
            px, py = pos[ids[x]]
            for y in range(x + 1, len(ids)):
                qx, qy = pos[ids[y]]
                dx, dy = px - qx, py - qy
                d2 = dx * dx + dy * dy + 0.01
                if d2 > 36_000_000:          # lejos: no se empujan (más rápido)
                    continue
                f = k * k / d2
                disp[ids[x]][0] += dx * f; disp[ids[x]][1] += dy * f
                disp[ids[y]][0] -= dx * f; disp[ids[y]][1] -= dy * f
        for a, b in pares:
            dx, dy = pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]
            d = math.sqrt(dx * dx + dy * dy) + 0.01
            f = d / k
            disp[a][0] -= dx * f; disp[a][1] -= dy * f
            disp[b][0] += dx * f; disp[b][1] += dy * f
        for i in ids:
            dx, dy = disp[i]
            d = math.sqrt(dx * dx + dy * dy) + 0.01
            pos[i][0] += dx / d * min(d, temp) - pos[i][0] * 0.002   # un poco de gravedad al centro
            pos[i][1] += dy / d * min(d, temp) - pos[i][1] * 0.002
        temp = max(10.0, temp * 0.97)
    return {i: (p[0], p[1]) for i, p in pos.items()}


def _canvas(nodos: list[dict], aristas: list[dict], centro: str = "CEREBRO", previo: Path | None = None) -> dict:
    """El mapa visual: cada nodo es su nota (se abre al hacer clic), con colores por tipo y racimos por tema."""
    previas = {}
    if previo and previo.exists():
        try:
            for n in json.loads(previo.read_text(encoding="utf-8")).get("nodes", []):
                previas[n["id"]] = (n["x"] + n["width"] / 2, n["y"] + n["height"] / 2)
        except Exception:
            previas = {}
    pos = _posiciones(nodos, aristas, previas)
    c_nodos = []
    for n in nodos:
        w, h = TAMANOS.get(n["tipo"], (280, 80))
        if n["tipo"] == "tema":
            w += min(300, 8 * n.get("peso", 1))
        x, y = pos[n["id"]]
        c_nodos.append({"id": n["id"], "type": "file", "file": n["ruta"], "x": int(x - w / 2), "y": int(y - h / 2),
                        "width": int(w), "height": int(h), "color": COLORES.get(n["tipo"], "1")})
    ids = {n["id"] for n in c_nodos}
    por_id = {n["id"]: n for n in nodos}
    c_aristas = [{"id": f"e{i}", "fromNode": a["de"], "toNode": a["a"],
                  "color": COLORES.get(por_id[a["de"]]["tipo"], "1")}
                 for i, a in enumerate(aristas) if a["de"] in ids and a["a"] in ids]
    return {"nodes": c_nodos, "edges": c_aristas}


def _subgrafo(nodos, aristas, proyecto: str):
    pid = f"proyecto:{proyecto}"
    ids = {pid} | {a["de"] for a in aristas if a["a"] == pid} | {a["a"] for a in aristas if a["de"] == pid}
    ids |= {a["a"] for a in aristas if a["de"] in ids and a["a"].startswith("tema:")}
    return [n for n in nodos if n["id"] in ids], [a for a in aristas if a["de"] in ids and a["a"] in ids]


def generar():
    """Regenera índices, hubs de temas, CEREBRO.md, grafo.json y los canvas. Nunca tumba un paso."""
    try:
        nodos, aristas = nodos_y_aristas()
        escribir_temas(nodos, aristas)
        escribir_indice(nodos)
        escribir_cerebro(nodos, aristas)
        mapas = _raiz() / "memoria" / "mapas"
        mapas.mkdir(parents=True, exist_ok=True)
        (mapas / "grafo.json").write_text(json.dumps(
            {"generado": nucleo.ahora().isoformat(timespec="seconds"), "nodos": nodos, "aristas": aristas},
            ensure_ascii=False, indent=1), encoding="utf-8")
        destino = mapas / "cerebro.canvas"
        destino.write_text(json.dumps(_canvas(nodos, aristas, previo=destino), ensure_ascii=False, indent=1),
                           encoding="utf-8")
        for p in proyectos():
            sn, sa = _subgrafo(nodos, aristas, p["nombre"])
            destino = mapas / f"{p['nombre']}.canvas"
            destino.write_text(json.dumps(_canvas(sn, sa, p["nombre"], previo=destino), ensure_ascii=False, indent=1),
                               encoding="utf-8")
        print(f"Mapas: {len(nodos)} nodos, {len(aristas)} relaciones")
        return nodos, aristas
    except Exception as e:  # los mapas son un extra: si fallan, el paso sigue
        print(f"No pude generar los mapas: {e}")
        return [], []
