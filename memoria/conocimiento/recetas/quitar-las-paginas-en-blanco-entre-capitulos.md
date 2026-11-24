---
tipo: "receta"
titulo: "Quitar las páginas en blanco entre capítulos"
temas: ["latex", "plantilla", "tfg", "memoria"]
claves: ["cleardoublepage", "openright", "página en blanco"]
proyectos: ["memoria-procesos"]
fuentes: ["include/extra.tex (memoria del Sprint 1)", "../../memoria/reglas-tfg.md"]
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

## Ampliación (2026-11-16, )
La memoria se entrega en PDF sin páginas en blanco entre capítulos. Esto implica configurar la clase de documento para que no inserte páginas en blanco (p. ej. usando `oneside` o `\let\cleardoublepage\clearpage` si la plantilla usa `openright`). El script `revisar_maquetacion.py` verifica automáticamente que no haya páginas vacías entre capítulos.

Relacionado: [[como-corregir-paginas-casi-vacias-regla-9-al-final-de-capitu]] · [[evitar-paginas-casi-vacias-regla-9]] · [[sin-paginas-casi-vacias-ni-secciones-sueltas-fundir-o-listar]] · [[reglas-de-maquetacion-de-javier-resumen-accionable]] · [[estilo-visual-global-titulos-negros-en-negrita-enlaces-sin-r]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
