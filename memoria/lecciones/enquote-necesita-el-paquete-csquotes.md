---
titulo: "\\enquote necesita el paquete csquotes"
temas: ["latex", "beamer"]
claves: ["enquote", "csquotes", "Undefined control sequence"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[beamer]]

## Problema
`\enquote{...}` da `Undefined control sequence` si el documento no carga `csquotes` (pasó en las diapositivas Beamer, que tenían su propio preámbulo).

## Solución
Añadir `\usepackage{csquotes}`. Cada documento con su propio preámbulo (anexo, diapositivas...) lo necesita por separado.

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
