---
tipo: "dato"
titulo: "Tabla de planificación VLIW vacía del examen (6 columnas, filas libres)"
temas: ["ac", "examen", "planificacion", "tabla", "vliw"]
claves: ["INT1", "INT2", "MEM1", "MEM2", "FP ADD", "FP MUL", "schedule", "tabla"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[planificacion]] · [[tabla]] · [[vliw]]

La tabla de planificación proporcionada en el examen tiene 6 columnas, una por cada unidad de ejecución:
- INT1, INT2: dos unidades enteras (ALU/saltos)
- MEM1, MEM2: dos unidades de memoria (carga/almacenamiento)
- FP ADD: unidad de suma de punto flotante
- FP MUL: unidad de multiplicación de punto flotante
Cada fila representa un ciclo de reloj. El estudiante debe colocar cada instrucción del bucle en la columna correspondiente a su unidad y en la fila (ciclo) que respete las latencias y dependencias, aprovechando el forwarding y el slot de retardo del salto. El examen indica "you may not need all the table rows", sugiriendo que el bucle cabe en menos ciclos de los que tiene la tabla impresa.

> a) Schedule the loop for this VLIW processor, using this table (you may not need all the table rows):       INT1              INT2             MEM1              MEM2             FP ADD           FP MUL
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[codigo-del-bucle-a-planificar-en-vliw-examen-ac-enero-2017]]
