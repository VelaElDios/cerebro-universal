---
tipo: "decision"
titulo: "Portada oficial única y elementos fijos de la plantilla TFG"
temas: ["latex", "memoria", "tfg", "plantilla", "portada", "memoria-procesos"]
claves: ["elements/portada.tex", "Memoria.tex", "elements/preambulo.tex", "declaración de autoría", "Resumen", "Abstract", "índices", "portada", "input"]
proyectos: ["memoria-procesos"]
fuentes: ["../../memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 1)", "memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

Temas: [[latex]] · [[memoria]] · [[tfg]]

La memoria debe usar **exclusivamente la portada oficial** definida en `elements/portada.tex`. No se permite añadir una segunda portada con logos (ni la «segunda portada» con logos UCLM/ESII de `elements/preambulo.tex`). La portada oficial se incluye mediante `\input{elements/portada}` en `Memoria.tex`.

**Detalle de la portada oficial** (`elements/portada.tex`): escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado.

**Plantilla completa inmutable**: portada, declaración de autoría, Resumen, Abstract, índices (general/figuras/tablas), capítulos, anexos, bibliografía. No se quita ni se altera nada de la plantilla salvo indicación expresa de Javier; solo se modifica lo que Javier pida expresamente.

> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[paso-1-completado-preambulo-tex-ya-cumple-regla-1-una-sola-p]] · [[resumen-y-abstract-en-elements-preambulo-tex-con-formato-ofi]] · [[una-sola-portada-oficial-en-elements-portada-tex]] · [[estructura-de-la-memoria-tfg-esiiab-uclm-plantilla-oficial]]
<<<CONTRADICCION>>
no

> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `../../memoria/reglas-tfg.md`
> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`.
> — `../../memoria/reglas-tfg.md`

Fusionada con: Portada única oficial del TFG (elements/portada.tex)

## Ampliación (2026-11-20, memoria-procesos)
Confirmado: elements/preambulo.tex ya tiene el comentario "Segunda portada eliminada" y solo contiene declaración de autoría, Resumen y Abstract. No se toca elements/portada.tex (protegido).

## Ampliación (2026-11-20, memoria-procesos)
La portada oficial se incluye mediante `\input{elements/portada}` en `Memoria.tex`. No se toca `elements/portada.tex` (protegido). La plantilla completa inmutable: portada, declaración, Resumen, Abstract, índices, capítulos, anexos, bibliografía.
relacionado: No se quita nada de la plantilla (regla 2 Javier)

## Ampliación (2026-11-20, memoria-procesos)
|
  Estructura correcta de elements/preambulo.tex:
  1. Configuración de página (raggedbottom, flotantes, etc.)
  2. Declaración de autoría (centrada, con firma)
  3. Resumen (≥150 palabras, dos sprints + juego) + Palabras clave
  4. Abstract (≥120 palabras, inglés) + Keywords
  5. Sin \input{elements/portada} ni textblock de logos.
  Confirmado: elements/preambulo.tex ya tiene el comentario "Segunda portada eliminada" y solo contiene declaración, Resumen y Abstract.

## Ampliación (2026-11-20, memoria-procesos)
Confirmado: elements/preambulo.tex ya tiene el comentario "Segunda portada eliminada" y solo contiene declaración de autoría, Resumen y Abstract. No se toca elements/portada.tex (protegido). La portada oficial se incluye mediante \input{elements/portada} en Memoria.tex.
