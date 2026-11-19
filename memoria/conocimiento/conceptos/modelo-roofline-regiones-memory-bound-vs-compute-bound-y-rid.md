---
tipo: "concepto"
titulo: "Modelo Roofline: regiones memory-bound vs compute-bound y ridge point"
temas: ["ac", "arquitectura", "rendimiento", "roofline"]
claves: ["memory-bound", "compute-bound", "ridge point", "intensidad aritmética", "techo DRAM"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[arquitectura]] · [[rendimiento]] · [[roofline]]

El modelo Roofline muestra el rendimiento máximo alcanzable según la intensidad aritmética (FLOPs/Byte). Dos techos: (1) Techo DRAM: pendiente = BW_DRAM (GB/s), región donde el rendimiento escala linealmente con la intensidad aritmética → memory-bound (el cuello de botella es la memoria). (2) Tope CPU: horizontal en GFLOPS_MAX, región donde el rendimiento se satura → compute-bound (el cuello de botella es la capacidad de cómputo). El punto de intersección (ridge point) = GFLOPS_MAX / BW_DRAM indica la intensidad aritmética mínima para saturar la CPU. Kernels a la izquierda del ridge point son memory-bound; a la derecha son compute-bound.

> Identificar límites por memoria (memory-bound) vs. cómputo.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py`

Relacionado: [[detenciones-en-pipeline-afectan-negativamente-a-prestaciones]] · [[ecuacion-fundamental-del-tiempo-de-ejecucion-en-arquitectura]]
