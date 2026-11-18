---
tipo: "dato"
titulo: "Análisis de dependencias en código FP con registro F1 (RAW y WAW)"
temas: ["ac", "dependencias", "pipeline", "punto-flotante", "riesgos"]
claves: ["RAW", "WAW", "dependencia datos", "dependencia salida", "F1", "ADD.D", "DIV.D", "S.D"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]] · [[punto-flotante]] · [[riesgos]]

Analizando el fragmento: I1 escribe F1; I2 lee F1 (RAW I1→I2) y escribe F1 (WAW I1→I2); I3 lee F1 (RAW I2→I3). Hay dos dependencias de datos (RAW: I1→I2 e I2→I3) y una dependencia de salida (WAW: I1→I2). La opción correcta es c) Dos dependencias de datos y una de salida.

> En este código, a través de F1 existen: ADD.D F1, F3, F2 ; I1 DIV.D F1, F1, F2 ; I2 S.D F1, 0(R1) ; I3 a) Dos dependencias de salida b) Dos dependencias de datos c) Dos dependencias de datos y una de salida d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]]
