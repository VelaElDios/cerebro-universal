---
tipo: "receta"
titulo: "Diagrama TikZ ancho: reducir text width y offsets para caber en \\textwidth"
temas: ["diagrama", "latex", "tikz"]
claves: ["text width", "node distance", "overfull hbox", "adjustbox"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[diagrama]] · [[latex]] · [[tikz]]

Un diagrama TikZ con nodos anchos y offsets horizontales supera \textwidth causando overfull hbox. Solución: reducir text width de los nodos (p.ej. 3.2cm/4.5cm), reducir offsets horizontales (p.ej. 1.8cm), usar font=\footnotesize o \scriptsize en nodos y etiquetas, y comprobar que el diagrama completo quepa en \linewidth.

> node/.style={text width=3.5cm, ...}, right=8.5cm of ui
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Relacionado: [[directlua-no-funciona-dentro-del-texto-de-un-node-usar-macro]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
