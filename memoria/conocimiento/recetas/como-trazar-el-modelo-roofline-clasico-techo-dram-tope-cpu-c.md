---
tipo: "receta"
titulo: "Cómo trazar el modelo Roofline clásico (techo DRAM + tope CPU) con matplotlib"
temas: ["ac", "matplotlib", "rendimiento", "roofline", "visualización"]
claves: ["loglog", "np.minimum", "BW_DRAM", "GFLOPS_MAX", "intensidad aritmética"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[matplotlib]] · [[rendimiento]] · [[roofline]] · [[visualización]]

1. Definir rango de intensidad aritmética: x = np.logspace(-2, 3, 1000) (0.01 a 1000 FLOPs/Byte). 2. Curva Roofline: y = min(BW_DRAM * x, GFLOPS_MAX). 3. Trazar con plt.loglog para ejes logarítmicos. 4. Añadir línea horizontal del tope CPU: plt.axhline(y=GFLOPS_MAX, linestyle="--"). 5. Etiquetas: X = "Intensidad Aritmética (FLOPs/Byte)", Y = "Rendimiento Máximo (GFLOPs/s)". Región por debajo de la rampa = memory-bound; región horizontal = compute-bound.

> plt.loglog(x, np.minimum(BW_DRAM * x, GFLOPS_MAX), label=f"Techo DRAM ({BW_DRAM} GB/s)", color="blue", lw=3)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_3_pintarRoofLin.py`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-fraccion-mejorada-al-do]] · [[comparacion-de-rendimiento-entre-procesadores-requiere-mismo]]
