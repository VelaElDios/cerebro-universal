---
tipo: "concepto"
titulo: "Dependencia de datos en pipeline → riesgo solo si instrucciones están cerca"
temas: ["ac", "dependencias datos", "pipeline", "riesgos"]
claves: ["dependencia datos", "riesgo datos", "pipeline", "distancia instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias datos]] · [[pipeline]] · [[riesgos]]

Una dependencia (RAW real) solo se convierte en riesgo (hazard) si la instrucción consumidora alcanza la etapa de lectura de operandos antes de que la productora haya escrito el resultado. Con forwarding (adelantamiento) se reduce la ventana de riesgo; si la distancia en ciclos ≥ latencia de la unidad funcional + forwarding, no hay parada.

> La existencia de una dependencia de datos entre dos instrucciones ejecutadas en un procesador segmentado: a) Puede provocar un riesgo de datos si las instrucciones están suficientemente cerca
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
