---
tipo: "concepto"
titulo: "Restricciones de uso del Bus de Datos Común y recursos en Tomasulo especulativo"
temas: ["ac", "bdc", "especulacion", "riesgos-estructurales", "tomasulo"]
claves: ["BDC", "mismo ciclo", "escribir dato", "iniciar ejecución", "recurso liberado", "ciclo siguiente"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bdc]] · [[especulacion]] · [[riesgos-estructurales]] · [[tomasulo]]

Dos restricciones clave para la simulación: 1) Conflicto BDC: si una instrucción escribe su resultado en el Common Data Bus en el ciclo N, otra instrucción que esperaba ese dato no puede comenzar su ejecución en el mismo ciclo N; debe esperar al ciclo N+1. 2) Liberación de recursos: una unidad funcional o buffer que queda libre al terminar una instrucción en el ciclo N no puede ser asignado a una nueva instrucción hasta el ciclo N+1.

> En el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que estuviera esperando ese dato. Un recurso que se libera en un ciclo no se puede usar hasta el ciclo siguiente.
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf` (cita sin comprobar)

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[convencion-de-nomenclatura-en-tablas-de-tomasulo-del-temario]]
