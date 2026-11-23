---
tipo: "decision"
titulo: "Diagramas de secuencia con pgf-umlsd: sintaxis válida y errores comunes"
temas: ["latex", "pgf-umlsd", "sequencediagram"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock", "adjustbox"]
proyectos: ["memoria-procesos"]
fuentes: ["spec del proyecto (ejemplo compilado y probado)"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[sequencediagram]]

Errores frecuentes que detecta revisar_umlsd.py: (1) acentos en etiquetas → quitar o usar \n para salto de línea; (2) paréntesis en \mess → reescribir sin paréntesis; (3) comandos LaTeX en textos → usar texto plano; (4) participantes usados sin declarar → añadir \newthread/\newinst; (5) más de 6 participantes → agrupar o partir en dos diagramas; (6) flechas que cruzan cajas → usar codos y separar cajas; (7) texto demasiado pequeño tras escalado → replantear diagrama, no encoger con adjustbox.

> El entorno es sequencediagram (en minúsculas; no existen sequenceDiagram ni un entorno alt: para alternativas, sdblock). Participantes con \newthread/\newinst, llamadas anidadas con call (origen, mensaje, destino, respuesta), mensajes sueltos con \mess y bloques alternativos con sdblock. En los textos de \mess, call, callself y \newinst no puede ir \#, \_, \&, \%,\$, \{, \}, ningún comando (\texttt…) ni #, &, _, $ sueltos, y en \mess tampoco paréntesis. Todo participante que se use tiene que estar declarado con \newthread/\newinst en ese diagrama.
> — `spec del proyecto (ejemplo compilado y probado)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
