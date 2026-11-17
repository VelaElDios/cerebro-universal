---
tipo: "concepto"
titulo: "Tipos de riesgos en pipeline: estructurales, datos, control"
temas: ["ac", "hazards", "pipeline", "riesgos"]
claves: ["hazard estructural", "hazard datos", "hazard control", "conflicto recurso", "dependencia datos", "saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hazards]] · [[pipeline]] · [[riesgos]]

Tres clases de hazards que degradan el CPI ideal de 1:
- Estructurales: dos instrucciones necesitan el mismo recurso hardware en el mismo ciclo (ej. un solo puerto de escritura en banco de registros).
- De datos: una instrucción necesita un operando que aún no ha sido producido por una instrucción anterior solapada (dependencias RAW, WAW, WAR).
- De control: el flujo de instrucciones depende del resultado de un salto; el PC no se sabe hasta tarde en el pipeline.

> Hazard o Riesgo: situación que impide que se pueda hacer la siguiente etapa en el cauce de una instrucción • Tipos de Riesgos: • Estructurales: provocados por un conflicto en el uso de un recurso hardware • De datos: cuando una instrucción depende del resultado de otra previa, y la superposición de la ejecución de ambas instrucciones puede provocar problemas • De control: provocados por la segmentación de los saltos y otras instrucciones que modifican el PC
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)
