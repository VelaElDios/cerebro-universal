---
tipo: "receta"
titulo: "Cómo evitar overfull hbox en rutas y diagramas"
temas: ["latex", "maquetación"]
claves: ["overfull", "hbox", "path", "allowbreak", "sequencediagram", "longtable"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla: nada fuera del margen) y lecciones de la memoria"]
confianza: "propuesto"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[maquetación]]

Al escribir rutas de archivos, nombres de módulos o mensajes en diagramas, insertar \allowbreak en los separadores naturales (., /, _, -). En longtable, usar columnas p{} con anchos que sumen ≤ \linewidth y evitar comandos que generen cajas irrompibles. En sequencediagram, usar \small, máx. 6 participantes, nombres cortos, y mensajes sin paréntesis ni comandos LaTeX.
relacionado: Una cita con autor largo se sale del margen: breakcites, Los identificadores largos en \texttt no se parten solos: usar \allowbreak dentro del comando

> Los identificadores largos en \texttt no se parten solos: usar \allowbreak dentro del comando
> — `memoria/reglas-tfg.md (regla: nada fuera del margen) y lecciones de la memoria` (cita sin comprobar)

Relacionado: [[como-evitar-overfull-hbox-con-texttt-largo-en-longtable]] · [[como-evitar-overfull-hbox-con-texttt-largo]] · [[dentro-de-cajas-no-se-parten-palabras-ni-rutas-text-width-ma]] · [[como-evitar-overfull-hbox-en-tablas-anchas-con-longtable]] · [[corregir-overfull-hbox-en-longtable-con-urls-largas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
