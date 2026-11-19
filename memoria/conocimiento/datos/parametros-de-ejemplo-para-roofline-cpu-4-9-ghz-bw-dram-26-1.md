---
tipo: "dato"
titulo: "Parámetros de ejemplo para Roofline: CPU 4.9 GHz, BW DRAM 26.143 GB/s, AVX2/FMA = 32 FLOPS/ciclo"
temas: ["ac", "benchmark", "hardware", "roofline"]
claves: ["FRECUENCIA_GHZ", "BW_DRAM", "FLOPSperCYCLE", "GFLOPS_MAX"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[hardware]] · [[roofline]]

Valores de referencia del script: Frecuencia CPU = 4.9 GHz (obtenida con `lscpu`). Ancho de banda DRAM = 26.143 GB/s (medido con benchmark STREAM). FLOPS por ciclo AVX2/FMA = 32. Peak GFLOPS calculado = 4.9 × 32 = 156.8 GFLOPS. Punto de inflexión (ridge point) = GFLOPS_MAX / BW_DRAM = 156.8 / 26.143 ≈ 6.0 FLOPs/Byte.

> FRECUENCIA_GHZ = 4.9     # Tu frecuencia en GHz (de lscpu) ... BW_DRAM = 26.143         # Tus GB/s de la RAM (de STREAM)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py` (cita sin comprobar)

Relacionado: [[definicion-de-peak-performance-rendimiento-pico]] · [[comparativa-de-coste-efectividad-entre-sistemas-rendimiento]]
