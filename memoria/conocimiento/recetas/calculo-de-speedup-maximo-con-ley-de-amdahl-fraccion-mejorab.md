---
tipo: "receta"
titulo: "Cálculo de speedup máximo con ley de Amdahl (fracción mejorable y factor k)"
temas: ["ac", "arquitectura-computadores", "ley-amdahl", "speedup"]
claves: ["speedup", "ley de Amdahl", "fracción mejorable", "factor mejora", "cota superior"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[ley-amdahl]] · [[speedup]]

Para un programa donde una fracción f del tiempo se ejecuta en código mejorable k veces más rápido: speedup = 1 / ((1-f) + f/k). La cota superior (k→∞) es 1/(1-f). En el ejercicio, f=0.9 → speedup_máx = 1/0.1 = 10.

> A medida que el factor de mejora (k) crece, la aceleración se hace mayor. En el límite, tendremos un factor de mejora ∞, y un speedup = 1/0.1 = 10. Esa es la cota superior para la aceleración.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
