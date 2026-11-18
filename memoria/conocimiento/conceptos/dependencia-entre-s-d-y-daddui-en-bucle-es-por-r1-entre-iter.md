---
tipo: "concepto"
titulo: "Dependencia entre S.D y DADDUI en bucle es por R1 entre iteraciones"
temas: ["ac", "antidependencia", "bucles", "dependencias", "pipeline", "war"]
claves: ["S.D", "DADDUI", "R1", "bucle", "iteraciones", "dependencia datos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014B.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[antidependencia]] · [[bucles]] · [[dependencias]] · [[pipeline]] · [[war]]

S.D F4, 0(R1) usa R1 como base; DADDUI R1, R1, #-8 actualiza R1. En la misma iteración: S.D lee R1, DADDUI escribe R1 → antidependencia WAR (Write After Read) en misma iteración. Pero la opción correcta dice "entre iteraciones": el R1 actualizado en iteración i se usa en iteración i+1 por S.D → dependencia de flujo (RAW) entre iteraciones a través de R1 (bucle carry dependence).

> Entre las instrucciones S.D y DADDUI... c) Existe una dependencia de datos, a través de R1, entre iteraciones
> — `repo:datos/temarios/AC/examenes/Noviembre2014B.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
