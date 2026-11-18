---
tipo: "receta"
titulo: "Métrica operaciones por ciclo (OPC) en VLIW"
temas: ["ac", "ipc", "metricas", "operaciones-por-ciclo", "vliw"]
claves: ["operaciones por ciclo", "OPC", "ancho VLIW 4", "utilización", "eficiencia"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ipc]] · [[metricas]] · [[operaciones-por-ciclo]] · [[vliw]]

OPC = (total operaciones útiles emitidas) / (ciclos totales de la planificación). En VLIW de 4 ops, el máximo teórico es 4. Se cuenta cuántas operaciones reales (no NOP) se colocan en la tabla de ciclos de la parte A) y se divide por el número de ciclos usados hasta que el patrón se repite (inicio de siguiente iteración).

> How many operations per cycle are reached?
> — `repo:datos/temarios/AC/examenes/January2018.pdf`

Relacionado: [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]] · [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw]] · [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]] · [[calculo-de-operaciones-por-ciclo-en-vliw-con-software-pipeli]]
