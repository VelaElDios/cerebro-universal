---
tipo: "receta"
titulo: "Cómo corregir solapes en diagramas de secuencia pgf-umlsd"
temas: ["latex", "maquetacion", "pgf-umlsd", "sequencediagram", "tikz"]
claves: ["sdblock", "alt", "call", "mess", "solape", "flechas", "lineas divisorias"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/proyectos/memoria-procesos/chapters/04-descripcion.tex (fig:sec-baja)"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]] · [[sequencediagram]] · [[tikz]]

Para evitar que las líneas divisorias de bloques `sdblock` (alternativas `alt`) corten flechas o cajas en diagramas `sequencediagram` de `pgf-umlsd`: (1) Añadir mensajes vacíos `\mess{}{}{}` entre la última llamada real y el `sdblock` para crear espacio vertical. (2) Usar `\newinst[1]` o `[2]` para reducir separación horizontal entre participantes (máx. 6). (3) Nombres y mensajes cortos (2-3 palabras). (4) Si no cabe, partir en dos diagramas (éxito / error). (5) Nunca usar `resizebox`, `adjustbox` ni `scale`: encogen las letras por debajo de 7,5 pt. El diagrama `fig:sec-baja` se corrigió así.

> Espacio vertical para que la línea divisoria del bloque alt no corte la llamada anterior: \mess{vis}{ }{api} antes del sdblock.
> — `memoria/proyectos/memoria-procesos/chapters/04-descripcion.tex (fig:sec-baja)` (cita sin comprobar)

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd-entorno-sequencediagram]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
