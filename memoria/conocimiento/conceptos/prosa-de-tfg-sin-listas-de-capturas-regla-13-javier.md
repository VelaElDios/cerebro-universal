---
tipo: "concepto"
titulo: "Prosa de TFG sin listas de capturas (regla 13 Javier)"
temas: ["latex", "redacción", "tfg", "figuras"]
claves: ["subfigure", "prosa", "manual de usuario", "\\ref"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla 13)", "memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[redacción]] · [[tfg]]

Reescribir secciones de manual de usuario (cap 4, 4b) como prosa continua: explicar qué hace el usuario y por qué la app responde, citando figuras con \ref dentro del texto. Agrupar capturas relacionadas en una sola figure con subfigure (dos por fila, \begin{subfigure}{0.48\textwidth}), un \caption general y \subcaption por subfigura. Eliminar cualquier frase que empiece por "La figura", "La captura", "En la imagen" seguida solo de descripción visual sin contexto de uso.

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md (regla 13)` (cita sin comprobar)

## Ampliación (2026-11-22, memoria-procesos)
Cada figura y tabla se cita en el texto y se explica, no hay texto de relleno y el orden de las secciones sigue el de la plantilla. Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
relacionado: Cada imagen una sola vez (regla 10), Capturas máx. height=0.42\textheight (regla 8)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
