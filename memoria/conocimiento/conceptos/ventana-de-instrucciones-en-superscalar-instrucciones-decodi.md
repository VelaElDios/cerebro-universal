---
tipo: "concepto"
titulo: "Ventana de instrucciones en superscalar: instrucciones decodificadas y renombradas no emitidas aún"
temas: ["ac", "issue", "superscalar", "ventana-instrucciones"]
claves: ["ventana instrucciones", "instruction window", "superscalar", "issue"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[issue]] · [[superscalar]] · [[ventana-instrucciones]]

La ventana de instrucciones (instruction window) es el buffer entre la fase de decode/rename y la de issue/dispatch. Contiene instrucciones ya decodificadas, renombradas (asignación de registros físicos) y esperando a que sus operandos y unidades funcionales estén listos para ser emitidas (issued) a las estaciones de reserva. No almacena solo accesos a memoria ni instrucciones ya confirmadas.

> The instruction window in a superscalar processor… b) Stores decoded and renamed instructions that have not been issued
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[paso-de-commit-en-superscalar-actualizacion-de-registros]]
