---
tipo: "concepto"
titulo: "Propósito del Branch Target Buffer (BTB) además de bits de predicción"
temas: ["ac", "arquitectura", "btb", "prediccion-saltos"]
claves: ["BTB", "branch target address", "predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[btb]] · [[prediccion-saltos]]

El BTB (Branch Target Buffer) almacena las direcciones destino (target addresses) de las instrucciones de salto para poder obtener el target en la etapa IF sin esperar a calcularlo en ID/EX. Junto con los bits de predicción (tomado/no tomado), permite especular la siguiente instrucción a buscar. No gestiona excepciones ni reduce latencia por sí mismo; su función es proveer el target temprano.

> Apart from storing prediction bits, what is the purpose of the branch target buffer (BTB) in the computer architecture? To store the branch target addresses of branch instructions.
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)` (cita sin comprobar)
