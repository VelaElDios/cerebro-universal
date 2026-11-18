---
tipo: "receta"
titulo: "Preguntas del Problema 1: Detenciones, CPI y Desenrollamiento con salto retardado"
temas: ["ac", "cpi", "delayed-branch", "loop-unrolling", "pipeline"]
claves: ["detenciones no dependencias", "CPR bucle original", "planificar sin detenciones", "desenrollamiento", "salto retardado", "código compacto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[delayed-branch]] · [[loop-unrolling]] · [[pipeline]]

Esquema de resolución: (a) Identificar hazards RAW/WAR/WAW entre pares consecutivos en el bucle original y traducir a ciclos de stall en pipeline (ID/EX/MEM). (b) CPR = (Ciclos totales iteración) / (Instrucciones iteración). (c) Desenrollar (unroll) el bucle para rellenar slots de salto retardado y evitar stalls por dependencias/latencias FP, moviendo instrucciones independientemente. (d) Recalcular CPR sobre el código desenrollado y planificado.

> a) (0,5 puntos) Indica las detenciones (no las dependencias) entre cada par de instrucciones que son necesarias para ejecutar correctamente cada iteración del bucle original. b) (0,25 puntos) Calcula el CPR del bucle original. Muestra las operaciones realizadas. c) (1,5 puntos) Planifica sin detenciones el bucle, aplicando, solo si es necesario, la técnica de desenrollamiento de bucles. Supón que el procesador usa salto retardado. Ten en cuenta que el código resultante debe ser lo más compacto posible y tener la misma funcionalidad que el código original. d) (0,25 puntos) ¿Cuál es el CPR del bucle resultante? Muestra las operaciones realizadas.
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf`

Relacionado: [[parametros-del-procesador-para-problema-1-ac-enero-2025]] · [[analisis-de-detenciones-stalls-en-bucle-con-media-ponderada]] · [[desenrollado-de-bucle-minimo-para-planificacion-sin-detencio]]
