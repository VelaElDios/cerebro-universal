---
tipo: "concepto"
titulo: "Gestión de buffers de carga/almacenamiento con direcciones decrecientes"
temas: ["ac", "buffer almacenamiento", "buffer carga", "direccionamiento", "tomasulo"]
claves: ["Carga 1 2 3", "Almac 1 2 3", "direccion efectiva", "x1", "stride 8"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[buffer almacenamiento]] · [[buffer carga]] · [[direccionamiento]] · [[tomasulo]]

Los buffers de carga y almacenamiento se asignan en orden de emisión y se liberan tras escribir/leer en memoria:
- **Cargas**: Carga 1 (dir 80) emitida ciclo 1, libre en ciclo 10; Carga 2 (dir 72) emitida ciclo 6, libre en ciclo 11; Carga 3 (dir 64) emitida ciclo 10, activa hasta ciclo 15.
- **Almacenes**: Almac 1 (dir 80) y Almac 2 (dir 72) quedan "Ocupada=SI" durante toda la simulación (ciclos 9-15) esperando el dato de fmul.d (Qi "Mult 1" y "Mult 2"). Almac 3 nunca se usa (solo 2 iteraciones en vuelo).
La dirección efectiva = x1 + offset (0). x1 vale 72 al inicio (ciclo 9) y 64 desde ciclo 10, confirmando decremento de 8 bytes por iteración (sizeof(double)).

> Buffers de carga/almac. Nombre Ocupada Direc. Qi Carga 1 SI 80 Carga 2 SI 72 Almac 1 SI 80 Almac 2 SI 72
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
