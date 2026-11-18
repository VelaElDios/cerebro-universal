---
tipo: "fuente"
titulo: "June2025 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/June2025.pdf`.

## Resumen
Este trozo contiene el examen final de Arquitectura de Computadores (junio 2025) con 30 preguntas tipo test y dos ejercicios prácticos. El test cubre: métricas de rendimiento (ley de Amdahl, speedup, coste-efectividad), pipeline MIPS (etapas, hazards, dependencias), técnicas de planificación (Scoreboard, Tomasulo, estática/dinámica), predicción de saltos (BTB, BHT, predictores 1-bit y correlacionados), arquitecturas superscalar/VLIW, jerarquía de memoria (caché L1 separada, UMA/NUMA, chiplets), unidades de rendimiento (Flops), multihilo, TPUs y modelos cloud. Los ejercicios requieren análisis 
Este trozo contiene el Ejercicio 3 de un examen de Arquitectura de Computadores (junio 2025). La Sección A pide rellenar tablas de ejecución para planificación estática con bits venenosos («dirty» para registros envenenados, «prohibited» para direcciones inválidas) en dos casos con distintos valores iniciales de R1 (0 y 5), indicando si se lanza excepción. La Sección B pide detallar la ejecución en Tomasulo con especulación para cuatro instrucciones (L.D, L.D, ADD.D, S.D) con restricciones concretas: ROB 32 entradas, load buffer 16, 2 estaciones de suma y 4 de multiplicación/división, latencia

## Lo que se sacó de él (17)
- [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]]
- [[arquitectura-que-implementa-instrucciones-predicadas-de-form]]
- [[calculo-de-ciclos-de-penalizacion-por-salto-tomado-en-pipeli]]
- [[calculo-de-coste-efectividad-entre-dos-sistemas-con-carga-de]]
- [[calculo-de-speedup-con-ley-de-amdahl-en-pregunta-de-examen]]
- [[como-rellenar-tabla-de-ejecucion-con-bits-venenosos-casos-r1]]
- [[condicion-necesaria-para-que-la-especulacion-sea-valida]]
- [[definicion-de-dependencia-de-nombre-name-dependency-entre-in]]
- [[diferencia-scoreboard-vs-tomasulo-en-resolucion-de-hazards-s]]
- [[estructura-que-almacena-direccion-destino-de-saltos-tomados]]
- [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]]
- [[instrucciones-especulativas-marcadas-con-en-codigo-mips64-ex]]
- [[parametros-de-recursos-y-latencias-para-tomasulo-con-especul]]
- [[pasos-para-completar-tabla-de-ejecucion-tomasulo-issue-execu]]
- [[planificacion-estatica-con-bits-venenosos-convencion-dirty-p]]
- [[regla-de-contencion-del-cdb-y-disponibilidad-de-recursos-en]]
- [[valores-iniciales-de-memoria-y-registros-para-los-dos-casos]]
