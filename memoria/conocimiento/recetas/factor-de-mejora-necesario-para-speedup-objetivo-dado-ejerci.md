---
tipo: "receta"
titulo: "Factor de mejora necesario para speedup objetivo dado (ejercicio 12)"
temas: ["ac", "algebra", "arquitectura-computadores", "ley-amdahl"]
claves: ["speedup objetivo", "factor mejora necesario", "fracción tiempo", "coma flotante"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[algebra]] · [[arquitectura-computadores]] · [[ley-amdahl]]

Dado speedup S, fracción f, tiempo T: S = T / (f*T/k + (1-f)*T) = 1 / (f/k + 1-f). Despejar k: k = f / (1/S - (1-f)). Ejercicio: S=1.5, f=0.4 → k = 0.4 / (1/1.5 - 0.6) = 0.4 / (0.6667 - 0.6) = 0.4 / 0.0667 = 6. Hay que mejorar 6x la parte de coma flotante.

> Una ganancia del 50% significa un speedup de 1.5. Entonces, 1.5 = 15 / (15×0.4/x + 15×0.6) → x=6
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-speedup-maximo-con-ley-de-amdahl-fraccion-mejorab]] · [[despeje-de-fraccion-de-tiempo-mejorable-dado-speedup-objetiv]] · [[como-calcular-el-factor-de-mejora-necesario-k-para-un-speedu]] · [[como-calcular-factor-de-mejora-necesario-segun-ley-de-amdahl]]
