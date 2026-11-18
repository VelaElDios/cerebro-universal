---
tipo: "concepto"
titulo: "Riesgo RAW (Read After Write) y su causa"
temas: ["ac", "dependencia de datos", "pipeline", "raw"]
claves: ["RAW", "dependencia de datos verdadera", "hazard"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencia de datos]] · [[pipeline]] · [[raw]]

RAW (Read After Write) es una dependencia de datos verdadera (true data dependence): una instrucción lee un operando que una instrucción anterior escribe. Es la única dependencia que transmite información. Las otras: WAW (output dependence) y WAR (antidependence) son dependencias de nombre, eliminables con renombrado. La opción correcta es d) None of the above (porque la causa es una dependencia de datos verdadera, no las opciones dadas).

> A RAW hazard is due to: a) A control dependence b) An output dependence c) An antidependence d) None of the above
> — `repo:datos/temarios/AC/examenes/January2020.pdf`
