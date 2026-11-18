---
tipo: "concepto"
titulo: "Arquitectura de cálculos en LuaLaTeX para plantilla SUS"
temas: ["arquitectura", "latex", "lua", "sus", "usabilidad"]
claves: ["sus-calculos.lua", "directlua", "tex.sprint", "LuaLaTeX"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[arquitectura]] · [[latex]] · [[lua]] · [[sus]] · [[usabilidad]]

La plantilla separa toda la lógica de cálculo en un archivo Lua independiente (`sus-calculos.lua`) que se carga una vez al inicio con `\directlua{dofile("sus-calculos.lua")}`. Desde el documento .tex solo se hacen llamadas cortas a funciones ya definidas en Lua (ej. `\directlua{sus.imprimir_tabla_resultados()}`).

Reglas críticas:
- **Nunca** escribir `%` (comentario Lua) ni `\` (comandos TeX) dentro de `\directlua{...}` porque TeX los procesa antes que Lua y rompe la compilación.
- Para devolver texto de Lua a LaTeX usar `tex.sprint(...)`.
- El archivo Lua también escribe `resultados.json` al compilar con `io.open(..., "w")` en UTF-8.

> Todo el código Lua va en `sus-calculos.lua` y se carga con `\directlua{dofile("sus-calculos.lua")}`. Dentro de `\directlua{...}` solo llamadas cortas a funciones ya definidas: **nunca** escribir `%` ni cadenas con `\` ahí dentro, porque TeX los interpreta antes que Lua y rompe la compilación.
> — `../plantilla-sus/spec.md`

Relacionado: [[criterios-de-terminado-de-la-plantilla-sus-checklist-de-acep]] · [[cuatro-graficas-sus-reutilizables-donut-barra-rango-velocime]] · [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]] · [[trampas-tecnicas-comprobadas-en-lualatex-evitar-errores-de-c]] · [[exportar-resultados-json-obligatorio-para-verificacion-autom]] · [[estructura-de-archivos-obligatoria-para-la-plantilla-sus]]

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
