---
tipo: "receta"
titulo: "Corregir etiquetas de eje Y en pgfplots que colisionan con la gráfica"
temas: ["latex", "maquetacion", "pgfplots"]
claves: ["ylabel", "anchor", "xshift", "scale only axis", "enlarge x limits"]
proyectos: ["memoria-procesos"]
fuentes: ["experiencia de corrección en este proyecto (fig:burndown-s1, fig:burndown-s2)"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[maquetacion]] · [[pgfplots]]

|
  Añadir en el entorno `axis`:
  ```latex
  ylabel style={anchor=east, xshift=-3pt},
  scale only axis,
  enlarge x limits=0.05,
  ```
  - `ylabel style={anchor=east, xshift=-3pt}`: separa la etiqueta del eje Y hacia la izquierda.
  - `scale only axis`: hace que `width` y `height` se refieran solo al área de la gráfica (sin etiquetas ni marcas), evitando que la gráfica se encoja y las etiquetas choquen.
  - `enlarge x limits`: da un pequeño margen en los extremos del eje X para que la primera/última marca no quede pegada al borde.
  Esto mueve la etiqueta y las marcas fuera de la zona de la curva, cumpliendo la regla 17.
relacionado: Inventario de diagramas obligatorios y su estado actualizado

> En los burndown charts (pgfplots), la etiqueta del eje Y («PBIs pendientes») y/o las marcas del eje Y quedaban demasiado cerca de la gráfica, causando que la línea de la gráfica o las marcas cruzaran el texto (regla 17: «ninguna línea ni flecha atraviesa una caja o un texto»).
> — `experiencia de corrección en este proyecto (fig:burndown-s1, fig:burndown-s2)` (cita sin comprobar)

Relacionado: [[burndown-real-con-pgfplots-fig-burndown-s1-y-fig-burndown-s2]] · Cómo replantear diagramas TikZ/pgf-umlsd para pasar revisar_maquetacion.py (reglas 16-18) · [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]] · [[los-diagramas-nunca-se-escalan-para-que-quepan]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
