---
tipo: "receta"
titulo: "Cómo trazar el modelo Roofline con matplotlib en escala log-log"
temas: ["ac", "matplotlib", "python", "roofline"]
claves: ["loglog", "fill_between", "np.minimum", "np.logspace", "axhline"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[matplotlib]] · [[python]] · [[roofline]]

Pasos clave:
1. Definir rango X en escala logarítmica: `x = np.logspace(-2, 3, 1000)` (0.01 a 1000 FLOPs/Byte).
2. Calcular techo combinado: `y_roof = np.minimum(BW_DRAM * x, GFLOPS_MAX)` — rampa de memoria (BW * intensidad) y horizontal de CPU.
3. Dibujar con `plt.loglog(x, y_roof, ...)` para ejes log-log.
4. Añadir línea horizontal del tope CPU: `plt.axhline(y=GFLOPS_MAX, color="black", linestyle="--", ...)`.
5. Colorear zonas con `fill_between` usando condición `where`:
   - Memory-bound: `where=(x <= I_KNEE)` → color "mistyrose".
   - Compute-bound: `where=(x >= I_KNEE)` → color "honeydew".
6. Puntos medidos: `plt.scatter(x_p, y_p, ...)` + `plt.annotate(...)` con `textcoords="offset points"` y `xytext` para desplazar etiquetas.
7. Formato: `plt.xlabel`, `plt.ylabel`, `plt.title`, `plt.grid(True, which="both", ls="-", color="0.85")`, `plt.legend(loc="lower right")`.

> plt.loglog(x, y_roof, label=f"Techo DRAM ({BW_DRAM} GB/s)", color="blue", lw=3)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py`
