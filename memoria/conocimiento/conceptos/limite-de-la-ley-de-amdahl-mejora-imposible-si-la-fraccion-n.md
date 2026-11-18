---
tipo: "concepto"
titulo: "Límite de la ley de Amdahl: mejora imposible si la fracción no mejorada domina"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "límite", "operaciones memoria", "speedup imposible"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Tiempo objetivo = 80/8 = 10 s. La parte no mejorada (no memoria) ya dura 10 s. Para lograr 10 s totales, las operaciones de memoria deberían tardar 0 s → mejora infinita (imposible). Respuesta d) This is not possible. Ilustra que el speedup máximo está acotado por la fracción no mejorada.

> Let’s assume that a program takes 80 seconds to run on a computer, of which 70 correspond to memory operations. How much do I have to improve the speed of memory operations if I want the program to run 8 times faster?
> — `repo:datos/temarios/AC/examenes/June2019.pdf`
