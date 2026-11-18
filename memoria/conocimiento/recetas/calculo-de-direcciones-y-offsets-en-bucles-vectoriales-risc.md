---
tipo: "receta"
titulo: "Cálculo de direcciones y offsets en bucles vectoriales RISC-V con puntero descendente"
temas: ["ac", "arrays", "direccionamiento", "punteros", "risc-v"]
claves: ["x1", "x2", "offset", "0xFF00", "0xFEE8", "0xFEE0", "0xFED8", "double-precision", "8-bytes"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arrays]] · [[direccionamiento]] · [[punteros]] · [[risc-v]]

Convención de direccionamiento para array de double precision (8 bytes/elemento) recorridos hacia abajo: x1 apunta al elemento actual. Inicial: x1 = &X[1000] = 0xFF00. Offsets en instrucciones: 0(x1) = elemento actual, -8(x1) = anterior, -16(x1) = dos atrás, -24(x1) = tres atrás. En desenrollado 4x: addi x1,x1,-32 avanza 4 elementos (32 bytes). En segmentación software: addi x1,x1,-8 avanza 1 elemento por iteración del kernel. El registro x2 sirve como límite (x2 = &X[0] - 8 o similar); en una variante se ajusta con addi x2,x2,16 al inicio. Direcciones mostradas: X[1000]=0xFF00, X[999]=0xFEE8, X[998]=0xFEE0, X[997]=0xFED8.

> x1 0xFED8 X[997] 0xFEE0 X[998] 0xFEE8 X[999] 0xFF00 X[1000]
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]] · [[bucle-risc-v-para-calibracion-imu-con-puntero-descendente]] · [[segmentacion-software-software-pipelining-para-suma-vectoria]] · [[desenrollamiento-de-bucles-loop-unrolling-4x-con-renombrado]]
