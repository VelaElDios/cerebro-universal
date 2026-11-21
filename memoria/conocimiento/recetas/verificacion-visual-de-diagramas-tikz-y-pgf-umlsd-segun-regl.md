---
tipo: "receta"
titulo: "Verificación visual de diagramas TikZ y pgf-umlsd según reglas 16-18"
temas: ["diagramas", "maquetacion", "pgf-umlsd", "tikz"]
claves: ["node distance", "codos", "flechas", "cruces", "letras diminutas", "participantes"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (reglas 16-18)"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[diagramas]] · [[maquetacion]] · [[pgf-umlsd]] · [[tikz]]

Para validar diagramas en PDF: 1) Abrir PDF y buscar páginas con diagramas. 2) Comprobar que no hay flechas cruzando cajas (usar codos |-/-|). 3) Medir tamaño de fuente en cajas y etiquetas: ≥8pt. 4) En diagramas de secuencia (pgf-umlsd): máx 6 participantes; si más, agrupar o partir. 5) Etiquetas de flechas fuera de cajas. 6) Si diagrama muy ancho, considerar pdflscape. 7) Corregir código TikZ/sequencediagram y recompilar hasta que pase revisión visual.

> Todo diagrama se lee bien a su tamaño en el PDF: las letras del dibujo, una vez escalado, nunca son más pequeñas que las del pie de figura (unos 8-9 pt). Ninguna línea ni flecha atraviesa una caja o un texto, y ninguna caja pisa a otra. Las flechas van de una caja a la siguiente (A → B, B → C), nunca de A a C pasando por encima de B.
> — `memoria/reglas-tfg.md (reglas 16-18)` (cita sin comprobar)

Relacionado: [[validacion-visual-de-diagramas-tikz-pgf-umlsd-en-pdf-reglas]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]] · [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]] · [[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
