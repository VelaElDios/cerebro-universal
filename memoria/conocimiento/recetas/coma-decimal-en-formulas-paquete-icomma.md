---
tipo: "receta"
titulo: "Coma decimal en fórmulas: paquete icomma"
temas: ["coma decimal", "icomma", "latex", "matematicas"]
claves: ["icomma", "coma decimal", "30", "28", "modo matematico"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/lecciones.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[coma decimal]] · [[icomma]] · [[latex]] · [[matematicas]]

En español, los decimales se escriben con coma (30,28). Sin icomma, en modo matemático $30,28$ sale como $30, 28$ (con espacio). La solución es cargar \usepackage{icomma} en el preámbulo (ya está en include/extra.tex). Al escribir números decimales en el texto, usar siempre coma: 30,28 no 30.28.

> Cargar \usepackage{icomma}: la coma seguida de un dígito no lleva espacio. Y para escribir decimales desde Lua, usar una función que cambie el punto por coma (en español no vale 38.8).
> — `memoria/lecciones.md` (cita sin comprobar)

Relacionado: [[bibliografia-gestionada-con-bibtex-en-la-memoria-tfg]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
