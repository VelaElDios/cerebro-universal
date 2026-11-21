---
tipo: "receta"
titulo: "Formato de títulos y enlaces en la memoria"
temas: ["latex", "memoria", "tfg"]
claves: ["definecolor", "tema", "RGB", "0", "0", "0", "bfseries", "section", "subsection", "hypersetup", "hidelinks"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

Configurar en el preámbulo: `\definecolor{tema}{RGB}{0,0,0}` para forzar color negro en títulos. Aplicar `\bfseries` a `\section` y `\subsection`. Usar `\hypersetup{hidelinks}` para eliminar recuadros de color en enlaces. Esto asegura títulos en negro negrita y enlaces invisibles visualmente.

> Títulos en negro y en negrita, sin azul: `\definecolor{tema}{RGB}{0,0,0}`, con `\bfseries` en section y subsection. Los enlaces van sin recuadros de color (`\hypersetup{hidelinks}`).
> — `../../memoria/reglas-tfg.md`

Relacionado: [[titulos-en-negro-y-negrita-en-la-plantilla-esiiab-uclm]] · [[reglas-de-figuras-y-paginas-tamanos-flotantes-duplicados-fle]] · [[sin-paginas-casi-vacias-ni-secciones-sueltas-fundir-o-listar]] · [[estructura-de-la-memoria-tfg-esiiab-uclm-plantilla-oficial]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]]
