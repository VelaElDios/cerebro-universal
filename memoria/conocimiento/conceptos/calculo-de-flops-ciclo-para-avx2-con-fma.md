---
tipo: "concepto"
titulo: "Cálculo de FLOPs/ciclo para AVX2 con FMA"
temas: ["ac", "arquitectura-computadores", "avx2", "fma", "simd"]
claves: ["FLOPSperCYCLE=32", "AVX2", "FMA", "256-bit", "8 floats", "2 unidades FMA"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[avx2]] · [[fma]] · [[simd]]

Justificación del valor 32 FLOPs/ciclo en el script:
1. Registros AVX2 de 256 bits → 8 floats de 32 bits (prec simple) por vector.
2. Instrucción FMA (Fused Multiply-Add) = 2 operaciones flotantes (mul + add) por elemento en 1 ciclo.
3. 2 unidades de ejecución FMA por núcleo (puerto 0 y 1 en Skylake/derivados).
Total = 8 × 2 × 2 = 32 FLOPs/ciclo/núcleo. Para AVX-512 serían 64 (16 floats × 2 × 2).

> FLOPSperCYCLE =32	 # En procesadores x86 modernos con soporte para AVX2 y FMA = 8 floats * 2 ops FMA * 2 unidades FMA = 32
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[calculo-de-flops-totales-para-el-kernel-de-la-tarea-2-1]] · [[latencia-de-carga-fp-y-multiplicacion-doble-en-la-simulacion]]
