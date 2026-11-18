---
tipo: "receta"
titulo: "Identificación de dependencia RAW entre ADD.S consecutivas por registro destino/fuente"
temas: ["ac", "dependencias", "mips", "pipeline", "punto-flotante", "raw"]
claves: ["ADD.S", "F4", "F3", "dependencia", "RAW", "hazard", "UF FP suma"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014B.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[mips]] · [[pipeline]] · [[punto-flotante]] · [[raw]]

I2 escribe F4 (destino), I3 lee F4 (fuente) → dependencia RAW (Read After Write) verdadera. Como la UF FP suma tarda 2 ciclos y hay forwarding, I3 debe esperar a que I2 produzca F4. Si I2 está en EX1, I3 en ID, hay hazard RAW que forwarding resuelve cuando I2 termina EX2 y pone resultado en CDB/registro.

> ADD.S F4, F3, F3 ; I2 ... ADD.S F5, F4, F3 ; I3 ... Entre la instrucción I2 e I3 a través de F4 existe: b) Una dependencia de datos que provoca un riesgo RAW
> — `repo:datos/temarios/AC/examenes/Noviembre2014B.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
