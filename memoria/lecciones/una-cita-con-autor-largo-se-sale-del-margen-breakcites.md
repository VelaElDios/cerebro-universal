---
titulo: "Una cita con autor largo se sale del margen: breakcites"
temas: ["latex", "bibtex"]
claves: ["Overfull \\hbox", "se sale", "[[]]", "cite"]
estado: "confirmada"
veces: 1
fecha: "2026-10-13"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[bibtex]]

## Problema
LaTeX mete cada cita en una caja que no se puede partir. Con autores largos («[Universidad de Castilla-La Mancha, 2026]»)
la cita no cabe al final de una línea y se sale del margen: el log dice «Overfull \hbox (70pt too wide) in paragraph»
y muestra el texto con la cita como «[[]]». Ensanchar tablas o figuras no lo arregla: no son ellas.

## Solución
Cargar `breakcites` (después de hyperref), que deja partir las citas entre líneas. Para encontrar el culpable, leer las
líneas del log justo después del aviso «Overfull»: muestran el texto que se sale.

## Ejemplo
```latex
% Citas que se pueden partir entre líneas
\usepackage{breakcites}
```

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
