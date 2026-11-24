---
tipo: "decision"
titulo: "Portada oficial única y elementos fijos de la plantilla TFG (elements/portada.tex)"
temas: ["elementos-fijos", "latex", "maquetacion", "memoria", "memoria-procesos", "plantilla", "plantilla-tfg", "portada", "tfg"]
claves: ["elements/portada.tex", "Memoria.tex", "elements/preambulo.tex", "declaración de autoría", "Resumen", "Abstract", "índices", "portada", "input", "preambulo.tex", "regla 1", "segunda portada", "declaracion", "resumen", "abstract"]
proyectos: ["memoria-procesos"]
fuentes: ["../../memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 1)", "memoria/reglas-tfg.md", "memoria/reglas-tfg.md regla 1"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-24"
---

Temas: [[elementos-fijos]] · [[latex]] · [[maquetacion]] · [[memoria]] · [[memoria-procesos]] · [[plantilla]] · [[plantilla-tfg]] · [[portada]] · [[tfg]]

# Portada oficial única y elementos fijos de la plantilla TFG
Temas: [[latex]] · [[maquetacion]] · [[memoria]] · [[memoria-procesos]] · [[plantilla]] · [[plantilla-tfg]] · [[portada]] · [[tfg]] · [[elementos-fijos]]

La memoria debe usar **exclusivamente la portada oficial** definida en `elements/portada.tex`. No se permite añadir una segunda portada con logos (ni la «segunda portada» con logos UCLM/ESII de `elements/preambulo.tex`). La portada oficial se incluye mediante `\input{elements/portada}` en `Memoria.tex`.

**Detalle de la portada oficial** (`elements/portada.tex`): escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado.

**Plantilla completa inmutable**: portada, declaración de autoría, Resumen, Abstract, índices (general/figuras/tablas), capítulos, anexos, bibliografía. No se quita ni se altera nada de la plantilla salvo indicación expresa de Javier; solo se modifica lo que Javier pida expresamente.

> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `../../memoria/reglas-tfg.md` (también referenciado como `memoria/reglas-tfg.md`)

**En `elements/preambulo.tex`**: el bloque «Segunda portada» (los `textblock` con los logos, el título y el autor) **debe eliminarse**. Lo que queda:
1. Configuración de página (raggedbottom, flotantes, etc.)
2. Declaración de autoría (centrada, con firma)
3. Resumen (≥150 palabras, dos sprints + juego) + Palabras clave
4. Abstract en inglés (≥120 palabras) + Keywords, mismo formato que Resumen (`\Large{\bft{Abstract}}`)
5. Sin `\input{elements/portada}` ni textblock de logos.

**Archivos protegidos (no tocar)**:
- `elements/portada.tex` (protegido)
- `Memoria.tex` (protegido, ya hace `\input{elements/portada}` al inicio del documento y `\input{elements/preambulo}` en `\frontmatter`)

**Verificación**: El PDF compilado debe tener exactamente una portada (la oficial), seguida de declaración, resumen, abstract, índices.

Relacionado: [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[paso-1-completado-preambulo-tex-ya-cumple-regla-1-una-sola-p]] · [[resumen-y-abstract-en-elements-preambulo-tex-con-formato-ofi]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[estructura-de-la-memoria-tfg-esiiab-uclm-plantilla-oficial]] · [[portada-unica-oficial-del-tfg-elements-portada-tex]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]]

---

## Ampliaciones (memoria-procesos)

### 2026-11-19
- **Regla 1 de Javier**: La memoria debe usar **exclusivamente la portada oficial** definida en `elements/portada.tex`. No se permite añadir una segunda portada con logos (ni la «segunda portada» con logos UCLM/ESII de `elements/preambulo.tex`).
- En `elements/preambulo.tex`: el bloque «Segunda portada» ya está eliminado. Quedan: declaración de autoría (no se toca), Resumen (≥150 palabras, dos sprints + juego) con «Palabras clave», Abstract en inglés (≥120 palabras) con «Keywords», mismo formato que Resumen (`\Large{\bft{Abstract}}`).
- No tocar: `elements/portada.tex` (protegido), `Memoria.tex` (protegido, ya hace `\input{elements/portada}`).
- Verificación: El PDF compilado debe tener exactamente una portada (la oficial), seguida de declaración, resumen, abstract, índices.
- `elements/preambulo.tex` debe contener solo: declaración de autoría, Resumen, Abstract. El bloque de «Segunda portada» (textblock con logos, título, autor) se elimina. La portada oficial ya está en `elements/portada.tex` y se incluye en `Memoria.tex` antes del frontmatter.
- La plantilla oficial del TFG ESIIAB-UCLM define una única portada en `elements/portada.tex` (con `textblock` posicionados absolutamente). En `elements/preambulo.tex` **no debe haber** ningún bloque de «segunda portada» (logos, título, autor). El preámbulo solo contiene: declaración de autoría, Resumen, Abstract, y configuraciones de maquetación (raggedbottom, flotantes, etc.). `Memoria.tex` incluye `\input{elements/portada}` al inicio del documento y `\input{elements/preambulo}` en `\frontmatter`.

