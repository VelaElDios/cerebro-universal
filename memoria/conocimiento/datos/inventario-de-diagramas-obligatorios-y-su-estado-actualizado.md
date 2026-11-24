---
tipo: "dato"
titulo: "Inventario de diagramas obligatorios y su estado actualizado"
temas: ["diagramas", "latex", "maquetacion", "memoria", "memoria-procesos", "pgf-umlsd", "pgfplots", "tikz", "verificacion"]
claves: ["fig:capas", "fig:modelo-datos", "fig:sec-registro", "fig:sec-confirmacion", "fig:sec-login", "fig:sec-google", "fig:sec-baja", "fig:sec-partida", "fig:sec-contratar", "fig:juego-arquitectura", "fig:pipeline", "fig:burndown-s1", "fig:burndown-s2"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex, memoria/chapters/04b-juego.tex, memoria/chapters/05-evaluacion.tex, memoria/chapters/a1-desarrollo.tex", "spec del proyecto y arquitectura.md", "spec del proyecto (figuras con etiqueta fija) y memoria/conocimiento/datos/inventario-de-diagramas-obligatorios-y-su-estado-actualizado.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-24"
---

Temas: [[diagramas]] · [[latex]] · [[maquetacion]] · [[memoria]] · [[memoria-procesos]] · [[pgf-umlsd]] · [[pgfplots]] · [[tikz]] · [[verificacion]]

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]] · [[tikz]] · [[diagramas]] · [[verificacion]]

## Tabla maestra de diagramas

| Diagrama | Tipo | Archivo | Estado actual (última actualización) |
|---|---|---|---|
| fig:capas | TikZ | 04-descripcion.tex | Ver historial abajo |
| fig:modelo-datos | TikZ | 04-descripcion.tex | Ver historial abajo |
| fig:sec-registro | sequencediagram | 04-descripcion.tex | Ver historial abajo |
| fig:sec-confirmacion | sequencediagram | 04-descripcion.tex | Ver historial abajo |
| fig:sec-login | sequencediagram | 04-descripcion.tex | Ver historial abajo |
| fig:sec-google | sequencediagram | 04-descripcion.tex | Ver historial abajo |
| fig:sec-baja | sequencediagram | 04-descripcion.tex | Ver historial abajo |
| fig:sec-partida | sequencediagram | 04b-juego.tex | Ver historial abajo |
| fig:sec-contratar | sequencediagram | 04b-juego.tex | Ver historial abajo |
| fig:juego-arquitectura | TikZ | 04b-juego.tex | Ver historial abajo |
| fig:pipeline | TikZ | 05-evaluacion.tex | Ver historial abajo |
| fig:burndown-s1 | pgfplots | a1-desarrollo.tex | Ver historial abajo |
| fig:burndown-s2 | pgfplots | a1-desarrollo.tex | Ver historial abajo |

> **Figuras con etiqueta fija** (las comprueba el test y tienen que ser dibujos, no imágenes):  
> fig:capas, fig:modelo-datos, fig:sec-registro, fig:sec-confirmacion, fig:sec-login, fig:sec-google, fig:sec-baja, fig:sec-partida, fig:sec-contratar, fig:pipeline (TikZ o sequencediagram) y fig:burndown-s1, fig:burndown-s2 (pgfplots).  
> — Fuentes: `memoria/chapters/04-descripcion.tex, memoria/chapters/04b-juego.tex, memoria/chapters/05-evaluacion.tex, memoria/chapters/a1-desarrollo.tex` (Nota A) y `spec del proyecto y arquitectura.md` (Nota B) — *citas sin comprobar*.

> **Requisitos de validación**: Todos deben pasar `revisar_umlsd.py` (para sequencediagram) y revisión visual PDF (reglas 16-18: letras ≥ 7,5 pt, sin flechas que crucen cajas, sin palabras partidas, codos en flechas).

---

## Historial de estados por fecha (cronológico fusionado)

