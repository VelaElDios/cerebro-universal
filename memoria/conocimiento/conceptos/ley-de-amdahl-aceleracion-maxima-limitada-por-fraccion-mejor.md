---
tipo: "concepto"
titulo: "Ley de Amdahl: aceleración máxima limitada por fracción mejorable"
temas: ["ac", "ley de amdahl", "rendimiento"]
claves: ["ley de Amdahl", "fracción tiempo", "aceleración máxima", "factor mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ley de amdahl]] · [[rendimiento]]

Speedup_global = 1 / ((1 - f) + f/k), donde f = fracción de tiempo que usa la parte mejorada y k = factor de mejora de esa parte. Si f → 0, speedup → 1; si f → 1, speedup → k. La opción c) es falsa porque el speedup no depende solo de k.

> La ley de Amdahl para el rendimiento indica que a) La aceleración máxima del rendimiento obtenida al realizar una mejora viene determinada por la fracción de tiempo que pueda utilizarse dicha mejora
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`

Relacionado: [[ley-de-amdahl-la-aceleracion-maxima-esta-limitada-por-la-fra]] · [[ley-de-amdahl-la-aceleracion-maxima-viene-determinada-por-la]] · [[ley-de-amdahl-para-speedup-con-mejora-parcial]]
