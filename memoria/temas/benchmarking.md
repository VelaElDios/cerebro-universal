---
tipo: "tema"
titulo: "benchmarking"
notas: 12
---
# benchmarking

Nodo del mapa del Cerebro con todo lo que se sabe de «benchmarking» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/benchmarking-comparativo-con-hyperfine-warmup-y-comillas|Benchmarking comparativo con Hyperfine (warmup y comillas)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/benchmarking-ilp-con-hyperfine-y-perf-para-medir-cycles-inst|Benchmarking ILP con hyperfine y perf para medir cycles, instructions e IPC]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-benchmarkear-y-perfilar-patrones-de-acceso-con-hyperfin|Cómo benchmarkear y perfilar patrones de acceso con hyperfine y perf stat (Tarea 2.1.a)]]
- 🧪 [[memoria/conocimiento/recetas/como-compilar-y-ejecutar-el-benchmark-de-patrones-de-acceso|Cómo compilar y ejecutar el benchmark de patrones de acceso a memoria]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-hacer-benchmark-estadistico-con-hyperfine-entre-patrone|Cómo hacer benchmark estadístico con hyperfine entre patrones temporal y aleatorio]]
- 🧪 [[memoria/conocimiento/recetas/como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per|Cómo medir impacto de cache-misses e IPC con hyperfine y perf en experimentos controlados]]
- 🧪 [[memoria/conocimiento/recetas/como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset|Cómo medir latencia de memoria con pointer chasing y taskset (Tarea 1.2)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/mapeo-de-patrones-de-acceso-en-grafico-roofline-gflops-s-y-f|Mapeo de patrones de acceso en gráfico Roofline (GFLOPs/s y FLOPs/Byte)]] · ⚠️ propuesto

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/fijar-ejecucion-en-un-unico-nucleo-con-taskset-para-evitar-m|Fijar ejecución en un único núcleo con taskset para evitar migración y ruido (Tarea 1.2)]]
- ⚖️ [[memoria/conocimiento/decisiones/uso-de-semilla-fija-42-en-mt19937-para-reproducibilidad-del|Uso de semilla fija (42) en mt19937 para reproducibilidad del patrón aleatorio]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/suite-spec-cpu-2017-metricas-specspeed-y-specrate|Suite SPEC CPU 2017: métricas SPECspeed y SPECrate]]

## Datos

- 📊 [[memoria/conocimiento/datos/resultados-specpower-ssj2008-para-amd-opteron-x4-2356-2-3-gh|Resultados SPECpower ssj2008 para AMD Opteron X4 2356 (2.3 GHz)]]

## Temas relacionados

[[ac]] · [[hyperfine]] · [[perf]] · [[taskset]] · [[rendimiento]] · [[consumo-energetico]] · [[specpower]] · [[afinidad]] · [[metodología]] · [[random]] · [[reproducibilidad]] · [[ipc]]
