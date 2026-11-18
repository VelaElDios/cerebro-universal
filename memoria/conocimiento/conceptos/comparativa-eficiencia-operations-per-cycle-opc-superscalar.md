---
tipo: "concepto"
titulo: "Comparativa eficiencia operations per cycle (OPC) superscalar vs VLIW en bucle desenrollado"
temas: ["ac", "examen", "pipeline", "superscalar", "vliw"]
claves: ["operations per cycle", "efficiency", "Processor A vs Processor B", "compare"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[pipeline]] · [[superscalar]] · [[vliw]]

OPC = total operaciones útiles (excluyendo nops/burbujas) / ciclos totales de ejecución del bucle desenrollado (4 iteraciones). Superscalar (A) limitado a 2 int + 2 FP/ciclo y emisión in-order por tipo; VLIW (B) 4 ops/ciclo sin restricción de tipo y reordenación libre. Se espera que B alcance OPC más alto (cercano a 4) al poder empaquetar mejor las operaciones FP de larga latencia (MUL.D 3 ciclos) con enteras y otras FP, mientras A sufre burbujas por restricción de 2 FP/ciclo y orden en programa. La respuesta debe dar OPC numérico para cada uno y declarar cuál es mejor.

> Calculate and compare the number of operations per cycle obtained for each processor. Which processor obtains the best efficiency in operations per cycle?
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[planificacion-en-vliw-4-operaciones-sin-restricciones-de-tip]] · [[comparativa-eficiencia-operaciones-ciclo-superscalar-con-res]] · [[metrica-de-comparacion-operaciones-por-ciclo-ipc-en-supersca]] · [[ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs]]
