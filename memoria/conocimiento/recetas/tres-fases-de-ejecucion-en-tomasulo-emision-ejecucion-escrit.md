---
tipo: "receta"
titulo: "Tres fases de ejecución en Tomasulo: Emisión, Ejecución, Escritura"
temas: ["ac", "arquitectura", "fases-ejecucion", "planificacion-dinamica", "tomasulo"]
claves: ["emisión", "ejecución", "escritura resultado", "CDB", "riesgo estructural", "RAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[fases-ejecucion]] · [[planificacion-dinamica]] · [[tomasulo]]

1. Emisión (Issue): Se toma la siguiente instrucción de la cola. Si es FP-aritmética y hay estación de reserva libre, se asigna y se copian operandos disponibles (valores) o etiquetas de sus productores. Si no hay estación libre → riesgo estructural, se frena. Para carga/almacena se requiere buffer libre.
2. Ejecución (Execute): La estación monitoriza el CDB; cuando llegan todos sus operandos (etiquetas coinciden), lanza la operación en su UF. Esta monitorización resuelve RAW.
3. Escritura (Write Result): Al terminar, el resultado se pone en el CDB con su etiqueta. Todas las estaciones, buffers y registros que esperaban esa etiqueta capturan el valor simultáneamente.

> Emisión: Obtiene una instrucción de la cola de operaciones, y Si es operación aritmética en punto flotante: se emite, si hay una estación de reserva vacía y envía los operandos a la estación de reserva (si están en los registros). Ejecución: Si aún no están disponibles los operandos, monitoriza el CDB a la espera del registro que se va a computar (este paso comprueba los riesgos RAW); Cuando todos los operandos están disponibles, ejecuta la operación en la UF correspondiente. Escritura del resultado: Cuando el resultado está disponible, se envía al CDB; Desde el CDB, a los registros y estaciones de reserva (incluyendo buffers de almacenamiento) que lo esperan
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)
