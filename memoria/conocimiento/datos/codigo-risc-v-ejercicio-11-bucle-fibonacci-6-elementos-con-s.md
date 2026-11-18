---
tipo: "dato"
titulo: "Código RISC-V Ejercicio 11: bucle Fibonacci 6 elementos con saltos B1 (beqz) y B2 (bnez)"
temas: ["ac", "prediccion-saltos"]
claves: ["lw", "beqz", "mul", "sw", "addi", "bnez", "Fibonacci", "x1-x5"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Código: loop: lw x3,0(x1); B1=beqz x3,next; mul x3,x3,x5; sw x3,0(x1); next: addi x1,x1,4; addi x2,x2,-1; B2=bnez x2,loop. x1=puntero array, x2=contador (inicializado a 6), x5=factor multiplicación. 6 iteraciones. B1 tomado solo en 1ª iteración (x3=0). B2 tomado en 5 primeras iteraciones, no tomado en la 6ª.

> El siguiente código de RISC-V lee de memoria los 6 primeros números de una serie de Fibonacci 0, 1, 1, 2, 3, 5. Asume que x1, x2 y x5 se han inicializado previamente.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[codigo-risc-v-ejercicio-10-bucle-conteo-a-en-exam18-con-salt]] · [[codigo-risc-v-ejercicio-12-bucle-vector-disperso-0-7-0-0-0-0]] · [[comportamiento-real-de-saltos-b1-y-b2-en-bucle-risc-v-que-re]]
