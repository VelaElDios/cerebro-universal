---
tipo: "dato"
titulo: "Inventario de diagramas obligatorios y su estado actualizado"
temas: ["latex", "maquetacion", "pgf-umlsd", "tikz", "memoria-procesos", "pgfplots", "diagramas"]
claves: ["fig:capas", "fig:modelo-datos", "fig:sec-registro", "fig:sec-confirmacion", "fig:sec-login", "fig:sec-google", "fig:sec-baja", "fig:sec-partida", "fig:sec-contratar", "fig:juego-arquitectura", "fig:pipeline", "fig:burndown-s1", "fig:burndown-s2"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex, memoria/chapters/04b-juego.tex, memoria/chapters/05-evaluacion.tex, memoria/chapters/a1-desarrollo.tex", "spec del proyecto y arquitectura.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]] · [[tikz]]

|
  | Diagrama | Tipo | Archivo | Estado actual |
  |---|---|---|---|
  | fig:capas | TikZ | 04-descripcion.tex | **CORREGIDO** (replanteado: text width ↓, separación ↑, \mbox{}, flechas con codos, font=\scriptsize) |
  | fig:modelo-datos | TikZ | 04-descripcion.tex | No revisado (Gemini 404) |
  | fig:sec-registro | sequencediagram | 04-descripcion.tex | Modificado, no revisado (Gemini 404) |
  | fig:sec-confirmacion | sequencediagram | 04-descripcion.tex | No revisado (Gemini 404) |
  | fig:sec-login | sequencediagram | 04-descripcion.tex | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox max totalheight) |
  | fig:sec-google | sequencediagram | 04-descripcion.tex | **PENDIENTE** (replantear: ≤5 participantes, etiquetas ≤2 líneas, codos) |
  | fig:sec-baja | sequencediagram | 04-descripcion.tex | **CORREGIDO** (Dialogo sin acento, etiquetas cortas) |
  | fig:sec-partida | sequencediagram | 04b-juego.tex | No revisado (Gemini 404) |
  | fig:sec-contratar | sequencediagram | 04b-juego.tex | No revisado (Gemini 404) |
  | fig:juego-arquitectura | TikZ | 04b-juego.tex | **CORREGIDO** (text width ↓, separación ↑, \mbox{}, font=\scriptsize) |
  | fig:pipeline | TikZ | 05-evaluacion.tex | No revisado (Gemini 404), `\mbox{Artifact}` aplicado |
  | fig:burndown-s1 | pgfplots | a1-desarrollo.tex | No revisado (Gemini 404) |
  | fig:burndown-s2 | pgfplots | a1-desarrollo.tex | No revisado (Gemini 404) |

  Todos deben pasar `revisar_umlsd.py` (para sequencediagram) y revisión visual PDF (reglas 16-18).

> Figuras con etiqueta fija (las comprueba el test y tienen que ser dibujos, no imágenes): fig:capas, fig:modelo-datos, fig:sec-registro, fig:sec-confirmacion, fig:sec-login, fig:sec-google, fig:sec-baja, fig:sec-partida, fig:sec-contratar, fig:pipeline (TikZ o sequencediagram) y fig:burndown-s1, fig:burndown-s2 (pgfplots).
> — `memoria/chapters/04-descripcion.tex, memoria/chapters/04b-juego.tex, memoria/chapters/05-evaluacion.tex, memoria/chapters/a1-desarrollo.tex` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
| Diagrama | Tipo | Archivo | Estado actual |
|---|---|---|---|
| fig:capas | TikZ | 04-descripcion.tex | **CORREGIDO** (replanteado: text width ↑, separación ↑, \mbox{}, flechas con codos) |
| fig:modelo-datos | TikZ | 04-descripcion.tex | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-registro | sequencediagram | 04-descripcion.tex | **PENDIENTE** (modificado, no revisado, Gemini 404) |
| fig:sec-confirmacion | sequencediagram | 04-descripcion.tex | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-login | sequencediagram | 04-descripcion.tex | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox) |
| fig:sec-google | sequencediagram | 04-descripcion.tex | **PENDIENTE** (replantear: ≤5 participantes, etiquetas ≤2 líneas, codos) |
| fig:sec-baja | sequencediagram | 04-descripcion.tex | **CORREGIDO** (Diálogo sin acento, etiquetas cortas) |
| fig:juego-arquitectura | TikZ | 04b-juego.tex | **CORREGIDO** (text width ↓, separación ↑, \mbox{}, font=\scriptsize) |
| fig:sec-partida | sequencediagram | 04b-juego.tex | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-contratar | sequencediagram | 04b-juego.tex | **PENDIENTE** (no revisado, Gemini 404) |
| fig:pipeline | TikZ | 05-evaluacion.tex | **PENDIENTE** (no revisado, Gemini 404), `\mbox{Artifact}` aplicado |
| fig:burndown-s1 | pgfplots | a1-desarrollo.tex | **PENDIENTE** (no revisado, Gemini 404) |
| fig:burndown-s2 | pgfplots | a1-desarrollo.tex | **PENDIENTE** (no revisado, Gemini 404) |

Todos deben pasar `revisar_umlsd.py` (para sequencediagram) y revisión visual PDF (reglas 16-18: letras ≥ 7,5 pt, sin flechas que crucen cajas, sin palabras partidas, codos en flechas).

## Ampliación (2026-11-23, memoria-procesos)
|
  | Diagrama | Tipo | Archivo | Estado actual |
  |---|---|---|---|
  | fig:capas | TikZ | 04-descripcion.tex | **CORREGIDO** (replanteado: text width ↑, separación ↑, \mbox{}, flechas con codos) |
  | fig:modelo-datos | TikZ | 04-descripcion.tex | **PENDIENTE** (no revisado, Gemini 404) |
  | fig:sec-registro | sequencediagram | 04-descripcion.tex | Modificado, **PENDIENTE** (Gemini 404) |
  | fig:sec-confirmacion | sequencediagram | 04-descripcion.tex | **PENDIENTE** (Gemini 404) |
  | fig:sec-login | sequencediagram | 04-descripcion.tex | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox) |
  | fig:sec-google | sequencediagram | 04-descripcion.tex | **PENDIENTE** (replantear: ≤5 participantes, etiquetas ≤2 líneas, codos) |
  | fig:sec-baja | sequencediagram | 04-descripcion.tex | **CORREGIDO** (Diálogo sin acento, etiquetas cortas) |
  | fig:juego-arquitectura | TikZ | 04b-juego.tex | **CORREGIDO** (text width ↓, separación ↑, \mbox{}, font=\scriptsize) |
  | fig:sec-partida | sequencediagram | 04b-juego.tex | **PENDIENTE** (Gemini 404) |
  | fig:sec-contratar | sequencediagram | 04b-juego.tex | **PENDIENTE** (Gemini 404) |
  | fig:pipeline | TikZ | 05-evaluacion.tex | **PENDIENTE** (Gemini 404), `\mbox{Artifact}` aplicado |
  | fig:burndown-s1 | pgfplots | a1-desarrollo.tex | **PENDIENTE** (Gemini 404) |
  | fig:burndown-s2 | pgfplots | a1-desarrollo.tex | **PENDIENTE** (Gemini 404) |

  Todos deben pasar `revisar_umlsd.py` (para sequencediagram) y revisión visual PDF (reglas 16-18).

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
