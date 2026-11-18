---
tipo: "concepto"
titulo: "Limitación de mejora en fracción pequeña (ley de Amdahl)"
temas: ["ac", "cuellos-botella", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "fracción pequeña", "límite speedup", "saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cuellos-botella]] · [[ley-amdahl]] · [[rendimiento]]

La ley de Amdahl implica que mejorar un componente que consume poco tiempo total tiene impacto limitado. En ejercicio 22b: saltos toman 30s de 200s (15%) en Prog A y 30s de 210s (14.3%) en Prog B. Aunque se redujeran a cero, el ahorro máximo sería 30s (15% y 14.3%), insuficiente para el 20% requerido (40s y 42s).

> Para conseguir un ahorro del 20% en el tiempo de ejecución, habría que reducir 40 segundos el tiempo de ejecución del programa A y 42 segundos el tiempo de ejecución del programa B. Sin embargo, mejorando solamente los saltos no es posible lograr ninguna de las dos reducciones.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[determinar-si-es-posible-alcanzar-un-speedup-objetivo-mejora]] · [[ley-de-amdahl-la-aceleracion-maxima-esta-limitada-por-la-fra]] · [[ley-de-amdahl-la-aceleracion-maxima-viene-determinada-por-la]]
