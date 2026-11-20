---
tipo: "decision"
titulo: "Prosa de TFG sin cadenas «La figura X muestra…» (regla 13 Javier)"
temas: ["figuras", "redaccion", "reglas-javier", "subfigure", "tfg"]
claves: ["La figura X muestra", "prosa", "subfigure", "caption general", "subcaption"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[figuras]] · [[redaccion]] · [[reglas-javier]] · [[subfigure]] · [[tfg]]

Reescribir secciones de manual de usuario (cap 4, 4b) como prosa continua: explicar qué hace el usuario y por qué la app responde, citando figuras con `\ref` dentro del texto. Agrupar capturas relacionadas en una sola `figure` con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), un `\caption` general y `\subcaption` por subfigura. Eliminar cualquier frase que empiece por "La figura", "La captura", "En la imagen" seguida solo de descripción visual sin contexto de uso.

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[como-se-agrupan-capturas-con-subfigure]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
