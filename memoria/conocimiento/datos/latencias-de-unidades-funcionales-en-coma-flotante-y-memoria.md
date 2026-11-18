---
tipo: "dato"
titulo: "Latencias de unidades funcionales en coma flotante y memoria en Tomasulo con especulación"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ADD.D 3 ciclos", "SUB.D 3 ciclos", "MUL.D 5 ciclos", "DIV.D 8 ciclos", "L.D/S.D 2 ciclos", "UF segmentadas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Latencias de ejecución (ciclos de reloj) para la simulación: - Carga (L.D) y Almacenamiento (S.D): 2 ciclos en etapa EX (cálculo dirección + acceso memoria). - ADD.D / SUB.D: 3 ciclos en UF suma/resta (segmentada). - MUL.D: 5 ciclos en UF multiplicación (segmentada). - DIV.D: 8 ciclos en UF división (segmentada). - "El resto 1 ciclo": probablemente instrucciones enteras o movimiento. Las UFs están segmentadas (pipelined), por lo que pueden aceptar nueva operación cada ciclo si no hay hazard estructural. La emisión (issue) toma 1 ciclo, escritura resultado (write result) 1 ciclo, terminación (commit) 1 ciclo.

> • La etapa de ejecución de una carga y de un almacenamiento emplea 2 ciclos de reloj. • Las UFs en coma flotante están segmentadas, teniendo 1 UF para suma/resta, 1 UF para la multiplicación y 1 UF para división. • La etapa de ejecución para las instrucciones ADD.D y SUB.D emplean 3 ciclos, 5 ciclos para MUL.D, 8 ciclos para DIV.D y el resto 1 ciclo.
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[buffer-de-carga-en-tomasulo-especulativo]]
