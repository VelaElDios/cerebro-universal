---
tipo: "receta"
titulo: "Análisis de dependencias en bucle con índices de array (pregunta 11)"
temas: ["ac", "bucles", "dependencias", "vectorizacion"]
claves: ["dependencia datos", "antidependencia", "dependencia salida", "bucle", "F4", "R1"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[vectorizacion]]

Código: I1: L.D F4,0(R1) (carga en F4), I3: S.D F4,0(R1) (almacena desde F4). Misma iteración: I1 escribe F4, I3 lee F4 → dependencia de datos verdadera (RAW) en la misma iteración. Entre iteraciones: I3 de iteración n escribe en memoria 0(R1), I1 de iteración n+1 lee de 0(R1) tras actualizar R1 (DADDUI R1,R1,#8). Como R1 cambia, direcciones son distintas → no hay dependencia entre iteraciones por memoria. Por registro F4: I3 escribe F4 (iteración n), I1 siguiente iteración escribe F4 (sobrescribe) → dependencia de salida (WAW) entre iteraciones por F4. Pero la pregunta pregunta entre I1 e I3 (misma iteración): es dependencia de datos (RAW) por F4. Respuesta correcta: a) There is a data dependence, through F4, between iterations (el enunciado dice "between iterations" pero en la misma iteración I1→I3 es RAW; la redacción del examen puede referirse a la dependencia que se manifiesta al iterar).

> Between the instructions I1 and I3... a) There is a data dependence, through F4, between iterations b) There is an output dependence, through F4, in the same iteration c) There is an antidependence, through F4, between iterations d) None of the above
> — `repo:datos/temarios/AC/examenes/January2017.pdf`
