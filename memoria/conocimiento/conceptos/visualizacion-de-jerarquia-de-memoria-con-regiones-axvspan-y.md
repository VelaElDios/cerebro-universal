---
tipo: "concepto"
titulo: "Visualización de jerarquía de memoria con regiones axvspan y escalas logarítmicas"
temas: ["ac", "rendimiento", "visualización"]
claves: ["axvspan", "axvline", "set_xscale log", "set_yscale log", "log2", "working set"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[rendimiento]] · [[visualización]]

Técnica de visualización para mostrar claramente los límites de la jerarquía de memoria:
- Usar `axvspan` en coordenadas log2 para pintar bandas de color tras cada nivel de caché (L1 rojo, L2 verde, L3 naranja, RAM gris).
- Dibujar `axvline` discontinuas en los límites exactos (log2(L1), log2(L2), log2(L3)).
- Eje X en log2(tamaño) para que las potencias de 2 queden equidistantes; ticks en posiciones log2(size_kib) y etiquetas con valores reales en KiB rotadas 45°.
- Eje Y en escala log en la visión global para ver saltos de órdenes de magnitud; escala lineal en zoom L1/L2 para resolver detalle sub-ns.
- Doble traza: línea continua fina (zorder=2) + step plot '--o' tenue (zorder=1, where='post') para resaltar que la latencia se mantiene constante hasta el siguiente tamaño medido.
- Anotaciones `annotate` con offset en puntos para no solapar marcadores.

> ax1.axvspan(np.log2(size_kib.min()), np.log2(L1), color='tab:red', alpha=0.15)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py`

Relacionado: [[comparacion-de-rendimiento-entre-procesadores-requiere-mismo]] · [[detenciones-en-pipeline-afectan-negativamente-a-prestaciones]]
