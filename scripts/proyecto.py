"""
Orquestador de proyectos del Cerebro Universal.

Cada ejecución da UN paso:
  1. CONSTRUCTOR avanza el borrador un poco (según spec, bitácora y errores)
  2. Se ejecuta la prueba (compilar LaTeX, tests...) sobre el borrador. Si falla, el
     constructor recibe el error y lo intenta arreglar (hasta max_intentos en total)
  3. REVISOR (otra IA) revisa, corrige lo evidente y deja tareas
  4. Si el borrador compila y está aprobado, se copia a final/
  5. Si se arregló un fallo, el revisor puede proponer una lección para memoria/

Las IAs reciben en cada mensaje las lecciones de memoria/ que encajan con los "temas" del
proyecto y con el error del momento (ver cerebro/memoria.py).

Uso:  python scripts/proyecto.py proyectos/<nombre>
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

from cerebro import memoria, nucleo
from cerebro import proveedores as prov

# ---------- Cronómetro ----------
# GitHub Actions corta el job a los 30 min (timeout-minutes del workflow) y entonces se pierde
# TODO el paso. Instalar LaTeX y subir el avance se llevan unos 3-4 min, así que el script tiene
# un presupuesto propio y, al acercarse, deja de llamar a IAs y termina guardando lo que haya.
PRESUPUESTO_MIN = float(os.environ.get("PRESUPUESTO_MINUTOS", "22"))
MIN_PARA_INTENTO = 6 * 60   # segundos que hacen falta para otro intento del constructor + su prueba
MIN_PARA_REVISOR = 4 * 60   # segundos que hacen falta para que el revisor conteste


class SinConstructor(Exception):
    """El constructor no ha podido dar el paso (sin IA disponible o sin tiempo)."""


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
- Si reescribes un archivo, conserva TODO lo que ya funcionaba (funciones, secciones...).
- Lee las LECCIONES DE LA MEMORIA: son errores que ya se resolvieron antes, en este u otros
  proyectos. No los repitas.

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

Comprobaciones (OBLIGATORIO):
- La prueba puede incluir un test automático que recalcula los valores por su cuenta. Si la prueba
  falla, el veredicto es "cambios": nunca apruebes algo que no pasa la prueba.
- Nunca digas que un cálculo, un valor o una tabla es "correcto", "verificado" o "comprobado" sin
  mostrar en COMPROBACIONES la operación completa o la cita de la fuente con la que lo has comparado.
  Ejemplo: "U1: impares (5−1)+(5−1)+(4−1)+(5−1)+(5−1)=19; pares (5−1)+(5−1)+(5−2)+(5−1)+(5−1)=19;
  (19+19)×2,5=95 → coincide con el documento".
- Lo que no hayas comprobado, dilo: "no comprobado". Un "aprobado" sin comprobaciones no cuenta.

Responde EXACTAMENTE con este formato:

<<<VEREDICTO>>>
aprobado   (o: cambios)
<<<COMPROBACIONES>>>
- una línea por cada cosa comprobada, con su operación o su cita
<<<COMENTARIOS>>>
Qué está bien, qué está mal y qué has corregido tú.
<<<ARCHIVO ruta/relativa.ext>>>
contenido COMPLETO corregido (opcional, solo si corriges algo)
<<<FIN>>>
<<<TAREAS>>>
- tareas concretas para el próximo paso del constructor
<<<TERMINADO>>>
no   (o: si)
<<<LECCION>>>
(OPCIONAL. Solo si en este paso se arregló un error que podría repetirse en otros proyectos y
que NO está ya en las lecciones de la memoria. Si no, omite este bloque.)
titulo: frase corta que resuma la regla
temas: temas separados por comas (p. ej. latex, lua, python)
claves: palabras exactas del mensaje de error, separadas por comas
problema: qué fallaba y por qué
solucion: qué hay que hacer
ejemplo: código mínimo correcto (opcional)"""


def muestra_operaciones(comprobaciones: str) -> bool:
    """True si al menos una línea de COMPROBACIONES enseña una operación o un valor comparado
    (un número junto a =, ≥, ≤, →, +, ×, −...). Un "todo verificado" a secas no vale."""
    return any(re.search(r"\d", l) and re.search(r"[=≥≤<>→+×*/−]", l)
               for l in comprobaciones.splitlines())


