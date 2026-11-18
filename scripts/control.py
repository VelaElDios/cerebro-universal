#!/usr/bin/env python3
"""
Control del conocimiento desde la línea de comandos (en el PC de Javier, sobre el vault):

    py scripts/control.py "olvidar tema: ac"
    py scripts/control.py "simular" "olvidar fuente: temarios/AC/examenes"
    py scripts/control.py "no aprender: temarios/AC/examenes"

Mismas órdenes que en las notas de proyectos/control/ (ver scripts/cerebro/control.py). El resultado se ve
al momento en Obsidian y Obsidian lo sube a GitHub como siempre.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cerebro import control, mapas  # noqa: E402

if len(sys.argv) < 2:
    sys.exit(__doc__)
print(control.ejecutar_orden("\n".join(sys.argv[1:])))
mapas.generar()
