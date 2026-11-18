"""Pruebas del núcleo del cerebro sin IAs de verdad: bloques CAMBIAR, freno a archivos que encogen
y que un paso que rompe la compilación se deshace solo.

Uso:  python scripts/pruebas_cerebro.py   (desde la raíz del repo o desde scripts/)
"""
import json, shutil, sys, tempfile
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "scripts"))
from cerebro import nucleo
import proyecto
from cerebro import proveedores as prov

# 1. parsear CAMBIAR
r = nucleo.parsear("""<<<RESUMEN>>>
hola
<<<CAMBIAR a.tex>>>
<<<BUSCAR>>>
linea dos
<<<POR>>>
linea DOS
<<<BUSCAR>>>
no existe
<<<POR>>>
x
<<<FIN>>>
<<<ARCHIVO b.tex>>>
nuevo
<<<FIN>>>
<<<SIGUIENTE>>>
nada""")
assert r["cambios"] == [("a.tex", "linea dos", "linea DOS"), ("a.tex", "no existe", "x")], r["cambios"]
assert r["archivos"] == {"b.tex": "nuevo\n"} and r["secciones"]["RESUMEN"] == "hola" and r["secciones"]["SIGUIENTE"] == "nada"

d = Path(tempfile.mkdtemp())
(d / "a.tex").write_text("linea uno\nlinea dos  \nlinea tres\n")
res = nucleo.aplicar_cambios(d, r["cambios"])
assert res[0] == "(cambio) a.tex" and res[1].startswith("(no aplicado: no encuentro"), res
assert "linea DOS" in (d / "a.tex").read_text()

# 2. archivo que encoge mucho → rechazado
(d / "largo.tex").write_text("x" * 10000)
res = nucleo.aplicar(d, {"largo.tex": "corto"}, [], 3)
assert res[0].startswith("(rechazado"), res
assert len((d / "largo.tex").read_text()) == 10000

# 3. foto / restaurar
f = nucleo.foto(d)
(d / "a.tex").write_text("roto")
(d / "nuevo.tex").write_text("n")
nucleo.restaurar(d, f)
assert "linea DOS" in (d / "a.tex").read_text() and not (d / "nuevo.tex").exists()

# 4. paso completo con IAs falsas: el constructor rompe la compilación → se deshace
proy = Path(tempfile.mkdtemp()) / "proyectos" / "prueba"
(proy / "borrador").mkdir(parents=True)
(proy / "borrador" / "doc.tex").write_text("Hola\nTexto bueno.\n")
(proy / "spec.md").write_text("spec")
(proy / "bitacora.md").write_text("# Bitácora\n")
(proy / "check.py").write_text("import sys\nt = open('doc.tex').read()\nif 'ROTO' in t:\n    print('doc.tex:1: roto')\n    sys.exit(1)\n")
cfg = {"estado": "en-construccion", "comando_prueba": "python3 ../check.py",
       "reintentar_si": r"^\S+\.tex:\d+:", "max_intentos": 1, "pasos": 0, "max_pasos": 5}
(proy / "proyecto.json").write_text(json.dumps(cfg))
respuestas = {
    "constructor": "<<<RESUMEN>>>\nrompo\n<<<CAMBIAR doc.tex>>>\n<<<BUSCAR>>>\nTexto bueno.\n<<<POR>>>\nTexto ROTO.\n<<<FIN>>>\n<<<SIGUIENTE>>>\n-",
    "revisor": "<<<VEREDICTO>>>\ncambios\n<<<COMPROBACIONES>>>\n- 1+1=2\n<<<COMENTARIOS>>>\nok\n<<<TAREAS>>>\n- nada\n<<<TERMINADO>>>\nno",
}
prov.pedir_rol = lambda rol, *a, **k: (respuestas[rol], "falsa", "modelo")
prov.cargar = lambda ruta: ({"roles": {}}, {})
prov.fijar_limite(30 * 60)
from cerebro import uso as _uso
_uso.ruta = lambda: proy / "uso.json"     # que la prueba no escriba en el vault de verdad
proyecto.dar_paso(proy, json.loads((proy / "proyecto.json").read_text()), proy / "proyecto.json", proy / "bitacora.md")
assert "Texto bueno." in (proy / "borrador" / "doc.tex").read_text(), "no se deshizo"
bit = (proy / "bitacora.md").read_text()
assert "paso deshecho" in bit, bit

