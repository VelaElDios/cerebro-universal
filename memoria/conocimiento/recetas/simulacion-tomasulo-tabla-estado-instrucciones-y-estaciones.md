---
tipo: "receta"
titulo: "Simulación Tomasulo: tabla estado instrucciones y estaciones de reserva antes de escritura segundo L.D (Problema 2)"
temas: ["ac", "buffer almacenamiento", "buffer carga", "cdb", "estaciones reserva", "simulación", "tomasulo"]
claves: ["Tomasulo", "L.D", "MUL.D", "ADD.D", "SUB.D", "DIV.D", "S.D", "CDB", "buffer carga", "buffer almacenamiento", "ciclos ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[buffer almacenamiento]] · [[buffer carga]] · [[cdb]] · [[estaciones reserva]] · [[simulación]] · [[tomasulo]]

**Pasos para resolver:** 1) Listar instrucciones en orden: L.D F0,0(R1); MUL.D F4,F0,F2; L.D F0,8(R1); ADD.D F10,F6,F8; SUB.D F0,F10,F0; DIV.D F2,F4,F0; S.D F0,0(R2). 2) Recursos: 3 sumadores (2 ciclos), 2 multiplicadores/divisores (4/8 ciclos), 1 buffer carga (carga1), 1 buffer almacenamiento. 3) Regla: mismo ciclo no se puede escribir en CDB e iniciar ejecución que espera ese dato. 4) L.D y S.D tardan 2 ciclos en ejecución. 5) Rellenar tabla de estado (Emisión, Ejecución inicio/fin, Escritura resultado) simulando ciclo a ciclo con renombrado de registros (F0 se renombra en segundo L.D y en SUB.D). 6) Para estaciones de reserva en ciclo previo a escritura del segundo L.D: indicar Ocupada (SÍ/NO), Op, Vj, Vk, Qj, Qk para Suma1-3 y Mult1-2. Usar notación M(d) para contenido memoria y R(r) para contenido registro. **Clave:** el segundo L.D escribe en F0 (renombrado), liberando dependencias para MUL.D (espera F0) y SUB.D (espera F0). El DIV.D espera F4 (de MUL.D) y F0 (del segundo L.D).

> Problema 2... Muestra el contenido de la tabla de estado de instrucciones al finalizar la ejecución de todas las instrucciones del programa indicado. Indica en cada casilla de la tabla en qué ciclos de reloj comienza y finaliza cada fase... Indica en la siguiente tabla el estado de las estaciones de reserva en el ciclo anterior al ciclo de escritura del segundo L.D.
> — `repo:datos/temarios/AC/examenes/Noviembre2012.pdf` (cita sin comprobar)
