---
tipo: "decision"
titulo: "Una sola imagen por captura en toda la memoria (regla 10 Javier)"
temas: ["duplicados", "figuras", "ref", "reglas-javier", "latex", "maquetacion", "memoria-procesos"]
claves: ["imagen repetida", "\\ref", "una sola vez", "capturas duplicadas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 10)"]
confianza: "verificado"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[duplicados]] · [[figuras]] · [[ref]] · [[reglas-javier]]

Buscar en todo el documento (`grep -r "includegraphics" chapters/`) cada archivo de imagen. Cada archivo debe aparecer en `\includegraphics` exactamente una vez. En los demás capítulos, reemplazar `\includegraphics{...}` por `\ref{fig:etiqueta-original}`. Prioridad: decidir dónde tiene más sentido cada captura (cap 4, 5, anexos) y mantenerla solo allí. Las capturas de DoneTonic, producción y prueba técnica son las que más riesgo tienen de duplicarse.

> Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone \ref a la figura que ya existe.
> — `memoria/reglas-tfg.md`

## Ampliación (2026-11-20, memoria-procesos)
Lista de capturas y su ubicación canónica: fig:donetonic-tablero (cap 3), fig:donetonic-graficas-s1 (cap 3), fig:donetonic-backlog (cap 3), fig:donetonic-s2-graficas (anexo A1), fig:donetonic-s2-tablero (anexo A1), fig:donetonic-s2-detalle (anexo A1), fig:actions-verde (cap 5), fig:correo-confirmacion (cap 5), fig:google-publicada (cap 5), fig:prueba-tecnica (cap 5), fig:produccion-verificacion (cap 5).

## Ampliación (2026-11-20, memoria-procesos)
Inventario de capturas por carpeta (mínimos spec): app/ (4), hito4/ (4), juego/ (8), donetonic/ (5), produccion/ (2), prueba-tecnica/ (1). Cada archivo físico en `figs/capturas/` debe usarse una sola vez en el documento.
relacionado: Prosa de TFG sin cadenas "La figura X muestra..." (regla 13 Javier), Capturas agrupadas en subfigure

Relacionado: [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[una-imagen-en-un-solo-sitio-y-en-el-resto-una-referencia]] · [[sin-figuras-repetidas-usar-ref-a-la-figura-existente]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
