---
tipo: "receta"
titulo: "Cómo corregir solapes de etiquetas en diagramas TikZ de entidad-relación"
temas: ["latex", "maquetacion", "pgf-umlsd", "tikz", "revisar_maquetacion.py"]
claves: ["revisar_maquetacion.py", "fig:modelo-datos", "etiqueta userId", "línea discontinua", "above", "yshift"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex", "bitácora 2026-11-25 (revisor nvidia-revisor)"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]] · [[tikz]]

Cuando `revisar_maquetacion.py` detecta que una etiqueta de relación (p. ej., 'userId') queda sobre la línea en un diagrama entidad-relación TikZ, la solución es aumentar la separación vertical usando `above=<dimensión>` en el nodo de la etiqueta, en lugar de `anchor=south, yshift=<dimensión>`. La sintaxis `above` coloca el nodo por encima de la línea con el espacio indicado y es más robusta. Para líneas horizontales, `above=30pt` suele ser suficiente; para líneas verticales, usar `anchor=east, xshift=-18pt, pos=0.5` (o `left=18pt`). No se debe usar `resizebox`, `adjustbox` ni `scale` sobre el diagrama completo (reglas 16 y 19 de Javier).

> \draw[arrow, dashed] (session.east) -- node[rel, midway, above=30pt] {userId} (users.west);
> — `chapters/04-descripcion.tex` (cita sin comprobar)

## Ampliación (2026-11-25, memoria-procesos)
Cuando `revisar_maquetacion.py` detecta que una línea cruza el texto de una etiqueta en un diagrama TikZ (reglas 16-18), la solución no es encoger el diagrama (`resizebox`, `scale`), sino reposicionar la etiqueta:

1. **Aumentar la separación vertical**: usar `above=50pt` (o más) en el nodo de la etiqueta, en lugar de `anchor=south, yshift=24pt`. La sintaxis `above` establece `anchor=south` y `yshift` automáticamente y es más robusta.
2. **Aplicar a ambas etiquetas horizontales** para consistencia visual.
3. **Verificar con la medición del PDF**: ejecutar `comando_prueba` tras cada ajuste; la medición geométrica es la que manda.
4. **No tocar las cajas ni las flechas**: solo el posicionamiento de los nodos de las etiquetas.
5. **Ejemplo correcto**:
   ```latex
   \draw[arrow, dashed] (session.east) -- node[rel, midway, above=50pt] {userId} (users.west);
   \draw[arrow] (users.east) -- node[rel, midway, above=50pt, align=center] {su\\club} (perfiles.west);
   ```
   La etiqueta vertical (`su mejor partida`) se ancla al trayecto con `anchor=east, xshift=-18pt, pos=0.5` y no da error.

## Ampliación (2026-11-25, memoria-procesos)
1. Ejecutar `revisar_maquetacion.py` (o `comando_prueba`) para ver qué etiqueta y qué línea se solapan. 2. En el código TikZ del diagrama, localizar el `\draw` de la flecha y el `node` de la etiqueta. 3. Cambiar `anchor=south, yshift=<valor>` por `above=<valor_mayor>` (p. ej., 50pt). 4. Aplicar la misma separación a etiquetas homólogas en el mismo diagrama por consistencia. 5. Volver a ejecutar la prueba hasta que no haya solapes medidos. No usar `resizebox`, `adjustbox` ni `scale`: eso encoge las letras y no soluciona el solape geométrico.

Relacionado: [[como-corregir-diagramas-de-entidad-relacion-en-tikz-para-que]] · [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[como-escribir-un-diagrama-de-entidad-relacion-en-tikz-legibl]]: La Nota A prohíbe explícitamente usar `resizebox`, `adjustbox` ni `scale` sobre el diagrama completo (reglas 16 y 19 de Javier). La Nota B recomienda usar `adjustbox{max width=\linewidth, max totalheight=0.6\textheight}` para escalar el diagrama. Ambas hablan del mismo tema (escalado global de diagramas TikZ ER) y dan instrucciones opuestas.
