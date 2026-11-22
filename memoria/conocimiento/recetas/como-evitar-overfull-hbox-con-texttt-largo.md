---
tipo: "receta"
titulo: "Cómo evitar overfull hbox con \\texttt largo"
temas: ["latex", "maquetación"]
claves: ["overfull", "hbox", "\\texttt", "\\allowbreak", "\\path"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla 6) y lecciones del cerebro"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[maquetación]]

Insertar \allowbreak en puntos naturales (tras punto, barra, dos puntos) dentro de \texttt. Ejemplo: \texttt{accountConfirmation\allowbreak.test.js} y \texttt{POST\allowbreak /api/\allowbreak prueba/\allowbreak dominio}. Para URLs, usar \path{} de xurl (ya cargado) que permite cortes en cualquier carácter.

> Los identificadores largos en \texttt no se parten solos: usar \allowbreak dentro del comando
> — `memoria/reglas-tfg.md (regla 6) y lecciones del cerebro` (cita sin comprobar)

Relacionado: [[como-evitar-overfull-hbox-con-texttt-largo-en-longtable]] · [[como-evitar-overfull-hbox-en-rutas-y-diagramas]] · [[dentro-de-cajas-no-se-parten-palabras-ni-rutas-text-width-ma]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
