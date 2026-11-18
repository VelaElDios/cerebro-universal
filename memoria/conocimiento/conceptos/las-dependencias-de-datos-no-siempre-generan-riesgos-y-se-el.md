---
tipo: "concepto"
titulo: "Las dependencias de datos no siempre generan riesgos y se eliminan con renombramiento"
temas: ["ac", "dependencias", "renombramiento", "riesgos"]
claves: ["dependencia de datos", "riesgo", "renombramiento", "WAR", "WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[renombramiento]] · [[riesgos]]

Las dependencias de datos (RAW verdaderas) no siempre causan riesgos si el hardware tiene anticipación (forwarding). Las dependencias de nombre (antidependencias WAR y dependencias de salida WAW) se eliminan mediante renombramiento de registros, ya sea por hardware (Tomasulo, ROB) o por software (compilador).

> Con respecto a las dependencias de datos: a) Siempre dan lugar a riesgos de datos b) No se pueden eliminar de ninguna forma c) Se eliminan mediante renombramiento d) Ninguna de las anteriores
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[antidependencia-war-siempre-genera-hazard-war]]
