---
tipo: "concepto"
titulo: "Definición de riesgo RAW (Read After Write)"
temas: ["ac", "pipeline", "riesgos"]
claves: ["RAW", "dependencia de datos", "true dependence"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[riesgos]]

La pregunta 5 presenta opciones incorrectas: RAW NO es dependencia de control (esa es riesgo de control), NO es dependencia de salida (WAW), NO es antidependencia (WAR). RAW es una dependencia de datos verdadera (true data dependence): una instrucción lee un dato que una anterior escribe. La respuesta correcta es d) Ninguna es correcta.

> Un riesgo de tipo RAW: Se corresponde con una dependencia de control
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf` (cita sin comprobar)

Relacionado: [[riesgo-raw-read-after-write-y-su-causa]] · [[riesgo-raw-como-dependencia-de-datos-verdadera]] · [[diferencia-entre-dependencia-de-datos-raw-antidependencia-wa]]
