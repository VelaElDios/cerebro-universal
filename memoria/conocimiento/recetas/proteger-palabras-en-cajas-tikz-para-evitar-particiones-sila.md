---
tipo: "receta"
titulo: "Proteger palabras en cajas TikZ para evitar particiones silábicas"
temas: ["diagramas", "latex", "tikz"]
claves: ["text width", "mbox", "palabras partidas", "guion", "entity-relationship"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "verificado"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[diagramas]] · [[latex]] · [[tikz]]

|
  En nodos TikZ con `text width` fijo, LaTeX puede partir palabras largas con guion (p.ej. "eliminadas" → "dele-") violando regla 18.
  Soluciones por orden de preferencia:
  1. **Aumentar `text width`** del estilo del nodo (p.ej. 3.2cm → 3.5cm o 4.0cm) para que quepa la palabra más larga.
  2. **Proteger palabras críticas** con `\mbox{palabra}` o `\mbox{palabra larga}` en el texto del nodo.
  3. **Forzar salto manual** con `\\` en el texto del nodo antes de la palabra larga.
  4. **No usar** `\hyphenation{}` global ni `\uchyph=0` porque afectan a todo el documento.
  Ejemplo aplicado en fig:modelo-datos: `\texttt{email TEXT} \uk (único no \mbox{eliminadas})` y ensanchado `text width=3.5cm` / `5.0cm`.

> \texttt{email TEXT} \uk (único no \mbox{eliminadas})\\
> — `chapters/04-descripcion.tex`

Relacionado: [[replanteo-de-diagrama-de-secuencia-pgf-umlsd-para-evitar-des]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
