---
tipo: "concepto"
titulo: "Fórmula del techo Roofline mononúcleo"
temas: ["ac", "arquitectura-computadores", "modelo-rendimiento", "roofline"]
claves: ["BW_DRAM", "GFLOPS_MAX", "intensidad aritmética", "min(BW * I", "P_max)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[modelo-rendimiento]] · [[roofline]]

El modelo Roofline clásico combina dos límites:
- Límite de memoria (rampa): Rendimiento = BW_DRAM (GB/s) × Intensidad Aritmética (FLOPs/Byte). Pendiente = ancho de banda.
- Límite de cómputo (horizontal): Rendimiento = GFLOPS_MAX = Frecuencia (GHz) × FLOPs/ciclo.
El techo real es el mínimo de ambos: `min(BW_DRAM * I, GFLOPS_MAX)`. La zona por debajo de la rampa es memory-bound; la zona por debajo de la horizontal y a la derecha del punto de inflexión es compute-bound.

> plt.loglog(x, np.minimum(BW_DRAM * x, GFLOPS_MAX), label=f\"Techo DRAM ({BW_DRAM} GB/s)\")
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py` (cita sin comprobar)
