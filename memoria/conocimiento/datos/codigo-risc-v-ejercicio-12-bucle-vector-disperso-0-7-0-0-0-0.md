---
tipo: "dato"
titulo: "Código RISC-V Ejercicio 12: bucle vector disperso (0,7,0,0,0,0,2,0) con saltos B1 (beqz), B2 (beq), j incondicional"
temas: ["ac", "prediccion-saltos"]
claves: ["add", "lw", "beqz", "addi", "beq", "j", "vector disperso", "x1-x4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Código: add x4,x0,x0; count: lw x3,0(x1); B1=beqz x3,isnull; addi x4,x4,1; isnull: B2=beq x1,x2,end; addi x1,x1,4; j count; end: sw x4... Vector 8 elementos: índices 0..7. x1=inicio, x2=fin. 8 iteraciones. B1 tomado cuando elemento==0 (6 veces), no tomado cuando !=0 (2 veces: 7 y 2). B2 tomado solo en última iteración (x1==x2), no tomado en 7 primeras. Salto incondicional 'j count' siempre tomado.

> El siguiente código RISC-V cuenta (en x4) el número de elementos no nulos que hay en un vector disperso almacenado en memoria. Un vector disperso es aquel en el que la mayoría de sus elementos son 0.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`
