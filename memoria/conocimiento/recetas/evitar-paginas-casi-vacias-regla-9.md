---
tipo: "receta"
titulo: "Evitar páginas casi vacías (Regla 9)"
temas: ["latex", "maquetación", "reglas-tfg", "maquetacion"]
claves: ["Regla 9", "página casi vacía", "sección corta"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-17"
---

Temas: [[latex]] · [[maquetación]] · [[reglas-tfg]]

Si una sección (o subsección) ocupa solo una o dos líneas al final de una página, fundirla con la sección anterior o convertirla en un ítem de una lista. En LaTeX, evitar `\clearpage` o `\cleardoublepage` innecesarios; usar `\section*` solo si es necesario y asegurarse de que haya suficiente contenido. Revisar el PDF página a página con `revisar_maquetacion.py`.

> Ninguna página casi vacía ni con una sección o una línea suelta: una sección de una o dos líneas se funde con otra o se convierte en un punto de una lista.
> — `memoria/reglas-tfg.md`

Relacionado: [[corregir-paginas-con-una-sola-imagen-regla-8]]

## Ampliación (2026-11-16, memoria-procesos)
Si una sección (subsubsection, subsection) tiene solo 1–2 líneas de texto, no merece ser sección independiente. Opciones: (1) fusionar con la sección anterior añadiendo su contenido como párrafo; (2) convertir en un ítem de una lista enumerada o con viñetas; (3) si es un anexo con solo una tabla/figura, moverla al capítulo principal y dejar el anexo solo con la referencia. En la memoria: la página 100 (8 palabras) probablemente es una subsección de una línea en conclusiones o anexos; se fusionará en Paso 6.

## Ampliación (2026-11-16, memoria-procesos)
Si una sección tiene menos de 3-4 líneas de texto real, fundirla con la anterior o siguiente, o convertirla en un item de lista. Revisar el PDF página a página tras compilar. Las secciones de 1-2 líneas delatan un trabajo poco profesional.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
