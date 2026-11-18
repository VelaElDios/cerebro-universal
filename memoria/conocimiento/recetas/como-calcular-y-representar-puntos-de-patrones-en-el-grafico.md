---
tipo: "receta"
titulo: "Cómo calcular y representar puntos de patrones en el gráfico Roofline (Tarea 2.1.d)"
temas: ["ac", "compute-bound", "intensidad aritmética", "memory-bound", "roofline"]
claves: ["intensidad aritmética", "GFLOPs/s", "Anexo B", "tarea2_1_pintarRoofLinconPuntos.py"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compute-bound]] · [[intensidad aritmética]] · [[memory-bound]] · [[roofline]]

Para cada patrón (temporal, espacial, aleatorio):
1. Calcular **intensidad aritmética (X)** = FLOPs totales / Bytes accedidos (fórmulas en Anexo B).
2. Calcular **rendimiento (Y)** = FLOPs totales / tiempo medido (en segundos) → GFLOPs/s.
3. Editar `tarea2_1_pintarRoofLinconPuntos.py` con las coordenadas (X,Y) de cada patrón.
4. Ejecutar script para generar Roofline con puntos superpuestos.
5. Interpretar: puntos bajo la rampa diagonal → *memory-bound*; puntos en la meseta horizontal → *compute-bound*. Explicar por qué cada patrón cae donde cae (ej. aleatorio: baja intensidad aritmética y bajo rendimiento → memory-bound extremo; temporal: alta intensidad si reusa datos en registros → puede acercarse a compute-bound).

> Calcula la posición (X,Y) de los patrones de acceso en el gráfico roofline de tu máquina utilizando las fórmulas del Anexo B y representa los puntos en la gráfica. (Nota: Puedes hacer uso del script tarea2_1_pintarRoofLinconPuntos.py para ayudarte a representar esos puntos en el roofline.)
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf` (cita sin comprobar)

Relacionado: [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[formula-del-techo-roofline-mononucleo]] · [[mapeo-de-patrones-de-acceso-en-grafico-roofline-gflops-s-y-f]] · [[mapeo-de-patrones-de-acceso-en-el-grafico-roofline]]
