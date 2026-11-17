---
tipo: "fuente"
titulo: "Tema1 ProbSol (Tema1-Introduccion)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`.

## Resumen
Este trozo contiene 8 ejercicios resueltos del Tema 1 de Arquitectura de Computadores (curso 2026/27). Cubre métricas fundamentales de rendimiento: efectividad en coste (rendimiento/coste), MIPS pico y nativo, CPI ponderado por mezcla de instrucciones, ley de Amdahl para speedup con mejora parcial, expansión de cuenta de instrucciones al emular punto flotante en entero, y la paradoja de que mayor MIPS no implica menor tiempo de ejecución (Ejercicio 6).
Este trozo contiene la resolución de ejercicios 8 a 15 de Arquitectura de Computadores (Tema 1), centrados en la ley de Amdahl, cálculo de speedup, métricas MIPS/CPI y comparación de mejoras de hardware. Se aplican fórmulas de aceleración fraccionaria, tiempo de ejecución ponderado y rendimiento en MIPS nativos y de pico para dos máquinas con distinto CPI y frecuencia.
Este trozo contiene siete ejercicios resueltos de evaluación de rendimiento en arquitectura de computadores (Tema 1). Cálculos de speedup mediante la ley de Amdahl (ejercicios 16, 18), speedup con cambio de CPI y frecuencia de reloj (ejercicio 17), comparación de máquinas con distinto CPI y frecuencia (ejercicios 19, 20), análisis de tiempo total de ejecución y speedups relativos (ejercicio 21), y cálculo de CPI a partir de tiempos por tipo de instrucción (ejercicio 22). Todas las soluciones aplican la fórmula fundamental: Tiempo = Instrucciones × CPI / Frecuencia.
Este trozo presenta el Ejercicio 23 resuelto: se aplica la ley de Amdahl para calcular qué fracción del tiempo de ejecución debe usar el disco (ahora 4 veces más rápido) para lograr una aceleración global de 3×. La solución establece la ecuación 3 = T / (xT/4 + (1-x)T) y obtiene x = 0.89, es decir, el disco debe utilizarse el 89 % del tiempo.

## Lo que se sacó de él (31)
- [[calculo-de-cpi-a-partir-de-tiempos-por-tipo-de-instruccion-y]]
- [[calculo-de-cpi-medio-mips-y-speedup-entre-dos-maquinas]]
- [[calculo-de-mips-nativos-y-de-pico-peak-mips-para-maquinas-co]]
- [[calculo-de-speedup-con-ley-de-amdahl-mejora-de-una-fraccion]]
- [[calculo-de-speedup-maximo-con-ley-de-amdahl-fraccion-mejorab]]
- [[calculo-de-tiempo-de-ejecucion-nuevo-y-speedup-con-mejora-fr]]
- [[como-calcular-cpi-medio-y-mips-nativo-con-mezcla-de-instrucc]]
- [[como-calcular-efectividad-en-coste-rendimiento-coste-entre-d]]
- [[como-calcular-el-factor-de-mejora-necesario-k-para-un-speedu]]
- [[como-calcular-la-fraccion-de-uso-requerida-para-un-speedup-o]]
- [[como-calcular-mips-pico-peak-mips-eligiendo-la-instruccion-m]]
- [[como-convertir-porcentaje-de-ganancia-speedup-a-factor-de-sp]]
- [[como-expandir-la-cuenta-de-instrucciones-al-emular-punto-flo]]
- [[comparacion-de-maquinas-por-tiempo-total-de-ejecucion-de-mul]]
- [[despeje-de-fraccion-de-tiempo-mejorable-dado-speedup-objetiv]]
- [[factor-de-mejora-necesario-para-speedup-objetivo-dado-ejerci]]
- [[igualar-mips-entre-dos-maquinas-despejando-frecuencia-de-rel]]
- [[igualar-rendimiento-de-dos-maquinas-ajustando-frecuencia-de]]
- [[ley-de-amdahl-aplicada-a-mejora-de-disco]]
- [[ley-de-amdahl-aplicada-a-speedup-con-mejora-parcial-de-un-su]]
- [[limitacion-de-mejora-en-fraccion-pequena-ley-de-amdahl]]
- [[paradoja-mips-vs-tiempo-de-ejecucion-mayor-mips-no-garantiza]]
- [[resultado-numerico-disco-4-mas-rapido-para-speedup-3-requier]]
- [[seleccion-de-mejora-hardware-multiplicacion-vs-memoria-ejerc]]
- [[seleccion-de-mejoras-mutuamente-excluyentes-con-ley-de-amdah]]
- [[speedup-combinado-de-mejoras-independientes-en-fracciones-di]]
- [[speedup-combinando-multiples-mejoras-independientes]]
- [[speedup-con-cambio-simultaneo-de-cpi-y-frecuencia-de-reloj]]
- [[uso-de-la-ley-de-amdahl-para-dimensionar-requisitos-de-uso-d]]
- [[valores-de-referencia-cpi-por-clase-de-instruccion-en-maquin]]
- [[valores-de-referencia-cpi-por-clase-en-dos-implementaciones]]
