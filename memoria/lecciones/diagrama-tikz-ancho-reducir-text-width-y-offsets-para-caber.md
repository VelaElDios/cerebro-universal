---
titulo: "Diagrama TikZ ancho: reducir text width y offsets para caber en \\textwidth"
temas: ["latex", "tikz"]
claves: ["Overfull \\hbox", "tikzpicture", "text width"]
estado: "confirmada"
veces: 1
fecha: "2026-10-13"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tikz]]

## Problema
Un diagrama TikZ con nodos anchos (text width=4.0cm/5.5cm) y offsets horizontales (right=2.2cm, left=2.2cm) supera \textwidth (~15.5cm en esta plantilla), causando overfull hbox aunque el caption sea corto.

## Solución
Reducir text width de los nodos (p.ej. 3.2cm/4.5cm), reducir offsets horizontales (p.ej. 1.8cm), usar font=\footnotesize o \scriptsize en nodos y etiquetas, y comprobar que el diagrama completo quepa en \linewidth.

## Ejemplo
```latex
  \begin{tikzpicture}[
    node/.style={text width=3.2cm, font=\footnotesize, ...},
    nodewide/.style={text width=4.5cm, font=\footnotesize, ...},
    decision/.style={text width=2.2cm, font=\footnotesize, ...},
    arrow/.style={...}
  ]
    \node[node] (push) {...};
    \node[nodewide, below=0.7cm of push] (ci) {...};
    \node[decision, below=0.8cm of ci] (dec) {...};
    \node[node, below=0.8cm of dec] (deploy) {...};
    \node[node, right=1.8cm of deploy] (render) {...};
    \node[node, left=1.8cm of dec] (nodeploy) {...};
    \node[node, below=0.7cm of deploy] (done) {...};
  \end{tikzpicture}
```

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
