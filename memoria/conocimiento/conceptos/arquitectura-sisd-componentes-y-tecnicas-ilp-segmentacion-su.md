---
tipo: "concepto"
titulo: "Arquitectura SISD: componentes y técnicas ILP (segmentación, superescalar, VLIW)"
temas: ["ac", "ilp", "monoprocesador", "segmentación", "sisd", "superescalar", "vliw"]
claves: ["CU", "PU", "MU", "segmentación", "superescalar", "VLIW", "ILP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)", "repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 4 de 5)"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[monoprocesador]] · [[segmentación]] · [[sisd]] · [[superescalar]] · [[vliw]]

El monoprocesador SISD consta de tres unidades funcionales:
- CU (Control Unit): fetch/decode, generación de señales de control.
- PU (Processing Unit): ALU, FPU, registros.
- MU (Memory Unit): caché, MMU, interfaz de bus.
Para mejorar prestaciones se explotan tres técnicas de ILP:
1. Segmentación (pipelining): solapa etapas de instrucciones consecutivas.
2. Superescalar: emite múltiples instrucciones por ciclo (CPI ideal < 1).
3. VLIW (Very Long Instruction Word): el compilador empaqueta operaciones independientes en una instrucción muy ancha; el hardware es más simple pero requiere compilador inteligente.

> SISD • Monoprocesador – CU: Control Unit – PU: Processsing Unit – MU: Memory Unit • Técnicas usadas para mejorar sus prestaciones  Paralelismo a nivel de instrucción (ILP) – Segmentación – Superescalares – VLIW
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)`

## Ampliación (2026-11-17, )
VLIW (Very Long Instruction Word) surge para evitar el elevado coste hardware y la complejidad de control de los procesadores superescalares. En VLIW, el compilador analiza el código y empaqueta varias operaciones independientes en una sola instrucción muy larga (palabra de instrucción muy larga). Estas operaciones se despachan simultáneamente a múltiples unidades funcionales independientes y se ejecutan en paralelo en una misma ciclo, sin necesidad de lógica de despacho dinámico compleja en hardware. El ejemplo de pipeline muestra varias operaciones (EX, MEM, WB) solapadas en el mismo ciclo. Esta técnica traslada la complejidad del hardware al compilador.

Relacionado: [[tecnica-de-mejora-de-rendimiento-en-sisd]] · [[diferencia-fundamental-vliw-vs-superescalar-compilador-vs-ha]] · [[funcionamiento-y-limites-de-la-segmentacion-pipelining-en-si]]
