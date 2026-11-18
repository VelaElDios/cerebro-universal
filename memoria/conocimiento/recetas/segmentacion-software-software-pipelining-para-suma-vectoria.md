---
tipo: "receta"
titulo: "Segmentación software (software pipelining) para suma vectorial en RISC-V"
temas: ["ac", "planificacion-estatica", "risc-v", "segmentacion-software", "software-pipelining"]
claves: ["fld", "fadd.d", "fsd", "addi", "bne", "start-up", "finish-up", "kernel", "prologue", "epilogue"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[planificacion-estatica]] · [[risc-v]] · [[segmentacion-software]] · [[software-pipelining]]

Estructura en tres fases: (1) Start-up (prólogo): fld f0,0(x1); fadd.d f4,f0,f2; fld f0,-8(x1) — carga dos elementos y calcula el primero. (2) Kernel (bucle principal): fsd f4,0(x1); fadd.d f4,f0,f2; fld f0,-16(x1); addi x1,x1,-8; bne x1,x2,loop — cada iteración almacena resultado anterior, suma el actual, carga el siguiente, decrementa puntero y salta. (3) Finish-up (epílogo): fsd f4,0(x1); fadd.d f4,f0,f2; fsd f4,-8(x1) — vacía la tubería almacenando los dos últimos resultados. Usa solo 3 registros FP (f0,f2,f4). El puntero x1 recorre el array desde X[1000] hacia abajo (direcciones 0xFF00, 0xFEE8, 0xFEE0, 0xFED8...).

> Consiste en transformar un bucle con instrucciones dependientes e iteraciones independientes en un bucle con instrucciones independientes e iteraciones dependientes
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]] · [[segmentacion-software-software-pipelining-en-bucles-sin-depe]] · [[kernel-de-segmentacion-software-para-bucle-de-acumulacion-in]]
