---
tipo: "decision"
titulo: "Elección de eje X logarítmico (logspace -2 a 3) para cubrir 4 órdenes de magnitud"
temas: ["ac", "arquitectura-computadores", "matplotlib", "roofline", "visualizacion"]
claves: ["np.logspace(-2", "3", "1000)", "plt.loglog", "intensidad aritmética"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[matplotlib]] · [[roofline]] · [[visualizacion]]

El script usa `np.logspace(-2, 3, 1000)` para generar 1000 puntos entre 10⁻² y 10³ FLOPs/Byte (0.01–1000). Esto cubre:
- Kernels memory-bound típicos (copia, escala, suma) ≈ 0.1–1 FLOPs/Byte.
- Kernels compute-bound (GEMM, convolución, stencil optimizado) ≈ 10–1000 FLOPs/Byte.
La escala log-log (`plt.loglog`) muestra la rampa como línea recta de pendiente 1 y la horizontal como línea plana, facilitando identificar el ridge point y clasificar kernels.

> x = np.logspace(-2, 3, 1000) # Rango del eje X
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py`

Relacionado: [[como-trazar-el-modelo-roofline-con-matplotlib-en-escala-log]] · [[como-generar-el-grafico-roofline-mononucleo-con-python]] · [[configuracion-de-ejes-log-lineal-y-etiquetas-de-potencias-de]]