# 5. conocimiento: citas comprobadas, ampliar una nota, elegir qué mandar
from cerebro import conocimiento, mapas, dataset, aprender
raiz_real = nucleo.RAIZ
nucleo.RAIZ = Path(tempfile.mkdtemp())
(nucleo.RAIZ / "proyectos" / "demo").mkdir(parents=True)
(nucleo.RAIZ / "proyectos" / "demo" / "proyecto.json").write_text(json.dumps({"estado": "en-construccion", "temas": ["latex"]}))
fuente = "La portada oficial está en elements/portada.tex y se incluye con input."
bloque = """tipo: receta
titulo: Cómo se pone la portada oficial
temas: latex, tfg
claves: portada.tex
fuente: memoria/reglas-tfg.md
cita: La portada oficial está en elements/portada.tex
contenido:
Memoria.tex hace \\input{elements/portada}. No se añade ninguna otra portada.
---
tipo: dato
titulo: Número de pruebas del Sprint 1
temas: saas
cita: esto no está en la fuente
contenido:
Hay 140 pruebas automáticas en la base SaaS."""
g = conocimiento.guardar(bloque, "demo", verificacion=fuente)
assert len(g) == 2, g
notas = {n["nombre"]: n for n in conocimiento.todas()}
assert notas["como-se-pone-la-portada-oficial"]["confianza"] == "verificado"
assert notas["numero-de-pruebas-del-sprint-1"]["confianza"] == "propuesto"
conocimiento.guardar("tipo: receta\ntitulo: Cómo se pone la portada oficial\ntemas: plantilla\ncontenido:\nY el preámbulo no lleva logos de una segunda portada.", "otro")
n = {n["nombre"]: n for n in conocimiento.todas()}["como-se-pone-la-portada-oficial"]
assert "otro" in n["proyectos"] and "plantilla" in n["temas"] and "Ampliación" in n["cuerpo"], n
sel = conocimiento.seleccionar(["latex"], "hay que arreglar portada.tex", "demo")
assert "portada oficial" in sel.lower(), sel
assert conocimiento.guardar_estado(nucleo.RAIZ / "proyectos" / "demo", "## Qué es\n" + "x" * 100, ["latex"])

# 6. mapas: hubs de temas, grafo y canvas válidos
nodos, aristas = mapas.generar()
assert any(n["id"] == "tema:latex" for n in nodos) and aristas
canvas = json.loads((nucleo.RAIZ / "memoria" / "mapas" / "cerebro.canvas").read_text(encoding="utf-8"))
ids = {c["id"] for c in canvas["nodes"]}
assert all(e["fromNode"] in ids and e["toNode"] in ids for e in canvas["edges"])
assert "como-se-pone-la-portada-oficial" in (nucleo.RAIZ / "memoria" / "temas" / "latex.md").read_text(encoding="utf-8")
assert (nucleo.RAIZ / "memoria" / "CEREBRO.md").exists()

# 7. datos de entrenamiento en local (sin repo privado)
dataset._registros.clear()
i = dataset.registrar("demo", "constructor", "constructor", "falsa", "m", "sis", "msg", "resp")
dataset.resultado(i, prueba_ok=True)
import os, gzip
os.environ.pop("DATOS_TOKEN", None)
assert "en local" in dataset.subir("demo")
filas = list((nucleo.RAIZ / ".cerebro-datos" / "datos").rglob("*.jsonl.gz"))
assert filas and json.loads(gzip.open(filas[0], "rt").readline())["resultado"]["prueba_ok"] is True
assert (nucleo.RAIZ / ".cerebro-datos" / "export" / "conocimiento.jsonl").read_text(encoding="utf-8").count("\n") >= 2

# 8. aprender: trocea un documento y guarda lo que saca la IA (falsa), con la cita comprobada
assert len(aprender.trocear("a" * 30000 + "\n\n" + "b" * 100, 14000)) == 3
apr = nucleo.RAIZ / "proyectos" / "aprendizaje"
apr.mkdir(parents=True)
(apr / "doc.md").write_text("# Scrum\n\nUn sprint dura como mucho un mes y acaba con una revisión.\n", encoding="utf-8")
cfg_apr = {"tipo": "aprender", "estado": "en-construccion", "aprender_de": [{"entrada": "doc.md", "temas": ["scrum"]}]}
(apr / "proyecto.json").write_text(json.dumps(cfg_apr))
prov.pedir_rol = lambda rol, *a, **k: ("<<<RESUMEN>>>\nScrum\n<<<CONOCIMIENTO>>>\ntipo: concepto\ntitulo: Duración de un sprint\n"
                                       "cita: Un sprint dura como mucho un mes\ncontenido:\nUn sprint dura un mes como máximo.", "falsa", "m")
