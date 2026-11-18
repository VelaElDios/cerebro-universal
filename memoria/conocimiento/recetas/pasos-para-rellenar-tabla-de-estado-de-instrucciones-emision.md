---
tipo: "receta"
titulo: "Pasos para rellenar tabla de estado de instrucciones (Emisión, Ejecución, Escritura, Terminación) en examen Tomasulo"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["tabla estado", "emisión", "ejecución", "escritura", "terminación", "ROB", "CDB", "estaciones de reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Procedimiento paso a paso para la tabla del apartado 2a (8 instrucciones × 4 columnas):
1. **Inicializar**: Ciclo 1. ROB vacío, RS libres, Load/Store Buffer libres, CDB libre.
2. **Bucle por ciclos** hasta que las 8 instr terminen Commit:
   - **Emisión (Issue)**: En orden, máx 1 instr/ciclo (típico en Tomasulo clásico, aunque superescalar podría emitir 2; enunciado no dice grado emisión, asumir 1 por simplicidad o seguir pista "6 entradas ROB" → 1 issue/ciclo). Condiciones: RS libre para tipo instr + entrada ROB libre. Asignar ROB#, renombrar destino → ROB#. Leer operandos: si en registro → valor; si pendiente → tag ROB#. Marcar ciclo Emisión.
   - **Inicio Ejecución**: Para cada RS con operandos listos (valores, no tags) y UF libre → empieza EX. **Regla CDB**: si en este ciclo alguien escribe CDB, los que esperaban ese dato NO pueden empezar EX este ciclo (empiezan siguiente). Marcar ciclo inicio Ejecución.
   - **Fin Ejecución / Escritura CDB**: Tras latencia EX (2 ciclos L.D/S.D, 2 ADD.D, 8 MUL.D, 10 DIV.D), instrucción pide CDB. Si CDB libre → escribe en ciclo T, marca ciclo Escritura = T. Actualiza RS esperando tag y ROB[#].Valor = dato, ROB[#].Terminada = s. Si CDB ocupado → espera (cola prioridad: cargas > stores > FP).
   - **Commit (Terminación)**: En orden ROB (cabeza). Si ROB[head].Terminada = s → escribe en registro/memoria, libera ROB, marca ciclo Terminación = ciclo actual. Si n → espera.
3. **Registrar ciclos**: Para cada instrucción, anotar ciclo en que **completa** cada etapa (Emisión, Ejecución, Escritura, Terminación). "Completa Ejecución" = fin de latencia EX, antes de CDB. "Completa Escritura" = ciclo CDB. "Completa Terminación" = ciclo Commit.
4. **Tabla final**: 8 filas × 4 columnas con números de ciclo.
Nota: Con 1 Load Buffer y 1 Store Buffer, L.D y S.D se serializan en emisión si buffer ocupado.

> Rellena el contenido de la tabla de estado de instrucciones al finalizar la ejecución de todas las instrucciones del programa, indicando los ciclos en los que se completa cada etapa.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[como-resolver-tabla-de-estado-en-tomasulo-con-rob-y-especula]] · [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[como-rellenar-la-tabla-de-estado-de-instrucciones-en-tomasul]] · [[pasos-para-simular-tomasulo-especulativo-con-rob-y-restricci]]
