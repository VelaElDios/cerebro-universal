#!/usr/bin/env python3
"""
Servidor MCP del Cerebro: conecta el vault a cualquier IA de chat que hable MCP (Claude Desktop, Claude Code,
ChatGPT, Cursor...). Así, desde un chat, la IA puede buscar en lo que sabe el cerebro, leer notas y fichas
de proyectos, y guardar lo que aprenda en la conversación (queda como «propuesto» hasta que se compruebe).

Se ejecuta en el PC de Javier, sobre el vault de Obsidian (Obsidian lo sube a GitHub como siempre):

    pip install "mcp" google-genai          (google-genai solo hace falta para buscar por significado)
    python scripts/mcp_cerebro.py           (lo arranca el cliente MCP, no hace falta lanzarlo a mano)

En Claude Desktop (Configuración → Desarrollador → Editar configuración), en claude_desktop_config.json:

    {"mcpServers": {"cerebro": {"command": "python",
        "args": ["C:\\\\Users\\\\Vela\\\\Documents\\\\cerebro-universal\\\\scripts\\\\mcp_cerebro.py"],
        "env": {"GEMINI_API_KEY": "(opcional: tu clave, para buscar por significado)"}}}}
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cerebro import conocimiento, mapas, memoria, nucleo  # noqa: E402

try:                                    # mcp 2.x
    from mcp.server.mcpserver import MCPServer
except ImportError:                     # mcp 1.x
    from mcp.server.fastmcp import FastMCP as MCPServer

INSTRUCCIONES = (open(nucleo.RAIZ / "memoria" / "CEREBRO.md", encoding="utf-8").read()[:3000]
                 if (nucleo.RAIZ / "memoria" / "CEREBRO.md").exists() else "Memoria compartida de las IAs de Javier.")

servidor = MCPServer("cerebro", instructions=INSTRUCCIONES)


def _dentro_del_vault(ruta: str) -> Path:
    p = (nucleo.RAIZ / ruta).resolve()
    if nucleo.RAIZ.resolve() not in p.parents or p.suffix != ".md" or ".obsidian" in p.parts:
        raise ValueError("Solo se pueden leer notas .md del vault")
    return p


@servidor.tool()
def buscar(consulta: str, temas: str = "", max_caracteres: int = 8000) -> str:
    """Busca en el conocimiento del cerebro (recetas, decisiones, conceptos, datos) y en las lecciones lo más
    relacionado con la consulta. Úsalo ANTES de responder sobre los proyectos de Javier o cómo se hace algo
    en ellos. `temas`: opcional, separados por comas (latex, saas, scrum...)."""
    lista = [t.strip() for t in temas.split(",") if t.strip()]
    max_caracteres = max(1000, min(int(max_caracteres), 20000))
    texto = conocimiento.seleccionar(lista, consulta, "", max_chars=max_caracteres)
    usadas = conocimiento.ultimas_usadas()
    lecciones = memoria.seleccionar(lista, consulta, max_chars=2500)
    return (f"{texto}\n\n# Lecciones (errores ya resueltos)\n{lecciones}\n\n"
            f"(Notas usadas: {', '.join(usadas) or 'ninguna'}. Léelas enteras con leer_nota.)")


@servidor.tool()
def leer_nota(ruta: str) -> str:
    """Lee una nota entera del vault por su ruta (p. ej. memoria/conocimiento/recetas/xxx.md o
    proyectos/memoria-procesos/estado.md)."""
    return _dentro_del_vault(ruta).read_text(encoding="utf-8")


@servidor.tool()
def mapa() -> str:
    """Índice de todo lo que sabe el cerebro, por temas, y la lista de proyectos con su estado."""
    proyectos = "\n".join(f"- {p['nombre']} ({p['estado']}): {p['ruta']}" for p in mapas.proyectos())
    return f"# Proyectos\n{proyectos}\n\n# Conocimiento por temas\n{conocimiento.mapa_textual(max_chars=8000)}"


@servidor.tool()
def ficha_proyecto(nombre: str) -> str:
    """La ficha de un proyecto (qué es, decisiones y convenciones, estado y siguiente paso)."""
    carpeta = nucleo.RAIZ / "proyectos" / nombre
    if not carpeta.is_dir():
        return f"No existe el proyecto «{nombre}». Usa mapa() para ver la lista."
    return conocimiento.leer_estado(carpeta)


@servidor.tool()
def guardar_conocimiento(tipo: str, titulo: str, contenido: str, temas: str = "", claves: str = "",
                         fuente: str = "", cita: str = "", proyecto: str = "") -> str:
    """Guarda en el cerebro algo útil aprendido en esta conversación para que lo usen las demás IAs.
    tipo: concepto | receta | decision | dato. Si `fuente` es un archivo del vault y `cita` aparece literal en
    él, la nota queda «verificado»; si no, «propuesto». Si ya existe una nota con ese título, se amplía."""
    bloque = (f"tipo: {tipo}\ntitulo: {titulo}\ntemas: {temas}\nclaves: {claves}\nfuente: {fuente or 'chat'}\n"
              f"cita: {cita}\ncontenido:\n{contenido}")
    verificacion = ""
    if fuente:
        try:
            verificacion = _dentro_del_vault(fuente).read_text(encoding="utf-8")
        except Exception:
            verificacion = ""
    guardadas = conocimiento.guardar(bloque, proyecto, verificacion=verificacion)
    if not guardadas:
        return "No se guardó: revisa que tipo sea concepto/receta/decision/dato y que el contenido no esté vacío."
    mapas.generar()
    return f"Guardado: {', '.join(guardadas)} (se subirá a GitHub con Obsidian)."


if __name__ == "__main__":
    servidor.run()
