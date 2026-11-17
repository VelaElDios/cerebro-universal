---
tipo: "decision"
titulo: "Elección de colores para zonas memory-bound y compute-bound"
temas: ["ac", "diseño", "roofline", "visualización"]
claves: ["mistyrose", "honeydew", "fill_between", "alpha", "memory-bound", "compute-bound"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[diseño]] · [[roofline]] · [[visualización]]

Decisión de diseño visual:
- Zona Memory-bound (intensidad ≤ I_KNEE): color "mistyrose" (rosa pálido) con alpha=0.6.
- Zona Compute-bound (intensidad ≥ I_KNEE): color "honeydew" (verde muy claro) con alpha=0.6.
Razones implícitas:
1. Colores pastel suaves no compiten con la línea del techo (azul) ni los puntos (verde/naranja/rojo).
2. Alpha=0.6 permite ver la cuadrícula y la línea del techo por debajo.
3. Etiquetas en leyenda ("Zona Memory-Bound", "Zona Compute-Bound") facilitan interpretación inmediata.
4. Uso de nombres de color CSS/HTML estándar (matplotlib los reconoce) en lugar de códigos hex.

> plt.fill_between(x, y_roof, where=(x <= I_KNEE), color="mistyrose", alpha=0.6, label="Zona Memory-Bound") ... plt.fill_between(x, y_roof, where=(x >= I_KNEE), color="honeydew", alpha=0.6, label="Zona Compute-Bound")
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py` (cita sin comprobar)
