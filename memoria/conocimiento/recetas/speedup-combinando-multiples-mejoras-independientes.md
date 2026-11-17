---
tipo: "receta"
titulo: "Speedup combinando múltiples mejoras independientes"
temas: ["ac", "ley-amdahl", "multiples-mejoras", "rendimiento"]
claves: ["speedup combinado", "Amdahl", "fracciones disjuntas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ley-amdahl]] · [[multiples-mejoras]] · [[rendimiento]]

Cuando se aplican varias mejoras a fracciones disjuntas del tiempo de ejecución: speedup_total = 1 / Σ(f_i/k_i) + f_resto. Ejercicio 18: multiplicación 25% ×5, memoria 45% ×3, resto 30% sin mejora. Speedup solo mult=1.25, solo mem=1.43, ambas=2.0. Fórmula: 1 / (0.25/5 + 0.45/3 + 0.30) = 2.0.

> Si combinamos ambas mejoras, tenemos: speedup = Tiempo sin mejora / (Tiempo_frac1/mejora1 + Tiempo_frac2/mejora2 + Tiempo_resto)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
