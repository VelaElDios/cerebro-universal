---
tipo: "decision"
titulo: "Detección y resolución de riesgo WAR en el marcador (ciclos 17-21)"
temas: ["ac", "fadd.d", "fsub.d", "hazard", "riesgo-war", "scoreboard"]
claves: ["WAR", "Write After Read", "fadd.d", "fsub.d", "f6", "f8", "f2", "ciclo 17", "ciclo 21"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[fadd.d]] · [[fsub.d]] · [[hazard]] · [[riesgo-war]] · [[scoreboard]]

En el ciclo 17 se anota "Riesgo WAR" y "No se escribe el resultado de fadd.d". La fadd.d (f6 = f8 + f2) quiere escribir f6, pero f6 es operando fuente (Fj) de la fsub.d (f8 = f6 - f2) que aún no ha leído sus operandos (su lectura ocurre en ciclo 7, pero la escritura de fadd.d sería en ciclo 16). El marcador retrasa la escritura de fadd.d hasta que fsub.d haya leído f6; en el ciclo 21 aparece "El riesgo WAR ha desaparecido" y la fadd.d escribe en ciclo 22.

> Ojo!! No se escribe el resultado de fadd.d Riesgo WAR
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)
