---
tipo: "concepto"
titulo: "Estructura de la memoria TFG ESIIAB-UCLM (plantilla oficial)"
temas: ["latex", "plantilla", "tfg"]
claves: ["elements/portada.tex", "elements/preambulo.tex", "Memoria.tex", "include/configuracion.tex"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[plantilla]] · [[tfg]]

La plantilla inmutable incluye: portada (elements/portada.tex), declaración de autoría, Resumen, Abstract, índices (general, figuras, tablas), capítulos, anexos, bibliografía. No se quita nada de la plantilla salvo indicación expresa de Javier. Los títulos en negro y negrita (\definecolor{tema}{RGB}{0,0,0}), enlaces sin recuadros (hidelinks), sin páginas en blanco entre capítulos (renewcommand{\cleardoublepage}{\clearpage}).

> Una sola portada: la oficial del TFG, la de elements/portada.tex (escudo, Universidad de Castilla-La Mancha y Escuela Superior de Ingeniería Informática, tipo de trabajo, título, autor y fecha, todo centrado). Memoria.tex hace \input{elements/portada}. No se añade ninguna otra portada; tampoco la «segunda portada» con los logos UCLM/ESII de elements/preambulo.tex.
> — `memoria/reglas-tfg.md`

Relacionado: [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[una-sola-portada-oficial-en-elements-portada-tex]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
