---
tipo: "receta"
titulo: "Trampas técnicas comprobadas en LuaLaTeX (evitar errores de compilación)"
temas: ["compilacion", "latex", "lua", "sus", "trampas", "usabilidad"]
claves: ["directlua", "%", "backslash", "tex.sprint", "dofile", "sus-calculos.lua"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[compilacion]] · [[latex]] · [[lua]] · [[sus]] · [[trampas]] · [[usabilidad]]

Lista de trampas documentadas que rompen la compilación en LuaLaTeX:

1. **Código Lua inline en `\directlua{...}`**: No escribir lógica Lua compleja dentro de `\directlua{}` en el .tex. Todo va en `sus-calculos.lua` y se carga una vez con `\directlua{dofile("sus-calculos.lua")}`. Desde el .tex solo llamadas cortas: `\directlua{sus.funcion()}`.

2. **Carácter `%` dentro de `\directlua{...}`**: TeX trata `%` como comentario y corta la línea antes de pasársela a Lua. **Nunca** usar comentarios Lua (`--` sí vale, `%` no) ni porcentajes en strings dentro de `\directlua{}`.

3. **Backslash `\` dentro de `\directlua{...}`**: TeX expande `\` antes que Lua. Si necesitas enviar `\` a Lua, escápalo en el .tex o construye el string en Lua.

4. **Devolver texto a LaTeX**: Usar `tex.sprint("texto")` desde Lua, no `print()` ni `return`.

5. **Escritura de JSON**: Hacer `io.open("resultados.json", "w")` desde Lua (en `sus-calculos.lua`), no desde `\directlua{}` en el .tex. Usar `%.6f` para números, UTF-8 para textos.

> Trampas técnicas comprobadas (evítalas): · Todo el código Lua va en `sus-calculos.lua` y se carga con `\directlua{dofile("sus-calculos.lua")}`. Dentro de `\directlua{...}` solo llamadas cortas a funciones ya definidas: **nunca** escribir `%` ni cadenas con `\` ahí dentro, porque TeX los interpreta antes que Lua y rompe la compilación. · Para devolver texto de Lua a LaTeX usar `tex.sprint(...)`.
> — `../plantilla-sus/spec.md` (cita sin comprobar)

Relacionado: [[arquitectura-de-calculos-en-lualatex-para-plantilla-sus]] · [[exportar-resultados-json-obligatorio-para-verificacion-autom]] · [[directlua-no-funciona-dentro-del-texto-de-un-node-usar-macro]]

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
