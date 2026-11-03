---
titulo: "Todas las figuras y tablas deben tener \\ref en el texto"
temas: ["latex", "verificacion"]
claves: ["figura no se cita en el texto", "verificar.py"]
estado: "propuesta"
veces: 1
fecha: "2026-11-03"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[verificacion]]

## Problema
El test automático verificar.py comprueba que cada figura/tabla con \label tenga al menos un \ref en el cuerpo del documento. Si falta, la compilación se considera fallida.

## Solución
Al insertar una figura o tabla, añadir inmediatamente una referencia en el párrafo anterior o posterior (ej.: "como se muestra en la Figura~\ref{fig:...}"). Revisar la lista de figuras del .lof y comprobar que todas aparecen en el texto.

## Ejemplo
\begin{figure}...\caption{...}\label{fig:ejemplo}\end{figure} ... según se muestra en la Figura~\ref{fig:ejemplo} ...

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
