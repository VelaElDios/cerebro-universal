---
tipo: "concepto"
titulo: "Ancho y tamaño en bits de un BTB implícito con 1024 entradas y bus de 24 bits"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["BTB implícito", "ancho", "entradas", "bus direcciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

Un BTB implícito almacena solo la dirección de destino (target) por entrada, sin etiqueta (tag), porque el índice deriva de la dirección de la instrucción de salto. Ancho = bits de dirección = 24. Total bits = entradas × ancho = 1024 × 24 bits.

> Indicate the width and the number of bits to implement an implicit BTB with 1024 entries, knowing that the address bus uses 24 bits
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[comportamiento-de-la-btb-en-caso-de-acierto-test-ac-q14]]
