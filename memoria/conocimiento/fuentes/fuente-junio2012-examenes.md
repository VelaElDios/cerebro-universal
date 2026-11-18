---
tipo: "fuente"
titulo: "Junio2012 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Junio2012.pdf`.

## Resumen
Este trozo contiene un examen extraordinario de Arquitectura de Computadores (junio 2012) con 30 preguntas de test teórico y tres problemas. El test cubre organización vs arquitectura, ley de Amdahl, taxonomía de Flynn, multithreading, MPI, riesgos de pipeline (RAW/WAR/WAW), dependencias, técnicas de marcador y Tomasulo, desenrollado de bucles, predicción de saltos (BHT, contadores saturados, predictores de dos niveles), especulación, buffer de reordenamiento, superescalares, VLIW y EPIC. Los problemas plantean una decisión de mejora vía ley de Amdahl y la planificación de un bucle vectorial e
Este trozo plantea un ejercicio de examen sobre el algoritmo de Tomasulo con especulación en un procesador MIPS64. Define la configuración completa: buffers de carga (2 entradas) y almacenamiento (1 entrada), unidades funcionales en coma flotante (2 sumadores/restadores de 2 ciclos, 2 multiplicadores de 6 ciclos, 1 divisor de 12 ciclos, cada una con 2 estaciones de reserva), bus común de datos (CDB) con restricción de no escritura e inicio de ejecución en el mismo ciclo, y una secuencia de 8 instrucciones (3 cargas, 2 ADD.D, 1 MUL.D, 2 almacenamientos). Pide completar la tabla de estado de ins

## Lo que se sacó de él (17)
- [[configuracion-de-tomasulo-con-especulacion-para-examen-ac-ju]]
- [[cpi-con-tecnica-parar-siempre-en-saltos-cpi-1-saltos-tomados]]
- [[definicion-de-antidependencia-j-escribe-sobre-un-registro-qu]]
- [[en-la-taxonomia-de-flynn-los-multicomputadores-son-maquinas]]
- [[en-tomasulo-sin-especulacion-la-emision-se-detiene-ante-ries]]
- [[estaciones-de-reserva-por-uf-2-por-unidad-funcional-en-confi]]
- [[la-bht-almacena-los-bits-de-prediccion-de-todas-las-instrucc]]
- [[latencias-de-ejecucion-fp-en-configuracion-examen-junio-2012]]
- [[ley-de-amdahl-la-aceleracion-maxima-viene-determinada-por-la]]
- [[mpi-proporciona-herramientas-para-comunicar-procesos-en-dist]]
- [[parametros-estandar-para-simular-tomasulo-con-especulacion-e]]
- [[penalizacion-de-salto-condicional-en-pipeline-de-5-etapas-re]]
- [[restriccion-de-cdb-en-tomasulo-no-escritura-e-inicio-simulta]]
- [[riesgo-entre-add-d-f4-f2-f0-y-s-d-f0-0-r1-es-war-antidepende]]
- [[rob-de-10-entradas-para-secuencia-de-8-instrucciones-en-exam]]
- [[se-pueden-solapar-iteraciones-de-un-bucle-si-no-hay-dependen]]
- [[secuencia-de-instrucciones-mips64-del-examen-junio-2012-toma]]
