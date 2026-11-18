---
tipo: "dato"
titulo: "Configuración del procesador para el ejercicio de desenrollado (AC June 2018)"
temas: ["ac", "pipeline", "processor-config"]
claves: ["1 FP adder", "1 FP multiplier", "2 integer units", "latency 0", "ignore branch delay"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[processor-config]]

Procesador con: 1 unidad funcional completamente en tubería para suma FP (ADD.D), 1 para multiplicación FP (MUL.D), 2 unidades enteras (para DADDUI, SLTI, BEQZ) con latencia 0 ciclos, y se ignora el retardo del salto (branch delay = 0). Esto permite emitir instrucciones enteras sin conflictos estructurales y sin penalización por salto.

> Assume the following processor characteristics:   •   1 completely pipelined functional unit per floating point operation type (addition and multiplication)   •   2 integer functional units, with a latency of 0   •   We ignore the branch delay
> — `repo:datos/temarios/AC/examenes/June2018.pdf`
