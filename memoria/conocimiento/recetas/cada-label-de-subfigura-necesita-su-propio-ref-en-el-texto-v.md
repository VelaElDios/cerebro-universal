---
tipo: "receta"
titulo: "Cada \\label de subfigura necesita su propio \\ref en el texto (verificar.py lo exige)"
temas: ["latex", "refs", "subcaption", "subfigure", "verificar"]
claves: ["no se cita en el texto", "subcaption", "subfigure", "label"]
proyectos: ["memoria-procesos"]
fuentes: ["resultado de verificar.py en este paso (comando_prueba)"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[refs]] · [[subcaption]] · [[subfigure]] · [[verificar]]

Al agrupar capturas con \begin{subfigure}...\subcaption{...}\label{fig:x-a}...\label{fig:x-b}, el test comprueba cada \label por separado: no basta con citar la figura general (\ref{fig:x}); hay que citar también cada subfigura en la prosa («la subfigura~\ref{fig:x-a} muestra…»). Si falta alguno, verificar.py falla con «la figura fig:... no se cita en el texto».

> ERROR: chapters/05-evaluacion.tex:137: la figura fig:prueba-tecnica-permitido no se cita en el texto (usa \ref{fig:prueba-tecnica-permitido})
> — `resultado de verificar.py en este paso (comando_prueba)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