def dejar_de_seguir_ignorados(carpeta: Path):
    """Saca del repo (git rm --cached) los archivos del proyecto que ya están en .gitignore,
    p. ej. temporales que se subieron antes de ignorarlos. Solo en GitHub Actions."""
    if not os.environ.get("GITHUB_ACTIONS"):
        return
    try:
        r = subprocess.run(["git", "ls-files", "-ci", "--exclude-standard", "--", str(carpeta)],
                           capture_output=True, text=True, cwd=nucleo.RAIZ, timeout=60)
        rutas = [l for l in r.stdout.splitlines() if l.strip()]
        if rutas:
            subprocess.run(["git", "rm", "--cached", "-q", "--", *rutas], cwd=nucleo.RAIZ, timeout=60)
            print(f"Quitados del repo por estar en .gitignore: {', '.join(rutas)}")
    except Exception as e:  # la limpieza nunca debe tumbar el paso
        print(f"No pude limpiar archivos ignorados: {e}")


def guardar_cfg(cfg_ruta: Path, cfg: dict):
    cfg_ruta.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def pausar(cfg_ruta: Path, cfg: dict, bitacora: Path):
    """Freno: al llegar a max_pasos el proyecto se pausa y se avisa en la bitácora."""
    cfg["estado"] = "pausado"
    guardar_cfg(cfg_ruta, cfg)
    nucleo.anotar(bitacora, "⏸️ Proyecto pausado",
                  f"Se ha llegado al máximo de pasos ({cfg['pasos']} de {cfg['max_pasos']}). "
                  "El workflow no hará nada más hasta que Javier lo revise.\n\n"
                  "Para continuar: en `proyecto.json`, subir `max_pasos` y volver a poner "
                  "`\"estado\": \"en-construccion\"`.")
    print(f"Proyecto pausado: {cfg['pasos']}/{cfg['max_pasos']} pasos.")


def resumen_prueba(ok: bool, informe: str) -> str:
    """Una línea para la bitácora: ✅ o ❌ con el primer error que encuentre en el informe."""
    if ok:
        return "✅ pasa la prueba"
    lineas = [l.strip() for l in informe.splitlines()]
    candidatas = []
    if "Errores:" in lineas:
        candidatas = lineas[lineas.index("Errores:") + 1:]
    elif "Final de la salida:" in lineas:
        candidatas = [l for l in lineas[lineas.index("Final de la salida:") + 1:]
                      if re.search(r"ERROR|FALLID|Error|error|^-", l)] or lineas[-3:]
    else:
        candidatas = lineas[1:]
    # Mejor una línea con archivo:línea o "!" (error de TeX) que el ruido de alrededor
    importantes = [l for l in candidatas if re.search(r"^!|^\S+\.(tex|sty|cls|lua):\d+:|ERROR|FALLID", l)]
    primera = next((l for l in importantes + candidatas if l), "falla")
    return "❌ " + (primera[:150] + "…" if len(primera) > 150 else primera)


