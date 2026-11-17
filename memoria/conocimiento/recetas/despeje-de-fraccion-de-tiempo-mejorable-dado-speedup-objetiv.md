---
tipo: "receta"
titulo: "Despeje de fracción de tiempo mejorable dado speedup objetivo y factor de mejora"
temas: ["ac", "algebra", "arquitectura-computadores", "ley-amdahl"]
claves: ["speedup", "fracción tiempo", "factor mejora", "despeje ecuación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[algebra]] · [[arquitectura-computadores]] · [[ley-amdahl]]

Dado speedup S, tiempo original T, factor mejora k: S = T / (T(1-x) + T*x/k) = 1 / ((1-x) + x/k). Despejar x: x = (1 - 1/S) / (1 - 1/k). En el ejercicio: S=5, k=10 → x = (1-0.2)/(1-0.1) = 0.8/0.9 = 0.888... ≈ 89%.

> Por lo tanto, 5 = 50 / (50(1-x) + 50x/10), de donde x = 0.89 (89%).
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-speedup-maximo-con-ley-de-amdahl-fraccion-mejorab]]
