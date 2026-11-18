---
tipo: "concepto"
titulo: "Qué ocurre cuando un salto mal predicho llega al tope del ROB"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["ROB", "Reorder Buffer", "mal predicho", "flush", "fetch correcto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Cuando un salto mal predicho llega al tope del ROB (punto de commit), ocurren tres cosas: 1) se actualizan las estructuras de predicción (BHT/BTB), 2) se inicia el fetch de la instrucción correcta (restaurando PC), 3) se vacía (flush) el ROB y pipeline de instrucciones especulativas posteriores. Todas las opciones son correctas.

> When a branch instruction that has been mispredicted reaches the top of the ROB: a) The data structures used for the prediction are updated b) The fetch of the correct instruction is initiated c) The ROB is flushed d) All are correct
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]]
