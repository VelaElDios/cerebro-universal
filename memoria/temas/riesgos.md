---
tipo: "tema"
titulo: "riesgos"
notas: 22
---
# riesgos

Nodo del mapa del Cerebro con todo lo que se sabe de «riesgos» (este archivo se genera solo).

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/antidependencia-war-y-dependencia-de-salida-waw-definiciones|Antidependencia (WAR) y dependencia de salida (WAW) definiciones]]
- 💡 [[memoria/conocimiento/conceptos/definicion-de-riesgo-raw-read-after-write|Definición de riesgo RAW (Read After Write)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/dependencia-de-datos-en-pipeline-riesgo-solo-si-instruccione|Dependencia de datos en pipeline → riesgo solo si instrucciones están cerca]]
- 💡 [[memoria/conocimiento/conceptos/dependencia-de-salida-waw-dos-instrucciones-escriben-mismo-r|Dependencia de salida (WAW): dos instrucciones escriben mismo registro/memoria]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/dependencias-en-bucle-mips-de-carga-modificacion-almacenamie|Dependencias en bucle MIPS de carga-modificación-almacenamiento (LW, DADD, SW, DADDUI, BNEZ)]]
- 💡 [[memoria/conocimiento/conceptos/deteccion-de-riesgos-war-y-waw-en-marcador-y-bloqueo-de-escr|Detección de riesgos WAR y WAW en marcador y bloqueo de escritura]]
- 💡 [[memoria/conocimiento/conceptos/gestion-de-riesgos-war-y-waw-en-tomasulo-pregunta-10|Gestión de riesgos WAR y WAW en Tomasulo (pregunta 10)]]
- 💡 [[memoria/conocimiento/conceptos/las-dependencias-de-datos-no-siempre-generan-riesgos-y-se-el|Las dependencias de datos no siempre generan riesgos y se eliminan con renombramiento]]
- 💡 [[memoria/conocimiento/conceptos/obtencion-de-operandos-y-deteccion-waw-war-en-scoreboard|Obtención de operandos y detección WAW/WAR en Scoreboard]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/problemas-en-segmentacion-de-coma-flotante-riesgos-estructur|Problemas en segmentación de coma flotante: riesgos estructurales RAW WAW y finalización fuera de orden]]
- 💡 [[memoria/conocimiento/conceptos/proposito-de-la-planificacion-por-software-software-pipelini|Propósito de la planificación por software (software pipelining) (pregunta 8)]]
- 💡 [[memoria/conocimiento/conceptos/riesgo-load-use-en-pipeline-mips-con-forwarding|Riesgo load-use en pipeline MIPS con forwarding]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/riesgo-raw-como-dependencia-de-datos-verdadera|Riesgo RAW como dependencia de datos verdadera]]
- 💡 [[memoria/conocimiento/conceptos/riesgo-war-dependencia-antidependencia-datos|Riesgo WAR = dependencia antidependencia (datos)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/riesgos-estructurales-en-tomasulo-solo-en-escritura-de-resul|Riesgos estructurales en Tomasulo solo en escritura de resultado]]
- 💡 [[memoria/conocimiento/conceptos/riesgos-resueltos-por-marcador-y-por-tomasulo-sin-especulaci|Riesgos resueltos por Marcador y por Tomasulo sin especulación]]
- 💡 [[memoria/conocimiento/conceptos/tipos-de-riesgos-en-pipeline-estructurales-datos-control|Tipos de riesgos en pipeline: estructurales, datos, control]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/tres-tipos-de-dependencias-en-codigo-datos-nombre-y-control|Tres tipos de dependencias en código: datos, nombre y control]]
- 💡 [[memoria/conocimiento/conceptos/tecnica-de-marcador-scoreboard-riesgos-war-waw-obligan-a-det|Técnica de Marcador (Scoreboard): riesgos WAR/WAW obligan a detener]]

## Datos

- 📊 [[memoria/conocimiento/datos/analisis-de-dependencias-en-codigo-fp-con-registro-f1-raw-y|Análisis de dependencias en código FP con registro F1 (RAW y WAW)]]
- 📊 [[memoria/conocimiento/datos/riesgo-entre-add-d-f4-f2-f0-y-s-d-f0-0-r1-es-war-antidepende|Riesgo entre ADD.D F4,F2,F0 y S.D F0,0(R1) es WAR (antidependencia)]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/riesgo-war-antidependencia-entre-sub-d-f10-f8-f6-y-l-d-f6-0|Riesgo WAR (antidependencia) entre SUB.D F10,F8,F6 y L.D F6,0(R1)]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[pipeline]] · [[dependencias]] · [[war]] · [[waw]] · [[tomasulo]] · [[scoreboard]] · [[dependencias datos]] · [[arquitectura]] · [[hazard]] · [[renombramiento]] · [[coma-flotante]]
