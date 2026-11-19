---
tipo: "receta"
titulo: "Diagramas de secuencia pgf-umlsd sintaxis correcta"
temas: ["diagramas", "latex", "pgf-umlsd"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[diagramas]] · [[latex]] · [[pgf-umlsd]]

Sintaxis obligatoria para diagramas de secuencia en esta plantilla: (1) Entorno `sequencediagram` (minúsculas). (2) Participantes: `\newthread{id}{Nombre}` para hilos, `\newinst[desplazamiento]{id}{Nombre}` para instancias. (3) Llamadas anidadas: `\begin{call}{origen}{mensaje}{destino}{respuesta}...\end{call}`. (4) Mensajes simples: `\mess{origen}{mensaje}{destino}`. (5) Alternativas: `\begin{sdblock}{alt}{condición}...\end{sdblock}`. (6) En textos de `\mess`, `call`, `callself`, `\newinst`: NO usar `#`, `_`, `&`, `%`, `$`, `{`, `}`, comandos LaTeX (`\texttt`...), paréntesis en `\mess`. (7) Todo participante usado debe estar declarado en ese diagrama. (8) Usar `\resizebox{\textwidth}{!}{...}` para diagramas anchos; `adjustbox{max totalheight=0.6\textheight}` si ocupan casi una página.

> El entorno es `sequencediagram` (en minúsculas; **no** existen `sequenceDiagram` ni un entorno `alt`: para alternativas, `sdblock`): participantes con `\newthread`/`\newinst`, llamadas anidadas con `call` (origen, mensaje, destino, respuesta), mensajes sueltos con `\mess` y bloques alternativos con `sdblock`.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
