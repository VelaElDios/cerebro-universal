---
tipo: "concepto"
titulo: "Speedup ideal vs real en pipeline y fórmula con detenciones"
temas: ["ac", "cpi", "pipeline", "speedup"]
claves: ["incremento ideal = número etapas", "etapas mal equilibradas", "sobrecarga", "CPI ideal = 1", "fórmula speedup"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[pipeline]] · [[speedup]]

El speedup teórico máximo es el número de etapas (p. ej., 5× para 5 etapas). En la práctica es menor por desequilibrio entre etapas y overhead de registros de pipeline. El CPI ideal es 1 (una instrucción por ciclo). La fórmula real: Speedup = (Ciclo_sin_segmentación) / (Ciclo_segmentado * (1 + Stalls_por_instrucción)). Los stalls provienen de riesgos estructurales, de datos y de control.

> Incremento ideal de velocidad = número de etapas • Idealmente: → Un pipeline de 5 etapas será 5 veces más rápida • En la realidad es menor → Las etapas pueden estar mal equilibradas → Existe una sobrecarga adicional • “En el mejor de los casos podrá ejecutarse una instrucción por ciclo” • Speedup = Ciclo sin segmentación / (1 + Ciclos de detención por instrucción * Ciclo segmentado)
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[definicion-y-proposito-de-la-segmentacion-pipeline]] · [[calculo-de-speedup-para-bucle-desenrollado-en-pipeline-con-h]] · [[ventaja-real-del-pipeline-mayor-throughput-instrucciones-uni]] · [[calculo-de-cpi-en-pipeline-con-stalls-y-tras-optimizacion]]
