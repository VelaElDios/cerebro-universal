---
tipo: "dato"
titulo: "Latencias de unidades funcionales FP en examen AC June 2020 (Adder 2, Multiplier 4, Divider 8)"
temas: ["ac", "ac-exam", "floating-point", "functional-units", "latency", "mips64"]
claves: ["FP Adder/Subtractor 2 cycles", "FP Multiplier 4 cycles", "FP Divider 8 cycles", "Rest of units 1 cycle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ac-exam]] · [[floating-point]] · [[functional-units]] · [[latency]] · [[mips64]]

Tabla oficial de latencias EX para unidades FP en este examen: FP Adder/Subtractor (ADD.S, SUB.S, ADD.D, SUB.D) = 2 ciclos; FP Multiplier (MUL.S, MUL.D) = 4 ciclos; FP Divider (DIV.S, DIV.D) = 8 ciclos; Unidades restantes (integer ALU, load/store, branch) = 1 ciclo. Estas latencias determinan stalls, CPR y factor de desenrollado.

> The next table shows the number of cycles employed by each functional unit: Functional Unit Number of cycles used FP Adder/Subtractor 2 FP Multiplier 4 FP Divider 8 Rest of units 1
> — `repo:datos/temarios/AC/examenes/June2020.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]]
