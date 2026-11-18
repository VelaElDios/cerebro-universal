---
tipo: "receta"
titulo: "Cómo calcular Cycles Per Result (CPR) en bucles pipelined con stalls"
temas: ["ac", "cpr", "loop", "mips64", "performance", "pipeline"]
claves: ["CPR", "Cycles Per Result", "stalls", "loop unrolling", "throughput"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpr]] · [[loop]] · [[mips64]] · [[performance]] · [[pipeline]]

CPR = (ciclos totales para ejecutar una iteración completa del bucle) / (resultados producidos por iteración). En este ejercicio: 1 resultado (temp °C) por iteración. Pasos: 1) Dibujar diagrama de pipeline con stalls para una iteración. 2) Contar ciclos desde inicio de I1 hasta inicio de I1 de siguiente iteración (periodo de iniciación). 3) Ese periodo = CPR porque hay 1 resultado/iteración. Con stalls calculados: I1(L.S) a I7(BNE) + stalls = longitud del ciclo de iniciación. Fórmula general: CPR = max(latencia_camino_crítico, ancho_recursos) considerando stalls por dependencias y restricciones estructurales (ej. no 2 WB FP mismo ciclo).

> b) Indicate the number of Cycles Per Result (CPR) for the code provided in the exercise.
> — `repo:datos/temarios/AC/examenes/June2020.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[como-se-agrupan-capturas-con-subfigure]] · [[desenrollado-de-bucle-minimo-para-eliminar-todos-los-stalls]] · [[calculo-de-detenciones-stalls-y-cpr-en-pipeline-risc-v-con-f]] · [[planificacion-de-bucle-jacobsthal-en-pipeline-mips64-con-uni]]
