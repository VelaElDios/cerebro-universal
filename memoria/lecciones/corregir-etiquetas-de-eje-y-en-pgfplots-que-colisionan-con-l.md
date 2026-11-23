---
titulo: "Corregir etiquetas de eje Y en pgfplots que colisionan con la gráfica"
temas: ["latex", "pgfplots", "maquetacion"]
claves: ["ylabel", "anchor", "xshift", "scale only axis", "enlarge x limits"]
estado: "propuesta"
veces: 1
fecha: "2026-11-23"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[pgfplots]] · [[maquetacion]]

## Problema
En los burndown charts (pgfplots), la etiqueta del eje Y («PBIs pendientes») y/o las marcas del eje Y quedaban demasiado cerca de la gráfica, causando que la línea de la gráfica o las marcas cruzaran el texto (regla 17: «ninguna línea ni flecha atraviesa una caja o un texto»).

## Solución
Añadir `ylabel style={anchor=east, xshift=-3pt}` para separar la etiqueta del eje, `scale only axis` para que width/height se refieran solo al área de la gráfica (sin etiquetas), y `enlarge x limits` para dar margen a los extremos. Esto mueve la etiqueta y las marcas fuera de la zona de la curva.

## Ejemplo
|
  \begin{axis}[
      width=0.95\linewidth,
      height=7cm,
      ylabel={PBIs pendientes},
      ylabel style={anchor=east, xshift=-3pt},
      scale only axis,
      enlarge x limits=0.05,
      ...
  ]
  \addplot coordinates {...};
  \end{axis}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