def probar(cfg: dict, carpeta: Path) -> tuple[bool, str]:
    """Ejecuta el comando de prueba del proyecto (compilar, tests...) y resume el resultado."""
    comando = cfg.get("comando_prueba")
    if not comando:
        return True, "Este proyecto no tiene comando de prueba."
    principal = cfg.get("archivo_principal")
    if principal and not (carpeta / principal).exists():
        return False, f"Todavía no existe el archivo principal {principal}."
    entorno = {**os.environ, "max_print_line": "1000"}  # que LaTeX no corte las líneas del log a 79 caracteres
    entorno["PYTHONDONTWRITEBYTECODE"] = "1"  # sin .pyc: un archivo reescrito en el mismo segundo no usa la versión vieja
    # Máximo 5 min, y nunca más de lo que queda de paso (con 30 s de margen)
    limite = int(max(30, min(300, prov.tiempo_restante() - 30)))
    try:
        r = subprocess.run(comando, shell=True, cwd=carpeta, capture_output=True,
                           text=True, timeout=limite, errors="replace", env=entorno)
    except subprocess.TimeoutExpired:
        return False, f"La prueba tardó más de {limite} s y se canceló (¿algo se queda colgado al compilar?)."

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
    cfg = json.loads(cfg_ruta.read_text(encoding="utf-8-sig"))
    bitacora = carpeta / "bitacora.md"
    estado_proyecto = cfg.get("estado", "en-construccion")
    if estado_proyecto != "en-construccion":
        print(f"Proyecto {estado_proyecto}. No hay nada que hacer.")
        return

    # ---------- 0. FRENO ----------
    # Cada ejecución cuenta un paso. Al llegar a max_pasos el proyecto se pausa.
    # Para que el workflow vaya rotando: se elige el proyecto que lleve más tiempo sin ejecutarse
    cfg["ultima_ejecucion"] = nucleo.ahora().isoformat(timespec="seconds")
    cfg["pasos"] = cfg.get("pasos", 0)
    max_pasos = cfg.get("max_pasos")
    if max_pasos is not None and cfg["pasos"] >= max_pasos:
        pausar(cfg_ruta, cfg, bitacora)  # p. ej. si alguien bajó max_pasos a mano
        return
    cfg["pasos"] += 1
    guardar_cfg(cfg_ruta, cfg)
    print(f"Paso {cfg['pasos']}" + (f" de {max_pasos}" if max_pasos is not None else ""))

    prov.fijar_limite(PRESUPUESTO_MIN * 60)
    try:
        dar_paso(carpeta, cfg, cfg_ruta, bitacora)
    except SinConstructor as e:
        # Si no hay IA (p. ej. Gemini saturado), el paso no cuenta y no se toca nada:
        # se reintenta en la próxima ejecución sin gastar del freno.
        cfg["pasos"] -= 1
        guardar_cfg(cfg_ruta, cfg)
        print(f"Paso no dado, no cuenta: {e}")
    finally:
        dejar_de_seguir_ignorados(carpeta)
        # Si este era el último paso permitido, se pausa ya: así la próxima ejecución
        # del workflow lo ve antes de instalar LaTeX y no gasta minutos.
        if (cfg.get("estado") == "en-construccion" and max_pasos is not None
                and cfg["pasos"] >= max_pasos):
            pausar(cfg_ruta, cfg, bitacora)


