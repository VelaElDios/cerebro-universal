---
tipo: "receta"
titulo: "Kernel de segmentación software para bucle de acumulación inversa en RISC-V"
temas: ["ac", "ensamblador", "planificacion-estatica", "risc-v"]
claves: ["fld", "fadd.d", "fsd", "addi", "bne", "prologue", "kernel", "epilogue"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ensamblador]] · [[planificacion-estatica]] · [[risc-v]]

Prologue (inicio): fld f0,0(x1)  // carga X[999] en f0; fadd.d f4,f0,f2  // f4 = X[999]+k; fld f0,-8(x1)  // carga X[998] en f0. Kernel (bucle L): fsd f4,0(x1)        // almacena resultado en M[i]; fadd.d f4,f0,f2    // calcula siguiente suma con f0 (X[i-1]); fld f0,-16(x1)     // carga X[i-2] en f0; addi x1,x1,-8      // decrementa puntero 8 bytes; bne x1,x0,L        // salta si x1≠0. Epílogo (fin): fsd f4,0(x1); fadd.d f4,f0,f2; fsd f4,-8(x1). Requiere que no haya dependencias entre iteraciones (bucle DOALL).

> L: fsd     f4,0(x1);   Almacena M[i]    fadd.d f4,f0,f2 ; Suma a M[i-1]    fld    f0,-16(x1); Carga M[i-2]    addi   x1,x1,-8    bne    x1,x0,L
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[segmentacion-software-software-pipelining-en-bucles-sin-depe]] · [[segmentacion-software-software-pipelining-para-suma-vectoria]] · [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]]
