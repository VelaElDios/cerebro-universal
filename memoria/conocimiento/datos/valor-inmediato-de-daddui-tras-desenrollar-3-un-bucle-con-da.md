---
tipo: "dato"
titulo: "Valor inmediato de DADDUI tras desenrollar 3× un bucle con DADDUI R1,R1,#-8"
temas: ["ac", "bucles", "loop-unrolling", "mips"]
claves: ["DADDUI", "inmediato", "unroll 3", "#-24"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[loop-unrolling]] · [[mips]]

Cada iteración original decrementa R1 en 8 (bytes). Tres iteraciones → decremento total 24. El inmediato pasa de #-8 a #-24 (opción d).

> After unrolling 3 times the loop of the previous question, the immediate value of the DADDUI instruction will be: d) #-24
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-instrucciones-tras-desenrollar-bucle-3-veces-unro]] · [[dependencia-entre-iteraciones-en-bucle-con-s-d-y-daddui-sobr]] · [[analisis-de-dependencias-en-bucle-mips-con-acceso-a-memoria]]
