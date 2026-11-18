---
tipo: "concepto"
titulo: "Procesador Tomasulo con especulación - características de latencia y recursos (examen enero 2025)"
temas: ["ac", "especulacion", "tomasulo"]
claves: ["latencia carga/almacén 1 ciclo", "FP mul 5 ciclos", "FP add 2 ciclos", "CDB exclusivo", "recurso liberado no reutilizable hasta siguiente ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[tomasulo]]

Reglas clave para la simulación: 1) Etapa de ejecución de carga/almacén = 1 ciclo. 2) Multiplicación FP = 5 ciclos. 3) Suma FP = 2 ciclos. 4) CDB: solo una escritura por ciclo; si hay conflicto, la instrucción espera (peligro estructural). 5) Recurso liberado en ciclo N no puede ser usado hasta ciclo N+1. 6) Especulación hardware + planificación dinámica Tomasulo. 7) Las instrucciones pasan por Issue, Execution, Write (CDB), Commit. En la tabla se anota ciclo inicio y fin de cada etapa y motivo de parada (RAW, estructural, orden programa, etc.).

> The load and store execution stage uses 1 cycle. The floating-point multiplication (FP) execution step takes 5 cycles. The floating point (FP) addition execution step takes 2 cycles. Any step of an instruction that wants to write to the CDB (Common Data Bus) cannot do so if another instruction is already using it. In general, any resource that is freed in one clock cycle cannot be used until the next clock cycle.
> — `repo:datos/temarios/AC/examenes/January 2025.pdf` (cita sin comprobar)
