"""
Medios: convertir CUALQUIER cosa que Javier suba en texto que el cerebro pueda aprender.

  texto (md, txt, código...)      se lee tal cual
  PDF                             pdftotext; si casi no tiene texto (escaneado, diapositivas), lo lee Gemini
  Word, PowerPoint, Excel         python-docx, python-pptx y openpyxl (si no están, lo lee Gemini)
  HTML                            se quita el código y queda el texto
  imágenes (fotos, diagramas...)  Gemini: texto literal, diagramas como listas, tablas, fórmulas
  audio                           Gemini: transcripción con marcas de tiempo
  vídeo                           Gemini: transcripción + lo que se ve (diapositivas, código, diagramas)
  enlaces                         un archivo enlaces*.txt (o .url) con una URL por línea:
                                  YouTube lo ve Gemini directamente; otras webs se descargan y se pasan a texto

Lo que sale de una IA (imágenes, audio, vídeo) es una «transcripción»: la fuente derivada contra la que se
comprueban las citas de las notas. Se guarda en el repo privado (transcripciones/) para no repetirla.

Todo con la API gratuita de Gemini (GEMINI_API_KEY), que ya usa el cerebro. Ojo: la capa gratuita tiene
límites diarios (peticiones y horas de vídeo de YouTube); lo que no dé tiempo se hace en la siguiente ejecución.
"""

import html
import mimetypes
import os
import re
import shutil
import subprocess
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

from . import proveedores as prov

TEXTO = {".md", ".txt", ".tex", ".csv", ".json", ".py", ".js", ".ts", ".sql", ".yml", ".yaml", ".lua",
         ".java", ".c", ".cpp", ".h", ".cs", ".go", ".rs", ".rb", ".php", ".css", ".xml", ".bib", ".ini", ".toml"}
HTML = {".html", ".htm"}
OFFICE = {".docx", ".pptx", ".xlsx"}
IMAGEN = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".heic", ".heif"}
AUDIO = {".mp3", ".m4a", ".wav", ".ogg", ".flac", ".aac", ".opus"}
VIDEO = {".mp4", ".mov", ".webm", ".mkv", ".avi", ".mpeg", ".mpg", ".3gp"}
MODELOS_GEMINI = ["gemini-flash-latest", "gemini-3.5-flash-lite"]
MIN_CHARS_POR_PAGINA = 300     # menos que esto en un PDF = escaneado o diapositivas: mejor que lo lea Gemini

PROMPTS = {
    "imagen": """Convierte esta imagen en texto para una base de conocimiento, sin perder nada:
1. Todo el texto que aparece, LITERAL (apuntes a mano incluidos), en orden de lectura.
2. Si hay diagramas o esquemas: cada caja o nodo y cada flecha o relación, como lista («A → B: etiqueta»).
3. Tablas en Markdown, fórmulas en LaTeX y código tal cual.
4. Al final, «## Qué explica»: 3-6 frases con la idea principal.
No inventes nada que no se vea. Responde solo con el contenido, en Markdown y en el idioma del original.""",
    "audio": """Transcribe este audio para una base de conocimiento:
1. «## Transcripción»: lo que se dice, LITERAL, por párrafos y con una marca de tiempo [mm:ss] cada minuto
   más o menos. Si hablan varias personas, indica quién («Persona 1:»).
2. «## Temas»: lista de los temas tratados con su marca de tiempo.
No resumas la transcripción ni inventes nada. Responde solo con el contenido, en Markdown y en el idioma del original.""",
    "video": """Convierte este vídeo en texto para una base de conocimiento:
1. «## Transcripción»: lo que se dice, LITERAL, por párrafos y con una marca de tiempo [mm:ss] cada minuto más o menos.
2. «## Lo que se ve»: con marcas de tiempo, el texto de las diapositivas o la pizarra, el código que aparece
   (tal cual), los diagramas (nodos y flechas como lista) y cualquier demostración importante.
3. «## Temas»: lista de los temas tratados con su marca de tiempo.
No inventes nada. Responde solo con el contenido, en Markdown y en el idioma del original.""",
    "documento": """Convierte este documento en texto para una base de conocimiento, sin perder nada: el texto LITERAL en orden de
lectura, las tablas en Markdown, las fórmulas en LaTeX, el código tal cual y cada diagrama o figura descrito
como lista de elementos y relaciones («A → B»). Responde solo con el contenido, en Markdown.""",
}


