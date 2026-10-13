# Bitácora del proyecto

Registro de lo que hace cada IA, paso a paso.

## 2026-10-13 · Preparación (Claude, a petición de Javier)

- `borrador/` parte de la plantilla oficial del TFG de la ESIIAB-UCLM (la que pasó Javier), ya compilando
  con LuaLaTeX: capítulos renombrados sin espacios, estructura según las recomendaciones del profesor
  (con Evaluación y anexos de material adicional y uso de la IA), tutor opcional en la segunda portada,
  una llave sin cerrar del índice corregida, `include/extra.tex` para paquetes nuevos y `latexmkrc`.
- Capturas reales de la aplicación y de DoneTonic en `borrador/figs/capturas/` (del repositorio del SaaS).
- Fuentes en `fuentes/`: la guía del proyecto, la documentación del repositorio y la estructura pedida.
- Test: `verificar.py`. Ahora falla a propósito (todo es texto de relleno): el trabajo es rellenarlo.

## 2026-10-13 02:21 · Constructor (gemini · gemini-3.5-flash-lite)

Se han configurado los metadatos iniciales en `include/opciones.tex` con el título y la fecha correctos, se ha adaptado la segunda portada, la declaración de autoría y el resumen (con más de 120 palabras y palabras clave) en `elements/preambulo.tex`, eliminando la dedicatoria, los agradecimientos y los datos de ejemplo, y se ha preparado la bibliografía en `bib/ref.bib` con las referencias requeridas.

**Archivos:** `include/opciones.tex`, `elements/preambulo.tex`, `bib/ref.bib`

**Intentos:**
- intento 1: ❌ VERIFICACIÓN FALLIDA: 28 problema(s)
- intento 2: no se hace, el fallo es por trabajo pendiente (no cumple «reintentar_si»); lo revisa el revisor

**Siguiente:** Configurar `include/extra.tex` con los paquetes TikZ y pgfplots (cargando la librería babel de TikZ según las lecciones aprendidas) y redactar los capítulos `01-introduccion.tex` y `03-propuesta.tex`.

## 2026-10-13 02:22 · Revisor (openrouter-grandes · nvidia/nemotron-3-ultra-550b-a55b:free)

**Veredicto:** cambios · **Prueba:** ❌ falla la prueba

**Comprobaciones:**
- Título en opciones.tex: "La Grada Colchonera: base SaaS y proceso de desarrollo" → coincide con guia.md §1 y spec
- Fecha en opciones.tex: "Octubre, 2026" → coincide con fin del Sprint 1 (27/10/2026) en guia.md
- Autor en opciones.tex: "Javier Vela González-Román" → coincide con guia.md
- Segunda portada en preambulo.tex: "TRABAJO DE PROCESOS DE INGENIERÍA DEL SOFTWARE" → cumple spec (cambia "TRABAJO FIN DE GRADO")
- Dedicatoria y agradecimientos eliminados en preambulo.tex → cumple spec (son personales)
- Declaración de autoría: estructura correcta (autor, título, atribución, mención anexo IA), sin DNI ni huecos → cumple spec
- Resumen en preambulo.tex: ~137 palabras (≥ 120) → cumple spec
- Línea "Palabras clave:" presente en preambulo.tex → cumple spec
- Bibliografía en bib/ref.bib: 9 referencias @misc con howpublished=\url{} (8 con URL, enunciado sin URL) → coincide exactamente con guia.md §10
- Referencias cubren: Express, GitHub Flow, Node.js, PostgreSQL, Cloud Run, GitHub Actions, Scrum Guide, Neon limits, Enunciado → todas en guia.md §10
- Espec en opciones.tex: "Ingeniería del Software" → coincide con guia.md

El constructor ha completado correctamente el primer paso (3 archivos de configuración). Los datos de título, fecha, autor y bibliografía coinciden con las fuentes. Se han eliminado dedicatoria y agradecimientos, y la segunda portada tiene el texto correcto.

**Dos correcciones menores en `elements/preambulo.tex`:**
1. La declaración de autoría dice "en el anexo correspondiente" pero la spec pide explícitamente "en el Anexo C (\ref{anx:ia})".
2. La fecha en la firma dice "Albacete, a \fecha" y la spec dice "Albacete, \fecha" (sin la preposición "a").

El resto de errores del test (capítulos con lipsum, 0 figuras/tablas, bibliografía sin citas, conteos de palabras) son esperables porque solo se han tocado estos 3 archivos; los capítulos se redactarán en los siguientes pasos.

**Correcciones del revisor:** `elements/preambulo.tex`

**Tareas para el constructor:**
- Configurar `include/extra.tex` con los paquetes necesarios: TikZ (con librería `babel`), pgfplots, booktabs, placeins, csquotes, icomma y cualquier otro que vaya a usarse en figuras y tablas.
- Redactar `chapters/01-introduccion.tex`: motivación (asignatura evalúa aplicación y proceso), objetivo principal y específicos (sacados de hitos/requisitos), alcance (Hitos 1–3), estructura de la memoria (capítulos y anexos con `\ref`). Mínimo 350 palabras. Incluir la frase «proyecto de aficionado sin relación oficial con el Club Atlético de Madrid».
- Redactar `chapters/03-propuesta.tex`: propuesta de solución sin detalles técnicos (§1 guía), metodología (Scrum en DoneTonic, GitHub Flow por hitos, §3, §5, contributing), herramientas en tabla agrupadas (gestión, desarrollo, despliegue, documentación, §6). Mínimo 500 palabras. Citar referencias con `\cite`.
