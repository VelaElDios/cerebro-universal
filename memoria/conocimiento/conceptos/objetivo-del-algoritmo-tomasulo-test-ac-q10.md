---
tipo: "concepto"
titulo: "Objetivo del algoritmo Tomasulo (test AC Q10)"
temas: ["ac", "ejecucion-fuera-orden", "renombrado", "tomasulo"]
claves: ["tomasulo", "estacion-reserva", "renombrado-registros", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ejecucion-fuera-orden]] · [[renombrado]] · [[tomasulo]]

El **algoritmo Tomasulo** (IBM 360/91) añade **renombrado de registros vía estaciones de reserva** y **bus común de datos (CDB)** al Marcador. Permite:
- **Ejecución fuera de orden** real: instrucciones independientes pasan adelante de las que esperan operandos.
- **Eliminación de riesgos WAR y WAW** (falsas dependencias) gracias al renombrado.
- **Adelantamiento (forwarding)** automático por broadcast en el CDB.
La estación de reserva guarda la operación, los operandos (valor o tag de la RS que lo producirá) y espera a que ambos estén listos.

> La técnica de Tomasulo se usa para… Permitir que las instrucciones independientes adelanten a las instrucciones que estén en espera
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)

Relacionado: [[en-tomasulo-sin-especulacion-la-emision-se-detiene-ante-ries]] · [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[tomasulo-sin-especulacion-detenciones-en-escritura-por-riesg]]
