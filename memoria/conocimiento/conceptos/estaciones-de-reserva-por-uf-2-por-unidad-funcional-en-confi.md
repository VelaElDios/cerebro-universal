---
tipo: "concepto"
titulo: "Estaciones de reserva por UF: 2 por unidad funcional en configuración examen"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["estaciones reserva", "2 por UF", "sumador", "multiplicador", "divisor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Cada unidad funcional (no cada tipo, sino cada instancia) tiene 2 estaciones de reserva. Con 2 sumadores → 4 estaciones ADD.D totales. 2 multiplicadores → 4 estaciones MUL.D totales. 1 divisor → 2 estaciones DIV.D totales. Esto permite emitir múltiples instrucciones del mismo tipo en paralelo si hay estaciones libres, evitando stalls estructurales por falta de estaciones de reserva.

> dispone de varias UF en coma flotante con 2 estaciones de reserva por UF
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf`

Relacionado: [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
