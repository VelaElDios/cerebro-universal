"""
Elige qué proyecto avanza en esta ejecución del workflow y qué hay que instalar.

- Si se pasa un proyecto (lanzado a mano con uno concreto), se usa ese.
- Si no, entre los proyectos "en-construccion" (que no empiecen por _ y no hayan llegado a
  max_pasos) se elige el que lleve más tiempo sin ejecutarse ("ultima_ejecucion" en su
  proyecto.json). Así todos van por turnos.

Escribe en $GITHUB_OUTPUT: activo, proyecto, apt, pip.  Sin GitHub, lo imprime.
Uso:  python scripts/elegir_proyecto.py [proyectos/<nombre>]
"""

import json
import os
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def leer_json(ruta: Path) -> dict:
    return json.loads(ruta.read_text(encoding="utf-8-sig"))


def activo(cfg: dict) -> bool:
    if cfg.get("estado", "en-construccion") != "en-construccion":
        return False
    maximo = cfg.get("max_pasos")
    return maximo is None or cfg.get("pasos", 0) < maximo


def candidatos() -> list[tuple[str, Path, dict]]:
    """(última ejecución, carpeta, cfg) de cada proyecto activo."""
    lista = []
    for cfg_ruta in sorted((RAIZ / "proyectos").glob("*/proyecto.json")):
        carpeta = cfg_ruta.parent
        if carpeta.name.startswith("_"):  # _plantilla y similares: nunca se ejecutan
            continue
        try:
            cfg = leer_json(cfg_ruta)
        except Exception as e:
            print(f"::warning::{cfg_ruta} no se puede leer: {e}")
            continue
        if activo(cfg):
            lista.append((cfg.get("ultima_ejecucion", ""), carpeta, cfg))
    return sorted(lista, key=lambda x: x[0])  # el más antiguo (o el que nunca se ejecutó) primero


def paquetes(cfg: dict) -> tuple[list[str], list[str]]:
    """Paquetes apt y pip que necesita el proyecto (por "necesita" + sueltos)."""
    entornos = leer_json(RAIZ / "config" / "entornos.json")
    apt, pip = list(cfg.get("apt", [])), list(cfg.get("pip", []))
    for nombre in cfg.get("necesita", []):
        if nombre not in entornos:
            print(f"::warning::Entorno desconocido en necesita: {nombre} (mira config/entornos.json)")
            continue
        apt += entornos[nombre].get("apt", [])
        pip += entornos[nombre].get("pip", [])
    return sorted(set(apt)), sorted(set(pip))


def main():
    forzado = sys.argv[1].strip().strip("/") if len(sys.argv) > 1 and sys.argv[1].strip() else ""
    salida = {"activo": "false", "proyecto": "", "apt": "", "pip": ""}

    if forzado:
        cfg_ruta = RAIZ / forzado / "proyecto.json"
        if not cfg_ruta.exists():
            print(f"::error::No existe {forzado}/proyecto.json")
            sys.exit(1)
        cfg = leer_json(cfg_ruta)
        if activo(cfg):
            elegido = (forzado, cfg)
        else:
            elegido = None
            print(f"::notice::{forzado} está '{cfg.get('estado')}' "
                  f"({cfg.get('pasos', 0)}/{cfg.get('max_pasos', '∞')} pasos): no se hace nada.")
    else:
        lista = candidatos()
        print("Proyectos activos: " + (", ".join(c.name for _, c, _ in lista) or "ninguno"))
        elegido = (lista[0][1].relative_to(RAIZ).as_posix(), lista[0][2]) if lista else None
        if not elegido:
            print("::notice::No hay ningún proyecto en construcción: no se hace nada.")

    if elegido:
        ruta, cfg = elegido
        apt, pip = paquetes(cfg)
        salida = {"activo": "true", "proyecto": ruta, "apt": " ".join(apt), "pip": " ".join(pip)}
        print(f"Elegido: {ruta}  ·  apt: {salida['apt'] or '-'}  ·  pip: {salida['pip'] or '-'}")

    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as f:
            for clave, valor in salida.items():
                f.write(f"{clave}={valor}\n")
    else:
        print(json.dumps(salida, ensure_ascii=False))


if __name__ == "__main__":
    main()
