---
tipo: "concepto"
titulo: "Diferencia fundamental VLIW vs Superescalar: compilador vs hardware detecta paralelismo"
temas: ["ac", "compilador", "hardware", "ilp", "superescalar", "vliw"]
claves: ["VLIW", "superescalar", "paralelismo instrucciones", "compilador", "hardware", "detección"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[compilador]] · [[hardware]] · [[ilp]] · [[superescalar]] · [[vliw]]

En VLIW (Very Long Instruction Word), el compilador analiza dependencias y empaqueta instrucciones independientes en palabras de instrucción larga para ejecución paralela; el hardware ejecuta lo que el compilador dice. En superescalar, el hardware (unidad de despacho/emisión) detecta dinámicamente instrucciones independientes en la ventana de instrucciones y las emite a unidades funcionales. Esta diferencia implica que VLIW requiere compiladores muy sofisticados y es sensible a cambios de microarquitectura (latencias, unidades funcionales) porque el horario está fijado en el binario.

> ¿Cuál es la principal diferencia entre una arquitectura superescalar y una VLIW? ... c. En las arquitecturas VLIW el compilador determina el paralelismo entre instrucciones, mientras que en las superescalares lo hace principalmente el hardware.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[rasgo-comun-entre-superescalares-y-vliw-multiples-unidades-d]] · [[definicion-de-procesador-vliw]] · [[vliw-el-compilador-empaqueta-varias-operaciones-en-una-instr]]