### Estado inicial (Nota A — sin fecha explícita, anterior a 2026-11-23)
| Diagrama | Estado |
|---|---|
| fig:capas | **CORREGIDO** (replanteado: text width ↓, separación ↑, \mbox{}, flechas con codos, font=\scriptsize) |
| fig:modelo-datos | No revisado (Gemini 404) |
| fig:sec-registro | Modificado, no revisado (Gemini 404) |
| fig:sec-confirmacion | No revisado (Gemini 404) |
| fig:sec-login | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox max totalheight) |
| fig:sec-google | **PENDIENTE** (replantear: ≤5 participantes, etiquetas ≤2 líneas, codos) |
| fig:sec-baja | **CORREGIDO** (Diálogo sin acento, etiquetas cortas) |
| fig:sec-partida | No revisado (Gemini 404) |
| fig:sec-contratar | No revisado (Gemini 404) |
| fig:juego-arquitectura | **CORREGIDO** (text width ↓, separación ↑, \mbox{}, font=\scriptsize) |
| fig:pipeline | No revisado (Gemini 404), `\mbox{Artifact}` aplicado |
| fig:burndown-s1 | No revisado (Gemini 404) |
| fig:burndown-s2 | No revisado (Gemini 404) |

### Estado inicial (Nota B — sin fecha explícita, anterior a 2026-11-23)
| Diagrama | Estado |
|---|---|
| fig:capas | **FALLA**: 55pt ancho, particiones "ro-" |
| fig:modelo-datos | No revisado (Gemini 404) |
| fig:sec-registro | Modificado, no revisado (Gemini 404) |
| fig:sec-confirmacion | No revisado (Gemini 404) |
| fig:sec-login | **FALLA**: 6.9pt, flechas cruzan "invalidas" |
| fig:sec-google | Pendiente |
| fig:sec-baja | **FALLA**: 7.5pt límite, flechas cruzan "403"/"204" |
| fig:sec-partida | No revisado (Gemini 404) |
| fig:sec-contratar | No revisado (Gemini 404) |
| fig:juego-arquitectura | **FALLA**: 68pt ancho, "ar-", flechas cruzan |
| fig:pipeline | No revisado (Gemini 404), `\mbox{Artifact}` aplicado |
| fig:burndown-s1 | No revisado (Gemini 404) |
| fig:burndown-s2 | No revisado (Gemini 404) |

---

### Ampliación 1 (2026-11-23, memoria-procesos — Nota A, primera versión)
| Diagrama | Estado |
|---|---|
| fig:capas | **CORREGIDO** (replanteado: text width ↑, separación ↑, \mbox{}, flechas con codos) |
| fig:modelo-datos | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-registro | **PENDIENTE** (modificado, no revisado, Gemini 404) |
| fig:sec-confirmacion | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-login | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox) |
| fig:sec-google | **PENDIENTE** (replantear: ≤5 participantes, etiquetas ≤2 líneas, codos) |
| fig:sec-baja | **CORREGIDO** (Diálogo sin acento, etiquetas cortas) |
| fig:juego-arquitectura | **CORREGIDO** (text width ↓, separación ↑, \mbox{}, font=\scriptsize) |
| fig:sec-partida | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-contratar | **PENDIENTE** (no revisado, Gemini 404) |
| fig:pipeline | **PENDIENTE** (no revisado, Gemini 404), `\mbox{Artifact}` aplicado |
| fig:burndown-s1 | **PENDIENTE** (no revisado, Gemini 404) |
| fig:burndown-s2 | **PENDIENTE** (no revisado, Gemini 404) |

### Ampliación 2 (2026-11-23, memoria-procesos — Nota A, segunda versión)
| Diagrama | Estado |
|---|---|
| fig:capas | **CORREGIDO** (replanteado: text width ↑, separación ↑, \mbox{}, flechas con codos) |
| fig:modelo-datos | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-registro | Modificado, **PENDIENTE** (Gemini 404) |
| fig:sec-confirmacion | **PENDIENTE** (Gemini 404) |
| fig:sec-login | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox) |
| fig:sec-google | **PENDIENTE** (replantear: ≤5 participantes, etiquetas ≤2 líneas, codos) |
| fig:sec-baja | **CORREGIDO** (Diálogo sin acento, etiquetas cortas) |
| fig:juego-arquitectura | **CORREGIDO** (text width ↓, separación ↑, \mbox{}, font=\scriptsize) |
| fig:sec-partida | **PENDIENTE** (Gemini 404) |
| fig:sec-contratar | **PENDIENTE** (Gemini 404) |
| fig:pipeline | **PENDIENTE** (Gemini 404), `\mbox{Artifact}` aplicado |
| fig:burndown-s1 | **PENDIENTE** (Gemini 404) |
| fig:burndown-s2 | **PENDIENTE** (Gemini 404) |

