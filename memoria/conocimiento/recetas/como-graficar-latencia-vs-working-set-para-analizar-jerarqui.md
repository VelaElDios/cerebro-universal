---
tipo: "receta"
titulo: "Cómo graficar latencia vs working set para analizar jerarquía de memoria"
temas: ["ac", "memoria", "pipeline", "rendimiento"]
claves: ["matplotlib", "axvspan", "log2", "working set", "latencia", "caché L1 L2 L3"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[memoria]] · [[pipeline]] · [[rendimiento]]

Pasos para replicar el análisis de latencia de memoria:
1. Obtener tamaños de caché reales con `lstopo` (hwloc) y rellenar TODO1: L1, L2, L3 en KiB.
2. Ejecutar benchmark de latencia (p.ej. `lat_mem_rd` de lmbench o similar) para medir latencia en ns para cada working set size del array `size_kib` y rellenar TODO2 en `latency_ns`.
3. Ejecutar `python3 tarea1_2_pintarLatvsMem.py`.
4. Interpretar saltos de latencia: cada salto coincide con el límite de una caché (L1→L2, L2→L3, L3→RAM).
Detalles de la gráfica:
- Eje X: log2(tamaño en KiB) en la gráfica completa; escala log base 2 en el zoom.
- Eje Y: escala log en completa; lineal (0.5–1.7 ns) en zoom L1/L2.
- Regiones coloreadas: rojo L1, verde L2, naranja L3, gris RAM (axvspan).
- Líneas verticales discontinuas en límites exactos de caché (axvline).
- Doble traza: línea continua (zorder=2) + step plot '--o' (zorder=1, alpha=0.35) para ver discontinuidades.
- Anotaciones numéricas sobre cada punto (formato 2 decimales <10 ns, 1 decimal ≥10 ns).

> Genera una gráfica de la latencia de acceso según el tamaño del working set.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_pintarLatvsMem.py`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]]
