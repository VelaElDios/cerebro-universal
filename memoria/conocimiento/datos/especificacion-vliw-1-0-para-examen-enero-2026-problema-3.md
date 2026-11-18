---
tipo: "dato"
titulo: "Especificación VLIW 1.0 para examen Enero 2026 Problema 3"
temas: ["ac", "examen", "vliw"]
claves: ["ancho emisión 5", "slots Memoria1 Memoria2 PF1 PF2 Entera/Salto", "fully pipelined", "delayed branch 1 ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[vliw]]

Arquitectura VLIW objetivo del Problema 3. 5 issue slots fijos por ciclo: 2 memoria (carga/almacena), 2 punto flotante (adder/multiplier/divider), 1 entera/salto. Fully pipelined = nueva op cada ciclo en cada unidad, sin conflictos estructurales. Delayed branch 1 ciclo: instrucción en slot de retardo se ejecuta siempre (útil para rellenar con instrucción útil o nop).

> en un procesador VLIW versión 1.0 con las siguientes características: a) Ancho de emisión: 5 operaciones por ciclo. Slots: [Memoria1 | Memoria2 | PF1 | PF2 | Entera/Salto] b) Todas las unidades funcionales están completamente segmentadas. d) Salto retardado: La instrucción de salto (bnez) tiene 1 ciclo de retardo.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

Relacionado: [[caracteristicas-del-procesador-vliw-del-examen-enero-2016-pr]] · [[configuracion-vliw-del-examen-ac-enero-2017-6-unidades-laten]] · [[parametros-temporales-de-pipeline-para-vliw-problema-3b]]
