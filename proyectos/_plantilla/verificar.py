#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar.py — Test automático del proyecto.

Está FUERA de borrador/ a propósito: las IAs no pueden modificarlo para aprobarse solas.
Se ejecuta desde borrador/ (es el "comando_prueba" de proyecto.json: python3 ../verificar.py).

Sale con 0 si todo va bien y con 1 si algo falla. Cada fallo se imprime con un mensaje
claro, porque es lo que lee el constructor para arreglarlo.
"""

import sys
from pathlib import Path

BORRADOR = Path.cwd()
fallos = []


def comprobar(condicion: bool, mensaje: str):
    """Apunta un fallo si la condición no se cumple."""
    if not condicion:
        fallos.append(mensaje)


# ---------- Comprobaciones del proyecto (cambiar por las de verdad) ----------

comprobar((BORRADOR / "principal.py").exists(), "Falta borrador/principal.py")

# Ejemplo: importar el código del borrador y comprobar resultados conocidos
# sys.path.insert(0, str(BORRADOR))
# from principal import suma
# comprobar(suma(2, 3) == 5, f"suma(2, 3) debería ser 5 y da {suma(2, 3)}")

# ---------- Resultado ----------

if fallos:
    print(f"VERIFICACIÓN FALLIDA: {len(fallos)} problema(s)")
    for f in fallos:
        print("  - ERROR:", f)
    sys.exit(1)
print("VERIFICACIÓN OK")
