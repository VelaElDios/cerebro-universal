---
tipo: "concepto"
titulo: "Antidependencia (WAR) en bucle entre carga y actualización de puntero en misma iteración"
temas: ["ac", "bucles", "dependencias", "pipeline", "war"]
claves: ["antidependencia", "WAR", "bucle", "puntero", "L.D", "DADDUI", "misma iteración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[pipeline]] · [[war]]

En el bucle dado, la 1ª instrucción (L.D) lee R1 y la 4ª (DADDUI) escribe R1. Existe una antidependencia (WAR) a través de R1 **en la misma iteración** (la carga usa el valor viejo del puntero antes de que se incremente). Ninguna de las opciones a, b, c describe exactamente esto (a dice dependencia de datos/RAW, b dice dependencia de salida/WAW, c dice entre iteraciones), por lo que la correcta es d) No existe ningún tipo de dependencia **entre las opciones dadas**, aunque realmente hay una WAR.

> Entre la primera y la cuarta instrucción... L.D F4, 0(R1) ... DADDUI R1, R1, #8
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
