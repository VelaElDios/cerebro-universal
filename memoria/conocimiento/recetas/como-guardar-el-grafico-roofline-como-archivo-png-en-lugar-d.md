---
tipo: "receta"
titulo: "Cómo guardar el gráfico Roofline como archivo PNG en lugar de mostrarlo"
temas: ["ac", "arquitectura-computadores", "matplotlib", "png", "roofline"]
claves: ["plt.savefig", "dpi=300", "roofline_clasico.png"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[matplotlib]] · [[png]] · [[roofline]]

El script incluye líneas comentadas para guardar la figura:
```python
# plt.savefig("roofline_clasico.png", dpi=300)
# print("¡Hecho! Guardado como 'roofline_clasico.png' sin líneas de cachés.")
```
Para usarlas: descomenta ambas líneas y comenta o elimina `plt.show()`. Genera un PNG de 300 DPI listo para incluir en informes. El nombre "sin líneas de cachés" indica que esta versión solo pinta el techo clásico (DRAM + CPU), sin añadir techos de L1/L2/L3.

> # Descomenta estas lineas si quieres guardar imagen en un fichero\n#plt.savefig(\"roofline_clasico.png\", dpi=300)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py` (cita sin comprobar)
