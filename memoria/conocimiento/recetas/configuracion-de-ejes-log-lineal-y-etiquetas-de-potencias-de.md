---
tipo: "receta"
titulo: "Configuración de ejes log/lineal y etiquetas de potencias de 2 en matplotlib"
temas: ["ac", "data-visualization", "log-scale", "matplotlib", "python"]
claves: ["set_xscale", "set_xticks", "set_xticklabels", "log2", "base=2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[data-visualization]] · [[log-scale]] · [[matplotlib]] · [[python]]

Técnica para que el eje X muestre tamaños en KiB (4, 8, 16…) aunque la coordenada interna sea log2:
- **Gráfica completa (ax1)**: `ax1.set_xticks(np.log2(size_kib))` coloca ticks en log2; `ax1.set_xticklabels(size_kib, rotation=45)` pone etiquetas legibles.
- **Zoom (ax2)**: `ax2.set_xscale('log', base=2)` activa escala logarítmica base 2 nativa; `ax2.set_xticks(size_kib[mask])` y `ax2.set_xticklabels(size_kib[mask], rotation=45)` usan valores directos.
- **Eje Y**: `ax1.set_yscale('log')` para ver décadas de ns; `ax2.set_yscale('linear')` con `set_ylim(0.5, 1.7)` para zoom lineal en L1/L2.

> ax1.set_xticks(np.log2(size_kib)) ... ax1.set_xticklabels(size_kib, rotation=45)
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py` (cita sin comprobar)

Relacionado: [[como-anotar-puntos-en-grafica-log-log-sin-solapar-etiquetas]] · [[como-trazar-el-modelo-roofline-con-matplotlib-en-escala-log]] · [[como-graficar-latencia-vs-working-set-con-jerarquia-de-cache]]
