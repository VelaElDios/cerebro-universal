"""
¿Sirve de verdad lo que sabe el cerebro? Cada vez que una nota se manda a una IA se apunta, y al acabar el
paso se apunta si salió bien (la prueba pasa y no se deshizo) o mal (se deshizo o rompió algo).

  memoria/mapas/uso.json   {ruta: {"usos": n, "bien": n, "mal": n, "ultimo": fecha}}

conocimiento.seleccionar da un poco más de peso a las notas que suelen acompañar pasos buenos y un poco
menos a las que acompañan pasos que se deshacen, y mapas.py publica el resumen en memoria/ESTADISTICAS.md.
"""

import json
from pathlib import Path

from . import nucleo


def ruta() -> Path:
    return nucleo.RAIZ / "memoria" / "mapas" / "uso.json"


def cargar() -> dict:
    try:
        return json.loads(ruta().read_text(encoding="utf-8")) if ruta().exists() else {}
    except Exception:
        return {}


def registrar(notas: list[str], bien: bool | None):
    """Apunta que estas notas se usaron en un paso, y si el paso salió bien (True), mal (False) o no se sabe."""
    if not notas:
        return
    datos = cargar()
    hoy = f"{nucleo.ahora():%Y-%m-%d}"
    for n in set(notas):
        d = datos.setdefault(n, {"usos": 0, "bien": 0, "mal": 0})
        d["usos"] += 1
        if bien is True:
            d["bien"] += 1
        elif bien is False:
            d["mal"] += 1
        d["ultimo"] = hoy
    ruta().parent.mkdir(parents=True, exist_ok=True)
    ruta().write_text(json.dumps(datos, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")


def bonificacion(datos: dict, nota: str) -> float:
    """Entre -1 y +1 según cómo le va a la nota (suavizado: con pocos usos apenas cuenta)."""
    d = datos.get(nota)
    if not d:
        return 0.0
    return (d.get("bien", 0) - d.get("mal", 0)) / (d.get("usos", 0) + 3)
