---
tipo: "decision"
titulo: "Cada imagen aparece una sola vez en el capítulo canónico"
temas: ["latex", "maquetacion", "reglas-tfg", "maquetación"]
claves: ["regla 10", "imágenes repetidas", "ref cruzadas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[maquetacion]] · [[reglas-tfg]]

Las capturas de DoneTonic, producción, prueba técnica y Hito 4 deben aparecer una sola vez en su capítulo «canónico» y referenciarse con `\ref` en los demás:
- Tablero Sprint 1 (`01-tablero-sprint`): canónico en **03-propuesta.tex** (fig:donetonic-tablero)
- Gráficas Sprint 1 (`02-graficas-sprint`): canónico en **a1-desarrollo.tex** (fig:donetonic-graficas-s1)
- Backlog (`03-backlog`): canónico en **a1-desarrollo.tex** (fig:donetonic-backlog)
- Tablero Sprint 2 (`04-tablero-sprint2`): canónico en **a1-desarrollo.tex** (fig:donetonic-s2-tablero)
- Gráficas Sprint 2 (`06-graficas-sprint2`): canónico en **a1-desarrollo.tex** (fig:donetonic-s2-graficas)
- Correo confirmación (`01-correo-confirmacion`): canónico en **05-evaluacion.tex** (fig:correo-confirmacion)
- Actions verde (`02-actions-verde`): canónico en **05-evaluacion.tex** (fig:actions-verde)
- Google publicada (`03-google-publicada`): canónico en **05-evaluacion.tex** (fig:google-publicada)
- Prueba técnica permitido (`01-dominio-permitido`): canónico en **05-evaluacion.tex** (fig:prueba-tecnica-permitido)
En los demás capítulos, usar `\ref{fig:...}` en lugar de `\includegraphics`.

> Regla 10: Sin figuras repetidas: cada imagen aparece una sola vez. Si hace falta en otro sitio, se pone `\ref` a la figura que ya existe.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

## Ampliación (2026-11-16, memoria-procesos)
Regla 10 de Javier: ninguna imagen se repite en el PDF. Se elige un capítulo canónico donde la imagen tiene más sentido (donde se explica por primera vez). En los demás capítulos se sustituye la inclusión de la imagen por una referencia cruzada (`\ref{fig:...}`) y, si es necesario, una breve mención («como se muestra en la Figura~\ref{fig:...}»). Esto evita duplicados y mantiene el PDF ligero.

## Ampliación (2026-11-16, memoria-procesos)
La Regla 10 de Javier prohíbe imágenes repetidas. La solución: elegir un capítulo canónico para cada captura (donde más sentido tiene) y en los demás capítulos/referencias usar `\ref{fig:etiqueta-canónica}`. En este proyecto: tablero Sprint 1 → Capítulo 3 (03-propuesta.tex, label fig:donetonic-tablero); tablero Sprint 2 → Anexo Desarrollo (a1-desarrollo.tex, label fig:donetonic-s2-tablero); backlog → Anexo Desarrollo (label fig:donetonic-backlog); gráficas Sprint 1 → Anexo Desarrollo (label fig:donetonic-graficas-s1); gráficas Sprint 2 → Anexo Desarrollo (label fig:donetonic-s2-graficas). El anexo Material (a2-material.tex) solo lista las figuras con \ref, no las incluye.

## Ampliación (2026-11-16, memoria-procesos)
Decidido por Javier: las capturas de producción, prueba técnica y DoneTonic salen ahora en varios capítulos. Cada una va una sola vez en el sitio donde más sentido tiene, y en el resto se cita con \ref. En este proyecto, las capturas de app/ y hito4/ van en el capítulo 4 (Descripción), las de juego/ en el capítulo 4b (Juego), las de donetonic/ en el anexo A1 (Desarrollo) y el capítulo 3 (Propuesta), las de produccion/ y prueba-tecnica/ en el capítulo 5 (Evaluación).

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
