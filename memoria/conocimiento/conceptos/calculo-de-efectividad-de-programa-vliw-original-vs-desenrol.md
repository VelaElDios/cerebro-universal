---
tipo: "concepto"
titulo: "Cálculo de efectividad de programa VLIW: original vs desenrollado (examen enero 2023)"
temas: ["ac", "vliw"]
claves: ["effectiveness", "VLIW", "percentage", "utilization", "aprovechamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[vliw]]

La efectividad (effectiveness) en VLIW se calcula típicamente como (slots útiles / slots totales) * 100%. Para el programa original (parte a), se cuentan los slots no-NOP en la tabla de 7 ciclos x 4 slots = 28 slots totales. Para el programa desenrollado y planificado (parte b), se cuentan slots útiles en la nueva tabla (ciclos totales x 4) y se divide por el total. El enunciado pide ambos porcentajes en la parte 3c.

> Effectiveness of the VLIW program I gave you (in %) Effectiveness of the VLIW program obtained in b (in %)
> — `repo:datos/temarios/AC/examenes/January2023.pdf`

Relacionado: [[como-desenrollar-4-veces-y-planificar-bucle-vliw-para-maximo]] · [[calculo-de-speedup-entre-bucle-original-y-desenrollado-en-vl]] · [[mejora-de-rendimiento-vliw-desenrollado-3x-vs-original-exame]]
