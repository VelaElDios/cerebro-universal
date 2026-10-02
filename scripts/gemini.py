"""
Cerebro Universal - agente Gemini

1. Lee las notas del cerebro (todas las carpetas notas-*)
2. Lee config/temas.md (lo que Javier quiere explorar)
3. Le pasa todo ese contexto a Gemini
4. Gemini escribe UNA nota nueva, enlazada con [[...]] a las existentes
5. La guarda en notas-gemini/AAAA-MM-DD/<Título>.md
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from google import genai
from google.genai import errors, types

RAIZ = Path(__file__).resolve().parent.parent
CARPETA_SALIDA = RAIZ / "notas-gemini"
ARCHIVO_TEMAS = RAIZ / "config" / "temas.md"
ZONA = ZoneInfo("Europe/Madrid")

# Plan A, B y C: si un modelo está saturado o no existe, pasa al siguiente
MODELOS = [m.strip() for m in os.environ.get(
    "GEMINI_MODELS", "gemini-flash-latest,gemini-3.5-flash-lite,gemini-2.5-flash"
).split(",") if m.strip()]
ESPERAS = [0, 30, 90]  # segundos de espera antes de cada intento con el mismo modelo

MAX_NOTAS_CONTEXTO = 15     # notas recientes que Gemini lee enteras
MAX_CHARS_POR_NOTA = 1500   # recorte por nota para no gastar tokens de más
PATRON_FECHA = re.compile(r"\d{4}-\d{2}-\d{2}")


def fecha_de_carpeta(ruta: Path) -> str:
    """Saca la fecha de la carpeta (2026-10-02) para ordenar las notas."""
    for parte in ruta.parts:
        if PATRON_FECHA.fullmatch(parte):
            return parte
    return "0000-00-00"


def notas_del_cerebro() -> list[Path]:
    """Todas las notas de todas las IAs, de más nueva a más vieja."""
    notas = []
    for carpeta in RAIZ.glob("notas-*"):
        notas.extend(p for p in carpeta.rglob("*.md") if not p.stem.startswith("_"))
    return sorted(notas, key=fecha_de_carpeta, reverse=True)


def quitar_frontmatter(texto: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", texto, count=1, flags=re.DOTALL).strip()


def nombre_seguro(titulo: str) -> str:
    """Título válido como nombre de archivo (y como enlace de Obsidian)."""
    limpio = re.sub(r'[\\/:*?"<>|#^\[\]]', "", titulo)
    limpio = re.sub(r"\s+", " ", limpio).strip()[:80]
    return limpio or "Nota sin título"


def construir_prompt(notas: list[Path]) -> str:
    if ARCHIVO_TEMAS.exists():
        temas = quitar_frontmatter(ARCHIVO_TEMAS.read_text(encoding="utf-8")) or "(vacío)"
    else:
        temas = "(sin temas definidos: elige tú algo interesante sobre tecnología, IA o ciencia)"

    titulos = "\n".join(f"- {p.stem}" for p in notas) or "(el cerebro está vacío: esta es la primera nota)"

    bloques = []
    for p in notas[:MAX_NOTAS_CONTEXTO]:
        autor = p.relative_to(RAIZ).parts[0].replace("notas-", "")
        cuerpo = quitar_frontmatter(p.read_text(encoding="utf-8"))[:MAX_CHARS_POR_NOTA]
        bloques.append(f"### {p.stem} (escrita por {autor})\n{cuerpo}")
    contexto = "\n\n".join(bloques) or "(no hay notas todavía)"

    return f"""Eres el agente Gemini dentro de "Cerebro Universal": una base de conocimiento
en Obsidian que comparten varias IAs y un humano, Javier. Cada nota se enlaza con las
demás y entre todas forman un grafo que crece.

Tu tarea: escribir UNA nota nueva que aporte algo que todavía no esté en el cerebro.
Puede ampliar, conectar o cuestionar notas existentes.

