---
tipo: "fuente"
titulo: "Junio2014 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Junio2014.pdf`.

## Resumen
Este trozo contiene un examen completo de Arquitectura de Computadores (curso 2013/14) con 30 preguntas tipo test y dos problemas. El test cubre conceptos fundamentales: definición de arquitectura, métricas de rendimiento, ley de Amdahl, taxonomía de Flynn, hazards y dependencias, técnicas de ILP (desenrollamiento, planificación software, Tomasulo, predicción de saltos, especulación, ROB), arquitecturas superescalares/EPIC/GPU, y sistemas paralelos (NUMA, MPI, cloud). Los problemas plantean: (1) análisis de dependencias, CPI, desenrollado y planificación de un bucle vectorial MIPS64; (2) simul
Este trozo corresponde al Problema 3 del examen extraordinario de AC (curso 2013/14). Describe un procesador MIPS64 con especulación hardware mediante algoritmo de Tomasulo con especulación, detallando su configuración: ROB de 4 entradas, una estación de reserva por unidad funcional con 2 entradas cada una, buffer de carga de 2 entradas, UFs segmentadas (suma/resta, multiplicación, división) y latencias específicas. Incluye la restricción de que no se puede escribir en el BDC e iniciar ejecución de una operación esperando ese dato en el mismo ciclo. El problema pide: a) esquema hardware con in

## Lo que se sacó de él (17)
- [[bus-comun-de-datos-cdb-en-tomasulo-difunde-resultados-de-uf]]
- [[calculo-de-cpi-en-mips-multiciclo-con-mezcla-de-instruccione]]
- [[configuracion-tomasulo-con-especulacion-del-examen-ac-junio]]
- [[definicion-de-arquitectura-de-computador-visible-al-programa]]
- [[dependencias-de-nombre-se-eliminan-mediante-renombramiento-d]]
- [[desenrollado-de-bucles-replicar-mientras-se-reduzcan-detenci]]
- [[diferencia-escritura-resultado-vs-terminacion-commit-en-toma]]
- [[hazard-war-corresponde-a-antidependencia-dependencia-de-nomb]]
- [[latencias-de-ejecucion-uf-fp-en-examen-ac-junio-2014-problem]]
- [[mejor-metrica-de-rendimiento-tiempo-de-ejecucion]]
- [[planificacion-dinamica-tomasulo-orden-de-ejecucion-por-dispo]]
- [[planificacion-software-software-pipelining-transforma-iterac]]
- [[que-mostrar-en-esquema-hardware-tomasulo-con-especulacion-pa]]
- [[restriccion-de-forwarding-por-cdb-en-tomasulo-no-escritura-e]]
- [[rob-de-4-entradas-limita-ventana-de-instrucciones-en-vuelo-e]]
- [[secuencia-de-instrucciones-del-problema-3-examen-ac-junio-20]]
- [[speedup-por-ley-de-amdahl-con-mejora-10x-usada-20-del-tiempo]]
