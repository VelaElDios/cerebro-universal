---
tipo: "concepto"
titulo: "Técnica de mejora de rendimiento en SISD"
temas: ["ac", "ilp", "sisd"]
claves: ["SISD", "ILP", "TLP", "DLP", "paralelismo a nivel de instrucción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[sisd]]

SISD (Single Instruction Single Data) es un único flujo de control y datos. Para mejorar rendimiento se explota ILP (Instruction Level Parallelism): segmentación (pipelining), superescalar, VLIW, ejecución fuera de orden, predicción de saltos. TLP (Thread Level Parallelism) requiere múltiples hilos (multicore, SMT). DLP (Data Level Parallelism) usa vectores/SIMD/GPU.

> In SISD computers, the technique used to improve performance is: a) ILP b) TLP c) DLP d) None of the above
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[arquitectura-sisd-componentes-y-tecnicas-ilp-segmentacion-su]] · [[definicion-de-paralelismo-a-nivel-de-threads-tlp-frente-a-il]] · [[tendencias-de-paralelismo-en-arquitectura-actual-ilp-tlp-dlp]]
