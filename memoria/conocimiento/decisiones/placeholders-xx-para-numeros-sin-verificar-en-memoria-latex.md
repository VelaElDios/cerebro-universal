---
tipo: "decision"
titulo: "Placeholders \"XX\" para números sin verificar en memoria LaTeX"
temas: ["latex", "memoria-procesos", "placeholders", "verificacion"]
claves: ["XX", "placeholder", "números", "verificar", "fuentes"]
proyectos: ["memoria-procesos"]
fuentes: ["experiencia del revisor en este proyecto"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[latex]] · [[memoria-procesos]] · [[placeholders]] · [[verificacion]]

Cuando las fuentes no están disponibles para verificar un número:
- Escribir "XX" en el texto LaTeX (visible en PDF, obliga a corregir)
- Añadir comentario `% TODO: verificar en <fuente> §<sección>` en la línea
- NO compilar versión final con placeholders; son solo para desarrollo
- El revisor debe rechazar cualquier entrega con placeholders sin resolver
- Ejemplo: `\item \textbf{Sprint 1} ... con XX PBIs (P1--P19) y XX tareas (T1--T32) % TODO: verificar en gestion/README.md`

> He reemplazado 19/32/29/50/48/82 por XX en chapters/01-introduccion.tex y chapters/03-propuesta.tex
> — `experiencia del revisor en este proyecto` (cita sin comprobar)

Relacionado: [[numeros-pequenos-tambien-se-verifican-en-fuentes]] · [[como-manejar-fuentes-faltantes-en-verificacion-automatica-de]] · [[numeros-en-la-memoria-deben-aparecer-tal-cual-en-las-fuentes]] · [[cada-cifra-del-documento-sale-de-las-fuentes-tambien-las-peq]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
