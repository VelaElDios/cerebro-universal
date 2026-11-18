---
tipo: "dato"
titulo: "Organización del banco de registros en RISC-V RV64G"
temas: ["ac", "registros", "risc-v"]
claves: ["x0-x31", "f0-f31", "GPR 64 bits", "PF 32/64 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[registros]] · [[risc-v]]

32 registros enteros (GPR) de 64 bits cada uno (x0..x31). 32 registros de punto flotante (PF) que pueden contener valores de 32 bits (single precision) o 64 bits (double precision). x0 siempre vale 0.

> 32 registros enteros o GPR (64 bits) – x0, x1, …, x31 • 32 registros PF (datos de 32 o 64 bits; SP o DP) – f0, f1, …, f31
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[isa-base-risc-v-rv64g-caracteristicas-principales]] · [[calculo-de-direcciones-y-offsets-en-bucles-vectoriales-risc]] · [[parametros-de-pipeline-risc-v-fp-para-ejercicios-tema-2-mult]]
