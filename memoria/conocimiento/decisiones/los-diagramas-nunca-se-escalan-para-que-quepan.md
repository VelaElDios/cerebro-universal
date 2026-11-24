---
tipo: "decision"
titulo: "Los diagramas nunca se escalan para que quepan"
temas: ["diagramas", "latex", "pgf-umlsd", "reglas-tfg"]
claves: []
proyectos: []
fuentes: ["Javier"]
confianza: "verificado"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[diagramas]] · [[latex]] · [[pgf-umlsd]] · [[reglas-tfg]]

Los diagramas (TikZ, pgf-umlsd y pgfplots) nunca se meten en \resizebox, adjustbox ni scale para que quepan: eso deja las letras por debajo de 7,5 pt y revisar_figuras.py lo rechaza (reglas 16 y 19 de memoria/reglas-tfg.md). Tienen que caber a tamaño real.
En un diagrama de secuencia (pgf-umlsd) se consigue con poca separación entre participantes (\newinst[1] o \newinst[2]; con [4] o [5] se sale del margen), nombres de participantes cortos (Servicio, Repositorio), mensajes de 2-3 palabras y como mucho 6 participantes. Si aun así no cabe, se parte en dos diagramas.
Ejemplo probado en memoria-procesos (24/11/2026): fig:sec-partida, con 5 participantes y \newinst[2] para el primero y [1] para el resto, cabe sin escalar y pasa la prueba completa.

> Los diagramas (TikZ, pgf-umlsd y pgfplots) nunca se meten en \resizebox, adjustbox ni scale para que quepan: eso deja las letras por debajo de 7,5 pt y revisar_figuras.py lo rechaza (reglas 16 y 19 de memoria/reglas-tfg.md).
> — `Javier`
