---
tipo: "proyecto"
titulo: "plantilla-sus"
temas: ["latex", "lua", "beamer", "pgfplots"]
actualizado: "2026-11-16 12:21"
---

# plantilla-sus

Temas: [[latex]] · [[lua]] · [[beamer]] · [[pgfplots]]

## Qué es
Plantilla LaTeX para el anexo de evaluación de usabilidad con SUS (System Usability Scale) de un TFG, con las gráficas para la defensa. Todo es automático: el usuario solo rellena `datos/respuestas.csv`, y puntuaciones, estadísticas, nota, adjetivo, tablas y gráficas se calculan al compilar.

## Decisiones y convenciones
- LuaLaTeX: los cálculos se hacen en Lua dentro del documento. Gráficas con TikZ/pgfplots, sin imágenes externas.
- Español con coma decimal.
- Doble uso: `anexo-sus.tex` compila solo y `contenido-sus.tex` se mete con `\input{}` en el TFG.
- `resultados.json` se genera al compilar. `verificar.py` y `probar_datos_raros.py` comprueban los cálculos.

## Estado
TERMINADO (08/10/2026): pasa todas las pruebas. También existe `defensa-sus.tex` (Beamer). Se reabrirá si el TFG lo necesita.

## Siguiente
Nada hasta que Javier lo reabra.

Bitácora completa: [[proyectos/plantilla-sus/bitacora|bitácora]] · Spec: [[proyectos/plantilla-sus/spec|spec]]
