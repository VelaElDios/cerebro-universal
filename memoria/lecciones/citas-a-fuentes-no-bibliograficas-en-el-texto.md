---
titulo: "Citas a fuentes no bibliográficas en el texto"
temas: ["latex", "bibliografia", "referencias"]
claves: ["\\cite{neonlimits}", "\\cite{documentacion-tecnica}", "undefined citation"]
estado: "propuesta"
veces: 1
fecha: "2026-10-30"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[bibliografia]] · [[referencias]]

## Problema
Se usaron \cite{} para referenciar URLs o archivos del repositorio que no son entradas bibliográficas válidas en bib/ref.bib. El test exige que toda cita exista en el .bib y que toda URL en el .bib esté en las fuentes.

## Solución
Para referenciar documentación interna o URLs de proyectos, usar referencias textuales (p. ej., «según la documentación técnica del proyecto» o «véase docs/documentacion-tecnica.md») en lugar de \cite{}. Reservar \cite{} solo para entradas del .bib (libros, RFCs, webs oficiales).

## Ejemplo
En lugar de \cite{documentacion-tecnica}, escribir: «según la documentación técnica del proyecto (docs/documentacion-tecnica.md)».

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
