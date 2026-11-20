---
tipo: "decision"
titulo: "Prosa de TFG sin cadenas «La figura X muestra…» (regla 13 Javier)"
temas: ["figuras", "redaccion", "reglas-javier", "subfigure", "tfg", "latex", "memoria", "maquetacion"]
claves: ["La figura X muestra", "prosa", "subfigure", "caption general", "subcaption"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 13)"]
confianza: "verificado"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[figuras]] · [[redaccion]] · [[reglas-javier]] · [[subfigure]] · [[tfg]]

Reescribir secciones de manual de usuario (cap 4, 4b) como prosa continua: explicar qué hace el usuario y por qué la app responde, citando figuras con `\ref` dentro del texto. Agrupar capturas relacionadas en una sola `figure` con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), un `\caption` general y `\subcaption` por subfigura. Eliminar cualquier frase que empiece por "La figura", "La captura", "En la imagen" seguida solo de descripción visual sin contexto de uso.

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md`

Relacionado: [[como-se-agrupan-capturas-con-subfigure]] · [[reescribir-frases-la-figura-x-muestra-como-prosa-integrada]] · [[prosa-de-tfg-vs-lista-de-capturas-regla-13-javier]] · [[prosa-de-tfg-vs-lista-de-capturas]]

## Ampliación (2026-11-20, memoria-procesos)
Ejemplo correcto en cap 4: subfiguras fig:app-inicio-registro, fig:app-errores-acceso, fig:app-perfil-baja, fig:app-admin-full, fig:app-responsive, fig:app-estados-especiales, fig:hito4-flujo, fig:hito4-admin-estados-privacidad. Cada una agrupa 2-4 capturas relacionadas con prosa que las integra.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
