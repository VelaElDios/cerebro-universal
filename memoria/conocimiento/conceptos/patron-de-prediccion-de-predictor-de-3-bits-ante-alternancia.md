---
tipo: "concepto"
titulo: "Patrón de predicción de predictor de 3 bits ante alternancia Taken/Not Taken"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor 3 bits", "alternancia T N", "saturación 3 bits", "MSB predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Un predictor de 3 bits (contador saturante 000-111) con MSB como predicción (0=NT, 1=T) ante una alternancia perfecta T,N,T,N... starting from 000:
- Estado 000 → predice NT. Resultado T → fallo → incrementa a 001.
- Estado 001 → predice NT (MSB=0). Resultado N → acierto → decrementa a 000.
- Ciclo: 000 ↔ 001. Nunca alcanza MSB=1, por tanto nunca predice Taken. Tasa de acierto 50% en este patrón.
Esto explica por qué Predictor 2 falla sistemáticamente en los Taken de B1.

> B1 (R2=0)         T          P2          N           MISS       00 00              1 0              001 000 B1 (R2=1)         N          P2          N           HIT        00 00              0 0              000 000 B1 (R2=0)         T          P2          N           MISS       00 00              1 0              001 000
> — `repo:datos/temarios/AC/examenes/June2017.pdf` (cita sin comprobar)

Relacionado: [[predictor-local-de-1-bit-predictor-1-y-predictor-local-de-3]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]]
