---
tipo: "dato"
titulo: "Riesgo entre ADD.D F4,F2,F0 y S.D F0,0(R1) es WAR (antidependencia)"
temas: ["ac", "pipeline", "riesgos", "war"]
claves: ["ADD.D", "S.D", "WAR", "antidependencia", "riesgo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[riesgos]] · [[war]]

La primera instrucción escribe en F0 (ADD.D F4, F2, F0 → F0 = F2+F0). La segunda lee F0 para almacenarlo (S.D F0, 0(R1)). Hay una antidependencia (WAR): la segunda instrucción lee un registro que la primera sobrescribe. En pipeline con adelantamiento, esto puede causar hazard WAR si la escritura llega antes de la lectura.

> Indica el tipo de riesgo que existe entre estas instrucciones: ADD.D F4, F2, F0 / S.D F0, 0(R1) a) Riesgo RAW b) Riesgo WAR c) Riesgo WAW d) Ninguno de los anteriores
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