def dar_paso(carpeta: Path, cfg: dict, cfg_ruta: Path, bitacora: Path):
    """Un paso completo: constructor → prueba → revisor → promoción a final/."""
    spec = (carpeta / "spec.md").read_text(encoding="utf-8")
    borrador, final = carpeta / "borrador", carpeta / "final"
    borrador.mkdir(exist_ok=True)
    maximo = cfg.get("max_archivos_por_paso", 3)

    config, proveedores = prov.cargar(nucleo.RAIZ / "config" / "ias.json")
    # Un proyecto puede cambiar qué IAs hacen cada rol ("roles" en su proyecto.json)
    config = {**config, "roles": {**config.get("roles", {}), **cfg.get("roles", {})}}
    temas = cfg.get("temas", [])
    nombre = carpeta.name

    # ---------- 1. CONSTRUCTOR ----------
    ok_antes, prueba_antes = probar(cfg, borrador)
    reciente = nucleo.bitacora_reciente(bitacora)
    mensaje = f"""# SPEC DEL PROYECTO
{spec}

# LECCIONES DE LA MEMORIA (errores ya resueltos: no los repitas)
{memoria.seleccionar(temas, prueba_antes + reciente[-3000:])}

# BITÁCORA RECIENTE (incluye las tareas del revisor)
{reciente}

# ESTADO DE LA PRUEBA DEL BORRADOR
{prueba_antes}

# ARCHIVOS ACTUALES DEL BORRADOR
{nucleo.volcar(nucleo.leer_carpeta(borrador))}"""

    try:
        texto, ia, modelo = prov.pedir_rol("constructor", config, proveedores,
                                           SISTEMA_CONSTRUCTOR.format(maximo=maximo), mensaje)
    except (RuntimeError, prov.TiempoAgotado) as e:
        raise SinConstructor(str(e))
    paso = nucleo.parsear(texto)
    cambios = nucleo.aplicar(borrador, paso["archivos"], paso["borrar"], maximo)
    s = paso["secciones"]
    print(f"Constructor: {len(cambios)} cambios")

    # ---------- 2. PRUEBA + INTENTOS DE ARREGLO ----------
    # Si la prueba falla, el constructor recibe el error en el momento y puede corregirlo
    # (hasta max_intentos en total) en vez de esperar al siguiente paso.
    ok, prueba = probar(cfg, borrador)
    intentos = [f"intento 1: {resumen_prueba(ok, prueba)}"]
    print(f"Prueba tras constructor: {'OK' if ok else 'FALLA'}")
    max_intentos = cfg.get("max_intentos", 3)

    for n in range(2, max_intentos + 1):
        if ok:
            break
        if prov.tiempo_restante() < MIN_PARA_INTENTO + MIN_PARA_REVISOR:
            intentos.append(f"intento {n}: no se hace, queda poco tiempo de paso (⏱️ "
                            f"{int(prov.tiempo_restante() // 60)} min); se sigue en el próximo paso")
            break
        mensaje = f"""# TU PASO NO PASA LA PRUEBA (intento {n} de {max_intentos})
Corrige SOLO lo necesario para que la prueba pase. No añadas funcionalidades nuevas.
Lee el error con atención: indica archivo y línea. Si un arreglo anterior no funcionó, prueba otro enfoque.

# LO QUE HABÍAS HECHO EN ESTE PASO
{s.get('RESUMEN', '')}

# RESULTADO DE LA PRUEBA
{prueba}

# LECCIONES DE LA MEMORIA (puede que este error ya se haya resuelto antes)
{memoria.seleccionar(temas, prueba)}

# SPEC DEL PROYECTO
{spec}

# ARCHIVOS ACTUALES DEL BORRADOR
{nucleo.volcar(nucleo.leer_carpeta(borrador))}"""
        try:
            texto, ia, modelo = prov.pedir_rol("constructor", config, proveedores,
                                               SISTEMA_CONSTRUCTOR.format(maximo=maximo), mensaje)
        except (RuntimeError, prov.TiempoAgotado) as e:
            intentos.append(f"intento {n}: no hay IA disponible a tiempo ({e})")
            break
        arreglo = nucleo.parsear(texto)
        nuevos = nucleo.aplicar(borrador, arreglo["archivos"], arreglo["borrar"], maximo)
        if not nuevos:
            intentos.append(f"intento {n}: el constructor no cambió ningún archivo")
            break
        cambios += [c for c in nuevos if c not in cambios]
        ok, prueba = probar(cfg, borrador)
        intentos.append(f"intento {n}: {resumen_prueba(ok, prueba)} "
                        f"(tocó {', '.join(f'`{c}`' for c in nuevos)})")
        print(f"Prueba tras intento {n}: {'OK' if ok else 'FALLA'}")

    nucleo.anotar(bitacora, f"Constructor ({ia} · {modelo})",
                  f"{s.get('RESUMEN', '(sin resumen)')}\n\n"
                  f"**Archivos:** {', '.join(f'`{c}`' for c in cambios) or 'ninguno'}\n\n"
                  f"**Intentos:**\n" + "\n".join(f"- {i}" for i in intentos) + "\n\n"
                  f"**Siguiente:** {s.get('SIGUIENTE', '-')}")

    # ---------- 3. REVISOR ----------
    mensaje = f"""# SPEC DEL PROYECTO
{spec}

# LECCIONES DE LA MEMORIA (ya guardadas: no las repitas en LECCION)
{memoria.seleccionar(temas, prueba + chr(10).join(intentos))}

# BITÁCORA RECIENTE
{nucleo.bitacora_reciente(bitacora)}

# LO QUE ACABA DE HACER EL CONSTRUCTOR
{s.get('RESUMEN', '')}
Archivos tocados: {', '.join(cambios) or 'ninguno'}
Intentos de compilar/probar en este paso:
{chr(10).join(intentos)}

# RESULTADO DE LA PRUEBA
{prueba}

# ARCHIVOS DEL BORRADOR
{nucleo.volcar(nucleo.leer_carpeta(borrador))}"""

    try:
        if prov.tiempo_restante() < MIN_PARA_REVISOR:
            raise prov.TiempoAgotado(f"⏱️ Solo quedan {int(prov.tiempo_restante())} s de paso: "
                                     "no da tiempo a que conteste el revisor.")
        texto, ia, modelo = prov.pedir_rol("revisor", config, proveedores,
                                           SISTEMA_REVISOR.format(maximo=maximo), mensaje)
    except (RuntimeError, prov.TiempoAgotado) as e:
        # El trabajo del constructor no se pierde: queda en el borrador, sin revisar
        nucleo.anotar(bitacora, "⚠️ Revisor no disponible",
                      f"{e}\n\nEl paso del constructor queda en `borrador/` sin revisar. "
                      f"Prueba: {'✅ compila' if ok else '❌ falla'}. Se revisará en el próximo paso.")
        print(e)
        return
    revision = nucleo.parsear(texto)
    correcciones = nucleo.aplicar(borrador, revision["archivos"], revision["borrar"], maximo)
    if correcciones:
        ok, prueba = probar(cfg, borrador)
        print(f"Prueba tras correcciones: {'OK' if ok else 'FALLA'}")

    r = revision["secciones"]
    veredicto = r.get("VEREDICTO", "cambios").strip().lower()
    terminado = r.get("TERMINADO", "no").strip().lower().startswith("s")
    comprobaciones = r.get("COMPROBACIONES", "").strip()

    # Un revisor que aprueba sin enseñar las operaciones no prueba nada (lección aprendida):
    # su aprobado y su "terminado" no cuentan.
    aviso_comprobaciones = ""
    if not muestra_operaciones(comprobaciones) and (veredicto.startswith("aprobado") or terminado):
        aviso_comprobaciones = ("\n\n⚠️ **El revisor aprueba sin mostrar operaciones en COMPROBACIONES:** "
                                "su aprobado y su \"terminado\" no cuentan en este paso.")
        veredicto = f"cambios (había dicho: {veredicto})"
        terminado = False
    elif not ok and veredicto.startswith("aprobado"):
        # Nunca se aprueba algo que no pasa la prueba
        veredicto = f"cambios (había dicho: {veredicto}, pero la prueba falla)"

    # ---------- 4. PROMOCIÓN A FINAL ----------
    promocionado = ok and (veredicto.startswith("aprobado") or bool(correcciones))
    if promocionado:
        nucleo.promocionar(borrador, final)

    resultado = "✅ compila" if ok else "❌ falla la prueba"
    nucleo.anotar(bitacora, f"Revisor ({ia} · {modelo})",
                  f"**Veredicto:** {veredicto} · **Prueba:** {resultado}"
                  f"{' · copiado a `final/`' if promocionado else ''}\n\n"
                  f"**Comprobaciones:**\n{comprobaciones or '(ninguna)'}{aviso_comprobaciones}\n\n"
                  f"{r.get('COMENTARIOS', '(sin comentarios)')}\n\n"
                  f"**Correcciones del revisor:** {', '.join(f'`{c}`' for c in correcciones) or 'ninguna'}\n\n"
                  f"**Tareas para el constructor:**\n{r.get('TAREAS', '- ninguna')}")

    # ---------- 5. MEMORIA ----------
    # Si en este paso se arregló un fallo y la prueba pasa, la lección que proponga el revisor
    # se guarda como "propuesta" (una persona la confirma luego).
    hubo_fallo = not ok_antes or any("❌" in i for i in intentos)
    if ok and (hubo_fallo or correcciones) and r.get("LECCION", "").strip():
        guardada = memoria.guardar_propuesta(r["LECCION"], nombre)
        if guardada:
            nucleo.anotar(bitacora, "🧠 Lección propuesta para la memoria",
                          f"[[{guardada}]] (pendiente de confirmar en `memoria/lecciones/`).")
            print(f"Lección propuesta: {guardada}")

    if terminado and ok:
        cfg["estado"] = "terminado"
        guardar_cfg(cfg_ruta, cfg)
        nucleo.anotar(bitacora, "🎉 Proyecto terminado", "El revisor da por cumplidos todos los criterios de la spec.")
        print("¡Proyecto terminado!")


if __name__ == "__main__":
    main()
