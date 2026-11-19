---
tipo: "decision"
titulo: "Una sola portada oficial en elements/portada.tex"
temas: ["latex", "plantilla", "portada", "maquetacion", "plantilla-tfg", "tfg"]
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

## Ampliación (2026-11-19, memoria-procesos)
|
  **Regla 1 de Javier**: La memoria debe usar **exclusivamente la portada oficial** definida en `elements/portada.tex`. No se permite añadir una segunda portada con logos (ni la «segunda portada» con logos UCLM/ESII de `elements/preambulo.tex`).
  
  **En elements/preambulo.tex**: El bloque «Segunda portada» (los `textblock` con los logos, el título y el autor) **ya está eliminado** en el borrador actual. Lo que queda es:
  1. Declaración de autoría (no se toca)
  2. Resumen (≥ 150 palabras, dos sprints + juego) con «Palabras clave»
  3. Abstract en inglés (≥ 120 palabras) con «Keywords», mismo formato que Resumen (`\Large{\bft{Abstract}}`)
  
  **No tocar**: `elements/portada.tex` (protegido), `Memoria.tex` (protegido, ya hace `\input{elements/portada}`).
  
  **Verificación**: El PDF compilado debe tener exactamente una portada (la oficial), seguida de declaración, resumen, abstract, índices.

## Ampliación (2026-11-19, memoria-procesos)
|
  El archivo elements/preambulo.tex debe contener solo: declaración de autoría, Resumen, Abstract. El bloque de «Segunda portada» (textblock con logos, título, autor) se elimina. La portada oficial ya está en elements/portada.tex y se incluye en Memoria.tex antes del frontmatter.

## Ampliación (2026-11-19, memoria-procesos)
La plantilla oficial del TFG ESIIAB-UCLM define una única portada en `elements/portada.tex` (con `textblock` posicionados absolutamente). En `elements/preambulo.tex` **no debe haber** ningún bloque de «segunda portada» (logos, título, autor). El preámbulo solo contiene: declaración de autoría, Resumen, Abstract, y configuraciones de maquetación (raggedbottom, flotantes, etc.). `Memoria.tex` incluye `\input{elements/portada}` al inicio del documento y `\input{elements/preambulo}` en `\frontmatter`.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
