---
tipo: "concepto"
titulo: "Estructura de la memoria TFG ESIIAB-UCLM (plantilla oficial)"
temas: ["latex", "plantilla", "tfg"]
claves: ["elements/portada.tex", "elements/preambulo.tex", "Memoria.tex", "include/configuracion.tex"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-20"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[plantilla]] · [[tfg]]

La plantilla inmutable incluye: portada (elements/portada.tex), declaración de autoría, Resumen, Abstract, índices (general, figuras, tablas), capítulos, anexos, bibliografía. No se quita nada de la plantilla salvo indicación expresa de Javier. Los títulos en negro y negrita (\definecolor{tema}{RGB}{0,0,0}), enlaces sin recuadros (hidelinks), sin páginas en blanco entre capítulos (renewcommand{\cleardoublepage}{\clearpage}).

> Una sola portada: la oficial del TFG, la de elements/portada.tex (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). Memoria.tex hace \input{elements/portada}. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de elements/preambulo.tex.
> — `memoria/reglas-tfg.md`

Relacionado: [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[elementos-de-plantilla-inmutables-no-se-quita-nada]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[estructura-de-8-capitulos-para-la-memoria-tfg-esiiab-uclm]]: La Nota A describe la plantilla inmutable como una secuencia donde los «capítulos» son un bloque previo y separado de «anexos» y «bibliografía» (portada, índices, capítulos, anexos, bibliografía). La Nota B afirma que la memoria debe tener exactamente 8 capítulos y que el capítulo 7 es Bibliografía y el 8 es Anexos, integrándolos dentro de la numeración de capítulos.
