#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar.py — Test automático del proyecto plantilla-sus.

Está FUERA de borrador/ a propósito: las IAs no pueden modificarlo para aprobarse.

Qué hace:
  1. Lee borrador/datos/respuestas.csv y calcula por su cuenta, para cada participante,
     la puntuación SUS, la nota (Sauro y Lewis, 2016), el adjetivo (Bangor et al., 2009)
     y la aceptabilidad (Bangor et al., 2008), más media, DT muestral, mínimo y máximo.
  2. Lo compara con borrador/resultados.json, que el documento exporta al compilar.
  3. Si algo no cuadra, imprime cada diferencia y sale con código 1. Si todo cuadra, sale con 0.

Uso (desde cualquier carpeta):  python3 verificar.py
También:  python3 verificar.py RUTA_CSV RUTA_JSON   (lo usa probar_datos_raros.py)
Solo usa la biblioteca estándar de Python.
"""

import csv
import json
import math
import sys
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
CSV = CARPETA / "borrador" / "datos" / "respuestas.csv"
JSON = CARPETA / "borrador" / "resultados.json"

TOLERANCIA = 0.01  # margen para comparar números con decimales


# ---------------------------------------------------------------------------
# Escalas de transformación (deben coincidir con las fuentes originales)
# ---------------------------------------------------------------------------

# Sauro y Lewis (2016): escala de notas curvada. (límite inferior, nota)
NOTAS = [
    (84.1, "A+"), (80.8, "A"), (78.9, "A-"), (77.2, "B+"), (74.1, "B"),
    (72.6, "B-"), (71.1, "C+"), (65.0, "C"), (62.7, "C-"), (51.7, "D"),
]

# Bangor, Kortum y Miller (2009): el artículo da la MEDIA de cada adjetivo.
# Se asigna el adjetivo cuya media está más cerca; los límites son los puntos
# medios entre medias consecutivas. (límite inferior, adjetivo)
ADJETIVOS = [
    (88.2, "El mejor imaginable"),  # media 90,9
    (78.45, "Excelente"),           # media 85,5
    (61.15, "Bueno"),               # media 71,4
    (43.3, "OK"),                   # media 50,9
    (28.0, "Pobre"),                # media 35,7
    (16.4, "Horrible"),             # media 20,3
]                                   # resto: El peor imaginable (media 12,5)


def nota(p):
    for limite, valor in NOTAS:
        if p >= limite:
            return valor
    return "F"


def adjetivo(p):
    for limite, valor in ADJETIVOS:
        if p >= limite:
            return valor
    return "El peor imaginable"


def aceptabilidad(p):
    # Bangor, Kortum y Miller (2008)
    if p >= 70:
        return "Aceptable"
    if p >= 50:
        return "Marginal"
    return "No aceptable"


# ---------------------------------------------------------------------------
# Cálculo independiente desde el CSV
# ---------------------------------------------------------------------------

def calcular_esperado(ruta_csv=None):
    """Devuelve (participantes, estadísticas, errores_csv) calculados desde el CSV."""
    participantes, errores = [], []
    with open(ruta_csv or CSV, encoding="utf-8-sig", newline="") as f:
        for num, fila in enumerate(csv.DictReader(f), start=2):
            pid = (fila.get("id") or "").strip()
            respuestas = []
            for i in range(1, 11):
                bruto = (fila.get(f"q{i}") or "").strip()
                try:
                    r = int(bruto)
                except ValueError:
                    r = None
                if r is None or not 1 <= r <= 5:
                    errores.append(f"línea {num} ({pid}): q{i} inválida ('{bruto}')")
                    break
                respuestas.append(r)
            else:
                # Ítems impares (posición 0, 2, 4...): r - 1 · ítems pares: 5 - r
                suma = sum(r - 1 if i % 2 == 0 else 5 - r for i, r in enumerate(respuestas))
                p = suma * 2.5
                participantes.append({
                    "id": pid, "puntuacion": p, "nota": nota(p),
                    "adjetivo": adjetivo(p), "aceptabilidad": aceptabilidad(p),
                })

    puntos = [x["puntuacion"] for x in participantes]
    n = len(puntos)
    media = sum(puntos) / n if n else 0.0
    dt = math.sqrt(sum((x - media) ** 2 for x in puntos) / (n - 1)) if n > 1 else 0.0
    stats = {
        "n": n, "media": media, "desviacion": dt,
        "minimo": min(puntos) if puntos else 0.0,
        "maximo": max(puntos) if puntos else 0.0,
    }
    return participantes, stats, errores


# ---------------------------------------------------------------------------
# Comparación con lo que exporta el documento
# ---------------------------------------------------------------------------

def comparar(nombre, esperado, obtenido, fallos):
    """Compara un valor y anota el fallo con un mensaje exacto."""
    if isinstance(esperado, (int, float)) and not isinstance(esperado, bool):
        ok = isinstance(obtenido, (int, float)) and not isinstance(obtenido, bool) \
             and abs(esperado - obtenido) <= TOLERANCIA
    else:
        ok = esperado == obtenido
    if not ok:
        fallos.append(f"{nombre}: esperado {esperado!r}, documento {obtenido!r}")


def main():
    global CSV, JSON
    if len(sys.argv) == 3:  # rutas alternativas (prueba con datos raros)
        CSV, JSON = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if not CSV.exists():
        print(f"ERROR: no existe {CSV}")
        return 1
    if not JSON.exists():
        print(f"ERROR: no existe {JSON.name}. "
              "El documento debe exportarlo al compilar (ver spec.md).")
        return 1

    participantes, stats, errores_csv = calcular_esperado()
    if errores_csv:
        # Con datos inválidos el documento solo debe avisar; aquí lo dejamos claro.
        print("AVISO: el CSV tiene respuestas inválidas (esas filas se excluyen):")
        for e in errores_csv:
            print("  -", e)

    try:
        doc = json.loads(JSON.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as e:
        print(f"ERROR: resultados.json no es JSON válido: {e}")
        return 1

    fallos = []
    doc_part = {p.get("id"): p for p in doc.get("participantes", []) if isinstance(p, dict)}
    esp_part = {p["id"]: p for p in participantes}

    for pid in esp_part.keys() - doc_part.keys():
        fallos.append(f"{pid}: falta en resultados.json")
    for pid in doc_part.keys() - esp_part.keys():
        fallos.append(f"{pid}: aparece en resultados.json pero no es un participante válido del CSV")

    for pid in [p["id"] for p in participantes if p["id"] in doc_part]:
        for campo in ("puntuacion", "nota", "adjetivo", "aceptabilidad"):
            comparar(f"{pid}.{campo}", esp_part[pid][campo], doc_part[pid].get(campo), fallos)

    doc_stats = doc.get("estadisticas", {})
    for campo in ("n", "media", "desviacion", "minimo", "maximo"):
        comparar(f"estadisticas.{campo}", stats[campo], doc_stats.get(campo), fallos)

    if fallos:
        print(f"VERIFICACIÓN FALLIDA: {len(fallos)} diferencia(s) entre el CSV y el documento")
        for f in fallos:
            print("  -", f)
        return 1

    print(f"VERIFICACIÓN OK: {stats['n']} participantes, media {stats['media']:.2f}, "
          f"DT {stats['desviacion']:.2f}, mín {stats['minimo']:.1f}, máx {stats['maximo']:.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
