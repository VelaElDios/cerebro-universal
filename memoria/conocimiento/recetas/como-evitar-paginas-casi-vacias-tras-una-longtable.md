---
tipo: "receta"
titulo: "Cómo evitar páginas casi vacías tras una longtable"
temas: ["latex", "longtable", "maquetacion"]
claves: ["Regla 9", "página casi vacía", "longtable", "párrafo suelto"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/a4-trazabilidad.tex"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]]

Cuando una `longtable` ocupa varias páginas, el texto que se coloca inmediatamente después puede quedar aislado en una página nueva si la tabla termina cerca del final de la página anterior. Para cumplir la Regla 9 (ninguna página casi vacía), integra ese texto en el párrafo que introduce la tabla (antes de la `longtable`) y elimina el párrafo posterior a la tabla. Así el texto fluye naturalmente y no queda una línea suelta en una página.

> La Tabla~\ref{tab:trazabilidad-completa} cubre los 48 PBIs (P1--P48) y las 82 tareas (T1--T82) de los dos sprints. Los cierres de hito del Sprint 1 fueron los PR \#9 (Hito 1), \#17 (Hito 2), \#24 (Hito 3), \#29 (cierre del sprint) y \#32 (revisión final y memoria); las releases publicadas son \texttt{hito-1}, \texttt{hito-2}, \texttt{hito-3}, \texttt{hito-4} y \texttt{sprint-1} (Anexo~\ref{anx:material}).
> — `chapters/a4-trazabilidad.tex` (cita sin comprobar)

Relacionado: [[longtable-sin-fila-huerfana-al-final]] · [[longtable-sin-fila-huerfana-al-final]] · [[como-corregir-paginas-casi-vacias-regla-9-al-final-de-capitu]] · [[longtable-sin-fila-huerfana-al-final-regla-7-javier]] · [[longtable-sin-fila-huerfana-al-final]] · [[como-anadir-en-longtables-para-evitar-filas-huerfanas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
