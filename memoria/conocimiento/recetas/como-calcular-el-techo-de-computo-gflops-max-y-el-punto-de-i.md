---
tipo: "receta"
titulo: "Cómo calcular el techo de cómputo (GFLOPS máx) y el punto de inflexión del modelo Roofline"
temas: ["ac", "avx2", "rendimiento", "roofline"]
claves: ["GFLOPS_MAX", "FLOPSperCYCLE", "FRECUENCIA_GHZ", "BW_DRAM", "I_KNEE"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[avx2]] · [[rendimiento]] · [[roofline]]

Para un núcleo x86 moderno con AVX2 y FMA:
- FLOPSperCYCLE = 32 (8 floats por registro AVX2 de 256 bits × 2 ops FMA por elemento × 2 unidades FMA por núcleo).
- GFLOPS_MAX = frecuencia_GHz × FLOPSperCYCLE.
- Punto de inflexión (rodilla) I_KNEE = GFLOPS_MAX / BW_DRAM (en FLOPs/Byte).
- La curva techo es y = min(BW_DRAM × x, GFLOPS_MAX).
- Zona memory-bound: x ≤ I_KNEE (limitada por ancho de banda).
- Zona compute-bound: x > I_KNEE (limitada por techo de cómputo).

> GFLOPS_MAX = FRECUENCIA_GHZ * FLOPSperCYCLE  # Techo de cómputo de la CPU en GFLPOs/s I_KNEE = GFLOPS_MAX / BW_DRAM                # Punto de inflexión (FLOPs/Byte)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py`
