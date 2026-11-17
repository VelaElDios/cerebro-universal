---
tipo: "receta"
titulo: "Diagramas de secuencia con pgf-umlsd (sequencediagram)"
temas: ["latex", "pgf-umlsd", "secuencia", "tikz"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[secuencia]] · [[tikz]]

El entorno es `sequencediagram` (minúsculas). Participantes con `\newthread`/`\newinst`. Llamadas anidadas con `call` (origen, mensaje, destino, respuesta). Mensajes sueltos con `\mess`. Bloques alternativos con `sdblock` (no existe entorno `alt`). En los textos de `\mess`, `call`, `callself` y `\newinst` no puede ir `#`, `_`, `&`, `%`, `$`, `{`, `}`, ningún comando (`\texttt`…) ni paréntesis en `\mess`. Todo participante usado debe estar declarado en ese diagrama. `revisar_umlsd.py` lo comprueba antes de compilar.

> \begin{sequencediagram} \newthread{u}{Usuario} \newinst[2]{v}{Vista registro} \begin{call}{u}{escribe email y contraseña}{v}{ok} \end{call} \begin{sdblock}{alt}{ya existe} \mess{s}{409 ConflictError}{a} \end{sdblock} \end{sequencediagram}
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
