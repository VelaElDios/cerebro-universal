---
tipo: "receta"
titulo: "Aplicación de la ley de Amdahl para speedup con mejora fraccional"
temas: ["ac", "amdahl", "rendimiento"]
claves: ["ley de Amdahl", "speedup", "fracción mejorada", "punto flotante"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[rendimiento]]

Ley de Amdahl: Speedup = 1 / [(1 - f) + f/k], donde f = fracción de tiempo mejorable (0.5), k = factor de mejora (2). Speedup = 1 / [0.5 + 0.5/2] = 1 / 0.75 = 1.333. La máquina es un 33% más rápida. Respuesta correcta: c) 33% más rápida.

> Un programa de prueba se ejecuta en un computador con una frecuencia de 1,2 GHz, tardando 12 segundos. La mitad de ese tiempo fue empleado en la ejecución de instrucciones de punto flotante. Mejoramos el computador haciendo que todas las instrucciones en punto flotante se ejecuten en la mitad de tiempo.
> — `repo:datos/temarios/AC/examenes/Noviembre2013.pdf`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-fraccion-mejorada-al-do]]
