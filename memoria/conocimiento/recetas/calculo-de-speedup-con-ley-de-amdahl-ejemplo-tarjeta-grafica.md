---
tipo: "receta"
titulo: "Cálculo de speedup con Ley de Amdahl (ejemplo tarjeta gráfica 4x, 40% tiempo)"
temas: ["ac", "pipeline"]
claves: ["Amdahl", "speedup", "fracción mejorada", "aceleración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

Speedup = 1 / ((1 - f) + f/s) donde f=0.4 (fracción mejorada) y s=4 (aceleración). Speedup = 1 / (0.6 + 0.1) = 1/0.7 ≈ 1.43. La respuesta correcta es 1.43 (opción b).

> La nueva tarjeta gráfica de nuestro ordenador es cuatro veces más rápida que la antigua. Suponiendo que un juego de ordenador concreto dedica el 40% de su tiempo de ejecución a realizar operaciones gráficas, ¿cuál será el speedup obtenido…
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf` (cita sin comprobar)

Relacionado: [[speedup-con-ley-de-amdahl-para-mejora-parcial-de-tarjeta-gra]] · [[calculo-de-speedup-con-ley-de-amdahl-mejora-parcial]] · [[calculo-de-ganancia-de-velocidad-speedup-con-la-ley-de-amdah]]
