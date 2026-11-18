---
tipo: "concepto"
titulo: "Qué es una estación de reserva en el algoritmo de Tomasulo"
temas: ["ac", "tomasulo"]
claves: ["reservation station", "Tomasulo", "dependencias de datos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Una estación de reserva en Tomasulo es una ubicación física de almacenamiento para dependencias de datos que permite su resolución. Cada estación guarda la operación, los operandos (o etiquetas Qj/Qk indicando qué estación los producirá) y espera a que estén listos para ejecutar. No almacena datos para especulación ni registros para renombrado directamente.

> What is a reservation station in the context of the Tomasulo algorithm? a) A physical storage location for data that allows their speculation b) A physical storage location for registers that allows their renaming c) A physical storage location for data dependencies that allows their resolution d) All are correct
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]] · [[buffer-de-carga-en-tomasulo-especulativo]]
