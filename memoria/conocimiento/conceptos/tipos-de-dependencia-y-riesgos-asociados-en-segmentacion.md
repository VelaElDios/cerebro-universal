---
tipo: "concepto"
titulo: "Tipos de dependencia y riesgos asociados en segmentación"
temas: ["ac", "paralelismo-instruccion", "riesgos-segmentacion"]
claves: ["RAW", "WAR", "WAW", "riesgo-control", "dependencia-datos", "antidependencia", "dependencia-salida", "dependencia-control"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[paralelismo-instruccion]] · [[riesgos-segmentacion]]

En una unidad segmentada, las dependencias entre instrucciones próximas generan riesgos (hazards) si su ejecución solapada altera el orden de acceso a los operandos. La correspondencia canónica es: dependencia de datos (verdadera) → riesgo RAW (Read After Write); antidependencia → riesgo WAR (Write After Read); dependencia de salida → riesgo WAW (Write After Write); dependencia de control → riesgo de control (salto mal predicho o no resuelto).

> Dependencia de datos → RAW, antidependencia → WAR, de salida → WAW, de control → de control
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[tipos-de-riesgos-en-pipeline-estructurales-datos-control]] · [[dos-estrategias-genericas-para-tratar-dependencias-de-datos]] · [[diferencia-entre-dependencia-de-datos-raw-antidependencia-wa]]
