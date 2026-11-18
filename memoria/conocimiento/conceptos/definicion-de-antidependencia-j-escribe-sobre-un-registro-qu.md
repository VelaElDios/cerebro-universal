---
tipo: "concepto"
titulo: "Definición de antidependencia: j escribe sobre un registro que lee i (i antes que j)"
temas: ["ac", "antidependencia", "dependencias"]
claves: ["antidependencia", "WAR", "dependencia", "registro", "memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[antidependencia]] · [[dependencias]]

Antidependencia (WAR) = lectura-escritura en orden inverso al programa. La instrucción posterior (j) escribe un operando que la anterior (i) lee. Requiere renombrado de registros o espera para evitar hazard WAR.

> Dadas dos instrucciones i y j (j lógicamente después de i) existe una antidependencia entre ellas si: b) La instrucción j escribe sobre un registro o una posición de memoria que lee la instrucción i
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[hazard-war-corresponde-a-antidependencia-dependencia-de-nomb]] · [[riesgo-war-dependencia-antidependencia-datos]]
