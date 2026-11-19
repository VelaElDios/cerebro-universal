---
tipo: "concepto"
titulo: "Derivación de FLOPSperCYCLE = 32 para x86 con AVX2 y FMA"
temas: ["ac", "avx2", "fma", "isa", "rendimiento"]
claves: ["FLOPSperCYCLE", "AVX2", "FMA", "256 bits", "8 floats", "2 unidades FMA"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[avx2]] · [[fma]] · [[isa]] · [[rendimiento]]

Justificación del valor 32 FLOPS/ciclo:
1. Registros AVX2 de 256 bits → 8 floats (32 bits cada uno) por instrucción vectorial.
2. Instrucción FMA (Fused Multiply-Add) = 2 operaciones de punto flotante (mul + add) por elemento por ciclo.
3. Dos unidades de ejecución FMA por núcleo (puerto 0 y puerto 1 en microarquitecturas Intel recientes).
Total: 8 × 2 × 2 = 32 FLOPS/ciclo/núcleo para precisión simple (FP32). Para doble precisión (FP64) serían 16 FLOPS/ciclo (4 doubles por registro).

> FLOPSperCYCLE =32	 # En procesadores x86 modernos con soporte para AVX2 y FMA = 8 floats * 2 ops FMA * 2 unidades FMA = 32 			 #    1.- Cada registro AVX2 (256 bits) procesa 8 datos de precisión simple o float s (de 32 bits). 			 #    2.- Instruccion FMA (Fused Multiply-Add), ejecuta 2 operaciones (1 multiplicación + 1 suma) por elemento en un solo ciclo. 			 #    3.- Cada núcleo tiene 2 unidades FMA
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py`

Relacionado: [[como-calcular-el-techo-de-computo-gflops-max-y-el-punto-de-i]]
