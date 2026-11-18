---
tipo: "concepto"
titulo: "Dependencia entre iteraciones en bucle con S.D y DADDUI sobre R1"
temas: ["ac", "dependencias", "loop-carried", "mips"]
claves: ["S.D", "DADDUI", "R1", "loop-carried dependence"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[loop-carried]] · [[mips]]

S.D F4, 0(R1) usa R1 como base; DADDUI R1, R1, #-8 actualiza R1. En la misma iteración: S.D lee R1 (RAW con DADDUI anterior? No, DADDUI está después). Entre iteraciones: DADDUI de iteración n actualiza R1 que S.D de iteración n+1 leerá → dependencia loop-carried por R1. Respuesta: c).

> Between the S.D and the DADDUI instructions... a) There are not dependences b) There is a data dependence, through R1, in the same iteration c) There is a data dependence, through R1, between iterations d) There is an output dependence, through R1, in the same iteration
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-mips-con-acceso-a-memoria]] · [[antidependencia-war-entre-s-d-y-daddui-por-r1-en-misma-itera]] · [[dependencias-en-fragmento-de-codigo-fp-mips-l-d-add-s-add-s]]
