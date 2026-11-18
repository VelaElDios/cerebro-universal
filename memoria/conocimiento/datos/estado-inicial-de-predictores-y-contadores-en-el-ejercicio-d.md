---
tipo: "dato"
titulo: "Estado inicial de predictores y contadores en el ejercicio de predictor híbrido"
temas: ["ac", "prediccion-saltos"]
claves: ["estado inicial", "Predictor 1 B1 0 B2 0", "Predictor 2 B1 000 B2 000", "Counters B1 00 B2 00"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Valores iniciales antes de la primera ejecución del bucle:
- Counters (selectores de 2 bits): B1=00, B2=00 → MSB=0 → se usa Predictor 2 para ambos saltos inicialmente.
- Predictor 1 (1 bit): B1=0 (predice NT), B2=0 (predice NT).
- Predictor 2 (3 bits): B1=000 (predice NT), B2=000 (predice NT).

> (initial state)        -         -            -          -        B1: 00   B2: 00    B1: 0   B2: 0   B1: 000   B2: 000
> — `repo:datos/temarios/AC/examenes/June2017.pdf`

Relacionado: [[predictor-local-de-1-bit-predictor-1-y-predictor-local-de-3]] · [[reglas-de-actualizacion-del-contador-selector-de-2-bits-en-p]] · [[estado-inicial-de-predictores-y-contadores-en-problema-de-pr]] · [[estados-iniciales-de-predictores-en-ejercicio-2-un-nivel-y-d]]
