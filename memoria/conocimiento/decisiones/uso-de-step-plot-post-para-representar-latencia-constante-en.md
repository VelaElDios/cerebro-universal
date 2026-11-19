---
tipo: "decision"
titulo: "Uso de step plot 'post' para representar latencia constante entre puntos medidos"
temas: ["ac", "análisis de datos", "visualización"]
claves: ["step", "where='post", "matplotlib", "discontinuidad"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[análisis de datos]] · [[visualización]]

Decisión de representación: `where='post'` en `ax.step` hace que el valor de latencia se mantenga constante (horizontal) desde el tamaño actual hasta el siguiente tamaño medido, y el salto vertical ocurre en el siguiente tamaño. Esto modela correctamente que la latencia no cambia hasta que el working set supera el siguiente umbral de caché. La línea continua superpuesta (zorder=2) muestra la tendencia suave; el step plot tenue (zorder=1) muestra la realidad escalonada de los datos discretos.

> ax1.step(x, latency_ns, '--o', where='post', linewidth=1.0, markersize=6, color='tab:blue', alpha=0.35, zorder=1)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py` (cita sin comprobar)

Relacionado: [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]]
