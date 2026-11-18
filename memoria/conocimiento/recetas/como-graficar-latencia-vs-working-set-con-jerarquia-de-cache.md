---
tipo: "receta"
titulo: "Cómo graficar latencia vs working set con jerarquía de caché en matplotlib"
temas: ["ac", "arquitectura-computadores", "cache-hierarchy", "matplotlib", "python"]
claves: ["axvspan", "axvline", "step plot", "log scale", "working set", "latency", "L1 L2 L3 cache"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[cache-hierarchy]] · [[matplotlib]] · [[python]]

Este script crea una visualización estándar para analizar la jerarquía de memoria:
1. **Configuración (TODO1)**: Define los tamaños de caché L1, L2, L3 en KiB según `lstopo` de tu máquina.
2. **Datos (TODO2)**: Introduce las latencias medidas en ns para cada tamaño de working set en `size_kib`.
3. **Eje X**: Usa `np.log2(size_kib)` para la gráfica completa (escala log) y valores directos para el zoom (escala log base 2).
4. **Regiones de caché (axvspan)**: Pinta cuatro franjas de color semitransparente:
   - Rojo: L1 (0 a L1)
   - Verde: L2 (L1 a L2)
   - Naranja: L3 (L2 a L3)
   - Gris: RAM (L3 a max)
5. **Líneas de frontera (axvline)**: Líneas discontinuas verticales en log2(L1), log2(L2), log2(L3).
6. **Dual plotting**: Superpone una línea continua (`plot '-', zorder=2`) y un gráfico de escalones (`step '--o', where='post', zorder=1, alpha=0.35`) para mostrar tanto la tendencia como la discontinuidad entre muestras.
7. **Anotaciones**: Bucle que escribe el valor de latencia sobre cada punto con `annotate`.
8. **Subgráfica zoom (ax2)**: Filtra `size_kib <= 256`, usa escala lineal en Y (0.5-1.7 ns) y log base 2 en X, repite el mismo esquema visual.
9. **Ejecución**: `python3 tarea1_2_pintarLatvsMem.py` muestra la ventana interactiva; descomenta `savefig` para guardar PNG.

> Genera una gráfica de la latencia de acceso según el tamaño del working set.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py`

Relacionado: [[patron-de-salto-de-latencia-en-fronteras-de-cache]] · [[working-set-size-vs-memory-access-latency-experiment]] · [[como-trazar-el-modelo-roofline-con-matplotlib-en-escala-log]]
