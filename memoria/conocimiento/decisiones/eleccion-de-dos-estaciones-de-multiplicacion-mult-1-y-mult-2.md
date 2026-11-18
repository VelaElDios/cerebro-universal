---
tipo: "decision"
titulo: "Elección de dos estaciones de multiplicación (Mult 1 y Mult 2) para solapar iteraciones"
temas: ["ac", "diseno", "estaciones reserva", "paralelismo", "tomasulo"]
claves: ["Mult 1", "Mult 2", "Suma 1 2 3", "grado paralelismo", "structural hazard"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[diseno]] · [[estaciones reserva]] · [[paralelismo]] · [[tomasulo]]

El diseño incluye **dos estaciones de multiplicación (Mult 1 y Mult 2)** y tres de suma (Suma 1-3, inactivas). Esto permite tener dos multiplicaciones en vuelo simultáneamente (una por iteración), eliminando riesgos estructurales cuando la latencia de carga (9 ciclos) supera la tasa de emisión (una iteración cada ~4 ciclos: emisiones en ciclos 1, 2, 3 y 6, 7, 8). Si solo hubiera un multiplicador, la segunda fmul.d esperaría en cola de emisión, reduciendo IPC. La simulación muestra Mult 1 procesando iteración 1 (ciclos 10-15) y Mult 2 iteración 2 (ciclos 10-15 en paralelo).

> Estaciones de reserva Nombre Ocupada Op Vj Vk Qj Qk Mult 1 SI Mult R(f2) Carga 1 Mult 2 SI Mult R(f2) Carga 2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[asignacion-de-estaciones-de-reserva-mult-1-y-mult-2-en-el-ej]] · [[como-evoluciona-la-tabla-de-estaciones-de-reserva-en-tomasul]] · [[como-se-traza-la-ejecucion-ciclo-a-ciclo-en-el-algoritmo-de]]
