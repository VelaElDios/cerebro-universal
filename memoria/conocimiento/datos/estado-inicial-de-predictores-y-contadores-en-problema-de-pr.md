---
tipo: "dato"
titulo: "Estado inicial de predictores y contadores en problema de predictor híbrido de examen Junio 2017"
temas: ["ac", "prediccion-saltos"]
claves: ["estado inicial", "Predictor 1: 0", "Predictor 2: 000", "Contadores: 00"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Valores iniciales antes de procesar la secuencia: Contadores de selección (2 bits): B1=00, B2=00 (MSB=0 → se usa Predictor 2 inicialmente). Predictor 1 (1 bit): B1=0 (predice no tomado), B2=0 (predice no tomado). Predictor 2 (3 bits): B1=000 (predice fuertemente no tomado), B2=000 (predice fuertemente no tomado).

> Estado inicial) -- -- -- B1: 00 B2: 00 B1: 0 B2: 0 B1: 000 B2: 000
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf` (cita sin comprobar)

Relacionado: [[predictor-hibrido-de-saltos-con-selectores-de-2-bits-entre-p]] · [[reglas-de-actualizacion-de-contadores-de-seleccion-en-predic]]
