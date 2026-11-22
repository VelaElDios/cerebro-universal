---
tipo: "receta"
titulo: "Cómo replantear diagramas TikZ/pgf-umlsd para pasar revisar_maquetacion.py (reglas 16-18)"
temas: ["latex", "maquetacion", "pgf-umlsd", "tikz"]
claves: ["revisar_maquetacion.py", "reglas 16-18", "fig:capas", "fig:juego-arquitectura", "fig:sec-login", "fig:sec-baja"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md y salida de revisar_maquetacion.py"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]] · [[tikz]]

Pasos obligatorios para cada diagrama que falle reglas 16-18:
1. **No escalar** con `\resizebox`, `\adjustbox{scale=...}`, `\tiny`, `\small` — eso reduce letras por debajo de 7.5 pt.
2. **Reducir participantes/columnas**: máx. 6 en diagramas de secuencia; agrupar relacionados (ej. "Frontend + api.js" → "Frontend").
3. **Acortar etiquetas**: máx. 2 líneas por flecha; usar abreviaturas claras.
4. **Aumentar separación**: `node distance` horizontal ≥3.0 cm, vertical ≥1.5 cm en TikZ; en `sequencediagram` usar `\newinst[1.5]` o menor para acercar, pero mejor aumentar separación real entre cajas.
5. **Cajas más anchas**: `text width` suficiente para que no partan palabras (usar `\mbox{}` en palabras problemáticas como "sprites.js," → `\mbox{sprites.js,}`).
6. **Flechas con codos**: en TikZ usar `|-` o `-|` (ej. `(A.east) -- ++(1.0,0) |- (B.west)`); en `sequencediagram` las flechas ya van de lifeline a lifeline, pero evitar que crucen otras lifelines reordenando participantes.
7. **Etiquetas fuera de cajas**: `node[near start, above, font=\scriptsize] {texto}` en TikZ; en `sequencediagram` las etiquetas van en `call`/`mess`, mantenerlas cortas.
8. **Fuente mínima**: `\scriptsize` (≈8 pt) en todo el diagrama; nunca `\tiny` ni `\footnotesize` si cabe `\scriptsize`.
9. **Envolver en adjustbox solo para ancho/alto máx.**: `\begin{adjustbox}{max width=\textwidth, max totalheight=0.6\textheight}` — esto NO escala si cabe, solo recorta si se pasa; mejor que el diagrama quepa solo.
10. **Compilar y abrir PDF**: medir letras con zoom 100%; si <7.5 pt, volver a paso 2.
Ejemplo correcto (fig:capas rehecho): text width 2.6 cm, separación 3.0 cm, `\scriptsize`, `\mbox{}` en "externos", flechas con codos `++(0.8,0) |-`.

> Todo diagrama se lee bien a su tamaño en el PDF: las letras del dibujo, una vez escalado, nunca son más pequeñas que las del pie de figura (unos 8-9 pt). Si para que quepa hay que encogerlo tanto que las letras quedan diminutas, el diagrama está mal planteado.
> — `memoria/reglas-tfg.md y salida de revisar_maquetacion.py` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
