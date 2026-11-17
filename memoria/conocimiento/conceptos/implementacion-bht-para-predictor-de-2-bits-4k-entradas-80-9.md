---
tipo: "concepto"
titulo: "Implementación BHT para predictor de 2 bits: 4K entradas, ~80-90% acierto"
temas: ["ac", "arquitectura-computadores", "bht", "prediccion-saltos"]
claves: ["Branch History Table", "BHT", "4K-entry", "2 bits/entry", "PC fetch", "target PC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[bht]] · [[prediccion-saltos]]

La BHT se indexa con bits del PC (fetch PC). Cada entrada tiene 2 bits (contador saturado). Al hacer fetch, se lee la entrada correspondiente al PC del salto. El bit más significativo da la predicción (T/NT). Tras resolver el salto, se actualiza el contador: incrementa si tomado, decrementa si no tomado (saturando en 00 y 11). Con 4K entradas y 2 bits/entrada, se logra ~80-90% de predicciones correctas.

> Implementación: Branch History Table (BHT) • Fetch PC • I-Cache • BHT Index • 2k-entry BHT, 2 bits/entry • Instruction Opcode • offset • Branch? • Target PC • Taken/¬Taken? • 4K-entry BHT, 2 bits/entry, ~80-90% correct predictions
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)
