---
tipo: "decision"
titulo: "Una sola portada oficial y elementos fijos de la plantilla TFG"
temas: ["latex", "plantilla", "portada"]
claves: ["elements/portada.tex", "elements/preambulo.tex", "portada única"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[latex]] · [[plantilla]] · [[portada]]

|
  Archivos protegidos (no tocar): elements/portada.tex, Memoria.tex, latexmkrc, include/configuracion.tex, include/colores.tex, include/opciones.tex, figs/*.
  En elements/preambulo.tex: quitar todo el bloque de textblock que dibuja la segunda portada. Mantener \raggedbottom, declaración de autoría, Resumen, Abstract.

> Una sola portada: la oficial del TFG, la de elements/portada.tex (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). Memoria.tex hace \input{elements/portada}. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de elements/preambulo.tex."
problema: El borrador tenía una segunda portada con logos en elements/preambulo.tex que incumple la regla 1 de Javier.
solucion: En elements/preambulo.tex, eliminar el bloque «Segunda portada» (los textblock con logos, título y autor). Dejar solo: configuración de página, declaración de autoría, Resumen (≥150 palabras) con Palabras clave, y Abstract en inglés (≥120 palabras) con Keywords, mismo formato que Resumen (\Large{\bft{Abstract}}).
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
