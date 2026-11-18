---
tipo: "fuente"
titulo: "Junio2018 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Junio2018.pdf`.

## Resumen
Este trozo contiene un examen de Arquitectura de Computadores (curso 2017/18) con 30 preguntas tipo test y dos problemas. El test cubre: ley de Amdahl, cálculo de tiempo de ejecución, conceptos de arquitectura, benchmarks, MFLOPS, dependencias y riesgos en pipeline, planificación estática/dinámica, algoritmos Scoreboard y Tomasulo, predicción de saltos (BHT, BTB, ROB, bits venenosos), superescalar, procesadores históricos (Itanium, PowerPC), GPUs, multithreading, computadores vectoriales y GRID. El Problema 1 analiza detenciones en un bucle MIPS64 con MUL.D (3 ciclos) y DIV.D (4 ciclos), pidie
Este trozo contiene el Problema 3 de un examen de Arquitectura de Computadores (curso 2017/18). Describe un bucle que procesa vectores A y B en un procesador superescalar de emisión dual (dos operaciones por ciclo, incluidas dos enteras), con una unidad funcional segmentada para suma PF y otra para multiplicación PF, dos unidades enteras de latencia 0, y retardo de salto ignorado. Se proporciona una tabla de latencias entre instrucciones productoras y consumidoras (PF ALU→PF ALU: 3 ciclos; PF ALU→S.D: 2; L.D→PF ALU: 1; L.D→S.D: 0). Se pide: A) desenrollar 4 veces y planificar para mínimo ciclo

## Lo que se sacó de él (20)
- [[analisis-de-dependencias-entre-instrucciones-de-punto-flotan]]
- [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]]
- [[bits-venenosos-excepcion-no-recuperable-marca-registro-desti]]
- [[btb-cache-de-direcciones-destino-de-saltos-con-bits-de-predi]]
- [[calculo-de-tiempo-de-ejecucion-con-cpi-y-mezcla-de-instrucci]]
- [[codigo-del-bucle-original-para-planificacion-examen-ac-2017]]
- [[como-calcular-ciclos-por-iteracion-en-codigo-original-con-la]]
- [[constantes-y-registros-del-bucle-f0-constante-r1-r2-punteros]]
- [[dependencias-raw-war-y-waw-en-el-bucle-de-producto-escalar-v]]
- [[formato-de-tabla-de-ayuda-para-planificacion-ciclo-emision-c]]
- [[metodo-para-calcular-speedup-de-bucle-desenrollado-y-planifi]]
- [[parametros-del-procesador-superescalar-en-problema-de-planif]]
- [[planificacion-estatica-el-compilador-reordena-para-reducir-d]]
- [[numero-de-tablas-bht-en-predictor-correlacionado-m-n]]
- [[problema-de-desenrollado-y-planificacion-de-bucle-superescal]]
- [[reorder-buffer-rob-permite-completacion-en-orden-en-ejecucio]]
- [[scoreboard-los-riesgos-estructurales-se-gestionan-en-la-etap]]
- [[supuestos-del-examen-retardo-de-salto-ignorado-y-unidades-en]]
- [[tabla-de-latencias-entre-instrucciones-productoras-y-consumi]]
- [[tomasulo-resultados-via-common-data-bus-cdb]]
