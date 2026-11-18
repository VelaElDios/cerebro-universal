---
tipo: "receta"
titulo: "Cómo anotar puntos en gráfica log-log sin solapar etiquetas"
temas: ["ac", "anotaciones", "matplotlib", "python", "visualización"]
claves: ["annotate", "offset points", "xytext", "ha", "zorder", "scatter"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[anotaciones]] · [[matplotlib]] · [[python]] · [[visualización]]

Técnica para colocar etiquetas junto a puntos en escala log-log sin que se solapen:
1. Definir arrays paralelos: `intensidades`, `rendimientos`, `etiquetas`, `colores`.
2. Preparar offsets y alineaciones horizontales por punto:
   ```python
   offsets_xy   = [(12, 10), (-12, 10), (0, +18)]  # (dx, dy) en puntos
   alineaciones = ['left', 'right', 'center']
   ```
3. Iterar con `zip` y llamar:
   ```python
   plt.scatter(x_p, y_p, color=color, s=150, zorder=5, label=etiqueta)
   plt.annotate(f"{etiqueta} \n ({x_p:.2f}, {y_p:.1f})",
                (x_p, y_p),
                textcoords="offset points",
                xytext=offset,
                ha=ha,
                fontsize=9,
                fontweight='bold',
                color=color)
   ```
- `textcoords="offset points"`: coordenadas relativas al punto en puntos (1/72 pulgada).
- `xytext`: desplazamiento (dx, dy) desde el punto.
- `ha` (horizontal alignment): 'left'/'right'/'center' según lado del punto.
- `zorder=5` en scatter asegura que los puntos queden por encima de las zonas rellenas.

> plt.annotate(f"{etiqueta} \n ({x_p:.2f}, {y_p:.1f})", (x_p, y_p), textcoords="offset points", xytext=offset, ha=ha, fontsize=9, fontweight='bold', color=color)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_pintarRoofLin_conPunto.py`

Relacionado: [[anotacion-automatica-de-valores-sobre-puntos-en-matplotlib]] · [[configuracion-de-ejes-log-lineal-y-etiquetas-de-potencias-de]] · [[como-trazar-el-modelo-roofline-con-matplotlib-en-escala-log]]
