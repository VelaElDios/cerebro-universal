---
tipo: "receta"
titulo: "Cómo calcular factor de mejora necesario según Ley de Amdahl"
temas: ["ac", "coma-flotante", "ley-amdahl", "rendimiento"]
claves: ["factor mejora", "Amdahl", "fracción mejorada", "speedup objetivo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2011.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[coma-flotante]] · [[ley-amdahl]] · [[rendimiento]]

Speedup_global = 1 / [(1-f) + f/k]. Queremos speedup_global = 1,5 (ganancia 50%), f = 0,8. 1,5 = 1 / [0,2 + 0,8/k] → 0,2 + 0,8/k = 2/3 → 0,8/k = 2/3 - 0,2 = 0,4667 → k = 0,8/0,4667 ≈ 1,71. Respuesta correcta: 1,71 (opción b).

> Un programa tiene un tiempo de ejecución de 5 segundos, dedicando el 80% de dicho tiempo a ejecutar instrucciones en coma flotante. Para obtener una ganancia del 50%, debemos tener un factor de mejora en la ejecución de las instrucciones en coma flotante de:
> — `repo:datos/temarios/AC/examenes/Noviembre2011.pdf` (cita sin comprobar)
