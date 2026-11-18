---
tipo: "concepto"
titulo: "El desenrollamiento de bucles reduce principalmente los riesgos de control (saltos)"
temas: ["ac", "pipeline"]
claves: ["desenrollamiento bucles", "loop unrolling", "riesgos control", "saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014A.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

Al replicar el cuerpo del bucle, se reduce la frecuencia de instrucciones de salto (branch), disminuyendo así los riesgos de control (control hazards) y la penalización por predicción errónea. También expone más ILP al compilador/hardware, pero su efecto directo en el test es la reducción de riesgos de control.

> La técnica de desenrollamiento de bucles reduce: b) Los riesgos de control
> — `repo:datos/temarios/AC/examenes/Noviembre2014A.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]]
