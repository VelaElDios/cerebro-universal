---
tipo: "concepto"
titulo: "Burndown real vs DoneTonic en Sprint 2 — explicación obligatoria en anexo desarrollo"
temas: ["donetonic", "metricas", "retrospectiva", "scrum"]
claves: ["recta DoneTonic", "backlog registrado al cierre", "evolución real por PRs"]
proyectos: ["memoria-procesos"]
fuentes: ["sprint-2.md § Retrospectiva y § Evolución del Sprint 2"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[donetonic]] · [[metricas]] · [[retrospectiva]] · [[scrum]]

**Hecho**: El juego se programó del 23 al 26/10, **antes** de que el profesor fijara el contenido del Sprint 2. El backlog (29 PBIs, 50 tareas) se registró en DoneTonic **al cerrar el sprint (29/10)** con todo ya en *Hecho*.
**Consecuencia**: DoneTonic marca todos los PBIs como hechos el 29/10 → gráficas en recta vertical (Burndown 29→0 en un día, Burnup 0→29 en un día).
**Solución en memoria**: En Anexo A (a1-desarrollo.tex) se debe:
1. Mostrar la **tabla de evolución real** (Tabla `evolucion-s2`) con PBIs pendientes por fecha de fusión de PR (23/10: 1, 24/10: 17, 26/10: 9, 29/10: 2).
2. Dibujar **fig:burndown-s2** con `pgfplots` usando esos datos reales (eje X: 23/10–29/10, eje Y: PBIs pendientes 28→0).
3. **Explicar explícitamente** en texto: "Las gráficas de DoneTonic del Sprint 2 salen en recta porque el backlog se registró al cerrar el sprint (29/10). La evolución real se reconstruye con las fechas de los PRs."
4. Incluir capturas de DoneTonic (fig:donetonic-s2-graficas) **junto a** la explicación, no como evidencia de evolución real.
Esto es requisito del profesor (estructura-memoria.md: "explicar que las gráficas de DoneTonic del Sprint 2 salen en recta porque el backlog se registró al cerrar el sprint").

> El backlog del Sprint 2 se registró en DoneTonic al cerrar el sprint (29/10/2026) con todos los PBIs ya en Hecho; por eso sus gráficas de Sprint Burndown y Burnup caen en recta de 29 a 0 ese mismo día. La evolución real, reconstruida a partir de las fechas de fusión de los pull requests en main, se detalla en la Tabla y la Figura.
> — `sprint-2.md § Retrospectiva y § Evolución del Sprint 2` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
