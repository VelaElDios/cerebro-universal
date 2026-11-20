---
tipo: "receta"
titulo: "Resumen y Abstract en elements/preambulo.tex con formato oficial"
temas: ["abstract", "latex", "preambulo", "resumen"]
claves: ["Resumen", "Abstract", "Palabras clave", "Keywords", "\\bft", "\\Large"]
proyectos: ["memoria-procesos"]
fuentes: ["elements/preambulo.tex (actual), spec del proyecto (Páginas iniciales)", "elements/preambulo.tex"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[abstract]] · [[latex]] · [[preambulo]] · [[resumen]]

En `elements/preambulo.tex` (tras la declaración de autoría): (1) `\cleardoublepage`, `\thispagestyle{plain}`, `\Large{\bft{Resumen}}`, texto ≥150 palabras, `\medskip\noindent\textbf{Palabras clave:} ...`. (2) `\cleardoublepage`, `\thispagestyle{plain}`, `\Large{\bft{Abstract}}`, texto en inglés ≥120 palabras, `\medskip\noindent\textbf{Keywords:} ...`. No añadir segunda portada (Regla 1). La declaración de autoría no se toca.

> Resumen (≥ 150 palabras, dos sprints y juego) con «Palabras clave», y una página nueva Abstract en inglés (≥ 120 palabras) con «Keywords», mismo formato (`\Large{\bft{Abstract}}`).
> — `elements/preambulo.tex (actual), spec del proyecto (Páginas iniciales)` (cita sin comprobar)

## Ampliación (2026-11-16, memoria-procesos)
El preámbulo oficial del TFG (elements/preambulo.tex) debe contener solo: declaración de autoría, Resumen (≥150 palabras, dos sprints y juego) con «Palabras clave», y Abstract (≥120 palabras, inglés) con «Keywords». No hay segunda portada. El formato usa \Large{\bft{Resumen}} y \Large{\bft{Abstract}} centrados, con \vskip1cm y \medskip. La declaración de autoría no se toca.

Relacionado: [[paso-1-completado-preambulo-tex-ya-cumple-regla-1-una-sola-p]] · [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[una-sola-portada-oficial-en-elements-portada-tex]] · [[estructura-de-la-memoria-tfg-esiiab-uclm-plantilla-oficial]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
