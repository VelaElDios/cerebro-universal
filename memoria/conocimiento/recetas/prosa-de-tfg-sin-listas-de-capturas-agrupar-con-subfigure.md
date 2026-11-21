---
tipo: "receta"
titulo: "Prosa de TFG sin listas de capturas (agrupar con subfigure)"
temas: ["latex", "redaccion", "tfg", "figuras", "memoria"]
claves: ["subfigure", "subcaption", "La figura X muestra", "prosa"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[redaccion]] · [[tfg]]

Para evitar el estilo «lista de capturas», escribir párrafos narrativos que expliquen la interacción del usuario con la aplicación, citando las figuras dentro del texto con `\ref`. Cuando varias capturas ilustran un mismo flujo o pantalla relacionada, agruparlas en una sola figura `figure` con entorno `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura. Ejemplo en `04-descripcion.tex` (Figuras `fig:app-inicio-registro`, `fig:app-errores-acceso`, `fig:app-perfil-baja`, `fig:app-admin-full`, `fig:app-responsive`, `fig:app-estados-especiales`, `fig:hito4-flujo`, `fig:hito4-estados-privacidad`) y en `04b-juego.tex` (Figuras `fig:juego-menu-vestuario`, `fig:juego-partida-mejora`, `fig:juego-jefe-ambiente`, `fig:juego-fin-pausa`, `fig:juego-club-pantallas-a`, `fig:juego-club-pantallas-b`).

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md`

Relacionado: [[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]] · [[prosa-de-tfg-nada-de-la-figura-x-muestra-suelto-agrupar-capt]] · [[prosa-de-tfg-vs-lista-de-capturas-regla-13-javier]] · [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]]

## Ampliación (2026-11-21, memoria-procesos)
En la memoria final, las capturas de la aplicación (app/, hito4/, juego/) y de DoneTonic se agrupan en figuras con `subfigure` (dos por fila, `\begin{subfigure}{0.48\textwidth}`) con caption general y subcaptions. El texto explica el flujo de uso citando las figuras dentro de la prosa, no como frases sueltas. Cada imagen aparece una sola vez en el sitio donde más sentido tiene; en el resto se cita con `\ref`.
relacionado: Cada entrega solo lleva lo de su sprint (alcance coherente)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
