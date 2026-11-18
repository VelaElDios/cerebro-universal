---
tipo: "concepto"
titulo: "Nomenclatura del campo Value en entradas del ROB (Tomasulo con especulación)"
temas: ["ac", "rob", "tomasulo"]
claves: ["(Rx)", "(Fx)", "Mem(d)", "#ROBx", "#ROBx(data)", "campo Value", "etapa Stage"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[rob]] · [[tomasulo]]

Al rellenar el ROB en un ciclo dado (ej. ciclo 12), cada entrada tiene: Instruction, Stage (etapa en ejecución o última completada), Destination Register, Value. El campo Value usa cinco formas: 1) (Rx) valor del registro entero Rx. 2) (Fx) valor del registro FP Fx. 3) Mem(d) contenido de dirección de memoria d. 4) #ROBx indica que el valor vendrá de la entrada ROBx (pendiente). 5) #ROBx(data) indica dato ya leído del campo Value de la entrada ROBx (ej. #ROB2(F1) significa el valor del registro F1 que está en la entrada ROB2). El campo Stage muestra la etapa actual o la última completada (Issue, Execution, Write, Commit).

> Make use of this nomenclature to complete the Value field: i. (Rx) Contents of the integer register Rx. Examples: (R1), (R2). ii. (Fx) Contents of the FP register Fx. Examples: (F8), (F5). iii. Mem(d) Content of memory address d. Examples: Mem(20), Mem((R1)+4). iv. #ROBx Value to be obtained from ROB entry x. Examples: #ROB1, #ROB7. v. #ROBx(data) Data read or retrieved from the Value field of the x input of the ROB. Examples: #ROB7(Mem(R1)), #ROB2(F1).
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[procesador-tomasulo-con-especulacion-caracteristicas-de-late]]