prov.cargar = lambda ruta: ({"roles": {"revisor": ["x"]}}, {})
prov.fijar_limite(30 * 60)
aprender.ejecutar(apr, cfg_apr, apr / "proyecto.json", apr / "bitacora.md")
nota = {n["nombre"]: n for n in conocimiento.todas()}["duracion-de-un-sprint"]
assert nota["confianza"] == "verificado" and "scrum" in nota["temas"], nota
assert json.loads((apr / "procesados.json").read_text())["doc.md"]["hechos"] == 1
assert any(n["tipo"] == "fuente" for n in conocimiento.todas())
assert "Nada nuevo" in aprender.ejecutar(apr, cfg_apr, apr / "proyecto.json", apr / "bitacora.md")

# 9. cualquier tipo de archivo: tipos, enlaces, HTML, Word, y una imagen «transcrita» (Gemini falso)
from cerebro import medios
assert medios.tipo_de("foto.JPG") == "imagen" and medios.tipo_de("clase.mp4") == "video"
assert medios.tipo_de("nota.m4a") == "audio" and medios.tipo_de("enlaces.txt") == "enlaces"
assert medios.tipo_de("https://youtu.be/abc") == "youtube" and medios.tipo_de("https://ejemplo.com/a") == "web"
assert "Hola mundo" in medios.html_a_texto("<html><script>x=1</script><p>Hola <b>mundo</b></p></html>")
try:
    import docx
    d = docx.Document(); d.add_paragraph("El patrón MVC separa modelo, vista y controlador."); d.save(str(apr / "mvc.docx"))
    assert "MVC" in medios.extraer(apr / "mvc.docx", "office")[0]
except ImportError:
    print("(sin python-docx: no pruebo Word)")
(apr / "pizarra.png").write_bytes(b"\x89PNG falso")
(apr / "enlaces.txt").write_text("Mira esto: https://www.youtube.com/watch?v=xyz\n", encoding="utf-8")
transcrito = []
def falso(origen, tipo):
    transcrito.append(tipo)
    return "## Qué explica\nEl diagrama muestra que el cliente llama a la API y la API a la base de datos."
medios.transcribir = falso
prov.pedir_rol = lambda rol, *a, **k: ("<<<RESUMEN>>>\nDiagrama\n<<<CONOCIMIENTO>>>\ntipo: concepto\ntitulo: Flujo cliente API base de datos\n"
                                       "cita: el cliente llama a la API y la API a la base de datos\ncontenido:\nEl cliente habla con la API y la API con la base de datos.", "falsa", "m")
cfg_apr["aprender_de"] = [{"entrada": "*.png", "temas": ["arquitectura"]}, {"entrada": "enlaces.txt", "temas": ["video"]}]
dataset._registros.clear(); dataset._adjuntos.clear()
aprender.ejecutar(apr, cfg_apr, apr / "proyecto.json", apr / "bitacora.md")
assert sorted(transcrito) == ["imagen", "youtube"], transcrito
nota = {n["nombre"]: n for n in conocimiento.todas()}["flujo-cliente-api-base-de-datos"]
assert nota["confianza"] == "verificado" and "transcripción" in nota["fuentes"][0], nota
assert any(k.startswith("transcripciones/") for k in dataset._adjuntos)
reg = json.loads((apr / "procesados.json").read_text())
assert "https://www.youtube.com/watch?v=xyz" in reg and reg["pizarra.png"]["hechos"] == 1

# 10. embeddings (Gemini falso: vector por palabras) y búsqueda por significado
from cerebro import embeddings, uso, jardin, preguntas
import math, hashlib as _h
def vec(texto):
    v = [0.0] * embeddings.DIM
    for w in re.findall(r"[a-záéíóúñ]{4,}", texto.lower()):
        v[int(_h.md5(w.encode()).hexdigest(), 16) % embeddings.DIM] += 1
    return embeddings._normalizar(v)
import re
embeddings._embeber = lambda textos, tarea: ([vec(t) for t in textos], "falso")
print(embeddings.actualizar())
vecs = embeddings.vectores()
assert vecs and abs(embeddings.coseno(*list(vecs.values())[:1] * 2) - 1) < 0.01
assert embeddings._desempaquetar(embeddings._empaquetar([0.5, -0.25])) == [0.5, -0.25]
sel = conocimiento.seleccionar([], "diagrama cliente servidor base datos", "nada")
assert "Flujo cliente API" in sel, sel

