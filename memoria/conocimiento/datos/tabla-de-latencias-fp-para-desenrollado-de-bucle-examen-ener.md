---
tipo: "dato"
titulo: "Tabla de latencias FP para desenrollado de bucle (examen enero 2021)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["latency", "FP ALU", "S.D", "L.D", "forwarding", "delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Latencias oficiales del enunciado para el bucle `L.D F10,0(R2); ADD.D F8,F10,F12; S.D F8,0(R2); DADDUI R2,R2,-8; BNE R2,R3,Bucle` con forwarding y salto retardado:
- **FP ALU → FP ALU** (p.ej. ADD.D → ADD.D): **3 ciclos**.
- **FP ALU → S.D** (p.ej. ADD.D → S.D): **1 ciclo**.
- **L.D → FP ALU** (p.ej. L.D → ADD.D): **1 ciclo**.
- **L.D → S.D** (p.ej. L.D → S.D): **0 ciclos** (forwarding directo sin burbuja).
Todas las unidades están **fully pipelined**. El salto retardado (delayed branch) implica que la instrucción en el *delay slot* se ejecuta siempre.

> The next latencies: Instruction producing the result / Instruction using the result / Latency in cycles: ALU FP / ALU FP / 3; ALU FP / S.D / 1; L.D / ALU FP / 1; L.D / S.D / 0
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[definicion-de-latencia-de-salto-y-huecos-de-retardo]]
