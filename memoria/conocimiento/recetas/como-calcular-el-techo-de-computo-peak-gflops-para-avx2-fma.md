---
tipo: "receta"
titulo: "Cómo calcular el techo de cómputo (peak GFLOPS) para AVX2/FMA en x86"
temas: ["ac", "avx2", "fma", "rendimiento", "roofline"]
claves: ["FLOPSperCYCLE", "AVX2", "FMA", "GFLOPS_MAX", "frecuencia GHz"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[avx2]] · [[fma]] · [[rendimiento]] · [[roofline]]

Para procesadores x86 con AVX2 y FMA: cada registro AVX2 de 256 bits contiene 8 floats (32 bits). La instrucción FMA (Fused Multiply-Add) ejecuta 2 operaciones (multiplicación + suma) por elemento en un ciclo. Cada núcleo tiene 2 unidades FMA. Fórmula: FLOPS_por_ciclo = 8 floats × 2 ops/FMA × 2 unidades = 32. Peak GFLOPS = Frecuencia_GHz × FLOPS_por_ciclo. Ejemplo: 4.9 GHz × 32 = 156.8 GFLOPS.

> FLOPSperCYCLE =32  # En procesadores x86 modernos con soporte para AVX2 y FMA = 8 floats * 2 ops FMA * 2 unidades FMA = 32
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py`

Relacionado: [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]] · [[definicion-de-peak-performance-rendimiento-pico]]
