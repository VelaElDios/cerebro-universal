---
tipo: "receta"
titulo: "Speedup con ley de Amdahl cuando una fracción se acelera"
temas: ["ac", "amdahl", "rendimiento"]
claves: ["speedup", "ley Amdahl", "fracción mejorada", "coprocesador"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014B.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[rendimiento]]

Speedup = 1 / ((1 - f) + f/k). f=0.96 (fracción matemáticas), k=2 (mitad de tiempo → doble velocidad). Speedup = 1 / (0.04 + 0.96/2) = 1 / (0.04 + 0.48) = 1 / 0.52 ≈ 1.92 (opción b).

> Instalamos un coprocesador matemático en nuestro ordenador capaz de realizar las operaciones matemáticas en la mitad de tiempo que nuestro viejo procesador. Suponiendo que un programa concreto dedicaba el 96% del tiempo de ejecución a realizar operaciones matemáticas, ¿cuál es el speedup obtenido al ejecutar dicho programa sobre la versión mejorada de nuestro ordenador?
> — `repo:datos/temarios/AC/examenes/Noviembre2014B.pdf`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-fraccion-mejorada-al-do]]
