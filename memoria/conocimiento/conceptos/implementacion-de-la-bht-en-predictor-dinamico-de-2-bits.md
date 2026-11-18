---
tipo: "concepto"
titulo: "Implementación de la BHT en predictor dinámico de 2 bits"
temas: ["ac", "bht", "prediccion-saltos", "saturating counter"]
claves: ["Branch History Table", "2-bit predictor", "saturating counter"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[prediccion-saltos]] · [[saturating counter]]

La **Branch History Table (BHT)** en un predictor dinámico de 2 bits consiste en una tabla indexada (por PC o por historia) donde cada entrada es un **contador saturante de 2 bits** (estados: 00=fuertemente no tomado, 01=débilmente no tomado, 10=débilmente tomado, 11=fuertemente tomado). El contador se incrementa en salto tomado y decrementa en no tomado, saturando en los extremos.

> The BHT (Branch History Table) in a 2-bit dynamic branch predictor is implemented by means of… b) 2-bit saturating counters.
> — `repo:datos/temarios/AC/examenes/January2018.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
