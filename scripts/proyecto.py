"""
Orquestador de proyectos del Cerebro Universal.

Cada ejecución da UN paso:
  1. CONSTRUCTOR avanza el borrador un poco (según spec, bitácora y errores)
  2. Se ejecuta la prueba (compilar LaTeX, tests...) sobre el borrador
  3. REVISOR (otra IA) revisa, corrige lo evidente y deja tareas
  4. Si el borrador compila y está aprobado, se copia a final/

Uso:  python scripts/proyecto.py proyectos/plantilla-sus
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

from cerebro import nucleo
from cerebro import proveedores as prov

FORMATO_CONSTRUCTOR = """Responde EXACTAMENTE con este formato, sin nada fuera de los bloques:

<<<RESUMEN>>>
Qué has hecho en este paso y por qué (2-4 frases).
<<<ARCHIVO ruta/relativa.ext>>>
contenido COMPLETO del archivo
<<<FIN>>>
<<<SIGUIENTE>>>
Qué debería hacerse en el próximo paso.

Puedes repetir el bloque ARCHIVO (máximo {maximo} archivos). Para borrar uno: <<<BORRAR ruta/relativa.ext>>>"""

SISTEMA_CONSTRUCTOR = """Eres el CONSTRUCTOR de un proyecto dentro de "Cerebro Universal", un sistema donde
varias IAs de empresas distintas colaboran. Otra IA revisará cada paso que des.

Cómo trabajas:
- Cada ejecución haces UN paso pequeño y bien hecho que acerque el proyecto a la spec.
- Prioridad: 1) si la prueba/compilación falla, arreglarla; 2) atender las tareas que dejó el
  revisor en la bitácora; 3) avanzar con lo siguiente de la spec.
- Escribe siempre archivos COMPLETOS. Nunca fragmentos, nunca "... resto igual ...".
- Rutas relativas a la carpeta del borrador. Comentarios del código en español.
- No inventes datos de fuentes bibliográficas: si no estás seguro de un valor, déjalo marcado
  con un comentario TODO para que el revisor lo compruebe.

""" + FORMATO_CONSTRUCTOR

SISTEMA_REVISOR = """Eres el REVISOR de un proyecto dentro de "Cerebro Universal". Otra IA (el constructor),
de otra empresa, acaba de dar un paso. Tu trabajo es que el resultado sea correcto y cumpla la spec.

Cómo trabajas:
- Comprueba: que compila/pasa la prueba, que cumple la spec, que los cálculos y datos son
  correctos, y que el código es limpio y entendible.
- Errores claros y localizados: corrígelos tú directamente (archivos COMPLETOS, máximo {maximo}).
- Lo que suponga más trabajo: déjalo como tarea concreta para el constructor.
- Sé exigente pero concreto. No pidas cambios por gusto personal.
- Marca TERMINADO solo si se cumplen TODOS los criterios de "terminado" de la spec.

Responde EXACTAMENTE con este formato:

<<<VEREDICTO>>>
aprobado   (o: cambios)
<<<COMENTARIOS>>>
Qué está bien, qué está mal y qué has corregido tú.
<<<ARCHIVO ruta/relativa.ext>>>
contenido COMPLETO corregido (opcional, solo si corriges algo)
<<<FIN>>>
<<<TAREAS>>>
- tareas concretas para el próximo paso del constructor
<<<TERMINADO>>>
no   (o: si)"""


def probar(cfg: dict, carpeta: Path) -> tuple[bool, str]:
    """Ejecuta el comando de prueba del proyecto (compilar, tests...) y resume el resultado."""
    comando = cfg.get("comando_prueba")
    if not comando:
        return True, "Este proyecto no tiene comando de prueba."
    principal = cfg.get("archivo_principal")
    if principal and not (carpeta / principal).exists():
        return False, f"Todavía no existe el archivo principal {principal}."
    entorno = {**os.environ, "max_print_line": "1000"}  # que LaTeX no corte las líneas del log a 79 caracteres
    try:
        r = subprocess.run(comando, shell=True, cwd=carpeta, capture_output=True,
                           text=True, timeout=600, errors="replace", env=entorno)
    except subprocess.TimeoutExpired:
        return False, "La prueba tardó más de 10 minutos y se canceló."

    salida = (r.stdout + "\n" + r.stderr).splitlines()
    # Si hay un .log de LaTeX, es la fuente más fiable de errores
    log = carpeta / Path(principal or "x").with_suffix(".log")
    lineas = log.read_text(encoding="utf-8", errors="replace").splitlines() if log.exists() else salida

    # TeX marca los errores con "!" o "archivo:línea:", y siempre los acompaña de "l.N <código>".
    patron_error = re.compile(r"^!|^\S+\.(tex|sty|cls|lua):\d+:|^\[\\directlua\]:\d+:")
    marcadas = set()
    for i, linea in enumerate(lineas):
        if "messages enabled" in linea:
            continue
        if patron_error.search(linea):
            marcadas.update(range(i, i + 4))
        elif re.match(r"^l\.\d+ ", linea):
            marcadas.update(range(i - 2, i + 2))  # el mensaje suele ir justo encima de l.N
    errores = [lineas[i] for i in sorted(marcadas) if 0 <= i < len(lineas)]
    avisos = sorted({l for l in lineas if "Warning" in l})[:15]

    informe = [f"Código de salida: {r.returncode} ({'OK' if r.returncode == 0 else 'FALLA'})"]
    if errores:
        informe += ["", "Errores:", *errores[:60]]
    if avisos:
        informe += ["", "Avisos:", *avisos]
    if not errores:
        informe += ["", "Final de la salida:", *salida[-30:]]
    return r.returncode == 0, "\n".join(informe)


def main():
    if len(sys.argv) != 2:
        sys.exit("Uso: python scripts/proyecto.py proyectos/<nombre>")

    carpeta = nucleo.RAIZ / sys.argv[1]
    cfg_ruta = carpeta / "proyecto.json"
    cfg = json.loads(cfg_ruta.read_text(encoding="utf-8"))
    if cfg.get("estado") == "terminado":
        print("Proyecto terminado. No hay nada que hacer.")
        return

    spec = (carpeta / "spec.md").read_text(encoding="utf-8")
    borrador, final = carpeta / "borrador", carpeta / "final"
    bitacora = carpeta / "bitacora.md"
    borrador.mkdir(exist_ok=True)
    maximo = cfg.get("max_archivos_por_paso", 3)

    config, proveedores = prov.cargar(nucleo.RAIZ / "config" / "ias.json")

    # ---------- 1. CONSTRUCTOR ----------
    ok_antes, prueba_antes = probar(cfg, borrador)
    mensaje = f"""# SPEC DEL PROYECTO
{spec}

