---
tipo: "concepto"
titulo: "Riesgos estructurales en Tomasulo solo en escritura de resultado"
temas: ["ac", "escritura", "estructurales", "riesgos", "tomasulo"]
claves: ["Tomasulo", "riesgo estructural", "fase escritura", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[escritura]] · [[estructurales]] · [[riesgos]] · [[tomasulo]]

En Tomasulo, las estaciones de reserva y el bus de datos común (CDB) evitan riesgos en lectura de operandos y ejecución. El único riesgo estructural posible es en la fase de escritura (Write Result) si varias unidades funcionales intentan emitir en el CDB simultáneamente; se resuelve con arbitraje de prioridad.

> En la técnica de Tomasulo: a) Se pueden producir riesgos estructurales en la fase de escritura
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]]
