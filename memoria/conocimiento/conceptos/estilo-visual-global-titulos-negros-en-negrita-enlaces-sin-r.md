---
tipo: "concepto"
titulo: "Estilo visual global: títulos negros en negrita, enlaces sin recuadros, sin páginas en blanco entre capítulos"
temas: ["latex", "memoria", "tfg"]
claves: ["definecolor", "tema", "RGB", "0", "0", "0", "bfseries", "hypersetup", "hidelinks", "páginas en blanco"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

- Color de títulos: `\definecolor{tema}{RGB}{0,0,0}` (negro puro).
- `\bfseries` en `\section` y `\subsection`.
- Enlaces invisibles: `\hypersetup{hidelinks}` (sin recuadros de color).
- Documento continuo: **no** insertar páginas en blanco entre capítulos (clase `report`/`book` con `openany` o `\let\cleardoublepage\clearpage`).
- Entrega final en PDF único.

> Títulos en negro y en negrita, sin azul: `\definecolor{tema}{RGB}{0,0,0}`, con `\bfseries` en section y subsection. Los enlaces van sin recuadros de color (`\hypersetup{hidelinks}`). Sin páginas en blanco entre capítulos: la memoria se entrega en PDF.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[estructura-de-la-memoria-tfg-esiiab-uclm-plantilla-oficial]] · [[reglas-de-maquetacion-de-javier-resumen-accionable]]
