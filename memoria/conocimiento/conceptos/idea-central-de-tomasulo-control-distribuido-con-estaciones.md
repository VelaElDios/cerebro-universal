---
tipo: "concepto"
titulo: "Idea central de Tomasulo: control distribuido con estaciones de reserva"
temas: ["ac", "arquitectura", "planificacion-dinamica", "tomasulo"]
claves: ["estaciones de reserva", "control distribuido", "buffers distribuidos", "unidad funcional"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[planificacion-dinamica]] · [[tomasulo]]

A diferencia del marcador centralizado, Tomasulo distribuye el control: cada unidad funcional tiene sus estaciones de reserva (reservation stations). Estas estaciones deciden localmente cuándo arrancar la ejecución, capturan operandos en cuanto están listos (eliminando lecturas del banco de registros) y guardan tanto los valores como las etiquetas de origen de los operandos pendientes.

> Idea básica: Control & Buffers distribuidos con UF Estación de reserva. La detección de riesgos y el control de la ejecución están distribuidos. Las estaciones de reserva, en cada unidad funcional, controlan cuándo puede comenzar la ejecución de una instrucción en esa unidad. Una estación de reserva busca un operando tan pronto esté disponible y lo retiene (se elimina la necesidad de obtener el operando de los registros)
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)
