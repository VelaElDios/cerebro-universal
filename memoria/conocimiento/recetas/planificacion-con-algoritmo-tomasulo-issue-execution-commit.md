---
tipo: "receta"
titulo: "Planificación con algoritmo Tomasulo: Issue, Execution, Commit con latencias y restricciones de buffers"
temas: ["ac", "fp", "planificacion-dinamica", "tomasulo"]
claves: ["Reservation stations", "Load buffer", "Store buffer", "CDB", "Common Data Bus", "ciclos de ejecución", "write result"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[fp]] · [[planificacion-dinamica]] · [[tomasulo]]

Pasos para rellenar tabla Issue/Execution/Commit: 1) Issue (emisión): en orden, si hay estación de reserva libre (para FP) o buffer de carga/almacenamiento libre. Se renombran operandos: si fuente disponible → valor (Vj/Vk); si no → tag de estación que lo producirá (Qj/Qk). 2) Execution: comienza cuando ambos operandos listos (Qj=Qk=0) y unidad funcional libre. Duración = latencia dada (load=1, add=3, mul=4, div=6). No puede empezar en el mismo ciclo en que su operando llega por CDB (empieza al siguiente). 3) Write Result (escritura en CDB): al terminar ejecución, si CDB libre, escribe y avisa a estaciones que esperan ese tag. 4) Commit (escritura en registro): para cargas/FP, tras Write Result; para stores, cuando dato y dirección listos y buffer de store libre. Respetar límites: 2 load buffers, 1 store buffer, 2 RS por unidad FP (adder, multiplier, divider).

> The processor has the following characteristics: • 1 cycle for loads and stores. • 4 cycles for floating-point multiplication (FP). • 3 cycles for floating-point addition (FP). • 6 cycles for floating-point division (FP). • Reservation stations per FP unit: 2 entries. • Load buffer: 2 entries. • Store buffer: 1 entry. • The execution stage of an instruction waiting for a result cannot start in the same cycle in which the result is written to the CDB.
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
