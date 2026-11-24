---
tipo: "dato"
titulo: "Inventario de diagramas obligatorios y su estado"
temas: ["diagramas", "latex", "verificacion", "pgf-umlsd", "pgfplots", "tikz"]
claves: ["fig:capas", "fig:modelo-datos", "fig:sec-registro", "fig:sec-confirmacion", "fig:sec-login", "fig:sec-google", "fig:sec-baja", "fig:sec-partida", "fig:sec-contratar", "fig:pipeline", "fig:burndown-s1", "fig:burndown-s2"]
proyectos: ["memoria-procesos"]
fuentes: ["spec del proyecto y arquitectura.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[diagramas]] · [[latex]] · [[verificacion]]

| Diagrama | Tipo | Archivo | Estado actual |
|---|---|---|---|
| fig:capas | TikZ | 04-descripcion.tex | **FALLA**: 55pt ancho, particiones "ro-" |
| fig:modelo-datos | TikZ | 04-descripcion.tex | No revisado (Gemini 404) |
| fig:sec-registro | sequencediagram | 04-descripcion.tex | Modificado, no revisado (Gemini 404) |
| fig:sec-confirmacion | sequencediagram | 04-descripcion.tex | No revisado (Gemini 404) |
| fig:sec-login | sequencediagram | 04-descripcion.tex | **FALLA**: 6.9pt, flechas cruzan "invalidas" |
| fig:sec-google | sequencediagram | 04-descripcion.tex | Pendiente |
| fig:sec-baja | sequencediagram | 04-descripcion.tex | **FALLA**: 7.5pt límite, flechas cruzan "403"/"204" |
| fig:sec-partida | sequencediagram | 04b-juego.tex | No revisado (Gemini 404) |
| fig:sec-contratar | sequencediagram | 04b-juego.tex | No revisado (Gemini 404) |
| fig:juego-arquitectura | TikZ | 04b-juego.tex | **FALLA**: 68pt ancho, "ar-", flechas cruzan |
| fig:pipeline | TikZ | 05-evaluacion.tex | No revisado (Gemini 404), `\mbox{Artifact}` aplicado |
| fig:burndown-s1 | pgfplots | a1-desarrollo.tex | No revisado (Gemini 404) |
| fig:burndown-s2 | pgfplots | a1-desarrollo.tex | No revisado (Gemini 404) |

Todos deben pasar `revisar_umlsd.py` (para sequencediagram) y revisión visual PDF (reglas 16-18).

> Figuras con etiqueta fija (las comprueba el test y tienen que ser dibujos, no imágenes): fig:capas, fig:modelo-datos, fig:sec-registro, fig:sec-confirmacion, fig:sec-login, fig:sec-google, fig:sec-baja, fig:sec-partida, fig:sec-contratar, fig:pipeline (TikZ o sequencediagram) y fig:burndown-s1, fig:burndown-s2 (pgfplots).
> — `spec del proyecto y arquitectura.md` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
|
  | Diagrama | Tipo | Archivo | Estado actual |
  |---|---|---|---|
  | fig:capas | TikZ | 04-descripcion.tex | **CORREGIDO** (replanteado: text width ↑, separación ↑, \mbox{}, flechas con codos) |
  | fig:modelo-datos | TikZ | 04-descripcion.tex | No revisado (Gemini 404) |
  | fig:sec-registro | sequencediagram | 04-descripcion.tex | Modificado, no revisado (Gemini 404) |
  | fig:sec-confirmacion | sequencediagram | 04-descripcion.tex | No revisado (Gemini 404) |
  | fig:sec-login | sequencediagram | 04-descripcion.tex | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox) |
  | fig:sec-google | sequencediagram | 04-descripcion.tex | Pendiente |
  | fig:sec-baja | sequencediagram | 04-descripcion.tex | **CORREGIDO** (etiquetas con \n, adjustbox) |
  | fig:sec-partida | sequencediagram | 04b-juego.tex | No revisado (Gemini 404) |
  | fig:sec-contratar | sequencediagram | 04b-juego.tex | No revisado (Gemini 404) |
  | fig:juego-arquitectura | TikZ | 04b-juego.tex | **CORREGIDO** (text width ↑, separación ↑, \mbox{sprites.js,}, flechas con codos) |
  | fig:pipeline | TikZ | 05-evaluacion.tex | No revisado (Gemini 404), \mbox{Artifact} aplicado |
  | fig:burndown-s1 | pgfplots | a1-desarrollo.tex | No revisado (Gemini 404) |
  | fig:burndown-s2 | pgfplots | a1-desarrollo.tex | No revisado (Gemini 404) |
relacionado: Cómo replantear diagramas TikZ y pgf-umlsd para pasar revisar_maquetacion.py, Validación final del PDF antes de marcar terminado

Relacionado: [[inventario-de-diagramas-obligatorios-y-su-estado-actualizado]] · [[arreglo-de-diagramas-segun-reglas-16-18-de-javier-feedback-1]] · Cómo replantear diagramas de secuencia pgf-umlsd para pasar revisar_maquetacion.py

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
