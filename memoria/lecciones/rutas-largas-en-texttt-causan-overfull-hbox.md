---
titulo: "Rutas largas en \\texttt{} causan overfull hbox"
temas: ["latex", "pgf-umlsd"]
claves: ["overfull hbox", "\\texttt", "allowbreak"]
estado: "propuesta"
veces: 1
fecha: "2026-11-03"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[pgf-umlsd]]

## Problema
Rutas de archivos o identificadores largos dentro de \texttt{} no se parten y se salen del margen (overfull hbox de 30-100 pt).

## Solución
Insertar \allowbreak en puntos naturales (tras barras, puntos, guiones) dentro del \texttt{}. Ejemplo: \texttt{services/\allowbreak accountConfirmationService.js} o \texttt{29/09/2026\allowbreak--27/10/2026}.

## Ejemplo
\texttt{src/\allowbreak services/\allowbreak accountConfirmationService.js}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
