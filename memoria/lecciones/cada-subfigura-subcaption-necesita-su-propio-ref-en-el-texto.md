---
titulo: "Cada subfigura (\\subcaption) necesita su propio \\ref en el texto"
temas: ["latex", "subcaption", "subfigure", "verificar"]
claves: ["no se cita en el texto", "fig:prueba-tecnica-permitido", "subcaption", "label en subfigura"]
estado: "propuesta"
veces: 1
fecha: "2026-11-23"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[subcaption]] · [[subfigure]] · [[verificar]]

## Problema
verificar.py exige que cada \label tenga su \ref en el texto, incluidas las subfiguras de un \subcaption; citar solo la figura general (fig:prueba-tecnica) no basta y falla con «la figura fig:... no se cita en el texto»

## Solución
en la prosa, citar cada subfigura con su propio \ref: «la subfigura~\ref{fig:app-inicio} muestra…», además del \ref de la figura general

## Ejemplo
«Las dos capturas de la Figura~\ref{fig:prueba-tecnica} documentan la respuesta: la subfigura~\ref{fig:prueba-tecnica-permitido} muestra \texttt{permitido: true} y la subfigura~\ref{fig:prueba-tecnica-rechazado} \texttt{permitido: false}.»

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
