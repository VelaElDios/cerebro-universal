---
titulo: "Los identificadores largos en \\texttt no se parten solos: usar \\allowbreak dentro del comando"
temas: ["latex", "overfull", "texttt"]
claves: ["Overfull \\hbox", "in paragraph at lines", "luatex.def"]
estado: "propuesta"
veces: 1
fecha: "2026-10-30"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[overfull]] · [[texttt]]

## Problema
un nombre como accountConfirmation.test.js o POST /api/prueba/dominio dentro de \texttt forma una caja irrompible; si la línea anterior está llena, la caja se sale del margen (overfull de 33–48 pt) aunque haya \emergencystretch, porque LaTeX no parte dentro de \texttt

## Solución
poner \allowbreak dentro del \texttt en los puntos naturales (tras el punto, la barra o en medio de la palabra); el espacio tras \allowbreak se ignora, así que el texto no cambia si no se parte

## Ejemplo
\texttt{accountConfirmation\allowbreak.test.js} y \texttt{POST\allowbreak /api/\allowbreak prueba/\allowbreak dominio}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
