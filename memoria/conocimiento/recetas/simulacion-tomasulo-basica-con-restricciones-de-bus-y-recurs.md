---
tipo: "receta"
titulo: "Simulación Tomasulo básica con restricciones de bus y recurso (examen Enero 2017)"
temas: ["ac", "simulacion", "tomasulo"]
claves: ["Tomasulo", "MIPS64", "L.D", "ADD.D", "SUB.D", "MUL.D", "CDB", "write-back", "resource reuse"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[simulacion]] · [[tomasulo]]

Parámetros del problema para simular a mano o programar un simulador:
- Procesador MIPS64 con planificación dinámica según Tomasulo (versión básica, sin especulación).
- Sin riesgos estructurales en estaciones de reserva ni buffers de carga.
- Latencias de ejecución: L.D = 2 ciclos; ADD.D = 3; SUB.D = 3; MUL.D = 7.
- Restricción de bus (CDB): la escritura de resultado (Write Result) no puede iniciarse en el mismo ciclo en que el dato aparece en el bus; debe esperar al siguiente ciclo.
- Restricción de reuso: una estación de reserva o buffer liberado en ciclo N solo puede asignarse a nueva instrucción en ciclo N+1.
- Código a simular (6 instrucciones):
  1. ADD.D F0,F2,F4
  2. L.D   F2,12(R2)
  3. SUB.D F4,F0,F2
  4. MUL.D F6,F4,F2
  5. ADD.D F6,F10,F8
  6. L.D   F4,20(R2)
- Salida requerida: tabla con ciclos de Emisión, Ejecución (inicio/fin), Escritura resultado.

> La ejecución de una instrucción que está esperando un resultado no puede comenzar en el mismo ciclo en el que este resultado es escrito en el Bus Común de Datos. Un recurso que es liberado en un ciclo de reloj no puede ser usado hasta el siguiente ciclo.
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[convencion-de-nomenclatura-en-tablas-de-tomasulo-del-temario]]
