# Aprendizaje: el cerebro lee y guarda lo que aprende

Proyecto especial (`"tipo": "aprender"`): no construye nada. Cada pocas horas (`cada_horas`), una IA lee
los documentos de `aprender_de` en `proyecto.json`, trozo a trozo, y guarda lo útil como notas de
conocimiento en `memoria/conocimiento/`, cada una con una cita literal comprobada (ver `scripts/cerebro/aprender.py`).

- **Documentación de los proyectos** (repos públicos y fuentes del vault): para que cualquier IA sepa cómo
  están hechos y cómo se trabaja en ellos sin volver a leerlo todo.
- **Temarios y documentos de Javier**: van en el repo PRIVADO `cerebro-datos`, carpeta `temarios/`. No se
  suben al vault público: aquí solo quedan las notas que se sacan de ellos. Vale **cualquier cosa**
  (ver `scripts/cerebro/medios.py`): texto, PDF (los escaneados los lee Gemini), Word, PowerPoint, Excel, HTML,
  imágenes (fotos de apuntes, diagramas: texto literal + nodos y flechas), audio (transcripción) y vídeo
  (transcripción + lo que se ve). Para vídeos de YouTube o webs: un archivo `enlaces.txt` con una URL por línea.
  Lo que transcribe una IA se guarda en `cerebro-datos/transcripciones/` y las citas se comprueban contra eso.

`procesados.json` recuerda qué trozos de cada archivo están aprendidos. Si un archivo cambia, se vuelve a leer.
Para añadir un documento: subirlo a `cerebro-datos/temarios/` o añadir su ruta a `aprender_de`.
