---
tipo: "dato"
titulo: "Comparativa de ciclos por dato: bucle original vs desenrollado vs desenrollado+planificado vs segmentación software"
temas: ["ac", "ciclos-por-dato", "metricas", "planificacion-estatica", "rendimiento"]
claves: ["7-ciclos", "3.5-ciclos", "cpi", "ilp"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ciclos-por-dato]] · [[metricas]] · [[planificacion-estatica]] · [[rendimiento]]

Métricas de rendimiento para la suma vectorial X = X + k en RISC-V: (a) Bucle original con detenciones por dependencias RAW (fld→fadd.d, fadd.d→fsd, salto): ~7 ciclos/dato. (b) Desenrollado 4x sin planificación: 16 ciclos / 4 datos = 4 ciclos/dato, pero con detenciones internas. (c) Desenrollado 4x CON planificación (reordenamiento cargas→sumas→stores): 3,5 ciclos/dato, eliminando todas las detenciones. (d) Segmentación software: kernel de 5 instrucciones (fsd, fadd.d, fld, addi, bne) con CPI ideal → 1 ciclo/iteración en steady state, pero requiere start-up/finish-up; efectivamente ~1 ciclo/dato tras amortizar prólogo/epílogo.

> Se obtienen 3,5 ciclos por cada dato del vector
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]] · [[segmentacion-software-software-pipelining-para-suma-vectoria]] · [[segmentacion-software-software-pipelining-en-bucles-sin-depe]]
