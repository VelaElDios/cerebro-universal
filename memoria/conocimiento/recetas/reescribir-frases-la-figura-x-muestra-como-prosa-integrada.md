---
tipo: "receta"
titulo: "Reescribir frases «La figura X muestra…» como prosa integrada"
temas: ["latex", "redaccion", "tfg"]
claves: ["Regla 13", "La figura X muestra", "subfigure", "cita integrada"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04b-juego.tex"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[latex]] · [[redaccion]] · [[tfg]]

En lugar de frases sueltas que solo citan la figura («La figura X muestra…»), escribe un párrafo que explique qué hace el usuario y qué se ve en la interfaz, citando la figura (y subfiguras) dentro de la explicación. Usa `subfigure` para agrupar capturas relacionadas (dos por fila, `\begin{subfigure}{0.48\textwidth}`) con un caption general y uno por subfigura.

> La Figura~\ref{fig:juego-menu-vestuario} muestra el menú principal (subfigura~\ref{fig:juego-menu}) y el vestuario (subfigura~\ref{fig:juego-vestuario}). En el menú principal, el jugador ve su avatar paseando, su ficha con mote, avatar y mejores tiempos, y el menú lateral con las opciones de juego.
> — `chapters/04b-juego.tex` (cita sin comprobar)

Relacionado: [[frases-prohibidas-la-figura-x-muestra-regla-13-reescribir-co]] · [[agrupar-capturas-con-subfigure]] · [[como-se-agrupan-capturas-con-subfigure]] · [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]] · [[prosa-de-tfg-sin-listas-de-capturas-agrupar-con-subfigure]] · [[prosa-de-tfg-nada-de-la-figura-x-muestra-suelto-agrupar-capt]] · [[prosa-de-tfg-vs-lista-de-capturas]] · [[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
