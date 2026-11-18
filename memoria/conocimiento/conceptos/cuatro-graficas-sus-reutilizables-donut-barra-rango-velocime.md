---
tipo: "concepto"
titulo: "Cuatro gráficas SUS reutilizables (donut, barra-rango, velocímetro, barras-participante)"
temas: ["defensa", "graficas", "latex", "pgfplots", "sus", "tikz", "usabilidad"]
claves: ["donut", "barra-rango", "velocimetro", "barras-participante", "graficas/*.tex"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[defensa]] · [[graficas]] · [[latex]] · [[pgfplots]] · [[sus]] · [[tikz]] · [[usabilidad]]

Cuatro gráficas TikZ/pgfplots independientes en `graficas/*.tex`, cada una en su archivo para `\input{}` tanto en el anexo como en la defensa:

1. **Donut** (`graficas/donut.tex`): Media SUS numérica grande en centro, arco circular proporcional a la puntuación (0-100), nota y adjetivo debajo.
2. **Barra de rango** (`graficas/barra-rango.tex`): Eje 0-100, marca en 68 (referencia), rango mínimo-máximo de participantes.
3. **Velocímetro** (`graficas/velocimetro.tex`): Semicírculo con tres zonas coloreadas: 0-50 rojo (no aceptable), 50-70 amarillo (marginal), 70-100 verde (aceptable); aguja en la media.
4. **Barras por participante** (`graficas/barras-participante.tex`): Barras horizontales/verticales por participante con su puntuación, línea de referencia en 68.

Requisitos: colores definidos en un solo sitio; etiquetas sin solaparse entre sí ni con barras/escalas; sin imágenes externas.

> Cada gráfica en su propio archivo dentro de `graficas/`, usable con `\input{}`: · **Donut**: media SUS en grande en el centro, arco proporcional a la puntuación, nota y adjetivo debajo. · **Barra de rango**: de 0 a 100, marcando el 68 de referencia y el rango mín-máx de los participantes. · **Velocímetro**: semicírculo con zonas no aceptable (0-50, rojo), marginal (50-70, amarillo) y aceptable (70-100, verde), con la aguja en la media. · **Barras por participante**: puntuación de cada uno con una línea en 68.
> — `../plantilla-sus/spec.md` (cita sin comprobar)

Relacionado: [[criterios-de-terminado-de-la-plantilla-sus-checklist-de-acep]] · [[burndown-real-vs-burndown-de-donetonic-en-sprint-2]] · [[arquitectura-de-calculos-en-lualatex-para-plantilla-sus]] · [[estructura-de-archivos-obligatoria-para-la-plantilla-sus]] · [[escalas-de-transformacion-sus-adoptadas-sauro-lewis-bangor-e]]

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
