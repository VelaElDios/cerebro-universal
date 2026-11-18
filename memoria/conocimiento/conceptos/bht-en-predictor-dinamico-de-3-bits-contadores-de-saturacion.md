---
tipo: "concepto"
titulo: "BHT en predictor dinámico de 3 bits: contadores de saturación de 3 bits"
temas: ["ac", "bht", "contador-saturacion", "prediccion-saltos"]
claves: ["BHT", "Branch History Table", "contador saturación", "3 bits", "predictor dinámico"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[contador-saturacion]] · [[prediccion-saltos]]

La BHT almacena el estado de predicción por entrada. En predictores dinámicos basados en contadores (como el de 2 bits clásico), cada entrada es un contador de saturación. Para un predictor de 3 bits, se usan contadores de saturación de 3 bits (valores 0-7, umbral en 3/4). Respuesta correcta: a.

> The BHT (Branch History Table) in a 3-bit dynamic branch predictor is implemented by means of… a) 3-bit saturating counters b) 3-bit shift registers c) 3-bit XOR operations d) None of the above
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[implementacion-bht-con-contadores-saturados-de-2-bits]] · [[implementacion-de-la-bht-en-predictor-dinamico-de-2-bits]]
