---
tipo: "receta"
titulo: "Cómo evitar overfull hbox con \\texttt largo en longtable"
temas: ["latex", "longtable", "overfull"]
claves: ["overfull", "hbox", "\\texttt", "\\allowbreak", "longtable"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[longtable]] · [[overfull]]

En las tablas tab:rnf, tab:modulos, tab:api, añadir \allowbreak después de cada segmento de ruta (p.ej., \texttt{services/\allowbreak accountConfirmation\allowbreak Service.js}). Si persiste, envolver la celda en \parbox o reducir ancho de columna.

> RNF-01 & \textbf{Seguridad} de credenciales y sesiones & Hash bcrypt \cite{bcrypt}, cookie \path{httpOnly} + \path{secure} + \path{sameSite}, regeneración de la sesión, permisos en el servidor, consultas parametrizadas\allowbreak{} \\
problema: Rutas de código largas dentro de celdas de longtable no se parten y causan overfull hbox.
solucion: Insertar \allowbreak en puntos naturales (tras punto, barra, dos puntos) dentro de \texttt{} o \path{}. Para URLs, usar \path{} de xurl (ya cargado) que permite cortes en cualquier carácter.
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Relacionado: [[como-evitar-overfull-hbox-con-texttt-largo]] · [[como-evitar-overfull-hbox-en-rutas-y-diagramas]] · [[longtable-sin-fila-huerfana-al-final]] · [[como-evitar-overfull-hbox-en-tablas-anchas-con-longtable]] · [[corregir-overfull-hbox-en-longtable-con-urls-largas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
