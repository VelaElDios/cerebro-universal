---
tipo: "concepto"
titulo: "ISA base RISC-V RV64G: características principales"
temas: ["ac", "isa", "risc-v"]
claves: ["RV64G", "load-store", "32 registros enteros", "32 registros flotantes", "word 32 bits", "doubleword 64 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[isa]] · [[risc-v]]

La ISA base usada en el curso es RV64G (2016). Es una arquitectura load-store de 32 bits por instrucción con registros de 64 bits. Dispone de 32 registros enteros de propósito general (x0–x31, donde x0 es cero hardwired) y 32 registros de punto flotante (f0–f31) que admiten simple (32 bits) y doble precisión (64 bits). Las instrucciones de memoria distinguen word (lw/sw) y doubleword (ld/sd).

> ISA tipo RISC, abierta • Arquitectura carga-almacenamiento • Tamaño de instrucción: 32 bits • 32 / 64 bits (aquí: ISA base “RV64G” - 2016) • “word”: 32 bits (lw, sw…) • “doubleword”: 64 bits (ld, sd…) • 32 registros enteros o GPR (64 bits) • 32 registros PF (datos de 32 o 64 bits; SP o DP)
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[organizacion-del-banco-de-registros-en-risc-v-rv64g]] · [[arquitecturas-load-store-arm-risc-v-y-alpha]] · [[analisis-de-dependencias-en-codigo-risc-v-raw-war-waw]]
