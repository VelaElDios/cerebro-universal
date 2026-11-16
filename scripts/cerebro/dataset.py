"""
Datos para entrenar una IA local: cada llamada a una IA (qué se le pidió, qué contestó y qué pasó después)
se guarda como una línea JSON. Con eso, el día de mañana se puede:

  - afinar un modelo local con los pasos que salieron bien (ejemplos «pregunta → buena respuesta»);
  - enseñarle a preferir lo bueno con las parejas deshecho / aceptado del mismo paso;
  - y usar el conocimiento del vault (export/conocimiento.jsonl) como documentos para RAG.

Como los mensajes llevan mucho texto (fuentes, archivos del borrador), los datos NO van al repo público:
se suben a un repo PRIVADO aparte, comprimidos por meses:

  <repo privado>/datos/AAAA-MM/<proyecto>.jsonl.gz     una línea por llamada a una IA
  <repo privado>/export/conocimiento.jsonl             todo el conocimiento del vault, listo para RAG

Configuración (secrets/variables del workflow): DATOS_TOKEN (token con permiso de escritura en el repo
privado) y DATOS_REPO (p. ej. VelaElDios/cerebro-datos). Sin ellos, los datos se guardan solo en
.cerebro-datos/ (ignorado por git) y en GitHub Actions se pierden al acabar: no rompe nada.
"""

import gzip
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from . import nucleo

_registros: list[dict] = []


def registrar(proyecto: str, rol: str, etapa: str, proveedor: str, modelo: str, sistema: str, mensaje: str,
              respuesta: str) -> int:
    """Apunta una llamada. Devuelve su índice para completar luego qué pasó (resultado)."""
    _registros.append({"fecha": nucleo.ahora().isoformat(timespec="seconds"), "proyecto": proyecto, "rol": rol,
                       "etapa": etapa, "proveedor": proveedor, "modelo": modelo, "sistema": sistema,
                       "mensaje": mensaje, "respuesta": respuesta, "resultado": {}})
    return len(_registros) - 1


def resultado(indice: int | None, **datos):
    """Qué pasó con esa respuesta: prueba ok, deshecho, veredicto del revisor..."""
    if indice is not None and 0 <= indice < len(_registros):
        _registros[indice]["resultado"].update(datos)


def pendientes() -> list[dict]:
    return list(_registros)


def exportar_conocimiento() -> list[dict]:
    """El vault como documentos (para RAG o para afinar): una línea por nota con su texto completo."""
    filas = []
    for carpeta, tipo_fijo in [("memoria/conocimiento", None), ("memoria/lecciones", "leccion")]:
        base = nucleo.RAIZ / carpeta
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.md")):
            texto = p.read_text(encoding="utf-8", errors="replace")
            m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
            meta = {}
            if m:
                for linea in m.group(1).splitlines():
                    if ":" in linea:
                        k, v = linea.split(":", 1)
                        try:
                            meta[k.strip()] = json.loads(v.strip())
                        except json.JSONDecodeError:
                            meta[k.strip()] = v.strip().strip("'\"")
                texto = m.group(2)
            filas.append({"id": p.relative_to(nucleo.RAIZ).as_posix(), "tipo": meta.get("tipo", tipo_fijo),
                          "titulo": meta.get("titulo", p.stem), "temas": meta.get("temas", []),
                          "proyectos": meta.get("proyectos", []),
                          "confianza": meta.get("confianza", "verificado" if meta.get("estado") == "confirmada" else "propuesto"),
                          "texto": re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", texto).strip()})
    for estado in sorted((nucleo.RAIZ / "proyectos").glob("*/estado.md")):
        texto = estado.read_text(encoding="utf-8", errors="replace")
        filas.append({"id": estado.relative_to(nucleo.RAIZ).as_posix(), "tipo": "proyecto",
                      "titulo": estado.parent.name, "temas": [], "proyectos": [estado.parent.name],
                      "confianza": "verificado", "texto": re.sub(r"^---\n.*?\n---\n", "", texto, flags=re.S)})
    return filas


def _escribir_en(base: Path, proyecto: str):
    mes = f"{nucleo.ahora():%Y-%m}"
    destino = base / "datos" / mes / f"{proyecto or 'cerebro'}.jsonl.gz"
    destino.parent.mkdir(parents=True, exist_ok=True)
    # gzip admite «miembros» concatenados: se puede añadir al final sin reescribir el archivo
    with gzip.open(destino, "at", encoding="utf-8") as f:
        for r in _registros:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    export = base / "export" / "conocimiento.jsonl"
    export.parent.mkdir(parents=True, exist_ok=True)
    export.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in exportar_conocimiento()),
                      encoding="utf-8")


def subir(proyecto: str) -> str:
    """Guarda lo apuntado en el repo privado (o en local si no está configurado). Nunca tumba un paso."""
    if not _registros:
        return "sin llamadas que guardar"
    token, repo = os.environ.get("DATOS_TOKEN"), os.environ.get("DATOS_REPO")
    try:
        if not (token and repo):
            local = nucleo.RAIZ / ".cerebro-datos"
            _escribir_en(local, proyecto)
            n = len(_registros)
            _registros.clear()
            return f"{n} llamadas guardadas en local (.cerebro-datos/): falta DATOS_TOKEN/DATOS_REPO para el repo privado"
        tmp = Path(tempfile.mkdtemp())
        url = f"https://x-access-token:{token}@github.com/{repo}.git"
        env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}

        def git(*args, ok_fallo=False):
            r = subprocess.run(["git", *args], cwd=tmp / "r", capture_output=True, text=True, timeout=180, env=env)
            if r.returncode and not ok_fallo:
                raise RuntimeError((r.stderr or r.stdout).replace(token, "***")[:300])
            return r

        r = subprocess.run(["git", "clone", "--depth", "1", "--quiet", url, str(tmp / "r")],
                           capture_output=True, text=True, timeout=180, env=env)
        if r.returncode:
            raise RuntimeError(r.stderr.replace(token, "***")[:300])
        _escribir_en(tmp / "r", proyecto)
        git("config", "user.name", "cerebro-bot")
        git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        git("add", "-A")
        git("commit", "-q", "-m", f"datos: {proyecto} {nucleo.ahora():%Y-%m-%d %H:%M}")
        for _ in range(3):
            if git("push", "-q", ok_fallo=True).returncode == 0:
                break
            git("pull", "--rebase", "-q", ok_fallo=True)
        else:
            raise RuntimeError("no se pudo subir tras 3 intentos")
        n = len(_registros)
        _registros.clear()
        shutil.rmtree(tmp, ignore_errors=True)
        return f"{n} llamadas subidas al repo privado {repo}"
    except Exception as e:
        return f"no pude guardar los datos de entrenamiento: {e}"
