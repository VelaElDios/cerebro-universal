---
tipo: "receta"
titulo: "Simulación paso a paso de Tomasulo con especulación (tabla ciclos por etapa)"
temas: ["ac", "cdb", "reservation-station", "rob", "simulacion", "tomasulo"]
claves: ["Emisión", "Ejecución", "Escritura CDB", "Terminación (Commit)", "stalls por RS llena", "LB llena", "ROB llena", "dependencias RAW", "CDB conflict", "resource reuse next cycle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cdb]] · [[reservation-station]] · [[rob]] · [[simulacion]] · [[tomasulo]]

Metodología: Ciclo a ciclo. Etapa Emisión (Issue): asignar ROB, RS (si hay), LB (si load), renombrar registros (Qj/Qk). Stall si ROB lleno, RS llena (para tipo), LB lleno. Etapa Ejecución (Execute): esperar operandos (Vj/Vk o CDB), esperar UF libre. Iniciar EX cuando operandos listos y UF libre. Duración fija por tipo. Regla CDB: si resultado llega CDB en ciclo C, consumidor no empieza EX hasta C+1. Etapa Escritura (Write Result/CDB): broadcast resultado en CDB, actualizar RS/ROB/LB esperando. Etapa Terminación (Commit): in-order desde cabeza ROB. Store espera dato y dirección. Liberar recursos al final de Commit (disponibles ciclo siguiente). Rellenar tabla con ciclos inicio/fin y causas de stall (RAW, Estructural RS/LB/ROB/UF, CDB conflict).

> Detalla la ejecución de la secuencia de instrucciones mostrada en la siguiente tabla al emplear el algoritmo de Tomasulo con especulación. Para ello, en cada fila debes indicar el ciclo de inicio y de fin (en su caso) de cada etapa. Si alguna etapa debe detenerse durante uno o más ciclos, debes indicar claramente (en la celda correspondiente) la causa de esta detención.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[buffer-de-carga-en-tomasulo-especulativo]] · [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[pasos-para-simular-tomasulo-especulativo-con-rob-y-restricci]] · [[como-resolver-tabla-de-estado-en-tomasulo-con-rob-y-especula]] · [[como-abordar-la-simulacion-tomasulo-con-rob-para-examen-ac]]
