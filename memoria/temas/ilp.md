---
tipo: "tema"
titulo: "ilp"
notas: 54
---
# ilp

Nodo del mapa del Cerebro con todo lo que se sabe de «ilp» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/condicion-para-solapar-iteraciones-de-un-bucle-desenrollado|Condición para solapar iteraciones de un bucle (desenrollado / software pipelining)]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-speedup-vliw-vs-mips64-segmentado-considerando-me|Cálculo de speedup VLIW vs MIPS64 segmentado considerando mejor planificación]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-manual-manual-unrolling-con-4-acumuladores-para|Desenrollado manual (Manual Unrolling) con 4 acumuladores para romper cadena de dependencia y subir IPC]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-minimo-de-bucle-para-planificacion-sin-detencio|Desenrollado mínimo de bucle para planificación sin detenciones (secuencia 0,1,0,2)]]
- 🧪 [[memoria/conocimiento/recetas/funcionamiento-y-limites-de-la-segmentacion-pipelining-en-si|Funcionamiento y límites de la segmentación (pipelining) en SISD]]
- 🧪 [[memoria/conocimiento/recetas/optimizacion-ilp-mediante-desenrollado-de-4-vias-con-acumula|Optimización ILP mediante desenrollado de 4 vías con acumuladores independientes]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul|Optimización ILP mediante desenrollado de bucle con 4 acumuladores independientes]]
- 🧪 [[memoria/conocimiento/recetas/planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en|Planificación VLIW de bucle con latencias dadas (examen AC enero 2018)]]
- 🧪 [[memoria/conocimiento/recetas/planificacion-vliw-para-bucle-con-latencias-mem-2-add-d-1-mu|Planificación VLIW para bucle con latencias MEM=2, ADD.D=1, MUL.D=2 (4 ops/ciclo)]]
- 🧪 [[memoria/conocimiento/recetas/proposito-del-desenrollado-de-bucles-loop-unrolling|Propósito del desenrollado de bucles (loop unrolling)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/secuencia-de-instrucciones-y-dependencias-en-el-ejemplo-toma|Secuencia de instrucciones y dependencias en el ejemplo Tomasulo del tema 3]]
- 🧪 [[memoria/conocimiento/recetas/tecnicas-avanzadas-estaticas-y-dinamicas-para-reducir-detenc|Técnicas avanzadas estáticas y dinámicas para reducir detenciones]] · ⚠️ propuesto

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/desenrollado-de-bucles-replicar-mientras-se-reduzcan-detenci|Desenrollado de bucles: replicar mientras se reduzcan detenciones (stalls)]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/alto-ilp-requiere-bajo-grado-de-dependencia-entre-instruccio|Alto ILP requiere bajo grado de dependencia entre instrucciones]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/arquitectura-sisd-componentes-y-tecnicas-ilp-segmentacion-su|Arquitectura SISD: componentes y técnicas ILP (segmentación, superescalar, VLIW)]]
- 💡 [[memoria/conocimiento/conceptos/caracteristicas-clave-de-procesadores-vliw|Características clave de procesadores VLIW]]
- 💡 [[memoria/conocimiento/conceptos/definiciones-clave-basic-block-antidependencia-loop-unrollin|Definiciones clave: basic block, antidependencia, loop unrolling, planificación estática, software pipelining, Scoreboard, Tomasulo CDB, predicción saltos (preguntas 7-15)]]
- 💡 [[memoria/conocimiento/conceptos/definicion-de-bloque-basico-en-paralelismo-a-nivel-de-instru|Definición de bloque básico en paralelismo a nivel de instrucción (pregunta 6)]]
- 💡 [[memoria/conocimiento/conceptos/definicion-de-procesador-vliw|Definición de procesador VLIW]]
- 💡 [[memoria/conocimiento/conceptos/definicion-y-objetivo-de-la-planificacion-de-trazas-trace-sc|Definición y objetivo de la planificación de trazas (trace scheduling)]]
- 💡 [[memoria/conocimiento/conceptos/dependencia-raw-en-acumulacion-secuencial-limita-ilp-en-pipe|Dependencia RAW en acumulación secuencial limita ILP en pipeline]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/dependencias-en-el-bucle-de-ejemplo-vliw-examen-ac-2018|Dependencias en el bucle de ejemplo VLIW (examen AC 2018)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/desenrollado-de-bucle-loop-unrolling-3-para-vliw-y-compactac|Desenrollado de bucle (loop unrolling) 3× para VLIW y compactación]]
- 💡 [[memoria/conocimiento/conceptos/desenrollamiento-de-bucles-loop-unrolling-permite-planificar|Desenrollamiento de bucles (loop unrolling) permite planificar instrucciones de distintas iteraciones]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/desenrollamiento-de-bucles-reduce-dependencias-de-control-me|Desenrollamiento de bucles: reduce dependencias de control mediante planificación estática]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/diferencia-fundamental-vliw-vs-superescalar-compilador-vs-ha|Diferencia fundamental VLIW vs Superescalar: compilador vs hardware detecta paralelismo]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/efectos-de-la-especulacion-en-flujo-de-datos-ilp-y-excepcion|Efectos de la especulación en flujo de datos, ILP y excepciones]]
- 💡 [[memoria/conocimiento/conceptos/ilp-alto-requiere-bajo-grado-de-dependencia-entre-instruccio|ILP alto requiere bajo grado de dependencia entre instrucciones]]
- 💡 [[memoria/conocimiento/conceptos/impacto-de-la-frecuencia-de-saltos-en-el-ilp-y-tamano-de-blo|Impacto de la frecuencia de saltos en el ILP y tamaño de bloque básico]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/name-dependency-dependencia-de-nombre-incluye-waw-y-war|Name dependency (dependencia de nombre) incluye WAW y WAR]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/planificacion-de-trazas-trace-scheduling-para-condicionales|Planificación de trazas (trace scheduling) para condicionales en bucles]]
- 💡 [[memoria/conocimiento/conceptos/planificacion-dinamica-tomasulo-orden-de-ejecucion-por-dispo|Planificación dinámica (Tomasulo): orden de ejecución por disponibilidad de operandos]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/planificacion-estatica-vs-dinamica-de-instrucciones-en-arqui|Planificación estática vs dinámica de instrucciones en Arquitectura de Computadores]]
- 💡 [[memoria/conocimiento/conceptos/planificacion-software-software-pipelining-transforma-iterac|Planificación software (software pipelining) transforma iteraciones dependientes en independientes]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/problema-examen-ac-planificacion-vliw-para-bucle-y-i-a-x-i-2|Problema examen AC: Planificación VLIW para bucle y(i)=A*x(i)² con latencias dadas]]
- 💡 [[memoria/conocimiento/conceptos/procesadores-superescalares-definicion-origen-risc-ejemplos|Procesadores superescalares: definición, origen RISC, ejemplos x86 (Pentium Pro/II)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/proposito-de-la-planificacion-por-software-software-pipelini|Propósito de la planificación por software (software pipelining) (pregunta 8)]]
- 💡 [[memoria/conocimiento/conceptos/proposito-de-la-segmentacion-software-software-pipelining-te|Propósito de la segmentación software (software pipelining) (test AC Q8)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/que-busca-conseguir-la-segmentacion-software-software-pipeli|Qué busca conseguir la segmentación software (software pipelining) en el código del bucle]]
- 💡 [[memoria/conocimiento/conceptos/que-es-un-bloque-basico-basic-block-en-ilp|Qué es un bloque básico (basic block) en ILP]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/reduccion-final-de-acumuladores-parciales-tras-desenrollado|Reducción final de acumuladores parciales tras desenrollado]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/relacion-ilp-y-cpi-en-procesadores-segmentados|Relación ILP y CPI en procesadores segmentados]]
- 💡 [[memoria/conocimiento/conceptos/romper-cadena-de-dependencias-para-exponer-ilp-en-pipeline-s|Romper cadena de dependencias para exponer ILP en pipeline superscalar]]
- 💡 [[memoria/conocimiento/conceptos/segmentacion-software-software-pipelining-en-bucles-sin-depe|Segmentación software (software pipelining) en bucles sin dependencias]]
- 💡 [[memoria/conocimiento/conceptos/segmentacion-software-software-pipelining-transforma-bucles|Segmentación software (software pipelining) transforma bucles con iteraciones dependientes en independientes]]
- 💡 [[memoria/conocimiento/conceptos/segmentacion-software-software-pipelining-y-planificacion-de|Segmentación software (software pipelining) y planificación de trazas (trace scheduling)]]
- 💡 [[memoria/conocimiento/conceptos/segmentacion-software-transforma-bucles-con-iteraciones-depe|Segmentación software transforma bucles con iteraciones dependientes en independientes (pregunta 12)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/tendencias-de-paralelismo-en-arquitectura-actual-ilp-tlp-dlp|Tendencias de paralelismo en arquitectura actual (ILP, TLP, DLP, multinúcleo)]]
- 💡 [[memoria/conocimiento/conceptos/tecnica-de-mejora-de-rendimiento-en-sisd|Técnica de mejora de rendimiento en SISD]]
- 💡 [[memoria/conocimiento/conceptos/tecnica-de-segmentacion-software-software-pipelining|Técnica de segmentación software (software pipelining)]]
- 💡 [[memoria/conocimiento/conceptos/tecnicas-ilp-estaticas-vs-dinamicas-pregunta-7-y-9|Técnicas ILP estáticas vs dinámicas (pregunta 7 y 9)]]
- 💡 [[memoria/conocimiento/conceptos/unidades-funcionales-y-ciclos-en-vliw-con-2-mem-2-fp-1-int-b|Unidades funcionales y ciclos en VLIW con 2 mem, 2 FP, 1 int/branch por ciclo]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/ventajas-e-inconvenientes-de-las-instrucciones-predicadas|Ventajas e inconvenientes de las instrucciones predicadas]] · ⚠️ propuesto

## Datos

- 📊 [[memoria/conocimiento/datos/limitaciones-del-paralelismo-en-bloques-basicos-y-solucion-a|Limitaciones del paralelismo en bloques básicos y solución a nivel de bucle]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[vliw]] · [[pipeline]] · [[planificacion]] · [[optimizacion]] · [[bucles]] · [[planificacion-estatica]] · [[dependencias]] · [[loop unrolling]] · [[superescalar]] · [[tomasulo]] · [[compilador]]
