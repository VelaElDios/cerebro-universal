---
tipo: "concepto"
titulo: "Se pueden solapar iteraciones de un bucle si no hay dependencias entre iteraciones"
temas: ["ac", "bucles", "dependencias-entre-iteraciones", "desenrollado"]
claves: ["solapamiento", "iteraciones", "bucle", "dependencias entre iteraciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias-entre-iteraciones]] · [[desenrollado]]

El solapamiento (software pipelining, desenrollado + planificación) requiere que no existan dependencias loop-carried (RAW, WAR, WAW entre iteraciones). Las dependencias dentro de una misma iteración se resuelven con adelantamiento o reordenamiento local.

> Se puede solapar la ejecución de distintas iteraciones de un bucle cuando éste: c) No presenta dependencias entre iteraciones
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[desenrollamiento-de-bucles-requiere-ausencia-de-dependencias]] · [[condicion-para-solapar-iteraciones-de-un-bucle-desenrollado]] · [[condicion-para-solapar-iteraciones-de-un-bucle-software-pipe]]
