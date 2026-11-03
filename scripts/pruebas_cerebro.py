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
print("TODO OK")
