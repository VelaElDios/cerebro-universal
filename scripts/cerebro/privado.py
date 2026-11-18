"""
Modo privado: lo que Javier sube a la carpeta privado/ del repo privado (cerebro-datos) genera conocimiento
que NUNCA llega al vault público. Las notas privadas viven en cerebro-datos/conocimiento/, las IAs las usan
igual que las demás (conocimiento.seleccionar las incluye, marcadas como privadas), pero no salen en el
grafo, los mapas, los índices ni los embeddings públicos, y el jardinero no las mezcla con las públicas.

En cada ejecución el repo privado se descarga en .cerebro-privado/ (ignorado por git) y al final se suben
los cambios. Sin DATOS_TOKEN no hay modo privado: todo sigue funcionando con lo público.
"""

import os
import subprocess
from pathlib import Path

from . import nucleo

CARPETA = ".cerebro-privado"


def ruta() -> Path:
    return nucleo.RAIZ / CARPETA


def disponible() -> bool:
    return (ruta() / ".git").exists() or (ruta() / "conocimiento").exists()


def carpeta_conocimiento() -> Path:
    return ruta() / "conocimiento"


def _git(*args, cwd=None, timeout=180) -> subprocess.CompletedProcess:
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
    return subprocess.run(["git", *args], cwd=cwd or ruta(), capture_output=True, text=True, timeout=timeout, env=env)


def _ocultar(texto: str) -> str:
    token = os.environ.get("DATOS_TOKEN", "")
    return texto.replace(token, "***") if token else texto


def preparar() -> str:
    """Descarga (o actualiza) el repo privado en .cerebro-privado/. Nunca tumba un paso."""
    token, repo = os.environ.get("DATOS_TOKEN"), os.environ.get("DATOS_REPO")
    if not (token and repo):
        return "modo privado: sin DATOS_TOKEN/DATOS_REPO"
    url = f"https://x-access-token:{token}@github.com/{repo}.git"
    try:
        if (ruta() / ".git").exists():
            r = _git("pull", "-q", "--rebase")
        else:
            r = _git("clone", "-q", "--depth", "1", url, str(ruta()), cwd=nucleo.RAIZ)
        if r.returncode:
            return "modo privado: no pude descargar el repo privado: " + _ocultar(r.stderr)[:200]
        _git("config", "user.name", "cerebro-bot")
        _git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        n = len(list(carpeta_conocimiento().rglob("*.md"))) if carpeta_conocimiento().exists() else 0
        return f"modo privado: listo ({n} notas privadas)"
    except Exception as e:
        return f"modo privado: no disponible ({_ocultar(str(e))[:200]})"


def subir(mensaje: str) -> str:
    """Sube lo que haya cambiado en el repo privado (notas privadas, registros...)."""
    if not (ruta() / ".git").exists():
        return "modo privado: nada que subir"
    try:
        _git("add", "-A")
        if _git("diff", "--staged", "--quiet").returncode == 0:
            return "modo privado: sin cambios"
        _git("commit", "-q", "-m", mensaje)
        for _ in range(3):
            if _git("push", "-q").returncode == 0:
                return "modo privado: cambios subidos"
            _git("pull", "-q", "--rebase")
        return "modo privado: no se pudo subir tras 3 intentos"
    except Exception as e:
        return f"modo privado: error al subir ({_ocultar(str(e))[:200]})"
