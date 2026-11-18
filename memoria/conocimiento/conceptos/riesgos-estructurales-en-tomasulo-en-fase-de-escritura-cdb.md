---
tipo: "concepto"
titulo: "Riesgos estructurales en Tomasulo en fase de escritura (CDB)"
temas: ["ac", "tomasulo"]
claves: ["Tomasulo", "riesgo estructural", "escritura", "CDB", "Bus Común de Datos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Aunque Tomasulo elimina riesgos estructurales en unidades funcionales mediante estaciones de reserva, el Bus Común de Datos (CDB) es un recurso compartido para escribir resultados. Si varias instrucciones terminan en el mismo ciclo, compiten por el CDB → riesgo estructural en fase de escritura.

> En la técnica de Tomasulo: a) Se pueden producir riesgos estructurales en la fase de escritura
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[riesgos-estructurales-en-tomasulo-solo-en-escritura-de-resul]] · [[tomasulo-sin-especulacion-detenciones-en-escritura-por-riesg]] · [[restriccion-cdb-mismo-ciclo-en-tomasulo-no-iniciar-ejecucion]]
