---
tipo: "receta"
titulo: "Cómo resolver tabla de estado en Tomasulo con ROB y especulación"
temas: ["ac", "pipeline", "prediccion-saltos", "tomasulo"]
claves: ["ROB", "buffer de reordenamiento", "Tomasulo especulativo", "CDB", "estaciones de reserva", "buffer de carga", "buffer de almacenamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]]

Pasos para rellenar la tabla de estado (Emisión, Ejecución, Escritura, Terminación) en Tomasulo con ROB:
1. **Emisión (Issue)**: En orden, una por ciclo si hay estación de reserva libre y entrada ROB libre. Se asigna entrada ROB, se renombra destino (apunta a ROB), se marcan operandos disponibles o se esperan tags de ROB.
2. **Ejecución (Execution)**: Empieza cuando operandos listos y UF libre. Duración = latencia de la UF. Para cargas/almacenas: 2 ciclos en etapa EX (cálculo dirección + acceso memoria). No se puede iniciar ejecución en el mismo ciclo que el dato llega por CDB (restricción del enunciado).
3. **Escritura (Write/CDB)**: Al terminar ejecución, se publica resultado en CDB (1 ciclo). Actualiza estaciones de reserva esperando ese tag y marca entrada ROB como completada (Valor listo). Si hay conflicto de CDB, prioridad típica: cargas > tiendas > FP ops.
4. **Terminación (Commit)**: En orden de programa, una por ciclo si entrada ROB en cabeza y ¿Terminada?=s. Escribe en registro arquitectónico / memoria. Libera entrada ROB.
Detalles clave del enunciado:
- ROB: 6 entradas (0-5)
- 1 Load Buffer, 1 Store Buffer (cada uno con su estación de reserva implícita)
- UF FP: Add/Sub (2 UF, 1 RS c/u, 2 ciclos), Mul (1 UF, 2 RS, 8 ciclos), Div (1 UF, 3 RS, 10 ciclos), resto 1 ciclo
- Restricción: mismo ciclo no se puede escribir en CDB e iniciar ejecución esperando ese dato
- Instrucciones: 2 L.D, ADD.D, MUL.D, L.D, ADD.D, 2 S.D
Para la tabla ROB en ciclo fin MUL.D: simular ciclo a ciclo hasta que MUL.D complete Escritura, volcar campos Entrada, Instrucción, Destino (registro arquitectónico o dirección memoria), Valor (tag o dato), ¿Terminada?.

> Se dispone de un procesador MIPS64 con especulación hardware según el método de Tomasulo con especulación y 6 entradas en el buffer de reordenamiento (ROB). El sistema dispone de un buffer de carga y un buffer de almacenamiento con 1 entrada.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-carga-en-tomasulo-especulativo]] · [[buffer-de-carga-en-tomasulo-especulativo-pregunta-18]] · [[pasos-para-rellenar-tabla-de-estado-de-instrucciones-emision]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[como-simular-tomasulo-especulativo-con-rob-de-4-entradas-y-l]]
