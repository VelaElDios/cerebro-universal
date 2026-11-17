---
tipo: "fuente"
titulo: "Tema1 2026 27 (Tema1-Introduccion)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`.

## Resumen
Este trozo presenta el Tema 1 de Arquitectura de Computadores (curso 2026/27): define arquitectura frente a organización (ISA vs microarquitectura), introduce métricas de rendimiento (latencia, ancho de banda, tiempo de ejecución, speedup), y desarrolla la fórmula del tiempo de CPU (instrucciones × CPI × duración de ciclo) con sus factores determinantes. Incluye ejemplos comparativos de procesadores Intel/AMD y referencias a benchmarks Top500/Green500.
Este trozo del temario de Arquitectura de Computadores (curso 2026/27) cubre la Ley de Amdahl con su fórmula y dos ejercicios numéricos (uno resuelto en clase y otro para entregar en Moodle), las definiciones y fórmulas de MIPS y MFLOPS, una comparativa histórica de potencia de cálculo (Data de Star Trek vs. TOP500 2026), y una taxonomía de benchmarks: sintéticos (Dhrystone, Whetstone), núcleos (Linpack, usado en TOP500), suites (SPEC CPU2006 con SPECint/SPECfp y TPC) y computadores de referencia (UltraSPARC II, DEC VAX 11/780, UNIVAC). Incluye una tabla de resultados SPEC para un AMD Opteron 
Este trozo cubre la medición de rendimiento con suites SPEC (CPU 2017 y SPECpower ssj2008), la clasificación de tipos de computadores según su ámbito (móviles, escritorio, servidores, clusters, empotrados), las tendencias de paralelismo (ILP, TLP, DLP, multinúcleo), la taxonomía de Flynn (SISD, MISD, SIMD, MIMD) y las técnicas clásicas para mejorar el monoprocesador: segmentación (pipelining), superescalar y VLIW, con ejemplos históricos (Pentium Pro/II, IBM 4361).
Este trozo presenta la arquitectura VLIW como alternativa al superescalar, detallando su funcionamiento (compilador empaqueta operaciones en instrucciones muy largas, ejecución paralela en unidades funcionales independientes) y el ejemplo EPIC/IA64 (Itanium e Itanium2). A continuación, se enumeran una serie de ejercicios de evaluación de rendimiento: aplicación de la ley de Amdahl (ganancia de velocidad por mejora de componentes), cálculo de CPI y MIPS con mezclas de instrucciones, comparación de coste-efectividad entre sistemas, y un problema de mejora de disco duro.
Este trozo contiene dos ejercicios de Arquitectura de Computadores (curso 2026/27). El Ejercicio 22 plantea cálculos de reducción de tiempo de ejecución por tipo de instrucción (coma flotante, enteros, load/store, saltos) y cálculo de CPI dado frecuencia y conteo de instrucciones. El Ejercicio 8 aplica la ley de Amdahl a la optimización de un compilador para instrucciones de coma flotante, preguntando por speedup máximo y proporción de tiempo en FP dado un speedup observado.

## Lo que se sacó de él (35)
- [[arquitectura-epic-ia64-y-procesadores-itanium]]
- [[arquitectura-sisd-componentes-y-tecnicas-ilp-segmentacion-su]]
- [[benchmarks-de-referencia-top500-flops-vs-green500-mflops-w]]
- [[benchmarks-sinteticos-dhrystone-y-whetstone-proposito-y-orig]]
- [[calculo-de-cpi-dado-frecuencia-de-reloj-y-conteo-de-instrucc]]
- [[calculo-de-proporcion-de-tiempo-en-fp-dado-speedup-observado]]
- [[calculo-de-reduccion-de-tiempo-total-al-mejorar-un-tipo-de-i]]
- [[calculo-de-speedup-y-porcentaje-de-mejora-entre-dos-maquinas]]
- [[clasificacion-de-tipos-de-computadores-segun-requisitos-de-d]]
- [[como-resolver-un-problema-de-la-ley-de-amdahl-con-fraccion-m]]
- [[comparacion-de-dos-implementaciones-de-la-misma-isa-cpi-y-fr]]
- [[comparativa-historica-data-star-trek-60-tflops-vs-top500-219]]
- [[computadores-de-referencia-para-medicion-de-rendimiento-ultr]]
- [[definicion-de-mflops-millones-de-operaciones-de-punto-flotan]]
- [[definicion-de-mips-millones-de-instrucciones-por-segundo]]
- [[determinar-si-es-posible-alcanzar-un-speedup-objetivo-mejora]]
- [[distincion-entre-arquitectura-isa-y-organizacion-microarquit]]
- [[ejemplos-de-misma-isa-distinta-organizacion-y-viceversa-fami]]
- [[ejercicio-de-coste-efectividad-comparacion-de-sistemas-por-r]]
- [[ejercicio-de-mejora-de-disco-duro-y-ley-de-amdahl-ej-23]]
- [[ejercicio-de-participacion-en-clase-mejora-de-multiplicacion]]
- [[ejercicios-de-cpi-mips-y-tiempo-de-ejecucion-con-mezcla-de-i]]
- [[ejercicios-de-evaluacion-de-rendimiento-basados-en-ley-de-am]]
- [[formula-del-tiempo-de-ejecucion-de-cpu-y-sus-tres-factores]]
- [[funcionamiento-y-limites-de-la-segmentacion-pipelining-en-si]]
- [[ley-de-amdahl-aplicada-a-optimizacion-de-compilador-para-com]]
- [[ley-de-amdahl-formula-del-tiempo-de-ejecucion-nuevo]]
- [[linpack-nucleo-de-benchmark-para-sistemas-cientificos-y-base]]
- [[metricas-de-rendimiento-latencia-vs-throughput-ancho-de-band]]
- [[procesadores-superescalares-definicion-origen-risc-ejemplos]]
- [[resultados-specpower-ssj2008-para-amd-opteron-x4-2356-2-3-gh]]
- [[suite-spec-cpu-2017-metricas-specspeed-y-specrate]]
- [[taxonomia-de-flynn-sisd-misd-simd-mimd-y-criterio-de-clasifi]]
- [[tendencias-de-paralelismo-en-arquitectura-actual-ilp-tlp-dlp]]
- [[tipos-de-benchmarks-sinteticos-reales-nucleos-reducidos-y-su]]
