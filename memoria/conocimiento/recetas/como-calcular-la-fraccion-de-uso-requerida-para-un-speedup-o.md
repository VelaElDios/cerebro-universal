---
tipo: "receta"
titulo: "Cómo calcular la fracción de uso requerida para un speedup objetivo con Amdahl"
temas: ["ac", "rendimiento", "resolución-problemas"]
claves: ["fórmula Amdahl", "despeje x", "speedup objetivo", "factor mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rendimiento]] · [[resolución-problemas]]

Pasos: 1) Identificar factor de mejora del componente (k=4). 2) Establecer speedup global deseado (S=3). 3) Usar S = 1 / ((x/k) + (1-x)). 4) Despejar x: x = (1 - 1/S) / (1 - 1/k). 5) Sustituir valores: x = (1 - 1/3) / (1 - 1/4) = (2/3) / (3/4) = 8/9 ≈ 0.889. 6) Interpretar: el componente mejorado debe usarse el 88.9 % del tiempo original.

> speedup = 3 = T / (xT/4 + (1-x)T) ⟹ x = 0.89 (el disco debe usarse el 89% del tiempo)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[ley-de-amdahl-aplicada-a-mejora-de-disco]] · [[ley-de-amdahl-aplicada-a-mejora-de-disco-fraccion-de-uso-par]] · [[aplicacion-de-la-ley-de-amdahl-para-determinar-fraccion-de-u]]
