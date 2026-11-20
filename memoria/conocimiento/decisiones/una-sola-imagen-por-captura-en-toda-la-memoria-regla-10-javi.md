---
tipo: "decision"
titulo: "Una sola imagen por captura en toda la memoria (regla 10 Javier)"
temas: ["duplicados", "figuras", "ref", "reglas-javier"]
claves: ["imagen repetida", "\\ref", "una sola vez", "capturas duplicadas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[duplicados]] · [[figuras]] · [[ref]] · [[reglas-javier]]

Buscar en todo el documento (`grep -r "includegraphics" chapters/`) cada archivo de imagen. Cada archivo debe aparecer en `\includegraphics` exactamente una vez. En los demás capítulos, reemplazar `\includegraphics{...}` por `\ref{fig:etiqueta-original}`. Prioridad: decidir dónde tiene más sentido cada captura (cap 4, 5, anexos) y mantenerla solo allí. Las capturas de DoneTonic, producción y prueba técnica son las que más riesgo tienen de duplicarse.

> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
