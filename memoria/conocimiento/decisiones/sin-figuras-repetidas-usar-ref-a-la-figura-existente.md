---
tipo: "decision"
titulo: "Sin figuras repetidas: usar \\ref a la figura existente"
temas: ["figuras", "latex", "memoria", "tfg", "maquetacion"]
claves: ["figuras repetidas", "ref", "cita cruzada"]
proyectos: ["memoria-procesos"]
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-24"
---

Temas: [[figuras]] · [[latex]] · [[memoria]] · [[tfg]]

Cada archivo de imagen se incluye una única vez en el documento. Para referenciarla en otro capítulo/sección, usar `\ref{etiqueta}` (y `\autoref`/`\cref` si se usa `cleveref`). No volver a hacer `\includegraphics` del mismo archivo.

> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone `\ref` a la figura que ya existe.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]] · [[como-centralizar-capturas-duplicadas-entre-capitulos-en-late]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]]

## Ampliación (2026-11-24, memoria-procesos)
Ejemplo: La captura del correo de confirmación (fig:correo-confirmacion) se muestra solo en Capítulo 5 (Evaluación). En Capítulo 4 se escribe: «el correo de confirmación transaccional se recibió correctamente en un buzón de Gmail (Figura~\ref{fig:correo-confirmacion}, Capítulo~\ref{cap:evaluacion})».
