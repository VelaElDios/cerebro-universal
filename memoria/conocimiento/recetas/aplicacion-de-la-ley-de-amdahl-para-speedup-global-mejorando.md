---
tipo: "receta"
titulo: "Aplicación de la ley de Amdahl para speedup global mejorando una parte"
temas: ["ac", "amdahl", "rendimiento", "speedup"]
claves: ["ley de Amdahl", "fracción mejorada", "speedup parcial", "speedup global"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[rendimiento]] · [[speedup]]

Ley de Amdahl: Speedup_global = 1 / ((1 - f) + f / k), donde f = fracción de tiempo en la parte mejorada, k = factor de mejora de esa parte. Aquí f = 100/150 = 2/3. Queremos Speedup_global = 2. 2 = 1 / (1/3 + (2/3)/k) → 1/2 = 1/3 + 2/(3k) → 1/6 = 2/(3k) → k = 4. Hay que mejorar 4 veces la velocidad de la suma. Respuesta: b) 4.

> Let us suppose that a program takes 150 seconds to run of which 100 are used in addition operations. How much do we have to improve the speed of the addition for the program to run at twice the speed?
> — `repo:datos/temarios/AC/examenes/January2020.pdf`
