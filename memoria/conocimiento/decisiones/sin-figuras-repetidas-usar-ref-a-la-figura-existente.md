---
tipo: "decision"
titulo: "Sin figuras repetidas: usar \\ref a la figura existente"
temas: ["figuras", "latex", "memoria", "tfg"]
claves: ["figuras repetidas", "ref", "cita cruzada"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[figuras]] · [[latex]] · [[memoria]] · [[tfg]]

Cada archivo de imagen se incluye una única vez en el documento. Para referenciarla en otro capítulo/sección, usar `\ref{etiqueta}` (y `\autoref`/`\cref` si se usa `cleveref`). No volver a hacer `\includegraphics` del mismo archivo.

> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone `\ref` a la figura que ya existe.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]] · [[como-centralizar-capturas-duplicadas-entre-capitulos-en-late]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]]
