---
tipo: "receta"
titulo: "Cómo trazar el modelo Roofline con matplotlib (escala log-log, zonas coloreadas, puntos anotados)"
temas: ["ac", "matplotlib", "roofline", "visualizacion"]
claves: ["loglog", "fill_between", "scatter", "annotate", "np.minimum", "np.logspace"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[matplotlib]] · [[roofline]] · [[visualizacion]]

Pasos clave:
1. x = np.logspace(-2, 3, 1000) para eje X logarítmico (0.01 a 1000 FLOPs/Byte).
2. y_roof = np.minimum(BW_DRAM * x, GFLOPS_MAX) define la curva techo.
3. plt.loglog(x, y_roof) dibuja la rampa de memoria y plt.axhline el techo de CPU.
4. plt.fill_between con where=(x <= I_KNEE) y where=(x >= I_KNEE) colorea las dos zonas.
5. plt.scatter + plt.annotate con offsets y alineaciones (ha) evita solapamiento de etiquetas.
6. plt.grid(True, which="both", ls="-", color="0.85") da rejilla log-log limpia.

> plt.loglog(x, y_roof, label=f"Techo DRAM ({BW_DRAM} GB/s)", color="blue", lw=3) plt.axhline(y=GFLOPS_MAX, color="black", linestyle="--", label=f"Tope Cómputo CPU ({GFLOPS_MAX:.1f} GFLOPs/s)") plt.fill_between(x, y_roof, where=(x <= I_KNEE), color="mistyrose", alpha=0.6, label="Zona Memory-Bound") plt.fill_between(x, y_roof, where=(x >= I_KNEE), color="honeydew", alpha=0.6, label="Zona Compute-Bound")
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py` (cita sin comprobar)

Relacionado: [[clasificacion-memory-bound-vs-compute-bound-en-el-modelo-roo]]
