---
tipo: "dato"
titulo: "Riesgo WAR (antidependencia) entre SUB.D F10,F8,F6 y L.D F6,0(R1)"
temas: ["ac", "pipeline", "riesgos", "war"]
claves: ["riesgo WAR", "antidependencia", "SUB.D", "L.D", "registro F6"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[riesgos]] · [[war]]

SUB.D lee F6 (fuente) y L.D escribe F6 (destino). Como la escritura de L.D ocurre después de la lectura de SUB.D en el orden del programa, es una antidependencia (WAR: Write After Read). La respuesta correcta es «Riesgo WAR» (opción b).

> Indica el tipo de riesgo que existe entre estas instrucciones: SUB.D F10, F8, F6 / L.D F6, 0(R1)
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-siempre-genera-hazard-war]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
