---
tipo: "decision"
titulo: "Una sola portada oficial y elementos fijos de la plantilla TFG"
temas: ["elementos-fijos", "plantilla", "portada", "tfg", "latex", "memoria"]
claves: ["elements/portada.tex", "elements/preambulo.tex", "segunda portada", "declaracion", "resumen", "abstract"]
proyectos: ["memoria-procesos"]
fuentes: ["../../memoria/reglas-tfg.md", "memoria/reglas-tfg.md regla 1"]
confianza: "verificado"
fecha: "2026-11-22"
actualizado: "2026-11-24"
---

Temas: [[elementos-fijos]] · [[plantilla]] · [[portada]] · [[tfg]]

|
  En `elements/preambulo.tex`: el bloque «Segunda portada» (los `textblock` con los logos, el título y el autor) **debe eliminarse**. Lo que queda:
  1. Configuración de página (raggedbottom, flotantes, etc.)
  2. Declaración de autoría (centrada, con firma)
  3. Resumen (≥150 palabras, dos sprints + juego) + Palabras clave
  4. Abstract en inglés (≥120 palabras) + Keywords, mismo formato que Resumen (`\Large{\bft{Abstract}}`)
  5. Sin `\input{elements/portada}` ni textblock de logos.
  
  Archivos protegidos (no tocar): `elements/portada.tex`, `Memoria.tex`.

> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[portada-unica-oficial-del-tfg-elements-portada-tex]] · [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]]

## Ampliación (2026-11-24, memoria-procesos)
La memoria debe usar EXCLUSIVAMENTE la portada oficial de `elements/portada.tex`. En `elements/preambulo.tex` el bloque «Segunda portada» (textblock con logos, título, autor) DEBE ELIMINARSE. Lo que queda: configuración de página, declaración de autoría, Resumen (≥150 palabras), Abstract (≥120 palabras, mismo formato). Archivos protegidos: `elements/portada.tex`, `Memoria.tex`, `include/configuracion.tex`, `include/colores.tex`, `include/opciones.tex`, `include/extra.tex`, `figs/*`. Verificación: PDF compilado tiene exactamente una portada (la oficial), seguida de declaración, resumen, abstract, índices.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
