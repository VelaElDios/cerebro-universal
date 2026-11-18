---
tipo: "receta"
titulo: "Parámetros de simulación Tomasulo especulativo para MIPS64 (examen AC enero 2022)"
temas: ["ac", "pipeline", "prediccion-saltos", "tomasulo"]
claves: ["Tomasulo", "especulación", "ROB", "reservation stations", "load buffer", "CDB", "latencias FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]]

Configuración exacta para simular el Ejercicio 2:
- Latencias: Load/Store = 1 ciclo, FP MUL = 6 ciclos, FP ADD = 4 ciclos, DIV.D (no especificada en el texto, pero aparece en el código)
- ROB: 4 entradas
- Reservation Stations: 2 por cada unidad FP (asumiendo unidades separadas para ADD, MUL, DIV)
- Load Buffer: 2 entradas
- Restricciones de timing críticas:
  1. "The execution stage of an instruction that is waiting for a result cannot start in the same cycle in which the result is written to the CDB" → hay 1 ciclo de burbuja entre CDB write y inicio de ejecución de consumidor.
  2. "A resource that is released in one clock cycle cannot be used until the next clock cycle" → liberación de RS/ROB/Load Buffer tiene 1 ciclo de latencia antes de reuso.
- Código a simular (8 instrucciones):
  1. MUL.D F4,F6,F12
  2. SUB.D F6,F4,F10
  3. L.D   F4,10(R2)
  4. DIV.D F0,F14,F16
  5. SUB.D F12,F14,F0
  6. ADD.D F20,F28,F24
  7. L.D   F0,10(R2)
  8. MUL.D F18,F28,F24
- Tabla a rellenar: Issue, Execution (start-end), Write result, Commit por instrucción.
- Tabla ROB a rellenar en el ciclo donde termina el primer L.D. (instr 3): Entry, Busy, Instruction, Status, Destination, Value.

> We assume a MIPS64 processor using hardware speculation and dynamic scheduling using the Tomasulo technique with speculation, with the following characteristics: • The load and store execution stage takes 1 cycle. • The floating-point multiplication (FP) execution step takes 6 cycles. • The floating-point addition (FP) execution step takes 4 cycles. • A 4-input reorder buffer (ROB) is available. • It has a 2-entry reservation stations for each unit in FP. • It has a 2-entry load/stage input load buffer.
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
