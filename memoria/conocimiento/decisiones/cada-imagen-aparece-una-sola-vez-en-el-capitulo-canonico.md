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

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
