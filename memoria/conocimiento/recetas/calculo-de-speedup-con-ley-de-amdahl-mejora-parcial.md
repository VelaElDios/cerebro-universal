---
tipo: "receta"
titulo: "Cálculo de speedup con ley de Amdahl (mejora parcial)"
temas: ["ac", "amdahl", "rendimiento"]
claves: ["speedup", "ley de Amdahl", "fracción mejorada", "factor mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[rendimiento]]

Speedup global = 1 / ((1 - f) + f / k), donde f = fracción de tiempo en la parte mejorada (0.87) y k = factor de mejora de esa parte (2, al tardar la mitad). Speedup = 1 / (0.13 + 0.87/2) = 1 / 0.565 ≈ 1.77. La respuesta correcta es 1.77 (opción b).

> La nueva tarjeta gráfica de nuestro ordenador realiza las operaciones en la mitad de tiempo que la antigua. Suponiendo que un juego concreto dedicaba el 87% del tiempo de ejecución a realizar operaciones gráficas, ¿cuál es el speedup obtenido al ejecutar dicho juego sobre la versión mejorada de nuestro ordenador?
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[speedup-con-ley-de-amdahl-para-mejora-parcial-de-tarjeta-gra]] · [[calculo-de-speedup-con-ley-de-amdahl-ejemplo-tarjeta-grafica]] · [[speedup-por-ley-de-amdahl-con-mejora-10x-usada-20-del-tiempo]]
