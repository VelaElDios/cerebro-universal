---
tipo: "receta"
titulo: "Anotación automática de valores sobre puntos en matplotlib"
temas: ["ac", "annotations", "data-visualization", "matplotlib", "python"]
claves: ["annotate", "offset points", "xytext", "fontsize", "weight", "color"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[annotations]] · [[data-visualization]] · [[matplotlib]] · [[python]]

Patrón reutilizable para etiquetar cada punto con su valor numérico:
```python
for i in range(len(x_vals)):
    val_text = f"{y_vals[i]:.2f}" if y_vals[i] < 10 else f"{y_vals[i]:.1f}"
    ax.annotate(
        val_text,
        (x_vals[i], y_vals[i]),
        textcoords="offset points",
        xytext=(0, 6),          # 6 pt arriba del marcador
        ha='center',
        fontsize=7,
        weight='bold',
        color='navy'
    )
```
Adapta `xytext`, `fontsize` y formato según densidad de puntos y escala del eje.

> for i in range(len(size_kib)): ... ax1.annotate(val_text, (x[i], latency_ns[i]), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=7, weight='bold', color='navy')
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py` (cita sin comprobar)

Relacionado: [[como-anotar-puntos-en-grafica-log-log-sin-solapar-etiquetas]] · [[configuracion-de-ejes-log-lineal-y-etiquetas-de-potencias-de]] · [[uso-de-step-plot-post-superpuesto-a-linea-continua-para-most]]
