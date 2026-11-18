---
tipo: "fuente"
titulo: "Enero2015 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Enero2015.pdf`.

## Resumen
Este trozo contiene el examen ordinario de Arquitectura de Computadores de enero de 2015. Incluye un test de 30 preguntas sobre métricas de rendimiento (CPI, speedup, MIPS), dependencias e ILP, algoritmo de Tomasulo (con y sin especulación), predicción de saltos, arquitectura de procesadores modernos (Haswell, Cortex-A9, PowerPC), y modelos de computación paralela (Grid, Cluster, MPP, MPI). También presenta dos problemas: uno de análisis de pipeline y desenrollamiento de bucles en MIPS64, y otro de configuración de Tomasulo con especulación, ROB y estaciones de reserva.
Este trozo contiene dos problemas de un examen de Arquitectura de Computadores (curso 2014/15). El Problema 3 trata sobre especulación estática con poison bits en MIPS64: se da un código con cargas especulativas (LW*) y saltos, donde el acceso a la dirección de memoria 0 lanza excepción; hay que resolver dos casos (sin ayuda para especulación y con poison bits) indicando qué instrucciones lanzan excepción, si termina el programa y el estado final de registros. El Problema 4 es de planificación en un superescalar MIPS64 de 4 vías (2 enteras/memoria + 2 PF) con latencias dadas (suma PF 2 ciclos,

## Lo que se sacó de él (18)
- [[calculo-de-cpi-en-bucle-desenrollado-superescalar-con-ancho]]
- [[calculo-de-tiempo-de-ejecucion-con-cpi-ic-y-duracion-de-cicl]]
- [[como-resolver-el-problema-3-de-especulacion-con-poison-bits]]
- [[dependencias-de-nombre-war-waw-se-eliminan-con-renombramient]]
- [[desenrollado-6-y-renombrado-de-registros-pf-para-superescala]]
- [[especulacion-con-bits-venenosos-programa-continua-y-finaliza]]
- [[especulacion-estatica-con-poison-bits-en-mips64-lw]]
- [[estaciones-de-reserva-almacenan-etiquetas-para-control-de-ri]]
- [[estado-inicial-de-registros-y-memoria-para-problema-3-enero]]
- [[latencias-de-ejecucion-fp-en-superescalar-mips64-del-examen]]
- [[planificacion-superescalar-mips64-4-vias-con-latencias-pf-pr]]
- [[predictor-gselect-indexa-la-bht-con-xor-de-bits-del-pc-y-del]]
- [[salto-retardado-delayed-branch-en-planificacion-superescalar]]
- [[segmentacion-software-software-pipelining-transforma-bucles]]
- [[speedup-con-ley-de-amdahl-para-mejora-parcial-de-tarjeta-gra]]
- [[tomasulo-sin-especulacion-detenciones-en-escritura-por-riesg]]
- [[ventana-de-instrucciones-almacena-instrucciones-activas-deco]]
- [[waw-corresponde-a-dependencia-de-salida]]
