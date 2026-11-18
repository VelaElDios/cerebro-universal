---
tipo: "concepto"
titulo: "Contenido de una estación de reserva en Tomasulo (test AC Q11)"
temas: ["ac", "estacion-reserva", "tomasulo"]
claves: ["estacion-reserva", "reservation-station", "operandos", "tags", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[estacion-reserva]] · [[tomasulo]]

Cada **estación de reserva (RS)** almacena una instrucción emitida que espera a ejecutarse. Campos típicos:
- `Op`: operación a realizar.
- `Qj`, `Qk`: tags de las RS que producirán los operandos (0 si ya disponible).
- `Vj`, `Vk`: valores de los operandos (cuando `Q`=0).
- `Busy`: indica si la RS está ocupada.
- `A`: campo de dirección para carga/almacenamiento (cálculo efectivo).
Cuando `Qj=Qk=0`, la RS está lista para enviar a la unidad funcional.

> En la técnica Tomasulo, una estación de reserva contiene… Las instrucciones emitidas y que están esperando su ejecución
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)
