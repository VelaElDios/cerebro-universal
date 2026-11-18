---
tipo: "fuente"
titulo: "Enero2016 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Enero2016.pdf`.

## Resumen
Examen de Arquitectura de Computadores (Enero 2016) con 30 preguntas tipo test y un problema de desenrollamiento de bucles en MIPS64. Cubre CPI, ley de Amdahl, arquitectura vs organización, VLIW, dependencias de datos (RAW, WAR, WAW), renombramiento, planificación estática, Tomasulo, segmentación software, predictores de dos niveles, BTAC, gselect, especulación con ROB y poison bits, superescalar, ARM, potencia, multicore, taxonomía de Flynn, cloud, SMP/UMA y TLP.
Este trozo contiene dos problemas de un examen de Arquitectura de Computadores (curso 2015/16). El primero pide simular la ejecución de 10 instrucciones MIPS64 en un procesador con especulación hardware según Tomasulo, detallando ciclos por etapa (emisión, ejecución, escritura resultado, terminación) y el contenido del ROB en un ciclo concreto. El segundo problema requiere planificar código para un procesador VLIW de 4 operaciones por instrucción, desenrollando 4 veces un bucle con 10 instrucciones, y calcular operaciones por ciclo.

## Lo que se sacó de él (18)
- [[analisis-de-dependencias-en-bucle-mips-con-acceso-a-memoria]]
- [[aplicacion-de-la-ley-de-amdahl-para-mejora-de-coma-flotante]]
- [[calculo-de-tiempo-de-ejecucion-con-cpi-y-frecuencia]]
- [[caracteristicas-del-procesador-vliw-del-examen-enero-2016-pr]]
- [[codigo-del-bucle-y-valores-iniciales-de-registros-para-vliw]]
- [[como-abordar-la-simulacion-tomasulo-con-rob-para-examen-ac]]
- [[configuracion-hardware-tomasulo-con-especulacion-para-examen]]
- [[definicion-de-dependencia-de-datos-raw-entre-instrucciones]]
- [[definicion-de-procesador-vliw]]
- [[diferencia-entre-arquitectura-y-organizacion-de-computadores]]
- [[eliminacion-de-dependencias-de-nombre-mediante-renombramient]]
- [[latencias-y-segmentacion-de-unidades-funcionales-en-examen-t]]
- [[parametros-temporales-de-pipeline-para-vliw-problema-3b]]
- [[planificacion-estatica-de-instrucciones-la-hace-el-compilado]]
- [[restricciones-de-uso-del-bus-de-datos-comun-y-recursos-en-to]]
- [[riesgos-estructurales-en-tomasulo-solo-en-escritura-de-resul]]
- [[secuencia-de-instrucciones-mips64-para-simulacion-tomasulo-p]]
- [[waw-corresponde-a-dependencia-de-salida]]
