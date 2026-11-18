---
tipo: "concepto"
titulo: "Cálculo de FLOPS por ciclo en x86 con AVX2/FMA"
temas: ["ac", "avx2", "fma", "hardware", "simd"]
claves: ["FLOPSperCYCLE", "AVX2", "FMA", "256 bits", "8 floats", "2 unidades FMA"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[avx2]] · [[fma]] · [[hardware]] · [[simd]]

Derivación del valor 32 FLOPS/ciclo para núcleos modernos x86 con AVX2 + FMA:
- Registro AVX2 de 256 bits → 8 floats de 32 bits (256/32 = 8).
- Instrucción FMA (Fused Multiply-Add) → 2 operaciones flotantes (mul + add) por elemento en 1 ciclo.
- 2 unidades FMA por núcleo → pueden ejecutar 2 instrucciones FMA por ciclo.
Total: 8 elementos × 2 ops × 2 unidades = 32 FLOPS/ciclo.
Este valor se multiplica por la frecuencia en GHz para obtener GFLOPS_MAX teórico.

> FLOPSperCYCLE =32	 # En procesadores x86 modernos con soporte para AVX2 y FMA = 8 floats * 2 ops FMA * 2 unidades FMA = 32
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py`

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[definicion-de-mflops-millones-de-operaciones-de-punto-flotan]] · [[latencia-de-carga-fp-y-multiplicacion-doble-en-la-simulacion]]
