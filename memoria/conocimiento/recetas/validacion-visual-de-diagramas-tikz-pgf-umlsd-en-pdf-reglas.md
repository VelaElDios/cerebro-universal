---
tipo: "receta"
titulo: "Validación visual de diagramas TikZ/pgf-umlsd en PDF (reglas 16-18 Javier)"
temas: ["diagramas", "pgf-umlsd", "reglas-javier", "tikz", "validacion-visual", "latex"]
claves: ["reglas 16-18", "letras diminutas", "flechas cruzan cajas", "participantes >6", "node distance", "codos |- -|"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "memoria/reglas-tfg.md (reglas 16-18)"]
confianza: "verificado"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[diagramas]] · [[pgf-umlsd]] · [[reglas-javier]] · [[tikz]] · [[validacion-visual]]

Para cada diagrama dibujado (TikZ o sequencediagram), abrir el PDF y comprobar: (1) Letras ≥8pt (comparar con pie de figura). (2) Flechas van de caja en caja (A→B, B→C), nunca atraviesan una caja intermedia; usar codos `|-` o `-|` y `node distance` suficiente. (3) Etiquetas de flechas no se montan sobre cajas ni líneas verticales. (4) Diagramas de secuencia: máx 6 participantes; si hay más, agrupar o partir en dos. (5) Cajas no se pisan; `text width` suficiente o texto en dos líneas con `\\`. (6) Si el diagrama ocupa casi una página, envolver en `adjustbox{max width=\textwidth,max totalheight=0.6\textheight}`. Si falla algo, corregir el código TikZ/sequencediagram, no discutir con el validador.

> **Todo diagrama se lee bien a su tamaño en el PDF:** las letras del dibujo, una vez escalado, nunca son más pequeñas que las del pie de figura (unos 8-9 pt). Si para que quepa hay que encogerlo tanto que las letras quedan diminutas, el diagrama está mal planteado:
> — `memoria/reglas-tfg.md`

Relacionado: [[diagrama-tikz-ancho-reducir-text-width-y-offsets-para-caber]] · [[verificacion-visual-de-diagramas-tikz-y-pgf-umlsd-segun-regl]] · Cómo corregir diagramas de secuencia pgf-umlsd para pasar reglas 16-18 de Javier · [[arreglo-de-diagramas-segun-reglas-16-18-de-javier-feedback-1]] · Cómo replantear diagramas TikZ/pgf-umlsd para pasar revisar_maquetacion.py (reglas 16-18)

## Ampliación (2026-11-20, memoria-procesos)
Checklist por diagrama: 
- fig:capas (TikZ): 10 nodos → agrupar "Frontend" (ui+cli+game) y "Servidor" (api+srv+repo+int+rules) → 2 columnas; aumentar right=8.5cm a 10cm; text width 3.5→3.0cm; font=\small→\footnotesize.
- fig:modelo-datos (TikZ): 4 entidades; right=11cm → 12cm; below=3.5cm → 4cm; text width 5.2cm → 4.8cm; font=\small.
- fig:sec-login (sequencediagram): 5 participantes OK; verificar \resizebox y adjustbox max totalheight=0.6\textheight.
- fig:sec-google (sequencediagram): 6 participantes OK; mismo ajuste.
- fig:sec-baja (sequencediagram): 5 participantes OK; mismo ajuste.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