### Ampliación 3 (2026-11-23, memoria-procesos — Nota A, tercera versión — **con mediciones concretas**)
| Diagrama | Estado |
|---|---|
| fig:capas | **PENDIENTE** (Gemini 404, requiere revisión visual) |
| fig:modelo-datos | **PENDIENTE** (Gemini 404) |
| fig:sec-registro | **FALLA MEDIDA** (letras 7.0 pt, flecha cruza «enviado») |
| fig:sec-confirmacion | **FALLA MEDIDA** (letras 7.5 pt límite) |
| fig:sec-login | **PENDIENTE** (Gemini 404) |
| fig:sec-google | **FALLA MEDIDA** (letras 6.2 pt, flecha cruza «verificado») |
| fig:sec-baja | **PENDIENTE** (Gemini 404) |
| fig:sec-partida | **PENDIENTE** (Gemini 404) |
| fig:sec-contratar | **PENDIENTE** (Gemini 404) |
| fig:juego-arquitectura | **PENDIENTE** (Gemini 404) |
| fig:pipeline | **PENDIENTE** (Gemini 404) |
| fig:burndown-s1 | **PENDIENTE** (Gemini 404) |
| fig:burndown-s2 | **PENDIENTE** (Gemini 404) |

### Ampliación 4 (2026-11-23, memoria-procesos — Nota A, cuarta versión — **valores numéricos precisos**)
| Diagrama | Estado |
|---|---|
| fig:capas | **PENDIENTE** (no revisado, Gemini 404) |
| fig:modelo-datos | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-registro | **FALLA MEDIDA**: 6.1 pt, flecha cruza "enviado" |
| fig:sec-confirmacion | **FALLA MEDIDA**: 7.5 pt límite, encogido |
| fig:sec-login | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-google | **FALLA MEDIDA**: 6.2 pt, flecha cruza "verificado" |
| fig:sec-baja | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-partida | **PENDIENTE** (no revisado, Gemini 404) |
| fig:sec-contratar | **PENDIENTE** (no revisado, Gemini 404) |
| fig:juego-arquitectura | **PENDIENTE** (no revisado, Gemini 404) |
| fig:pipeline | **PENDIENTE** (no revisado, Gemini 404) |
| fig:burndown-s1 | **PENDIENTE** (no revisado, Gemini 404) |
| fig:burndown-s2 | **PENDIENTE** (no revisado, Gemini 404) |

### Ampliación 5 (2026-11-23, memoria-procesos — Nota B, única ampliación)
| Diagrama | Estado |
|---|---|
| fig:capas | **CORREGIDO** (replanteado: text width ↑, separación ↑, \mbox{}, flechas con codos) |
| fig:modelo-datos | No revisado (Gemini 404) |
| fig:sec-registro | Modificado, no revisado (Gemini 404) |
| fig:sec-confirmacion | No revisado (Gemini 404) |
| fig:sec-login | **CORREGIDO** (etiquetas sin acentos, saltos \n, adjustbox) |
| fig:sec-google | Pendiente |
| fig:sec-baja | **CORREGIDO** (etiquetas con \n, adjustbox) |
| fig:sec-partida | No revisado (Gemini 404) |
| fig:sec-contratar | No revisado (Gemini 404) |
| fig:juego-arquitectura | **CORREGIDO** (text width ↑, separación ↑, \mbox{sprites.js,}, flechas con codos) |
| fig:pipeline | No revisado (Gemini 404), \mbox{Artifact} aplicado |
| fig:burndown-s1 | No revisado (Gemini 404) |
| fig:burndown-s2 | No revisado (Gemini 404) |

