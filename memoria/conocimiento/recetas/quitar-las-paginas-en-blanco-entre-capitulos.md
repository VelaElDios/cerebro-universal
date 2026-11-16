---
tipo: "receta"
titulo: "Quitar las páginas en blanco entre capítulos"
temas: ["latex", "plantilla", "tfg"]
claves: ["cleardoublepage", "openright", "página en blanco"]
proyectos: ["memoria-procesos"]
fuentes: ["include/extra.tex (memoria del Sprint 1)"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[plantilla]] · [[tfg]]

La plantilla es `book` a doble cara: cada capítulo empieza en página impar y deja páginas en blanco. Para entregar en PDF, al final de `include/extra.tex`:

```latex
\renewcommand{\cleardoublepage}{\clearpage}
```

> Documento para leer en PDF: sin páginas en blanco entre capítulos
> — `include/extra.tex (memoria del Sprint 1)`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
