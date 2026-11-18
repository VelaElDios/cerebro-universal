---
tipo: "receta"
titulo: "Condición para solapar iteraciones de un bucle (software pipelining)"
temas: ["ac", "bucles", "pipeline", "software-pipelining"]
claves: ["solapamiento iteraciones", "dependencias entre iteraciones", "segmentación software"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[pipeline]] · [[software-pipelining]]

Para solapar iteraciones (software pipelining) no debe haber dependencias **entre iteraciones** (loop-carried dependencies). Las dependencias dentro de la misma iteración se resuelven con adelantamiento o reordenación. Respuesta correcta: b).

> Se puede solapar la ejecución de distintas iteraciones de un bucle cuando éste a) No presenta dependencias en la misma iteración b) No presenta dependencias entre iteraciones c) El número de iteraciones del bucle es múltiplo del número de iteraciones desenrolladas
> — `repo:datos/temarios/AC/examenes/Noviembre2011.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