---

## Referencias cruzadas
- [[inventario-de-diagramas-obligatorios-y-su-estado-actualizado]] (Nota A)
- [[inventario-de-diagramas-obligatorios-y-su-estado-actualizado]] (Nota B)
- [[arreglo-de-diagramas-segun-reglas-16-18-de-javier-feedback-1]]
- *Cómo replantear diagramas de secuencia pgf-umlsd para pasar revisar_umlsd.py* / *revisar_maquetacion.py*
- *Validación final del PDF antes de marcar terminado*

Relacionado: [[validacion-visual-de-diagramas-tikz-pgf-umlsd-en-pdf-reglas]] · [[como-replantear-diagramas-de-secuencia-pgf-umlsd-para-evitar]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> Figuras con etiqueta fija (las comprueba el test y tienen que ser dibujos, no imágenes): fig:capas, fig:modelo-datos, fig:sec-registro, fig:sec-confirmacion, fig:sec-login, fig:sec-google, fig:sec-baja, fig:sec-partida, fig:sec-contratar, fig:pipeline (TikZ o sequencediagram) y fig:burndown-s1, fig:burndown-s2 (pgfplots).
> — `memoria/chapters/04-descripcion.tex, memoria/chapters/04b-juego.tex, memoria/chapters/05-evaluacion.tex, memoria/chapters/a1-desarrollo.tex` (cita sin comprobar)
> Figuras con etiqueta fija (las comprueba el test y tienen que ser dibujos, no imágenes): fig:capas, fig:modelo-datos, fig:sec-registro, fig:sec-confirmacion, fig:sec-login, fig:sec-google, fig:sec-baja, fig:sec-partida, fig:sec-contratar, fig:pipeline (TikZ o sequencediagram) y fig:burndown-s1, fig:burndown-s2 (pgfplots).
> — `spec del proyecto y arquitectura.md` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: Múltiples contradicciones entre notas y entre ampliaciones de la misma nota: (1) Nota A inicial da fig:capas, fig:sec-login, fig:sec-baja, fig:juego-arquitectura como **CORREGIDO**; Nota B inicial da los mismos como **FALLA** con mediciones concretas. (2) En Nota A, las ampliaciones 1-2 marcan fig:capas, fig:sec-login, fig:sec-baja, fig:juego-arquitectura como **CORREGIDO**, pero ampliaciones 3-4 los marcan como **PENDIENTE** o **FALLA MEDIDA** (con valores: 6.1 pt, 7.5 pt, 6.2 pt). (3) Nota B ampliación 5 vuelve a marcar fig:capas, fig:sec-login, fig:sec-baja, fig:juego-arquitectura como **CORREGIDO** con detalles distintos (text width ↑ vs ↓, \mbox{sprites.js,}). (4) fig:sec-registro: Nota A ampliación 1 = PENDIENTE, ampliación 2 = Modificado PENDIENTE, ampliación 3-4 = FALLA MEDIDA (7.0 pt / 6.1 pt); Nota B inicial = Modificado no revisado, ampliación 5 = Modificado no revisado. (5) fig:sec-google: Nota A siempre PENDIENTE con especificación (≤5 participantes, ≤2 líneas, codos); Nota B inicial = Pendiente sin detalle, ampliación 5 = Pendiente sin detalle. (6) fig:sec-confirmacion: Nota A ampliación 3-4 = FALLA MEDIDA (7.5 pt límite / encogido); Nota B siempre = No revisado. (7) Detalles técnicos difieren: fig:juego-arquitectura text width ↑ (Nota B amp5, Nota A amp1-2) vs ↓ (Nota A inicial, amp1-2 segunda mención); \mbox{} genérico vs \mbox{sprites.js,}. (8) Fuentes de figuras fijas: Nota A cita 4 archivos .tex en memoria/chapters; Nota B cita "spec del proyecto y arquitectura.md".

Fusionada con: Inventario de diagramas obligatorios y su estado

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
