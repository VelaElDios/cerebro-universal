---
tipo: "decision"
titulo: "Uso de step plot 'post' superpuesto a línea continua para mostrar discontinuidad"
temas: ["ac", "data-visualization", "matplotlib", "plot-design", "python"]
claves: ["step plot", "where='post", "zorder", "alpha", "dual plotting"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[data-visualization]] · [[matplotlib]] · [[plot-design]] · [[python]]

Decisión de diseño visual: dibujar dos capas para la misma serie:
1. **Línea continua** (`plot '-', linewidth=1.2, alpha=1.0, zorder=2`): tendencia suave, fácil de seguir.
2. **Escalones** (`step '--o', where='post', linewidth=1.0, alpha=0.35, zorder=1`): representa la realidad de que la latencia es constante dentro de un intervalo de working set y salta en el siguiente; `where='post'` mantiene el valor hasta la siguiente muestra.
La transparencia (alpha=0.35) y el zorder inferior evitan que los escalones oculten la línea principal.

> ax1.step(x, latency_ns, '--o', where='post', ... alpha=0.35, zorder=1) ... ax1.plot(x, latency_ns, '-', ... alpha=1.0, zorder=2)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py` (cita sin comprobar)

Relacionado: [[como-graficar-latencia-vs-working-set-con-jerarquia-de-cache]] · [[configuracion-de-ejes-log-lineal-y-etiquetas-de-potencias-de]] · [[patron-de-salto-de-latencia-en-fronteras-de-cache]]