# BITÁCORA RECIENTE (incluye las tareas del revisor)
{nucleo.bitacora_reciente(bitacora)}

# ESTADO DE LA PRUEBA DEL BORRADOR
{prueba_antes}

# ARCHIVOS ACTUALES DEL BORRADOR
{nucleo.volcar(nucleo.leer_carpeta(borrador))}"""

    texto, ia, modelo = prov.pedir_rol("constructor", config, proveedores,
                                       SISTEMA_CONSTRUCTOR.format(maximo=maximo), mensaje)
    paso = nucleo.parsear(texto)
    cambios = nucleo.aplicar(borrador, paso["archivos"], paso["borrar"], maximo)
    s = paso["secciones"]
    nucleo.anotar(bitacora, f"Constructor ({ia} · {modelo})",
                  f"{s.get('RESUMEN', '(sin resumen)')}\n\n"
                  f"**Archivos:** {', '.join(f'`{c}`' for c in cambios) or 'ninguno'}\n\n"
                  f"**Siguiente:** {s.get('SIGUIENTE', '-')}")
    print(f"Constructor: {len(cambios)} cambios")

    # ---------- 2. PRUEBA ----------
    ok, prueba = probar(cfg, borrador)
    print(f"Prueba tras constructor: {'OK' if ok else 'FALLA'}")

    # ---------- 3. REVISOR ----------
    mensaje = f"""# SPEC DEL PROYECTO
{spec}

# BITÁCORA RECIENTE
{nucleo.bitacora_reciente(bitacora)}

# LO QUE ACABA DE HACER EL CONSTRUCTOR
{s.get('RESUMEN', '')}
Archivos tocados: {', '.join(cambios) or 'ninguno'}

# RESULTADO DE LA PRUEBA
{prueba}

# ARCHIVOS DEL BORRADOR
{nucleo.volcar(nucleo.leer_carpeta(borrador))}"""

    texto, ia, modelo = prov.pedir_rol("revisor", config, proveedores,
                                       SISTEMA_REVISOR.format(maximo=maximo), mensaje)
    revision = nucleo.parsear(texto)
    correcciones = nucleo.aplicar(borrador, revision["archivos"], revision["borrar"], maximo)
    if correcciones:
        ok, prueba = probar(cfg, borrador)
        print(f"Prueba tras correcciones: {'OK' if ok else 'FALLA'}")

    r = revision["secciones"]
    veredicto = r.get("VEREDICTO", "cambios").strip().lower()
    terminado = r.get("TERMINADO", "no").strip().lower().startswith("s")

    # ---------- 4. PROMOCIÓN A FINAL ----------
    promocionado = ok and (veredicto.startswith("aprobado") or bool(correcciones))
    if promocionado:
        nucleo.promocionar(borrador, final)

    estado = "✅ compila" if ok else "❌ falla la prueba"
    nucleo.anotar(bitacora, f"Revisor ({ia} · {modelo})",
                  f"**Veredicto:** {veredicto} · **Prueba:** {estado}"
                  f"{' · copiado a `final/`' if promocionado else ''}\n\n"
                  f"{r.get('COMENTARIOS', '(sin comentarios)')}\n\n"
                  f"**Correcciones del revisor:** {', '.join(f'`{c}`' for c in correcciones) or 'ninguna'}\n\n"
                  f"**Tareas para el constructor:**\n{r.get('TAREAS', '- ninguna')}")

    if terminado and ok:
        cfg["estado"] = "terminado"
        cfg_ruta.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        nucleo.anotar(bitacora, "🎉 Proyecto terminado", "El revisor da por cumplidos todos los criterios de la spec.")
        print("¡Proyecto terminado!")


if __name__ == "__main__":
    main()
