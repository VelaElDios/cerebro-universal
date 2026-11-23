---
tipo: "concepto"
titulo: "Reglas de maquetación de Javier (resumen accionable)"
temas: ["maquetacion", "reglas", "tfg", "latex", "memoria-procesos"]
claves: ["portada", "tablas", "figuras", "diagramas", "prosa", "sprint"]
proyectos: ["memoria-procesos"]
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[maquetacion]] · [[reglas]] · [[tfg]]

Resumen de comprobación obligatoria antes de TERMINADO: (1) Una sola portada (elements/portada.tex); (2) No quitar nada de la plantilla; (3) Títulos negros negrita, hidelinks; (4) Sin páginas en blanco; (5) Tablas p{} + \small + \addlinespace + \\* en últimas filas; (6) Código en \path{} o \texttt{} + \allowbreak; (7) longtable para tablas largas; (8) Capturas height=0.42\textheight, diagramas max totalheight, flotantes [htbp] relajados; (9) Sin secciones de 1-2 líneas; (10) Sin figuras repetidas (usar \ref); (11) Flechas $\rightarrow$; (12) Cada entrega solo su sprint; (13) Prosa sin «La figura X muestra…» suelto; (14) Todo citado y explicado; (15) PDF revisado página a página + revisar_maquetacion.py verde; (16) Diagramas legibles a tamaño real (≤6 participantes en secuencia, letras ≥7,5 pt); (17) Sin flechas cruzando cajas, codos y separación; (18) Sin palabras partidas en cajas; (19) Diagramas mirados en PDF de verdad, no solo escalados.

> Reglas 1-19 listadas en el documento.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
|
  **Portada y plantilla (1-4):** Una sola portada (`elements/portada.tex`); no quitar nada de la plantilla; títulos negros negrita sin azul; sin páginas en blanco entre capítulos.
  **Tablas (5-7):** Celdas `p{}` (no `m{}`), `\small` en longtable, código con `\path{}` o `\texttt{}\allowbreak`, última fila con `\\*` para no quedar sola.
  **Figuras y páginas (8-11):** Ninguna página con una sola imagen (capturas ≤ `height=0.42\textheight`); ninguna página casi vacía; sin figuras repetidas (usar `\ref`); flechas con `$\rightarrow$` no `->`.
  **Diagramas (16-19):** Leer bien a tamaño real (letras ≥ 8-9 pt); máx. 6 participantes en secuencia; flechas caja a caja con codos (`|-`, `-|`); cajas sin palabras partidas; **mirar de verdad en el PDF** (regla 19: `revisar_figuras.py` mide coordenadas reales; si falla, replantear dibujo, no encoger con `adjustbox`).
  **Contenido (12-14):** Cada entrega solo su sprint; prosa TFG (no listas de capturas); todo citado y con sentido.
  **Comprobación (15):** Antes de TERMINADO, PDF página a página + `revisar_maquetacion.py` en verde.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
