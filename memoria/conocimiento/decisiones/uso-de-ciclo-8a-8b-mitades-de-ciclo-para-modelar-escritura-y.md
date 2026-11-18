---
tipo: "decision"
titulo: "Uso de «ciclo 8a / 8b» (mitades de ciclo) para modelar escritura y emisión en mismo ciclo"
temas: ["ac", "arquitectura", "ciclo", "modelo-temporal", "scoreboard", "simulacion"]
claves: ["ciclo 8a", "ciclo 8b", "mitad", "escritura", "emisión", "mismo ciclo", "marcador"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[ciclo]] · [[modelo-temporal]] · [[scoreboard]] · [[simulacion]]

El documento divide el **ciclo 8 en dos mitades (8a y 8b)** para representar eventos que ocurren en el mismo ciclo de reloj pero en distinta fase:

- **8a (primera mitad)**: se muestra la **emisión de `fdiv.d`** (columna Emisión = 8) y el estado de UF **antes** de que las escrituras de resultados del ciclo anterior propaguen banderas Rj/Rk. Las UF Mult1 y Suma aún tienen Rj/Rk = NO/SI.
- **8b (segunda mitad)**: **después** de la escritura de resultados (Write Result) del ciclo 7-8, las banderas Rj/Rk se actualizan a SI en Mult1 y Suma, permitiendo que lean operandos en el siguiente ciclo (9). La UF Entera queda libre (Ocupada=NO).

Esta convención de «mitad de ciclo» es un truco didáctico para **separar la fase de escritura de resultados (WB) de la fase de emisión/lectura (ID/IS)** dentro de un mismo ciclo de reloj, evitando ambigüedad sobre si una instrucción puede leer un registro que otra escribe en el mismo ciclo. En hardware real esto se resuelve con bypass/forwarding o escritura en flanco descendente y lectura en flanco ascendente.

> ciclo 8a 1ª mitad Instrucción Emisión Operandos completa resultado fdiv.d f10, f0, f6 8 ciclo 8b 2ª mitad Instrucción Emisión Operandos completa resultado
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]] · [[como-leer-la-evolucion-ciclo-a-ciclo-de-un-marcador-con-carg]] · [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]] · [[representacion-del-estado-del-marcador-scoreboard-para-instr]]
