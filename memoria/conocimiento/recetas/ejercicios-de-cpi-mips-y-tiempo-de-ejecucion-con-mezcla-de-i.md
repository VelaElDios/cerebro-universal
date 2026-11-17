---
tipo: "receta"
titulo: "Ejercicios de CPI, MIPS y tiempo de ejecución con mezcla de instrucciones"
temas: ["ac", "compilador", "cpi", "mezcla de instrucciones", "mips", "tiempo de ejecución"]
claves: ["CPI", "cycles per instruction", "MIPS", "frecuencia de reloj", "mezcla de instrucciones", "compilador 1 vs 2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilador]] · [[cpi]] · [[mezcla de instrucciones]] · [[mips]] · [[tiempo de ejecución]]

Problemas para calcular CPI medio, MIPS y tiempo de ejecución dado CPI por tipo de instrucción, frecuencia de reloj y mezcla de instrucciones (porcentaje o cuenta absoluta). Ej.10: CPI base vs optimizado con frecuencias distintas (500 vs 600 MHz) y mezcla 40/25/25/10; Ej.11: comparar M1 (CPI variables 2,6,4 a 400 MHz) vs M2 (CPI fijo 3 a 750 MHz) con mezcla 40/50/10, calcular MIPS y MIPS pico; Ej.20: igual que Ej.10 pero con 4 tipos; Ej.6: dos compiladores generan distintas cuentas de instrucciones (A,B,C) para mismo programa, misma máquina (800 MHz, CPI 1,2,3). ¿Cuál es más rápido según MIPS? ¿Según tiempo de ejecución? (MIPS = frecuencia / CPI_medio; tiempo = instrucciones * CPI_medio / frecuencia). El compilador que genera menos instrucciones totales puede tener peor MIPS pero mejor tiempo.

> M1 necesita 2, 6, y 4 ciclos de reloj para ejecutar las instrucciones de tipo A, B y C, respectivamente. Por su parte, M2 emplea 3 ciclos para todos los tipos. M1 tiene una frecuencia de reloj de 400 MHz y M2 una frecuencia de 750 MHz.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)`

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]]
