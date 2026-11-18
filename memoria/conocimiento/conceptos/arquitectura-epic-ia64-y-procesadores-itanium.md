---
tipo: "concepto"
titulo: "Arquitectura EPIC (IA64) y procesadores Itanium"
temas: ["ac", "epic", "ia64", "itanium", "vliw"]
claves: ["EPIC", "Explicitly Parallel Instruction Computing", "IA64", "Itanium", "Itanium2", "128 bits", "registros", "operaciones por ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[epic]] · [[ia64]] · [[itanium]] · [[vliw]]

EPIC (Explicitly Parallel Instruction Computing) es la implementación comercial de VLIW para la arquitectura IA64 (Intel/HP). Características: instrucciones fijas de 128 bits que contienen múltiples operaciones (hasta 6 por ciclo en Itanium); formato de tres operandos con campo TMP para codificar dependencias entre operaciones dentro de la misma instrucción; banco de registros grande: 128 registros enteros de 64 bits y 128 registros de punto flotante de 82 bits. Itanium (2001): 6 operaciones/ciclo, pipeline de 10 etapas, 800 MHz. Itanium 2 (2005): 6 operaciones/ciclo, pipeline de 8 etapas, 1,66 GHz. Ambos mantienen la filosofía VLIW: paralelismo explícito decidido en tiempo de compilación.

> Ejemplo: EPIC (Explicitly Parallel Instruction Computing) – IA64 instrucciones de 128 bits ... Itanium (2001): 6 ops. por ciclo, 10 etapas, 800Mhz Itanium2 (2005): 6 ops. por ciclo, 8 etapas, 1,66Ghz
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[itanium-ia64-primer-procesador-intel-no-compatible-con-x86]] · [[instrucciones-predicadas-convertir-dependencias-de-control-e]] · [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]]
