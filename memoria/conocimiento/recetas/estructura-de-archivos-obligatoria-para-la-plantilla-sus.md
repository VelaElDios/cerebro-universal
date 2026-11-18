---
tipo: "receta"
titulo: "Estructura de archivos obligatoria para la plantilla SUS"
temas: ["archivos", "estructura", "latex", "sus", "usabilidad"]
claves: ["anexo-sus.tex", "contenido-sus.tex", "sus-calculos.lua", "graficas/", "referencias.bib", "resultados.json"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[archivos]] · [[estructura]] · [[latex]] · [[sus]] · [[usabilidad]]

Estructura de directorios y archivos requerida en `final/`:

- `anexo-sus.tex`: Documento LaTeX completo compilable independientemente (incluye preámbulo, `\begin{document}`, etc.)
- `contenido-sus.tex`: Solo el contenido del anexo (sin preámbulo), para hacer `\input{contenido-sus}` desde la plantilla principal del TFG
- `sus-calculos.lua`: **Todo** el código Lua (cálculos, generación de tablas, gráficas, exportación JSON, textos condicionales)
- `datos/respuestas.csv`: Datos de entrada (ver receta "Cómo estructurar el CSV de entrada")
- `graficas/*.tex`: Un archivo .tex por gráfica (donut, barra-rango, velocímetro, barras-participante), cada uno usable con `\input{}`
- `referencias.bib`: Bibliografía BibTeX con todas las fuentes citadas
- `resultados.json`: Se genera **automáticamente al compilar** (ver receta "Exportar resultados.json")

Colores de gráficas definidos en un único sitio para fácil cambio.

> Estructura de archivos: final/ ├── anexo-sus.tex # documento independiente ├── contenido-sus.tex # contenido para \input en el TFG ├── sus-calculos.lua # todos los cálculos ├── datos/respuestas.csv ├── graficas/*.tex └── referencias.bib
> — `../plantilla-sus/spec.md` (cita sin comprobar)

Relacionado: [[arquitectura-de-calculos-en-lualatex-para-plantilla-sus]] · [[como-estructurar-el-csv-de-entrada-para-la-plantilla-sus]] · [[criterios-de-terminado-de-la-plantilla-sus-checklist-de-acep]]

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
