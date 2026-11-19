---
tipo: "tema"
titulo: "roofline"
notas: 30
---
# roofline

Nodo del mapa del Cerebro con todo lo que se sabe de «roofline» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/calculo-de-flops-totales-para-el-kernel-de-la-tarea-2-1|Cálculo de FLOPs totales para el kernel de la tarea 2.1]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-intensidad-aritmetica-eje-x-flops-byte-con-perf-c|Cálculo de intensidad aritmética (eje X: FLOPs/Byte) con perf cache-misses]]
- 🧪 [[memoria/conocimiento/recetas/calculo-del-rendimiento-real-eje-y-gflops-s-con-hyperfine|Cálculo del rendimiento real (eje Y: GFLOPs/s) con hyperfine]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-calcular-el-techo-de-computo-gflops-max-y-el-punto-de-i|Cómo calcular el techo de cómputo (GFLOPS máx) y el punto de inflexión del modelo Roofline]]
- 🧪 [[memoria/conocimiento/recetas/como-calcular-el-techo-de-computo-peak-gflops-para-avx2-fma|Cómo calcular el techo de cómputo (peak GFLOPS) para AVX2/FMA en x86]]
- 🧪 [[memoria/conocimiento/recetas/como-calcular-y-representar-puntos-de-patrones-en-el-grafico|Cómo calcular y representar puntos de patrones en el gráfico Roofline (Tarea 2.1.d)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-generar-el-grafico-roofline-mononucleo-con-python|Cómo generar el gráfico Roofline mononúcleo con Python]]
- 🧪 [[memoria/conocimiento/recetas/como-generar-el-modelo-roofline-del-procesador-con-lscpu-y-s|Cómo generar el modelo Roofline del procesador con lscpu y STREAM (Tarea 1.3)]]
- 🧪 [[memoria/conocimiento/recetas/como-guardar-el-grafico-roofline-como-archivo-png-en-lugar-d|Cómo guardar el gráfico Roofline como archivo PNG en lugar de mostrarlo]]
- 🧪 [[memoria/conocimiento/recetas/como-obtener-los-parametros-de-hardware-para-el-modelo-roofl|Cómo obtener los parámetros de hardware para el modelo Roofline en Linux]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-obtener-los-parametros-reales-de-tu-maquina-para-el-roo|Cómo obtener los parámetros reales de tu máquina para el Roofline]]
- 🧪 [[memoria/conocimiento/recetas/como-trazar-el-modelo-roofline-clasico-techo-dram-tope-cpu-c|Cómo trazar el modelo Roofline clásico (techo DRAM + tope CPU) con matplotlib]]
- 🧪 [[memoria/conocimiento/recetas/como-trazar-el-modelo-roofline-con-matplotlib-escala-log-log|Cómo trazar el modelo Roofline con matplotlib (escala log-log, zonas coloreadas, puntos anotados)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-trazar-el-modelo-roofline-con-matplotlib-en-escala-log|Cómo trazar el modelo Roofline con matplotlib en escala log-log]]
- 🧪 [[memoria/conocimiento/recetas/mapeo-de-patrones-de-acceso-en-grafico-roofline-gflops-s-y-f|Mapeo de patrones de acceso en gráfico Roofline (GFLOPs/s y FLOPs/Byte)]] · ⚠️ propuesto

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/eleccion-de-colores-para-zonas-memory-bound-y-compute-bound|Elección de colores para zonas memory-bound y compute-bound]] · ⚠️ propuesto
- ⚖️ [[memoria/conocimiento/decisiones/eleccion-de-eje-x-logaritmico-logspace-2-a-3-para-cubrir-4-o|Elección de eje X logarítmico (logspace -2 a 3) para cubrir 4 órdenes de magnitud]]
- ⚖️ [[memoria/conocimiento/decisiones/uso-de-todo1-y-todo2-como-puntos-de-personalizacion-obligato|Uso de TODO1 y TODO2 como puntos de personalización obligatorios para el alumno]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/clasificacion-memory-bound-vs-compute-bound-en-el-modelo-roo|Clasificación memory-bound vs compute-bound en el modelo Roofline]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/formula-del-techo-roofline-mononucleo|Fórmula del techo Roofline mononúcleo]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/interpretacion-de-regiones-memory-bound-vs-compute-bound-en|Interpretación de regiones memory-bound vs compute-bound en el gráfico]]
- 💡 [[memoria/conocimiento/conceptos/mapeo-de-patrones-de-acceso-en-el-grafico-roofline|Mapeo de patrones de acceso en el gráfico Roofline]]
- 💡 [[memoria/conocimiento/conceptos/modelo-roofline-regiones-memory-bound-vs-compute-bound-y-rid|Modelo Roofline: regiones memory-bound vs compute-bound y ridge point]]
- 💡 [[memoria/conocimiento/conceptos/punto-de-inflexion-knee-del-modelo-roofline-mononucleo|Punto de inflexión (knee) del modelo Roofline mononúcleo]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/punto-de-inflexion-knee-del-modelo-roofline-i-knee-gflops-ma|Punto de inflexión (knee) del modelo Roofline: I_KNEE = GFLOPS_MAX / BW_DRAM]]
- 💡 [[memoria/conocimiento/conceptos/punto-de-inflexion-ridge-point-en-el-modelo-roofline|Punto de inflexión (ridge point) en el modelo Roofline]]

## Datos

- 📊 [[memoria/conocimiento/datos/parametros-de-ejemplo-del-script-cpu-4-9-ghz-ddr4-26-143-gb|Parámetros de ejemplo del script (CPU 4.9 GHz, DDR4 26.143 GB/s)]]
- 📊 [[memoria/conocimiento/datos/parametros-de-ejemplo-para-roofline-cpu-4-9-ghz-bw-dram-26-1|Parámetros de ejemplo para Roofline: CPU 4.9 GHz, BW DRAM 26.143 GB/s, AVX2/FMA = 32 FLOPS/ciclo]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/valores-de-ejemplo-de-intensidad-y-rendimiento-para-tres-pat|Valores de ejemplo de intensidad y rendimiento para tres patrones de acceso (temporal, secuencial, aleatorio)]]
- 📊 [[memoria/conocimiento/datos/valores-de-ejemplo-para-cpu-del-laboratorio-frecuencia-bw-pu|Valores de ejemplo para CPU del laboratorio (frecuencia, BW, puntos medidos)]]

## Temas relacionados

[[ac]] · [[rendimiento]] · [[arquitectura-computadores]] · [[matplotlib]] · [[hardware]] · [[benchmark]] · [[mediciones]] · [[practica]] · [[visualización]] · [[visualizacion]] · [[intensidad aritmética]] · [[perf]]
