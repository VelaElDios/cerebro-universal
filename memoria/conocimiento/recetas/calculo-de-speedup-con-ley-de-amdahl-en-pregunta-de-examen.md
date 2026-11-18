---
tipo: "receta"
titulo: "Cálculo de speedup con ley de Amdahl en pregunta de examen"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["speedup", "multiplicación", "tiempo ejecución", "mejora parcial"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Aplicación de la ley de Amdahl: tiempo total original = 120 s, tiempo multiplicación = 96 s (fracción f = 96/120 = 0.8), tiempo resto = 24 s. Speedup global deseado = 5 → tiempo nuevo = 24 s. Como el resto no mejora, 24 s = tiempo_resto + tiempo_mult_nuevo = 24 + 96/k → 96/k = 0 → imposible. Respuesta correcta: d. It's impossible.

> Suppose a program takes 2 minutes to run on a machine, of which 96 seconds are for multiplication operations. How much do I have to improve the speed of multiplication if I want the program to run five times faster?
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]]
