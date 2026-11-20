---
tipo: "receta"
titulo: "Agrupar capturas relacionadas en subfiguras con prosa integrada"
temas: ["latex", "maquetacion", "subcaption"]
claves: ["subfigure", "prosa", "regla 13 Javier"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[maquetacion]] · [[subcaption]]

Para cada grupo de capturas relacionadas (máx. 2 por fila), usar `\begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta}\subcaption{...}\label{fig:sub1}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}...\end{subfigure}\caption{Caption general}\label{fig:general}\end{figure}`. En el texto, referenciar la figura general y/o las subfiguras dentro de la prosa que explica la acción del usuario y la respuesta de la app. Ejemplo: "Al registrarse, el formulario valida email y contraseña en cliente (Figura~\ref{fig:app-inicio-registro}, subfiguras~\ref{fig:app-inicio} y~\ref{fig:app-registro})."

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