class NoSePuede(Exception):
    """Este archivo no se puede convertir ahora (falta la API, formato raro...)."""


def tipo_de(nombre: str) -> str:
    ext = Path(nombre).suffix.lower()
    if nombre.startswith(("http://", "https://")):
        return "youtube" if re.search(r"(youtube\.com|youtu\.be)/", nombre) else "web"
    if Path(nombre).name.lower().startswith("enlaces") and ext in (".txt", ".md") or ext == ".url":
        return "enlaces"
    for tipo, exts in (("texto", TEXTO), ("html", HTML), ("office", OFFICE), ("imagen", IMAGEN),
                       ("audio", AUDIO), ("video", VIDEO)):
        if ext in exts:
            return tipo
    return "pdf" if ext == ".pdf" else "desconocido"


def enlaces_de(ruta: Path) -> list[str]:
    """URLs de un archivo de enlaces (una por línea; vale el formato [InternetShortcut] URL=...)."""
    texto = ruta.read_text(encoding="utf-8", errors="replace")
    return list(dict.fromkeys(re.findall(r"https?://[^\s<>\")\]]+", texto)))


# ---------- Sin IA ----------

class _Texto(HTMLParser):
    SALTAR = {"script", "style", "noscript", "svg", "nav", "footer", "header"}

    def __init__(self):
        super().__init__()
        self.partes, self._saltar = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SALTAR:
            self._saltar += 1
        elif tag in ("p", "br", "li", "h1", "h2", "h3", "h4", "tr", "div", "pre"):
            self.partes.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SALTAR and self._saltar:
            self._saltar -= 1

    def handle_data(self, data):
        if not self._saltar:
            self.partes.append(data)


def html_a_texto(codigo: str) -> str:
    p = _Texto()
    p.feed(codigo)
    texto = html.unescape("".join(p.partes))
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", texto)).strip()


def pdf_a_texto(ruta: Path) -> tuple[str, int]:
    """(texto, número de páginas) con pdftotext."""
    if not shutil.which("pdftotext"):
        return "", 0
    r = subprocess.run(["pdftotext", "-layout", str(ruta), "-"], capture_output=True, text=True,
                       errors="replace", timeout=300)
    texto = r.stdout if r.returncode == 0 else ""
    return texto, max(1, texto.count("\f"))


def office_a_texto(ruta: Path) -> str:
    ext = ruta.suffix.lower()
    if ext == ".docx":
        import docx  # python-docx
        d = docx.Document(str(ruta))
        partes = [p.text for p in d.paragraphs]
        for t in d.tables:
            for fila in t.rows:
                partes.append(" | ".join(c.text.strip() for c in fila.cells))
        return "\n".join(partes)
    if ext == ".pptx":
        import pptx  # python-pptx
        partes = []
        for i, diapo in enumerate(pptx.Presentation(str(ruta)).slides, start=1):
            partes.append(f"\n## Diapositiva {i}")
            for forma in diapo.shapes:
                if getattr(forma, "has_text_frame", False) and forma.text_frame.text.strip():
                    partes.append(forma.text_frame.text)
            if diapo.has_notes_slide and diapo.notes_slide.notes_text_frame.text.strip():
                partes.append("Notas: " + diapo.notes_slide.notes_text_frame.text)
        return "\n".join(partes)
    if ext == ".xlsx":
        import openpyxl
        partes = []
        for hoja in openpyxl.load_workbook(str(ruta), read_only=True, data_only=True).worksheets:
            partes.append(f"\n## Hoja {hoja.title}")
            for fila in hoja.iter_rows(values_only=True):
                if any(v is not None for v in fila):
                    partes.append(" | ".join("" if v is None else str(v) for v in fila))
        return "\n".join(partes)
    raise NoSePuede(f"formato de Office no soportado: {ext}")


