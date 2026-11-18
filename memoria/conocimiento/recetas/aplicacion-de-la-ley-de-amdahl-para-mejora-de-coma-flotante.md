---
tipo: "receta"
titulo: "Aplicación de la ley de Amdahl para mejora de coma flotante"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "speedup", "fracción mejorada", "coma flotante"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Speedup_global = 1 / ((1 - f) + f/k), donde f=fracción mejorada (0.7), k=factor de mejora. Para speedup 1.4: 1.4 = 1/(0.3 + 0.7/k) → k ≈ 1.69. La mejora necesaria en la parte flotante es ~1.69x.

> Supongamos que el 70% de las instrucciones de dicho programa son instrucciones en coma flotante. ¿En qué medida habría que mejorar la ejecución de las instrucciones en coma flotante de nuestra máquina para obtener una ganancia del 40% para este programa de prueba?
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf`