### 2026-11-20
- Confirmado: `elements/preambulo.tex` ya tiene el comentario «Segunda portada eliminada» y solo contiene declaración de autoría, Resumen y Abstract. No se toca `elements/portada.tex` (protegido).
- La portada oficial se incluye mediante `\input{elements/portada}` en `Memoria.tex`. No se toca `elements/portada.tex` (protegido). La plantilla completa inmutable: portada, declaración, Resumen, Abstract, índices, capítulos, anexos, bibliografía. Relacionado: No se quita nada de la plantilla (regla 2 Javier).
- Estructura correcta de `elements/preambulo.tex`:
  1. Configuración de página (raggedbottom, flotantes, etc.)
  2. Declaración de autoría (centrada, con firma)
  3. Resumen (≥150 palabras, dos sprints + juego) + Palabras clave
  4. Abstract (≥120 palabras, inglés) + Keywords
  5. Sin `\input{elements/portada}` ni textblock de logos.
- Confirmado: `elements/preambulo.tex` ya tiene el comentario «Segunda portada eliminada» y solo contiene declaración, Resumen y Abstract.
- Confirmado (reiterado): `elements/preambulo.tex` ya tiene el comentario «Segunda portada eliminada» y solo contiene declaración de autoría, Resumen y Abstract. No se toca `elements/portada.tex` (protegido). La portada oficial se incluye mediante `\input{elements/portada}` en `Memoria.tex`.

### 2026-11-21
- La memoria debe usar exclusivamente la portada oficial definida en `elements/portada.tex`. No se permite añadir una segunda portada con logos. La portada oficial se incluye mediante `\input{elements/portada}` en `Memoria.tex`. Plantilla completa inmutable: portada, declaración de autoría, Resumen, Abstract, índices, capítulos, anexos, bibliografía.
- Relacionado: Cada entrega solo lleva lo de su sprint (alcance coherente).
- Archivos protegidos (no tocar): `elements/portada.tex`, `Memoria.tex`, `include/configuracion.tex`, `include/colores.tex`, `include/opciones.tex`, `latexmkrc`, `figs/*`.

### 2026-11-24
- La portada oficial se incluye mediante `\input{elements/portada}` en `Memoria.tex`. En `elements/preambulo.tex` solo queda: configuración de página, declaración de autoría, Resumen (≥150 palabras), Abstract (≥120 palabras) con mismo formato.
- **Ampliación adicional**: La memoria debe usar EXCLUSIVAMENTE la portada oficial de `elements/portada.tex`. En `elements/preambulo.tex` el bloque «Segunda portada» (textblock con logos, título, autor) DEBE ELIMINARSE. Lo que queda: configuración de página, declaración de autoría, Resumen (≥150 palabras), Abstract (≥120 palabras, mismo formato). Archivos protegidos: `elements/portada.tex`, `Memoria.tex`, `include/configuracion.tex`, `include/colores.tex`, `include/opciones.tex`, `include/extra.tex`, `figs/*`. Verificación: PDF compilado tiene exactamente una portada (la oficial), seguida de declaración, resumen, abstract, índices.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
<<<CONTRADICCION>>
Diferencia en la lista de archivos protegidos entre la ampliación 2026-11-21 (incluye `latexmkrc`, no incluye `include/extra.tex`) y la ampliación 2026-11-24 de la nota B (incluye `include/extra.tex`, no menciona `latexmkrc`).

> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `../../memoria/reglas-tfg.md` (también referenciado como `memoria/reglas-tfg.md`)
> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `../../memoria/reglas-tfg.md`
> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`.
> — `../../memoria/reglas-tfg.md`
> Una sola portada: la oficial del TFG, la de `elements/portada.tex` (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). `Memoria.tex` hace `\input{elements/portada}`. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de `elements/preambulo.tex`.
> — `memoria/reglas-tfg.md`

Fusionada con: Una sola portada oficial y elementos fijos de la plantilla TFG

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
