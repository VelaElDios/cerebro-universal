---
tipo: "receta"
titulo: "Cómo obtener los parámetros de hardware para el modelo Roofline en Linux"
temas: ["ac", "benchmark", "hardware", "linux", "roofline"]
claves: ["lscpu", "STREAM", "BW_DRAM", "FRECUENCIA_GHZ"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[hardware]] · [[linux]] · [[roofline]]

1. Frecuencia CPU: ejecutar `lscpu` y buscar "CPU max MHz" o "CPU MHz", convertir a GHz. 2. Ancho de banda DRAM: compilar y ejecutar benchmark STREAM (stream.c) que mide Copy, Scale, Add, Triad; usar el valor de Triad (GB/s) como BW_DRAM sostenible. 3. FLOPS/ciclo: consultar manual de optimización del fabricante (Intel 64 and IA-32 Architectures Optimization Reference Manual) para saber capacidades SIMD (AVX2, AVX-512) y unidades FMA por núcleo.

> FRECUENCIA_GHZ = 4.9     # Tu frecuencia en GHz (de lscpu) ... BW_DRAM = 26.143         # Tus GB/s de la RAM (de STREAM)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py` (cita sin comprobar)

Relacionado: [[comparacion-de-rendimiento-entre-procesadores-requiere-mismo]] · [[comparativa-de-coste-efectividad-entre-sistemas-rendimiento]]
