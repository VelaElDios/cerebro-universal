---
tipo: "tema"
titulo: "cache"
notas: 15
---
# cache

Nodo del mapa del Cerebro con todo lo que se sabe de «cache» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/como-medir-contadores-hardware-con-perf-stat-para-comparar-p|Cómo medir contadores hardware con perf stat para comparar patrones de memoria]]
- 🧪 [[memoria/conocimiento/recetas/optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl|Optimizar std::list a std::vector con reserva y fusión de bucles (Tarea 3.1 AC)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/transformacion-aos-a-soa-para-optimizacion-de-cache-esquema|Transformación AoS a SoA para optimización de caché (esquema de código)]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache-por-campos|AoS vs SoA: desperdicio de ancho de banda en caché por campos no usados]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/calculo-teorico-de-reduccion-de-lineas-de-cache-en-soa-frent|Cálculo teórico de reducción de líneas de caché en SoA frente a AoS]]
- 💡 [[memoria/conocimiento/conceptos/fusion-de-bucles-loop-fusion-para-localidad-temporal|Fusión de bucles (loop fusion) para localidad temporal]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/mips64-usa-caches-separadas-para-instrucciones-y-datos-harva|MIPS64 usa cachés separadas para instrucciones y datos (Harvard modificada)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/metricas-hardware-clave-para-comparar-patrones-de-acceso|Métricas hardware clave para comparar patrones de acceso]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/parametros-del-experimento-tamano-de-datos-bloque-y-repetici|Parámetros del experimento: tamaño de datos, bloque y repeticiones]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector|Pointer chasing en std::list vs acceso contiguo en std::vector]]
- 💡 [[memoria/conocimiento/conceptos/tres-patrones-de-acceso-a-memoria-para-evaluar-localidad-de|Tres patrones de acceso a memoria para evaluar localidad de datos]] · ⚠️ propuesto

## Datos

- 📊 [[memoria/conocimiento/datos/latencias-de-cache-asumidas-en-el-ejemplo-de-bucle-vector-es|Latencias de caché asumidas en el ejemplo de bucle vector-escalar]]
- 📊 [[memoria/conocimiento/datos/parametros-del-benchmark-aos-soa-n-60m-iter-4-cache-line-64b|Parámetros del benchmark AoS/SoA: N=60M, ITER=4, cache line=64B]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/porcentaje-de-aprovechamiento-de-linea-de-cache-en-aos-acced|Porcentaje de aprovechamiento de línea de caché en AoS accediendo solo a id]]
- 📊 [[memoria/conocimiento/datos/tamano-del-vector-y-bloque-en-bytes-y-lineas-de-cache|Tamaño del vector y bloque en bytes y líneas de caché]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[memoria]] · [[optimizacion]] · [[perf]] · [[rendimiento]] · [[cpp]] · [[aos]] · [[soa]] · [[aos-soa]] · [[optimizacion-memoria]] · [[analisis-rendimiento]] · [[loop-transformation]]
