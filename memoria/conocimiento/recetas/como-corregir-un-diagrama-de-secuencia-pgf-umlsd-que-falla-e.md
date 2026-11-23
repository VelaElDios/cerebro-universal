---
tipo: "receta"
titulo: "Cómo corregir un diagrama de secuencia pgf-umlsd que falla en revisar_maquetacion.py (reglas 16-18)"
temas: ["latex", "maquetacion", "pgf-umlsd"]
claves: ["flechas cruzan texto", "letras diminutas", "participantes", "etiquetas largas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]]

Cuando `revisar_maquetacion.py` reporta que un diagrama de secuencia tiene flechas cruzando texto o letras <7.5pt:
1. Reducir participantes a ≤5 (regla 16). Agrupar si hay más (ej. "Frontend" en vez de "Vista + api.js").
2. Aumentar separación horizontal: `\newinst[3]` o `\newinst[4]` en lugar de `[2]`.
3. Acortar etiquetas a ≤2 líneas, sin acentos, sin comandos LaTeX, sin paréntesis en `\mess`. Usar "o" en vez de "/".
4. Usar `sdblock` para alternativas, no `alt` (no existe).
5. Envolver en `adjustbox{max width=\textwidth, max totalheight=0.6\textheight}` (no `resizebox` que encoge letras).
6. Fuente `\scriptsize` o `\footnotesize` en el entorno `sequencediagram` para que las letras midan ≥8pt en PDF.
7. Verificar que ninguna flecha salta un participante: las llamadas deben ser entre vecinos (A→B, B→C). Si hay que ir de A a C, usar dos flechas A→B y B→C.
8. Ejecutar `revisar_umlsd.py` y compilar; revisar visualmente el PDF a tamaño real.

> Las flechas van de una caja a la siguiente (A → B, B → C), nunca de A a C pasando por encima de B; si hay que rodear, con codos (|-, -|) y separando bien las cajas (node distance suficiente). Las etiquetas de las flechas no se montan sobre las cajas.
> — `memoria/reglas-tfg.md`

Relacionado: [[inventario-de-diagramas-obligatorios-y-su-estado-actualizado]] · [[como-replantear-diagramas-de-secuencia-pgf-umlsd-para-evitar]] · [[como-replantear-diagramas-de-secuencia-pgf-umlsd-para-pasar]] · [[como-replantear-diagramas-tikz-pgf-umlsd-para-pasar-revisar]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]]: Nota A dice «participantes a ≤5 (regla 16)»; Nota B dice «Máximo 6 participantes por diagrama». Nota A prohíbe `resizebox` para diagramas anchos («no `resizebox` que encoge letras») y manda usar `adjustbox`; Nota B indica «Diagramas anchos: envolver en `\resizebox{\textwidth}{!}{% ... %}`» y reserva `adjustbox` solo para diagramas altos.