# 11. uso: las notas usadas en pasos buenos suben
uso.registrar(conocimiento.ultimas_usadas(), bien=True)
assert uso.cargar() and uso.bonificacion(uso.cargar(), conocimiento.ultimas_usadas()[0]) > 0

# 12. jardinero: cita casi igual → verificada; repetidas → fusionadas; enlaces nuevos
(nucleo.RAIZ / "fuente.md").write_text("Los sprints de este proyecto duran dos semanas exactas, sin excepciones.", encoding="utf-8")
conocimiento.guardar("tipo: dato\ntitulo: Duración de los sprints del proyecto\nfuente: fuente.md\n"
                     "cita: Los sprints de este proyecto duran dos semanas exactas sin excepcion\ncontenido:\nCada sprint dura dos semanas.", "demo")
conocimiento.guardar("tipo: dato\ntitulo: Cuánto dura cada sprint del proyecto\ncontenido:\nCada sprint del proyecto dura dos semanas.", "demo")
n = {n["nombre"]: n for n in conocimiento.todas()}["duracion-de-los-sprints-del-proyecto"]
assert n["confianza"] == "propuesto"
prov.pedir_rol = lambda rol, *a, **k: ("<<<TITULO>>>\nDuración de los sprints\n<<<CONTENIDO>>>\nCada sprint del proyecto dura dos semanas exactas.\n<<<CONTRADICCION>>>\nno", "falsa", "m")
jardin.UMBRAL_DUPLICADO = 0.5; jardin.UMBRAL_CONTRADICCION = 0.5
jd = nucleo.RAIZ / "proyectos" / "jardinero"; jd.mkdir(parents=True)
res = jardin.ejecutar(jd, {}, jd / "proyecto.json", jd / "bitacora.md")
notas = {n["nombre"]: n for n in conocimiento.todas()}
assert "duracion-de-los-sprints-del-proyecto" in notas and "cuanto-dura-cada-sprint-del-proyecto" not in notas, res
assert notas["duracion-de-los-sprints-del-proyecto"]["confianza"] == "propuesto"   # una de las dos no estaba verificada
assert "Citas comprobadas: 1" in res or "Notas repetidas fusionadas: 1" in res, res

# 13. preguntas: contesta debajo de la nota y solo se ejecuta si hay alguna pendiente
import elegir_proyecto
pq = nucleo.RAIZ / "proyectos" / "preguntas"; pq.mkdir(parents=True)
(pq / "Cuánto dura un sprint.md").write_text("¿Y quién lo decide?", encoding="utf-8")
assert elegir_proyecto.hay_preguntas(pq)
prov.pedir_rol = lambda rol, *a, **k: ("Dura un mes como mucho [[duracion-de-un-sprint]].", "falsa", "m")
preguntas.ejecutar(pq, {}, pq / "proyecto.json", pq / "bitacora.md")
assert "## Respuesta del cerebro" in (pq / "Cuánto dura un sprint.md").read_text(encoding="utf-8")
assert not elegir_proyecto.hay_preguntas(pq)

# 14. servidor MCP: sus herramientas funcionan (sin arrancar el protocolo)
try:
    import mcp_cerebro
    assert "Duración" in mcp_cerebro.buscar("cuánto dura un sprint")
    assert "Proyectos" in mcp_cerebro.mapa()
    assert "Guardado" in mcp_cerebro.guardar_conocimiento("receta", "Cómo se pregunta al cerebro",
                                                          "Se crea una nota en proyectos/preguntas.", temas="cerebro")
except ImportError as e:
    print(f"(sin el paquete mcp: no pruebo el servidor MCP: {e})")