Reglas:
- Escribe en español.
- Enlaza con [[Título exacto]] SOLO a notas de la lista de títulos existentes. No inventes enlaces.
- Si hay notas relacionadas, enlaza al menos a una o dos.
- No repitas temas ya tratados.
- El contenido va en Markdown, sin frontmatter y sin repetir el título como encabezado.
- Entre 200 y 500 palabras.

Temas que Javier quiere explorar:
{temas}

Títulos existentes en el cerebro:
{titulos}

Contenido de las notas más recientes:
{contexto}

Responde SOLO con un JSON con esta forma:
{{"titulo": "...", "tags": ["...", "..."], "contenido": "..."}}"""


def parsear_respuesta(texto: str) -> dict:
    texto = re.sub(r"^```(?:json)?|```$", "", texto.strip(), flags=re.MULTILINE).strip()
    datos = json.loads(texto)
    if not datos.get("titulo") or not datos.get("contenido"):
        raise ValueError("La respuesta no trae titulo o contenido")
    return datos


def guardar_nota(datos: dict, modelo: str) -> Path:
    ahora = datetime.now(ZONA)
    carpeta = CARPETA_SALIDA / ahora.strftime("%Y-%m-%d")
    carpeta.mkdir(parents=True, exist_ok=True)

    nombre = nombre_seguro(datos["titulo"])
    ruta = carpeta / f"{nombre}.md"
    if ruta.exists():
        ruta = carpeta / f"{nombre} ({ahora.strftime('%H%M')}).md"

    tags = [re.sub(r"\s+", "-", str(t).strip().lstrip("#")) for t in datos.get("tags", []) if str(t).strip()]
    frontmatter = "\n".join([
        "---",
        f"titulo: {json.dumps(datos['titulo'], ensure_ascii=False)}",
        "createdBy: gemini",
        f"model: {modelo}",
        f"createdAt: {ahora.strftime('%Y-%m-%d %H:%M')}",
        f"tags: {json.dumps(tags, ensure_ascii=False)}",
        "---",
    ])
    ruta.write_text(f"{frontmatter}\n\n{datos['contenido'].strip()}\n", encoding="utf-8")
    return ruta


def pedir_a_gemini(cliente, prompt: str) -> tuple[dict, str]:
    """Prueba cada modelo con varios intentos. Devuelve (datos, modelo que respondió)."""
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        temperature=0.9,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )

    for modelo in MODELOS:
        for intento, espera in enumerate(ESPERAS, start=1):
            if espera:
                print(f"  Esperando {espera}s antes de reintentar...")
                time.sleep(espera)
            print(f"Modelo {modelo}, intento {intento}/{len(ESPERAS)}")
            try:
                respuesta = cliente.models.generate_content(model=modelo, contents=prompt, config=config)
                return parsear_respuesta(respuesta.text), modelo

            except errors.ServerError as e:
                # 500/503: Google saturado -> esperar y reintentar el mismo modelo
                print(f"  Servidor ocupado ({e.code}): {e.message}")

            except errors.ClientError as e:
                if e.code in (404, 429):
                    # Modelo inexistente o cupo agotado -> pasar directamente al siguiente
                    print(f"  {e.code} con {modelo}: {e.message}. Paso al siguiente modelo.")
                    break
                raise  # 400/401/403: key mal puesta o petición rota, no tiene sentido reintentar

            except (json.JSONDecodeError, ValueError) as e:
                print(f"  Respuesta ilegible: {e}")

    sys.exit("Ningún modelo ha respondido. Se volverá a intentar en la próxima ejecución.")


def main():
    clave = os.environ.get("GEMINI_API_KEY")
    if not clave:
        sys.exit("Falta GEMINI_API_KEY. ¿Está creado el secret en GitHub?")

    notas = notas_del_cerebro()
    print(f"Notas en el cerebro: {len(notas)}")

    cliente = genai.Client(api_key=clave)
    datos, modelo = pedir_a_gemini(cliente, construir_prompt(notas))
    ruta = guardar_nota(datos, modelo)
    print(f"Nota creada con {modelo}: {ruta.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
