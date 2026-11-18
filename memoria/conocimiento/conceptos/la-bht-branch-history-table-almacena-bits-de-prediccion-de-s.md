---
tipo: "concepto"
titulo: "La BHT (Branch History Table) almacena bits de predicción de saltos condicionales"
temas: ["ac", "prediccion-saltos"]
claves: ["BHT", "bits predicción", "salto condicional"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014A.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

La Branch History Table (BHT) o tabla de historia de saltos guarda el estado del predictor para cada salto (o grupo de saltos indexados), típicamente contadores de saturación de 2 bits. No almacena direcciones destino (eso hace el BTB, Branch Target Buffer) ni la dirección del salto en sí.

> La BHT almacena : c) Los bits de predicción de las instrucciones de salto condicional
> — `repo:datos/temarios/AC/examenes/Noviembre2014A.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]]
