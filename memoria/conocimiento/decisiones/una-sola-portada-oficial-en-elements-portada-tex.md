---
tipo: "decision"
titulo: "Una sola portada oficial en elements/portada.tex"
temas: ["latex", "plantilla", "portada"]
claves: ["portada", "elements/portada.tex", "preambulo.tex", "regla 1"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[latex]] · [[plantilla]] · [[portada]]

La memoria debe usar exclusivamente la portada oficial definida en `elements/portada.tex`. En `elements/preambulo.tex` se debe eliminar el bloque «Segunda portada» (los `textblock` con los logos, el título y el autor) y dejar solo la declaración de autoría, el Resumen y el Abstract. `Memoria.tex` ya incluye `\input{elements/portada}` al inicio del documento.

> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
