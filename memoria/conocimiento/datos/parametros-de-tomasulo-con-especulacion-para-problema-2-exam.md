---
tipo: "dato"
titulo: "Parámetros de Tomasulo con especulación para Problema 2 (examen Junio 2026)"
temas: ["ac", "especulacion", "load-buffer", "reservation-station", "rob", "tomasulo"]
claves: ["fld/fsd 2 ciclos EX", "fmul.d 6 ciclos EX", "fadd.d/fsub.d 2 ciclos EX", "ROB 6 entradas", "1 UF add FP + 1 UF mul FP (segmentadas)", "2 RS por UF", "1 buffer carga", "CDB write conflict (espera 1 ciclo)", "recurso libre en ciclo siguiente"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[load-buffer]] · [[reservation-station]] · [[rob]] · [[tomasulo]]

Configuración completa para simulación Tomasulo: Latencias EX: Load/Store=2, FP Mul=6, FP Add/Sub=2. ROB: 6 entradas (permite hasta 6 instrucciones en vuelo). RS: 2 para FP Add, 2 para FP Mul. Load Buffer: 1 entrada (solo 1 carga en vuelo). Store Buffer: no especificado, asumir 1 o parte de ROB. Reglas críticas: 1) Resultado en CDB en ciclo T -> instrucción esperando ese dato no puede iniciar EX hasta T+1. 2) Recurso (RS, ROB, LB, UF) liberado en T -> disponible en T+1. Instrucciones: fld f0, fld f2, fadd.d f4, fsub.d f10, fmul.d f16, fadd.d f18, fsd f16.

> Sea un procesador RISC-V que usa especulación hardware y planificación dinámica de instrucciones mediante la técnica de Tomasulo con especulación, con las siguientes características: • La etapa de ejecución de fld y fsd emplea 2 ciclos. • La etapa de ejecución de fmul.d emplea 6 ciclos. • La etapa de ejecución de fadd.d y fsub.d emplea 2 ciclos. • Usa un buffer de reordenamiento (ROB) de 6 entradas. • Incluye una UF para suma/resta en PF y otra UF para multiplicación en PF. Ambas UF están completamente segmentadas. • Dispone de 2 estaciones de reserva por UF de PF. • Dispone de un buffer de carga de 1 entrada. • La etapa de ejecución de una instrucción que está esperando un resultado no puede comenzar en el mismo ciclo en el que se escribe el resultado en el CDB (Common Data Bus). • En general, cualquier recurso liberado en un ciclo de reloj no puede usarse hasta el siguiente.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffer-de-carga-en-tomasulo-especulativo-pregunta-18]] · [[bits-de-veneno-poison-bits-en-carga-especulativa-marcan-regi]] · [[simulacion-tomasulo-con-especulacion-parametros-de-hardware]] · [[parametros-de-simulacion-tomasulo-con-especulacion-del-exame]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]]
