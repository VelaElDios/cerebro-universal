---
tipo: "concepto"
titulo: "Identificación de antidependencia (WAR) entre store e incremento de puntero en bucle"
temas: ["ac", "dependencias", "pipeline"]
claves: ["antidependencia", "WAR", "store", "DADDUI", "puntero"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]]

En el bucle dado, I3 (SW R1,0(R2)) lee R2 para la dirección de memoria; I4 (DADDUI R2,R2,#4) escribe R2. Esto crea una antidependencia (WAR) porque la lectura de R2 en I3 debe ocurrir antes de la escritura en I4. En pipeline con forwarding, esta WAR puede causar parada si no hay renombrado de registros.

> There is an antidependence between I3 and I4
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]] · [[definicion-de-riesgo-raw-read-after-write]]
