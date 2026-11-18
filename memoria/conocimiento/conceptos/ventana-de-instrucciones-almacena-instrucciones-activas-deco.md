---
tipo: "concepto"
titulo: "Ventana de instrucciones almacena instrucciones activas, decodificadas pero no finalizadas"
temas: ["ac", "superscalar", "ventana de instrucciones"]
claves: ["ventana de instrucciones", "instruction window", "instrucciones activas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[superscalar]] · [[ventana de instrucciones]]

La ventana de instrucciones (instruction window) en procesadores superscalares fuera de orden contiene todas las instrucciones que han sido decodificadas y renombradas, esperando a que sus operandos estén listos para ser emitidas a las unidades funcionales. Incluye instrucciones en estaciones de reserva, ROB, etc., que aún no han completado su ejecución.

> La ventana de instrucciones: a) Almacena instrucciones activas, decodificadas pero no finalizadas b) Almacena las instrucciones de acceso a memoria (ld, sd) según el orden del programa c) Almacena instrucciones que se han decodificado y renombrado peno no se han emitido d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[ventana-de-instrucciones-en-superscalar-instrucciones-decodi]] · [[paso-de-commit-en-superscalar-actualizacion-de-registros]] · [[uso-de-ranura-de-retardo-de-1-ciclo-en-superescalar-para-ocu]]
