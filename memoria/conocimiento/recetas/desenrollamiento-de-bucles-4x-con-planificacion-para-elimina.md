---
tipo: "receta"
titulo: "Desenrollamiento de bucles 4x con planificación para eliminar detenciones (RISC-V)"
temas: ["ac", "loop-unrolling", "planificacion-estatica", "risc-v"]
claves: ["fld", "fadd.d", "fsd", "addi", "bne", "desenrollamiento", "planificacion", "detenciones", "ciclos-por-dato"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[loop-unrolling]] · [[planificacion-estatica]] · [[risc-v]]

Transformación de un bucle simple de suma vectorial (fld → fadd.d → fsd → addi → bne) en versión desenrollada 4x con reordenamiento: primero todas las cargas (fld f0,0(x1); fld f6,-8(x1); fld f10,-16(x1); fld f14,-24(x1)), luego todas las sumas (fadd.d f4,f0,f2; fadd.d f8,f6,f2; fadd.d f12,f10,f2; fadd.d f16,f14,f2), luego stores y control (fsd f4,0(x1); fsd f8,-8(x1); addi x1,x1,-32; bne x1,x2,loop; fsd f12,16(x1); fsd f16,8(x1)). Se usan 8 registros de punto flotante (f0,f4,f6,f8,f10,f12,f14,f16) más f2 para la constante k. Resultado: 3,5 ciclos por dato del vector (frente a 7 ciclos/dato sin planificación y 16 ciclos/4 datos en desenrollamiento simple).

> Se separan las instrucciones dependientes insertando tantas instrucciones entre ellas como detenciones había
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[desenrollamiento-de-bucles-loop-unrolling-4x-con-renombrado]] · [[comparativa-de-ciclos-por-dato-bucle-original-vs-desenrollad]] · [[segmentacion-software-software-pipelining-para-suma-vectoria]]
