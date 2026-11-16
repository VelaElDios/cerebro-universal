---
tipo: "receta"
titulo: "Escribir diagramas de secuencia con pgf-umlsd (sequencediagram)"
temas: ["diagramas", "latex", "pgf-umlsd"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["spec del proyecto (bloque «Cómo se escribe un diagrama de secuencia»)"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[diagramas]] · [[latex]] · [[pgf-umlsd]]

Reglas obligatorias para que compile y pase revisar_umlsd.py: (1) Entorno `sequencediagram` en minúsculas. (2) Participantes: `\newthread{id}{Nombre}` o `\newinst[dist]{id}{Nombre}`. (3) Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta} ... \end{call}`. (4) Mensajes simples: `\mess{origen}{mensaje}{destino}`. (5) Alternativas: `\begin{sdblock}{alt}{condición} ... \end{sdblock}`. (6) **Prohibido** en textos de `\mess`, `call`, `callself`, `\newinst`: `\#`, `\_`, `\&`, `\%`, `\$`, `\{`, `\}`, comandos LaTeX (`\texttt`...), y `#`, `&`, `_`, `$` sueltos. En `\mess` tampoco paréntesis. (7) Todo participante usado debe estar declarado en ese diagrama. (8) Diagramas anchos: envolver en `\resizebox{\textwidth}{!}{% ... %}`. (9) Diagramas altos: `\begin{adjustbox}{max width=\textwidth,max totalheight=0.6\textheight}`. (10) Códigos de estado HTTP exactos de la doc técnica (ej. 400, no 422).

> El entorno es sequencediagram (en minúsculas; no existen sequenceDiagram ni un entorno alt: para alternativas, sdblock). Participantes con \newthread/\newinst, llamadas anidadas con call (origen, mensaje, destino, respuesta), mensajes sueltos con \mess y bloques alternativos con sdblock.
> — `spec del proyecto (bloque «Cómo se escribe un diagrama de secuencia»)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
