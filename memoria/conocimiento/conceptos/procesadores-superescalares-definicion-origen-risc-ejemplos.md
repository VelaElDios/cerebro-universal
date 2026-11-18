---
tipo: "concepto"
titulo: "Procesadores superescalares: definición, origen RISC, ejemplos x86 (Pentium Pro/II)"
temas: ["ac", "cisc", "cpi", "ilp", "pentium ii", "pentium pro", "risc", "superescalar"]
claves: ["superescalar", "n instrucciones/ciclo", "CPI ideal 0.5", "RISC", "CISC", "microarquitectura RISC", "2 ALU + 1 FP", "1998"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cisc]] · [[cpi]] · [[ilp]] · [[pentium ii]] · [[pentium pro]] · [[risc]] · [[superescalar]]

- **Definición**: emiten/ejecutan *n* instrucciones por ciclo de reloj (ideal CPI = 1/n). Ejemplo n=2 → CPI ideal 0.5.
- **Origen**: primero en RISC (implementación sencilla, instrucciones de longitud fija, pocas modalidades de direccionamiento). Luego adoptado por CISC mediante traducción a micro-ops tipo RISC.
- **Hitos**: desde 1998 todos los procesadores comerciales son superescalares.
- **Ejemplo x86**: Pentium Pro (1995) y Pentium II (1997) son ISA CISC pero internamente usan microarquitectura RISC superescalar con 2 ALU enteras + 1 FPU.
- Requiere: fetch/decoder ancho, renombrado de registros, emisión fuera de orden (out-of-order), predicción de saltos avanzada, múltiples unidades funcionales.

> Superescalares • Lanzan n instrucciones en cada ciclo de reloj Ejemplo: n = 2 (CPI Ideal = 0,5) • Origen: procesadores RISC (de implementación más simple); luego incorporado en los CISC • Desde 1998 todos los procesadores comerciales son superescalares • Ejemplos: INTEL Pentium Pro y Pentium II son procesadores CISC con microarquitectura RISC superescalar (2 ALU + 1 FP)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)` (cita sin comprobar)

Relacionado: [[identificacion-de-superescalar-por-ancho-de-emision-y-cpi]] · [[procesador-a-superscalar-mips64-4-issue-2-enteros-2-fp]] · [[procesadores-superscalar-son-maquinas-sisd]]
