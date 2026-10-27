"""
Comprueba qué IAs de config/ias.json funcionan ahora mismo, sin tocar ningún proyecto.

Para cada proveedor con clave: mira si cada modelo existe en su lista (/models, si la API la tiene)
y le pide una respuesta mínima. Imprime una tabla con ✅/❌, el tiempo y el error.
Sale con 1 si un rol (constructor o revisor) se queda sin ninguna IA que funcione.

Uso:  python scripts/probar_ias.py        (lo lanza el workflow «Cerebro - Probar IAs»)
"""

import sys
import time
from pathlib import Path

from cerebro import proveedores as prov

RAIZ = Path(__file__).resolve().parents[1]
SISTEMA = "Responde solo con la palabra OK."
MENSAJE = "Di OK."


def main():
    config, proveedores = prov.cargar(RAIZ / "config" / "ias.json")
    prov.fijar_limite(20 * 60)
    funcionan = set()
    print(f"{'proveedor':<20} {'modelo':<45} {'estado':<6} {'s':>5}  detalle")
    for nombre, p in proveedores.items():
        if not p.disponible:
            print(f"{nombre:<20} {'-':<45} {'—':<6} {'':>5}  sin clave ({p.cfg['clave_env']})")
            continue
        existentes = None
        if isinstance(p, prov.CompatibleOpenAI):
            try:
                existentes = {m.get("id") for m in p._http("GET", "/models").get("data", [])}
            except Exception as e:
                print(f"{nombre:<20} {'(lista de modelos)':<45} {'?':<6} {'':>5}  {str(e)[:80]}")
        for modelo in p.modelos():
            if existentes is not None and modelo not in existentes:
                print(f"{nombre:<20} {modelo:<45} {'❌':<6} {'':>5}  no está en /models")
                continue
            inicio = time.monotonic()
            try:
                texto = p._llamar(modelo, SISTEMA, MENSAJE)
                ok = bool(texto and texto.strip())
                detalle = (texto or "(vacía)").strip().replace("\n", " ")[:40]
            except Exception as e:
                ok, detalle = False, f"{type(e).__name__}: {str(e)[:90]}"
            s = time.monotonic() - inicio
            print(f"{nombre:<20} {modelo:<45} {'✅' if ok else '❌':<6} {s:5.1f}  {detalle}")
            if ok:
                funcionan.add(nombre)

    print()
    sin_ia = []
    for rol, lista in config["roles"].items():
        vivos = [n for n in lista if n in funcionan]
        print(f"{rol}: {' → '.join(lista)}   (funcionan: {', '.join(vivos) or 'ninguno'})")
        if not vivos:
            sin_ia.append(rol)
    if sin_ia:
        print(f"::error::Sin ninguna IA que funcione para: {', '.join(sin_ia)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
