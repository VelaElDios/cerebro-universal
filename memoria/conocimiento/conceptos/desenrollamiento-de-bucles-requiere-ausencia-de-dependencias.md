---
tipo: "concepto"
titulo: "Desenrollamiento de bucles requiere ausencia de dependencias entre iteraciones"
temas: ["ac", "bucles", "dependencias", "desenrollamiento"]
claves: ["desenrollamiento bucles", "loop unrolling", "dependencias entre iteraciones", "loop-carried dependencies"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[desenrollamiento]]

Para solapar iteraciones (software pipelining o unrolling + scheduling) no debe haber dependencias *loop-carried* (RAW, WAR, WAW entre iteraciones). Las dependencias dentro de la misma iteración se manejan con scheduling local. La opción b) (múltiplo de iteraciones desenrolladas) es condición para limpieza exacta, no para solapamiento en sí.

> Se puede solapar la ejecución de distintas iteraciones de un bucle cuando éste: c) No presenta dependencias entre iteraciones
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf` (cita sin comprobar)
