---
tipo: "receta"
titulo: "Fijar colocación de figura referenciada con FloatBarrier"
temas: ["figuras", "latex", "maquetacion"]
claves: ["FloatBarrier", "placeins", "figura no aparece", "referencia cruzada"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04b-juego.tex"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]]

|
  Cuando una figura flotante (figure) se referencia con \ref pero el algoritmo de LaTeX la coloca páginas después:
  1. Cargar `placeins` (ya en include/extra.tex).
  2. Poner `\FloatBarrier` **justo antes** del primer párrafo que contiene `\ref{fig:...}`.
  3. Alternativamente, mover el entorno `figure` inmediatamente antes de esa referencia.
  4. Esto obliga a LaTeX a vaciar la cola de flotantes pendientes antes de continuar, garantizando que la figura aparezca en la misma página o anterior a la referencia.
  5. No abusar: cada FloatBarrier fuerza salto de página si hay muchas figuras; usarlo solo donde la referencia esté lejos de la figura en el fuente.

> \FloatBarrier\n\nLa separación en tres bloques es la que se ve en la Figura~\ref{fig:juego-arquitectura}...
> — `chapters/04b-juego.tex` (cita sin comprobar)


Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
