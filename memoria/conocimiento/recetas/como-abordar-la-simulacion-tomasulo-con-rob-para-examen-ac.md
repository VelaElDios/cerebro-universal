---
tipo: "receta"
titulo: "Cómo abordar la simulación Tomasulo con ROB para examen AC"
temas: ["ac", "bdc", "estaciones-reserva", "examen", "rob", "simulacion", "tomasulo"]
claves: ["emisión", "ejecución", "escritura resultado", "terminación", "ROB vacío", "ciclos", "tabla"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bdc]] · [[estaciones-reserva]] · [[examen]] · [[rob]] · [[simulacion]] · [[tomasulo]]

Pasos para resolver: 1) Listar instrucciones en orden de programa. 2) Simular ciclo a ciclo: Emisión (asignar entrada ROB y estación de reserva/buffer si hay hueco; renombrar registros destino con etiqueta ROB), Ejecución (esperar operandos y unidad libre; respetar latencias y segmentación), Escritura resultado (en BDC; 1 ciclo; avisa a dependientes y marca ROB listo), Terminación (commit en orden de programa; libera ROB y escribe en registro arquitectónico si es cabeza de ROB). 3) Aplicar restricciones: no escribir BDC e iniciar ejecución esperando ese dato en mismo ciclo; recurso liberado en ciclo N usable en N+1. 4) Para parte b), volcar contenido ROB (entrada, instrucción, destino, valor/etiqueta, estado) en el ciclo que termina MUL.D F2,F4,F0.

> Rellena la siguiente tabla, indicando los ciclos en los que se completa cada etapa y suponiendo que el ROB está inicialmente vacío. Instrucción Emisión Ejecución Escritura resultado Terminación
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf`

Relacionado: [[configuracion-hardware-tomasulo-con-especulacion-para-examen]] · [[restricciones-de-uso-del-bus-de-datos-comun-y-recursos-en-to]] · [[latencias-y-segmentacion-de-unidades-funcionales-en-examen-t]] · [[simulacion-paso-a-paso-de-tomasulo-con-especulacion-tabla-ci]] · [[pasos-para-simular-tomasulo-especulativo-con-rob-y-restricci]] · [[como-simular-tomasulo-especulativo-con-rob-de-4-entradas-y-l]]
