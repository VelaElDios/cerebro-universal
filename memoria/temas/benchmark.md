---
tipo: "tema"
titulo: "benchmark"
notas: 17
---
# benchmark

Nodo del mapa del Cerebro con todo lo que se sabe de «benchmark» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/comparacion-de-maquinas-por-tiempo-total-de-ejecucion-de-mul|Comparación de máquinas por tiempo total de ejecución de múltiples programas]]
- 🧪 [[memoria/conocimiento/recetas/construccion-de-permutacion-aleatoria-en-ciclo-para-pointer|Construcción de permutación aleatoria en ciclo para pointer chasing]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-mips-para-comparar-dos-computadores-con-mismo-isa|Cálculo de MIPS para comparar dos computadores con mismo ISA]]
- 🧪 [[memoria/conocimiento/recetas/como-compilar-y-ejecutar-el-benchmark-de-latencia-de-memoria|Cómo compilar y ejecutar el benchmark de latencia de memoria]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-compilar-y-medir-lista-vs-vector-con-g-o2-hyperfine-y-p|Cómo compilar y medir lista vs vector con g++ -O2, hyperfine y perf]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-obtener-los-parametros-reales-de-tu-maquina-para-el-roo|Cómo obtener los parámetros reales de tu máquina para el Roofline]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-obtener-parametros-de-hardware-para-el-modelo-roofline|Cómo obtener parámetros de hardware para el modelo Roofline en Linux]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/medicion-de-latencia-con-50-millones-de-accesos-dependientes|Medición de latencia con 50 millones de accesos dependientes]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/prevencion-de-eliminacion-de-codigo-muerto-dce-en-benchmark|Prevención de eliminación de código muerto (DCE) en benchmark]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/compilar-con-o2-y-medir-con-perf-hyperfine-en-la-practica-ac|Compilar con -O2 y medir con perf/hyperfine en la práctica AC]] · ⚠️ propuesto
- ⚖️ [[memoria/conocimiento/decisiones/rango-de-working-set-4-kib-a-256-mib-en-potencias-de-2|Rango de working set: 4 KiB a 256 MiB en potencias de 2]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults|Calentamiento (warm-up) para poblar TLB y evitar page faults]]
- 💡 [[memoria/conocimiento/conceptos/tecnica-pointer-chasing-para-medir-latencia-real-de-memoria|Técnica pointer chasing para medir latencia real de memoria]] · ⚠️ propuesto

## Datos

- 📊 [[memoria/conocimiento/datos/parametros-del-experimento-lista-vs-vector-n-20m-media-50-0f|Parámetros del experimento lista vs vector: N=20M, media=50.0f, semilla=123]]
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-benchmark-semilla-accesos-formato-salid|Parámetros fijos del benchmark: semilla, accesos, formato salida]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-experimento-aos-soa-tarea-3-2|Parámetros fijos del experimento AoS/SoA (tarea 3.2)]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-fijos-del-experimento-de-branchless-tamanio-repet|Parámetros fijos del experimento de branchless (TAMANIO, REPETICIONES, semilla)]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[arquitectura-computadores]] · [[parametros]] · [[compilacion]] · [[hyperfine]] · [[perf]] · [[rendimiento]] · [[lscpu]] · [[stream]] · [[page-fault]] · [[tlb]] · [[warmup]]
