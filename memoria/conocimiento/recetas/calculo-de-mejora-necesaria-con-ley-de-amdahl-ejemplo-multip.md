---
tipo: "receta"
titulo: "Cálculo de mejora necesaria con Ley de Amdahl (ejemplo multiplicación)"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "speedup", "fracción mejorada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Para que el programa dure la mitad (100 s), la parte no mejorada (50 s) queda fija. La parte de multiplicación (150 s) debe reducirse a 50 s, por lo que su velocidad debe multiplicarse por 3 (150/50). Fórmula general: speedup_global = 1 / ((1 - f) + f/k), donde f es la fracción de tiempo en la parte mejorada y k el factor de mejora de esa parte. Despejando k: k = (f * speedup_global) / (speedup_global * (1 - f) + f - 1). En el ejemplo: f = 150/200 = 0.75, speedup_global = 2 → k = 3.

> Suppose a program takes 200 seconds to run on a machine, 150 seconds of which are for multiplication operations. How much do I have to improve the multiplication speed if I want the program to run twice as fast?
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)`
