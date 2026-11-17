---
tipo: "dato"
titulo: "Parámetros de ejemplo del script (CPU 4.9 GHz, DDR4 26.143 GB/s)"
temas: ["ac", "arquitectura-computadores", "hardware", "roofline"]
claves: ["FRECUENCIA_GHZ=4.9", "BW_DRAM=26.143", "GFLOPS_MAX=156.8"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[hardware]] · [[roofline]]

Valores de ejemplo incluidos en el script:
- FRECUENCIA_GHZ = 4.9 GHz (frecuencia turbo típica de un Core i7/i9 reciente).
- BW_DRAM = 26.143 GB/s (ancho de banda medido con STREAM, compatible con DDR4-3200 dual-channel).
- FLOPSperCYCLE = 32 (AVX2 + FMA: 8 floats × 2 ops × 2 unidades).
- GFLOPS_MAX = 4.9 × 32 = 156.8 GFLOPs/s (tope teórico de cómputo mononúcleo).
- Punto de inflexión (ridge point): I = GFLOPS_MAX / BW_DRAM ≈ 6.0 FLOPs/Byte.

> FRECUENCIA_GHZ = 4.9     # Tu frecuencia en GHz (de lscpu)\nBW_DRAM = 26.143         # Tus GB/s de la RAM (de STREAM)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py` (cita sin comprobar)
