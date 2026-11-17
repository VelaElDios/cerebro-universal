---
tipo: "receta"
titulo: "Speedup con cambio simultáneo de CPI y frecuencia de reloj"
temas: ["ac", "cpi", "frecuencia-reloj", "rendimiento"]
claves: ["speedup", "CPI", "frecuencia reloj", "coma flotante", "instrucciones enteras"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[frecuencia-reloj]] · [[rendimiento]]

Cuando una mejora cambia tanto el CPI de cierto tipo de instrucciones como la frecuencia de reloj: 1) Calcular tiempo original: T_orig = Σ (N_i × CPI_i_orig × T_ciclo_orig). 2) Calcular tiempo nuevo: T_new = Σ (N_i × CPI_i_new × T_ciclo_new). 3) Speedup = T_orig / T_new. Ejercicio 17: CPI_fp pasa de 4×CPI_int a 0.35×(4×CPI_int), ciclo sube 20% (×1.2). Con 6M int + 2M fp: speedup = 1.33 (33% más rápido).

> Tiempo de ejecución = Número de Instrucciones × CPI × Duración del ciclo
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]]
