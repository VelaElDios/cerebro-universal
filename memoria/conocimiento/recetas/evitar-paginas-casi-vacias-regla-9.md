---
tipo: "receta"
titulo: "Evitar páginas casi vacías (Regla 9)"
temas: ["latex", "maquetación", "reglas-tfg"]
claves: ["Regla 9", "página casi vacía", "sección corta"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[maquetación]] · [[reglas-tfg]]

Si una sección (o subsección) ocupa solo una o dos líneas al final de una página, fundirla con la sección anterior o convertirla en un ítem de una lista. En LaTeX, evitar `\clearpage` o `\cleardoublepage` innecesarios; usar `\section*` solo si es necesario y asegurarse de que haya suficiente contenido. Revisar el PDF página a página con `revisar_maquetacion.py`.

> Ninguna página casi vacía ni con una sección o una línea suelta: una sección de una o dos líneas se funde con otra o se convierte en un punto de una lista.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[corregir-paginas-con-una-sola-imagen-regla-8]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
