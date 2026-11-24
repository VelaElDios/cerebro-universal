---
tipo: "decision"
titulo: "Diagramas de secuencia pgf-umlsd: reglas para pasar revisar_maquetacion.py"
temas: ["diagramas", "latex", "maquetación", "pgf-umlsd"]
claves: ["sequencediagram", "newthread", "newinst", "call", "mess", "sdblock", "flechas", "node distance"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md reglas 16-18"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[diagramas]] · [[latex]] · [[maquetación]] · [[pgf-umlsd]]

Para que los diagramas de secuencia pasen la revisión visual (reglas 16-18 de Javier):
1. **Máximo 6 participantes** por diagrama. Si hay más, agrupar (ej. "Vista + api.js" → "Frontend") o partir en dos diagramas.
2. **node distance**: vertical ≥1.5cm, horizontal ≥2.5cm entre participantes.
3. **Flechas con codos**: usar `\draw[arrow] (A.east) -- ++(1.5,0) |- (B.west);` en lugar de líneas rectas que cruzan cajas. En `sequencediagram`, los `call` y `mess` anidados ya hacen esto, pero los `sdblock` alternativos pueden necesitar ajuste manual.
4. **Etiquetas fuera de líneas verticales**: `node[near start, above/left/right, font=\footnotesize] {texto}`.
5. **Sin palabras partidas en cajas**: aumentar `text width` o usar `\\` manual.
6. **Todos los participantes declarados** con `\newthread`/`\newinst` en ese diagrama (nombres no vacíos).
7. **En textos de \mess, call, callself, newinst**: NO usar `#`, `_`, `&`, `%`, `$`, `\`, `{`, `}`, comandos LaTeX, paréntesis en `\mess`. Escapar o reescribir.
8. **Letras ≥7,5 pt** tras escalado: no usar `resizebox`/`adjustbox` para encoger diagramas grandes; replantear el dibujo.
9. Ejecutar `revisar_umlsd.py` antes de compilar: detecta etiquetas con acentos, paréntesis en \mess, participantes no declarados, etc.

> Las flechas van de una caja a la siguiente (A → B, B → C), nunca de A a C pasando por encima de B; si hay que rodear, con codos (|-, -|) y separando bien las cajas (node distance suficiente).
> — `memoria/reglas-tfg.md reglas 16-18` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
