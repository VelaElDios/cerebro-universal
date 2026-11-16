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
nucleo.RAIZ = raiz_real
print("TODO OK")
