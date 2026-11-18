---
tipo: "receta"
titulo: "Cómo calcular speedup global con ley de Amdahl cuando una fracción se acelera"
temas: ["ac", "rendimiento"]
claves: ["speedup", "ley de Amdahl", "fracción mejorada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014A.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[rendimiento]]

Speedup = 1 / ((1 - f) + f/s), donde f = fracción de tiempo en la parte mejorada (0.87), s = factor de aceleración de esa parte (2, porque tarda la mitad). Speedup = 1 / (0.13 + 0.87/2) = 1 / 0.565 ≈ 1.77. Respuesta correcta: 1.77 (opción b).

> La nueva tarjeta gráfica de nuestro ordenador realiza las operaciones en la mitad de tiempo que la antigua. Suponiendo que un juego concreto dedicaba el 87% del tiempo de ejecución a realizar operaciones gráficas, ¿cuál es el speedup obtenido al ejecutar dicho juego sobre la versión mejorada de nuestro ordenador?
> — `repo:datos/temarios/AC/examenes/Noviembre2014A.pdf`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-fraccion-mejorada-al-do]] · [[definicion-de-speedup-y-relacion-con-reduccion-de-tiempo]]
