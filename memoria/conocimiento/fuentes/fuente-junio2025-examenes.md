---
tipo: "fuente"
titulo: "Junio2025 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Junio2025.pdf`.

## Resumen
Este trozo contiene un examen completo de Arquitectura de Computadores (convocatoria extraordinaria junio 2025) con 30 preguntas tipo test y 2 problemas de desarrollo. El test cubre: ley de Amdahl, benchmarks, pipeline MIPS, dependencias, Marcador/Tomasulo, planificación estática/dinámica, predicción de saltos, especulación, superescalar, VLIW, multicore UMA/NUMA, chiplets, TPUs y modelos cloud. Los problemas requieren análisis de riesgos en bucle con coma flotante (L.D, ADD.D, S.D) y simulación de predictores de 1-bit sobre una secuencia de saltos alternantes.
Este trozo contiene tres ejercicios de arquitectura de computadores: (1) cálculo de tasa de acierto de un predictor correlacionado (1,2) con historial de saltos y tablas BHT inicializadas a "no tomado fuerte"; (2) ejecución con planificación estática y poison bits en MIPS64 para dos casos iniciales distintos, marcando registros "sucios" y direcciones "prohibidas"; (3) simulación detallada de Tomasulo con especulación para cuatro instrucciones (dos cargas, una suma FP, un store), con restricciones de ciclos por unidad funcional, contención del CDB y liberación de recursos al ciclo siguiente.

## Lo que se sacó de él (17)
- [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]]
- [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]]
- [[calculo-de-speedup-con-desenrollamiento-de-bucle-y-superesca]]
- [[como-calcular-instrucciones-vliw-necesarias-para-codigo-inde]]
- [[como-calcular-speedup-global-mejorando-un-componente-ley-de]]
- [[como-comparar-efectividad-en-coste-entre-dos-sistemas]]
- [[definicion-de-dependencia-de-nombre-anti-y-salida]]
- [[instrucciones-especulativas-marcadas-con-asterisco-en-codigo]]
- [[penalizacion-de-salto-tomado-con-condicion-en-ex-y-direccion]]
- [[planificacion-estatica-con-poison-bits-en-mips64-reglas-de-e]]
- [[planificacion-estatica-el-compilador-reordena-para-reducir-d]]
- [[predictor-correlacionado-1-2-con-bhr-y-dos-bhts]]
- [[rellenar-tabla-de-ejecucion-tomasulo-columnas-issue-executio]]
- [[restriccion-de-uso-del-cdb-y-liberacion-de-recursos-en-tomas]]
- [[riesgos-resueltos-por-marcador-y-por-tomasulo-sin-especulaci]]
- [[simulacion-tomasulo-con-especulacion-parametros-de-hardware]]
- [[tabla-de-iteraciones-para-calculo-de-tasa-de-acierto-en-pred]]
