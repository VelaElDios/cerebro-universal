---
tipo: "receta"
titulo: "Configuración Tomasulo con ROB para simulación de examen (enero 2021)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB", "reservation station", "load buffer", "FP Adder", "FP Multiplier", "FP Divider", "CDB", "issue execute write commit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Configuración exacta del enunciado para simular 10 instrucciones (MUL.D, DIV.D, ADD.D, S.D, MUL.D, DIV.D, L.D, ADD.D, MUL.D, ADD.D):
- ROB: 8 entradas, inicialmente vacía.
- Load buffer: 1 entrada.
- Reservation stations: 1 para FP add (RE), 2 para FP mul, 2 para FP div.
- Unidades funcionales:
  * FP Adder: 1 unidad, 2 ciclos, segmentada (pipelined).
  * FP Multiplier: 1 unidad, 4 ciclos, segmentada.
  * FP Divider: 1 unidad, 8 ciclos, NO segmentada.
  * LOAD/STORE: 1 unidad, 2 ciclos, segmentada.
  * INT ALU: 1 unidad, 1 ciclo, no segmentada.
- Reglas de temporización:
  1. En el mismo ciclo en que un resultado se escribe en el CDB, se inicia la ejecución de cualquier instrucción que esperara ese resultado.
  2. Un recurso liberado en un ciclo no puede usarse hasta el siguiente ciclo.
- Tabla a rellenar por instrucción: Issue, Execute, Write result, Commit.
- Tabla de stalls: causa (p.ej. "structural hazard due to the RE") y dónde (p.ej. "execution of instruction number 3").

> There is an 8-entry ROB (initially EMPTY), 1 load buffer, 1 reservation station (RE) for FP addition, 2 reservation stations for FP multiplication, and 2 reservation stations for FP division.
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
