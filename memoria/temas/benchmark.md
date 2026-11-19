---
tipo: "tema"
titulo: "benchmark"
notas: 28
---
# benchmark

Nodo del mapa del Cerebro con todo lo que se sabe de «benchmark» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/comparacion-de-maquinas-por-tiempo-total-de-ejecucion-de-mul|Comparación de máquinas por tiempo total de ejecución de múltiples programas]]
- 🧪 [[memoria/conocimiento/recetas/construccion-de-permutacion-aleatoria-en-ciclo-para-pointer|Construcción de permutación aleatoria en ciclo para pointer chasing]]
- 🧪 [[memoria/conocimiento/recetas/construccion-del-array-de-pointer-chasing-con-permutacion-ci|Construcción del array de pointer chasing con permutación cíclica aleatoria]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/calculo-de-mips-para-comparar-dos-computadores-con-mismo-isa|Cálculo de MIPS para comparar dos computadores con mismo ISA]]
- 🧪 [[memoria/conocimiento/recetas/como-calcular-speedup-global-mejorando-un-componente-ley-de|Cómo calcular speedup global mejorando un componente (Ley de Amdahl)]]
- 🧪 [[memoria/conocimiento/recetas/como-comparar-efectividad-en-coste-entre-dos-sistemas|Cómo comparar efectividad en coste entre dos sistemas]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-compilar-y-ejecutar-el-benchmark-de-latencia-de-memoria|Cómo compilar y ejecutar el benchmark de latencia de memoria]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-compilar-y-medir-lista-vs-vector-con-g-o2-hyperfine-y-p|Cómo compilar y medir lista vs vector con g++ -O2, hyperfine y perf]]
- 🧪 [[memoria/conocimiento/recetas/como-obtener-los-parametros-de-hardware-para-el-modelo-roofl|Cómo obtener los parámetros de hardware para el modelo Roofline en Linux]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-obtener-los-parametros-reales-de-tu-maquina-para-el-roo|Cómo obtener los parámetros reales de tu máquina para el Roofline]]
- 🧪 [[memoria/conocimiento/recetas/como-obtener-parametros-de-hardware-para-el-modelo-roofline|Cómo obtener parámetros de hardware para el modelo Roofline en Linux]]
- 🧪 [[memoria/conocimiento/recetas/medicion-de-latencia-con-50-millones-de-accesos-dependientes|Medición de latencia con 50 millones de accesos dependientes]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/medicion-de-latencia-con-cadena-de-dependencias-y-cronometro|Medición de latencia con cadena de dependencias y cronómetro high-resolution]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/medicion-de-rendimiento-con-hyperfine-y-perf-para-comparar-a|Medición de rendimiento con hyperfine y perf para comparar AoS vs SoA]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/prevencion-de-eliminacion-de-codigo-muerto-dce-en-benchmark|Prevención de eliminación de código muerto (DCE) en benchmark]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/compilar-con-o2-y-medir-con-perf-hyperfine-en-la-practica-ac|Compilar con -O2 y medir con perf/hyperfine en la práctica AC]] · ⚠️ propuesto
- ⚖️ [[memoria/conocimiento/decisiones/rango-de-working-set-4-kib-a-256-mib-en-potencias-de-2|Rango de working set: 4 KiB a 256 MiB en potencias de 2]]
- ⚖️ [[memoria/conocimiento/decisiones/uso-de-taskset-c-0-para-fijar-afinidad-de-cpu-y-reducir-vari|Uso de taskset -c 0 para fijar afinidad de CPU y reducir variabilidad]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults|Calentamiento (warm-up) para poblar TLB y evitar page faults]]
- 💡 [[memoria/conocimiento/conceptos/tecnica-pointer-chasing-para-medir-latencia-real-de-memoria|Técnica pointer chasing para medir latencia real de memoria]]

## Datos

- 📊 [[memoria/conocimiento/datos/parametros-de-ejemplo-para-roofline-cpu-4-9-ghz-bw-dram-26-1|Parámetros de ejemplo para Roofline: CPU 4.9 GHz, BW DRAM 26.143 GB/s, AVX2/FMA = 32 FLOPS/ciclo]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-del-benchmark-aos-soa-n-60m-iter-4-cache-line-64b|Parámetros del benchmark AoS/SoA: N=60M, ITER=4, cache line=64B]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-del-experimento-lista-vs-vector-n-20m-media-50-0f|Parámetros del experimento lista vs vector: N=20M, media=50.0f, semilla=123]]
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-benchmark-rangos-y-conteos|Parámetros fijos del benchmark: rangos y conteos]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-benchmark-semilla-accesos-formato-salid|Parámetros fijos del benchmark: semilla, accesos, formato salida]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-benchmark-tamano-de-array-bloque-y-repe|Parámetros fijos del benchmark: tamaño de array, bloque y repeticiones]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-experimento-aos-soa-tarea-3-2|Parámetros fijos del experimento AoS/SoA (tarea 3.2)]]
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-experimento-de-branchless-tamanio-repet|Parámetros fijos del experimento de branchless (TAMANIO, REPETICIONES, semilla)]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[rendimiento]] · [[hardware]] · [[roofline]] · [[parametros]] · [[hyperfine]] · [[perf]] · [[linux]] · [[arquitectura-computadores]] · [[compilacion]] · [[lscpu]] · [[stream]]
