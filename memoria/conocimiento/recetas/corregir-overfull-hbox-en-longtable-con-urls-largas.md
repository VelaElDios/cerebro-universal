---
tipo: "receta"
titulo: "Corregir overfull hbox en longtable con URLs largas"
temas: ["latex", "overfull", "tablas"]
claves: ["overfull hbox", "\\allowbreak", "longtable", "URLs"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/a4-trazabilidad.tex"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[latex]] · [[overfull]] · [[tablas]]

En `longtable`, las URLs en celdas `p{}` o `L{}` no se parten aunque haya `\emergencystretch`. Solución: insertar `\allowbreak` en puntos naturales de la URL (tras `/`, `.`, `:`). Ejemplo: `\texttt{https://github.com/\allowbreak VelaElDios/\allowbreak la-grada-colchonera-saas/\allowbreak pull/\allowbreak 56}`. El espacio tras `\allowbreak` se ignora si no se parte. También funciona dentro de `\path{}` o `\url{}` si se usa `\UrlBreaks` extendido en preámbulo (ya está en include/extra.tex).

> Overfull hbox en a4-trazabilidad.tex líneas 206-207 y 377-378
> — `chapters/a4-trazabilidad.tex` (cita sin comprobar)

Relacionado: [[como-evitar-overfull-hbox-con-texttt-largo-en-longtable]] · [[como-evitar-overfull-hbox-en-rutas-y-diagramas]] · [[como-evitar-overfull-hbox-en-tablas-anchas-con-longtable]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
