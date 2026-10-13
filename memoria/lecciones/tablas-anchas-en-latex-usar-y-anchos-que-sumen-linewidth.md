---
titulo: "Tablas anchas en LaTeX: usar @{} y anchos que sumen ≤ \\linewidth"
temas: ["latex", "tablas"]
claves: ["se sale", "del margen", "Overfull \\hbox"]
estado: "confirmada"
veces: 1
fecha: "2026-10-13"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tablas]]

## Problema
Las tablas con columnas L{...} sumaban más de \linewidth (≈15.5cm en esta plantilla), causando desbordamiento horizontal. El paquete `array` con `L{...}` añade padding lateral que suma al ancho total.

## Solución
Usar `@{}L{...}@{}` en la definición de la tabla (o `@{}` al inicio y final del preámbulo tabular) para eliminar el padding lateral, y reducir anchos de columna para que la suma sea ≤ \linewidth (p.ej., 13–14cm). Alternativamente, envolver en `\begin{adjustwidth}{-1cm}{-1cm}` o usar `\small`/`\footnotesize`.

## Ejemplo
```latex
\begin{tabular}{@{}L{1.5cm} L{8.0cm} L{3.5cm}@{}} ... \end{tabular}
```

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