def descargar_web(url: str) -> str:
    peticion = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (cerebro-universal)"})
    with urllib.request.urlopen(peticion, timeout=60) as r:
        tipo = r.headers.get("Content-Type", "")
        datos = r.read(15_000_000)
    if "pdf" in tipo:
        tmp = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "cerebro-web.pdf"
        tmp.write_bytes(datos)
        return pdf_a_texto(tmp)[0]
    return html_a_texto(datos.decode("utf-8", errors="replace"))


# ---------- Con Gemini (imágenes, audio, vídeo, YouTube, PDF escaneados) ----------

def _cliente():
    clave = os.environ.get("GEMINI_API_KEY", "").strip()
    if not clave:
        raise NoSePuede("falta GEMINI_API_KEY para leer imágenes, audio o vídeo")
    from google import genai
    from google.genai import types
    espera = int(max(60, min(900, prov.tiempo_restante() - 60)))
    return genai.Client(api_key=clave, http_options=types.HttpOptions(timeout=espera * 1000)), types


def transcribir(origen: str | Path, tipo: str) -> str:
    """Pide a Gemini que convierta una imagen, audio, vídeo, PDF o vídeo de YouTube en texto."""
    if prov.tiempo_restante() < 8 * 60:
        raise prov.TiempoAgotado("sin tiempo para transcribir: se hará en la próxima ejecución")
    cliente, types = _cliente()
    prompt = PROMPTS["video" if tipo == "youtube" else ("documento" if tipo in ("pdf", "office") else tipo)]
    subido = None
    try:
        if tipo == "youtube":
            parte = types.Part(file_data=types.FileData(file_uri=str(origen)))
        else:
            ruta = Path(origen)
            mime = mimetypes.guess_type(ruta.name)[0] or "application/octet-stream"
            subido = cliente.files.upload(file=str(ruta), config=types.UploadFileConfig(mime_type=mime))
            # Los vídeos y audios largos tardan en procesarse antes de poder usarlos
            while getattr(subido.state, "name", "ACTIVE") == "PROCESSING":
                if prov.tiempo_restante() < 6 * 60:
                    raise prov.TiempoAgotado("el archivo sigue procesándose en Gemini")
                time.sleep(10)
                subido = cliente.files.get(name=subido.name)
            if getattr(subido.state, "name", "ACTIVE") == "FAILED":
                raise NoSePuede("Gemini no pudo procesar el archivo")
            parte = subido
        ultimo = None
        for modelo in MODELOS_GEMINI:
            try:
                r = cliente.models.generate_content(model=modelo, contents=[parte, prompt],
                                                    config=types.GenerateContentConfig(temperature=0.1))
                if r.text and r.text.strip():
                    return r.text.strip()
            except Exception as e:      # cupo agotado, modelo saturado...: probar el siguiente
                ultimo = e
                print(f"  [gemini {modelo}] {str(e)[:200]}")
        raise NoSePuede(f"Gemini no pudo transcribirlo: {str(ultimo)[:200]}")
    finally:
        if subido is not None:
            try:
                cliente.files.delete(name=subido.name)
            except Exception:
                pass


def extraer(origen: str | Path, tipo: str) -> tuple[str, bool]:
    """(texto, es_transcripción). es_transcripción=True si el texto lo ha escrito una IA (fuente derivada)."""
    if tipo == "texto":
        return Path(origen).read_text(encoding="utf-8", errors="replace"), False
    if tipo == "html":
        return html_a_texto(Path(origen).read_text(encoding="utf-8", errors="replace")), False
    if tipo == "web":
        return descargar_web(str(origen)), False
    if tipo == "office":
        try:
            return office_a_texto(Path(origen)), False
        except ImportError:
            return transcribir(origen, "office"), True
    if tipo == "pdf":
        texto, paginas = pdf_a_texto(Path(origen))
        if len(texto.strip()) >= MIN_CHARS_POR_PAGINA * paginas * 0.5:
            return texto, False
        return transcribir(origen, "pdf"), True          # escaneado o casi todo imágenes
    if tipo in ("imagen", "audio", "video", "youtube"):
        return transcribir(origen, tipo), True
    raise NoSePuede(f"no sé leer este tipo de archivo ({Path(str(origen)).suffix or tipo})")
