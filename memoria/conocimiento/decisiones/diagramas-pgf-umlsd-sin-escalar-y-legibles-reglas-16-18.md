---
tipo: "decision"
titulo: "Diagramas pgf-umlsd sin escalar y legibles (reglas 16-18)"
temas: ["latex", "pgf-umlsd", "tikz"]
claves: ["sequencediagram", "adjustbox", "resizebox", "text width", "node distance", "flechas codos"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (reglas 16-18) y revisión de Javier"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[tikz]]

1) Quitar adjustbox/resizebox. 2) ≤6 participantes por diagrama. 3) text width=2.5-3cm en \newthread/\newinst, font=\footnotesize. 4) node distance ≥1.2cm. 5) Flechas solo entre cajas vecinas (A→B, B→C) con codos (-|, |-) si hay que rodear. 6) Etiquetas cortas; guardas de alt en una palabra. 7) Nombres largos en dos líneas manuales (\\). 8) Si no cabe, partir en dos diagramas (frontend/backend) o usar pdflscape.

> Los diagramas se miran de verdad en el PDF: scripts/revisar_figuras.py mide cada diagrama con las coordenadas reales del PDF (líneas que pasan por encima de letras, cajas que se pisan, palabras partidas con guion, letras de menos de 7,5 pt) y, si eso pasa, Gemini lo mira además a ojo. No se arregla encogiendo el dibujo (adjustbox, resizebox, scale): eso deja las letras diminutas; hay que replantear el dibujo para que quepa a tamaño real.
> — `memoria/reglas-tfg.md (reglas 16-18) y revisión de Javier` (cita sin comprobar)

Relacionado: [[verificacion-visual-de-diagramas-tikz-y-pgf-umlsd-segun-regl]] · [[validacion-visual-de-diagramas-tikz-pgf-umlsd-en-pdf-reglas]] · [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