# 15. modo privado: las notas privadas no salen en lo público y solo se usan si se pide
from cerebro import privado, control
conocimiento.USAR_PRIVADO = False   # (el servidor MCP de la prueba 14 lo activa)
(nucleo.RAIZ / ".cerebro-privado" / "conocimiento").mkdir(parents=True)
assert privado.disponible()
g = conocimiento.guardar("tipo: receta\ntitulo: Mi solución secreta de la práctica\ntemas: ac\ncontenido:\nSe resuelve con un predictor de 2 bits y una BTB.", "", privada=True)
assert g and (nucleo.RAIZ / ".cerebro-privado" / "conocimiento" / "recetas" / f"{g[0]}.md").exists()
assert all(not n.get("privada") for n in conocimiento.todas(publicas_solo=True))
assert "secreta" not in conocimiento.seleccionar(["ac"], "predictor de 2 bits práctica solución secreta", "")
assert "secreta" in conocimiento.seleccionar(["ac"], "predictor de 2 bits práctica solución secreta", "", privadas=True)
nodos, _ = mapas.generar()
assert not any("secreta" in n["titulo"] for n in nodos)
assert "secreta" not in (nucleo.RAIZ / "memoria" / "indice.md").read_text(encoding="utf-8")
(pq / "privado - mi práctica.md").write_text("¿Cómo resolví la práctica?", encoding="utf-8")
prov.pedir_rol = lambda rol, *a, **k: ("Con un predictor de 2 bits [[mi-solucion-secreta-de-la-practica]].", "falsa", "m")
preguntas.ejecutar(pq, {}, pq / "proyecto.json", pq / "bitacora.md")
publica = (pq / "privado - mi práctica.md").read_text(encoding="utf-8")
assert "Respuesta privada" in publica and "predictor" not in publica.split("##")[-1]
assert "predictor" in (nucleo.RAIZ / ".cerebro-privado" / "preguntas" / "privado - mi práctica.md").read_text(encoding="utf-8")

# 16. notebooks y zip
import zipfile
nb = {"cells": [{"cell_type": "markdown", "source": ["# Caché\n", "Una caché asociativa por conjuntos."]},
                {"cell_type": "code", "source": ["print(2**10)"], "outputs": [{"text": ["1024\n"]}]}],
      "metadata": {"kernelspec": {"language": "python"}}}
(apr / "cache.ipynb").write_text(json.dumps(nb), encoding="utf-8")
assert medios.tipo_de("cache.ipynb") == "notebook"
t = medios.extraer(apr / "cache.ipynb", "notebook")[0]
assert "asociativa por conjuntos" in t and "print(2**10)" in t and "1024" in t
with zipfile.ZipFile(apr / "practica.zip", "w") as z:
    z.writestr("practica/main.c", "int main(){return 0;}")
    z.writestr("practica/LEEME.txt", "Simulador de caché")
    z.writestr("__MACOSX/._main.c", "basura")
cola = aprender.pendientes(apr, {"aprender_de": [{"entrada": "practica.zip"}]}, {"publico": {}, "privado": {}})
etiquetas = sorted(c[1] for c in cola)
assert etiquetas == ["practica.zip!practica/LEEME.txt", "practica.zip!practica/main.c"], etiquetas

# 17. control: olvidar, aprender algo concreto, no aprender y reaprender
inf = control.ejecutar_orden("simular\nolvidar tema: ac")
assert "simulación" in inf and (nucleo.RAIZ / ".cerebro-privado" / "conocimiento" / "recetas" / f"{g[0]}.md").exists()
inf = control.ejecutar_orden("aprender:\ntipo: receta\ntemas: ac\nLa BTB guarda la dirección destino de los saltos tomados.", "Qué guarda la BTB")
n = {x["nombre"]: x for x in conocimiento.todas()}["que-guarda-la-btb"]
assert n["confianza"] == "verificado" and n["tipo"] == "receta" and "Javier" in n["fuentes"], inf
inf = control.ejecutar_orden("olvidar tema: ac")
assert "que-guarda-la-btb" not in {x["nombre"] for x in conocimiento.todas()} and "Olvidar tema" in inf
assert not (nucleo.RAIZ / ".cerebro-privado" / "conocimiento" / "recetas" / f"{g[0]}.md").exists()
control.ejecutar_orden("no aprender: practica.zip")
assert aprender.pendientes(apr, {"aprender_de": [{"entrada": "practica.zip"}]}, {"publico": {}, "privado": {}}) == []
json.dump({"doc.md": {"md5": "x", "hechos": 1, "total": 1, "notas": []}}, open(apr / "procesados.json", "w"))
borr, quit = control.reaprender("doc.md")
assert quit == 1 and "doc.md" not in json.load(open(apr / "procesados.json"))
ct = nucleo.RAIZ / "proyectos" / "control"; ct.mkdir()
(ct / "Olvidar sprints.md").write_text("olvidar nota: Duración de los sprints", encoding="utf-8")
assert elegir_proyecto.hay_preguntas(ct, control.MARCA)
control.ejecutar(ct, {}, ct / "proyecto.json", ct / "bitacora.md")
assert control.MARCA in (ct / "Olvidar sprints.md").read_text(encoding="utf-8")
nucleo.RAIZ = raiz_real
print("TODO OK")
