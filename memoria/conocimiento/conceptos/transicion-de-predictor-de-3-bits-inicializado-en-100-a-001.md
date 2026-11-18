---
tipo: "concepto"
titulo: "Transición de predictor de 3 bits inicializado en 100 a 001 tras tres ejecuciones"
temas: ["ac", "prediccion-saltos"]
claves: ["3-bit predictor", "saturating counter", "branch prediction"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Un predictor de 3 bits es un contador saturante (000=fuertemente NT ... 111=fuertemente T). Inicializado en 100 (débilmente T). Tras tres ejecuciones llega a 001 (débilmente NT). Cada ejecución decrementa el contador si la rama es NT, incrementa si es T. Para pasar de 100 (4) a 001 (1) se necesitan tres decrementos => las tres ejecuciones fueron NOT TAKEN (NT). La última ejecución fue NT. Opción correcta: (b).

> A 3-bit predictor initialized with 100 becomes 001 after three executions of the branch instruction to which it is associated. We can state that:
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]]
