---
tipo: "receta"
titulo: "Cómo mover una figura antes de su primera referencia en LaTeX"
temas: ["figuras", "latex", "maquetación"]
claves: ["fig:juego-arquitectura", "referencia indefinida", "float"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04b-juego.tex"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[figuras]] · [[latex]] · [[maquetación]]

Cuando una figura se referencia antes de su definición y flota después, LaTeX genera "Referencia indefinida" y "??". Solución: mover el entorno `figure` completo (con su `\label`) ANTES del primer `\ref` en el texto. Usar `[htbp]` y parámetros de flotantes relajados (`\topfraction`, `\bottomfraction`, etc. en preámbulo) para que comparta página con el texto. Si la figura es grande, envolver en `adjustbox{max width=\linewidth, max totalheight=0.6\textheight}` para que no ocupe página entera.

> La separación en tres bloques es la que se ve en la Figura~\ref{fig:juego-arquitectura}: la simulación determinista...
> — `chapters/04b-juego.tex` (cita sin comprobar)

Relacionado: [[fijar-colocacion-de-figura-referenciada-con-floatbarrier]] · [[como-fijar-colocacion-de-figura-referenciada-pero-no-apareci]] · [[figuras-que-comparten-pagina-con-el-texto-parametros-de-flot]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
