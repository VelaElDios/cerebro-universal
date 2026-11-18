---
tipo: "concepto"
titulo: "Interpretación de regiones memory-bound vs compute-bound en el gráfico"
temas: ["ac", "analisis-rendimiento", "arquitectura-computadores", "roofline"]
claves: ["memory-bound", "compute-bound", "ridge point", "intensidad aritmética"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[analisis-rendimiento]] · [[arquitectura-computadores]] · [[roofline]]

En el gráfico Roofline resultante:
- Zona bajo la rampa azul (pendiente 1): **memory-bound**. El rendimiento escala linealmente con la intensidad aritmética; el cuello de botella es el ancho de banda de memoria. Ejemplos: `memcpy`, `stream`, stencil simples.
- Zona bajo la horizontal negra (GFLOPS_MAX): **compute-bound**. El rendimiento se satura en el tope de cómputo; la memoria no es el límite. Ejemplos: DGEMM optimizado, FFT, convoluciones con reuse de datos.
- **Ridge point** (punto de inflexión): I = GFLOPS_MAX / BW_DRAM ≈ 6 FLOPs/Byte en el ejemplo. A la izquierda → memory-bound; a la derecha → compute-bound.
El objetivo de optimización: mover kernels hacia arriba (mejorar uso de BW o cómputo) y/o hacia la derecha (aumentar intensidad aritmética con blocking, tiling, fusion).

> Análisis:     Identificar límites por memoria (memory-bound) vs. cómputo.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_3_pintarRoofLin.py`

Relacionado: [[punto-de-inflexion-ridge-point-en-el-modelo-roofline]] · [[punto-de-inflexion-knee-del-modelo-roofline-i-knee-gflops-ma]] · [[como-calcular-y-representar-puntos-de-patrones-en-el-grafico]]
