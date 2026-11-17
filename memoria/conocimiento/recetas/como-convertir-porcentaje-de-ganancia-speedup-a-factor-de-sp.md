---
tipo: "receta"
titulo: "Cómo convertir porcentaje de ganancia (speedup %) a factor de speedup (n)"
temas: ["ac", "evaluacion-rendimiento", "porcentaje-ganancia", "speedup"]
claves: ["ganancia 50%", "speedup 1.5", "factor aceleración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[evaluacion-rendimiento]] · [[porcentaje-ganancia]] · [[speedup]]

Fórmula: %ganancia = (speedup - 1) × 100.
Por tanto: speedup = 1 + (%ganancia / 100).
Ejemplo: 50% ganancia → speedup = 1.5; 67% ganancia → speedup = 1.67.

> Una ganancia (o aceleración) del 50% significa que la relación entre los tiempos de ejecución sin y con mejora es 1.5, ya que: f = (n − 1) × 100 → 50 = (n − 1) × 100 → n = 1.5
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[ley-de-amdahl-aplicada-a-speedup-con-mejora-parcial-de-un-su]]
