---
tipo: "concepto"
titulo: "BHT con contadores de saturación de 2 bits (pregunta 17)"
temas: ["ac", "bht", "contador-saturacion", "prediccion-saltos"]
claves: ["BHT", "Branch History Table", "predictor dinámico 2 bits", "contador saturación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[contador-saturacion]] · [[prediccion-saltos]]

Respuesta correcta: b) A 2-bit saturating counter. La BHT almacena contadores de saturación de 2 bits (00=fuertemente no tomado, 01=débilmente no tomado, 10=débilmente tomado, 11=fuertemente tomado) que se actualizan según resultado real del salto.

> The BHT (Branch History Table) in a 2-bit dynamic branch predictor is implemented by: a) A 2-bit XOR operation b) A 2-bit saturating counter c) A 2-bit shift register d) None of the above
> — `repo:datos/temarios/AC/examenes/June2021.pdf`
