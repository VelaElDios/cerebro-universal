---
tipo: "receta"
titulo: "Aplicación de la ley de Amdahl para determinar fracción de uso de un componente mejorado"
temas: ["ac", "ley de amdahl", "rendimiento"]
claves: ["Amdahl", "speedup", "fracción de uso", "disco"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley de amdahl]] · [[rendimiento]]

Speedup global = 1 / [(1 - f) + f/k], donde f = fracción de tiempo que se usa el componente, k = factor de mejora. Despejar f: f = (1 - 1/S) / (1 - 1/k). Para S=3, k=6: f = (1 - 1/3) / (1 - 1/6) = (2/3) / (5/6) = 4/5 = 80%. El disco debe usarse el 80% del tiempo.

> If the hard disk of a computer is replaced by another disk six times faster than the current one, calculate the use that should be made of this device if we want to make the computer run three times faster
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]]
