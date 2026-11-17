---
tipo: "receta"
titulo: "Cálculo de tiempo de ejecución nuevo y speedup con mejora fraccionaria (ejercicio 9)"
temas: ["ac", "arquitectura-computadores", "ley-amdahl", "tiempo-ejecucion"]
claves: ["tiempo ejecución nuevo", "speedup", "fracción mejorada", "factor mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[ley-amdahl]] · [[tiempo-ejecucion]]

Fórmula general: T_nuevo = (f * T_original) / k + (1-f) * T_original. Speedup = T_original / T_nuevo. Ejercicio 9: T_orig=100s, f=0.9, k=10 → T_nuevo = 90/10 + 10 = 19s. Speedup = 100/19 ≈ 5.26. Fracción tiempo nuevo en parte mejorada = (f*T_orig/k) / T_nuevo = 9/19 ≈ 47.37%.

> Tiempo ejecución nuevo = Tiempo afectado por la mejora / Cantidad de la mejora + Tiempo no afectado por la mejora
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-speedup-maximo-con-ley-de-amdahl-fraccion-mejorab]]
