---
tipo: "dato"
titulo: "Discrepancia en las fuentes: 24 armas (§9.3) vs 29 armas (§14 métricas)"
temas: ["datos", "fuentes", "juego", "verificar", "memoria-procesos", "metricas"]
claves: ["24 armas", "29 armas", "config.js", "documentacion-tecnica.md §9.3 §14"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[datos]] · [[fuentes]] · [[juego]] · [[verificar]]

Ambas cifras están en la fuente, así que el test no falla, pero la memoria debe usar una sola: 24 en la tabla de sistemas del juego (04b) y 29 en la tabla de métricas (05) es inconsistente. Elegir una (la de §9.3, 24, para sistemas; o la de §14, 29, para métricas) y unificar en todos los capítulos antes de entregar.

> §9.3: «Armas y habilidades | 24, con 5 niveles»; §14: «Contenido del juego | 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 24 combinaciones…
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[numeros-clave-del-proyecto-contrastados-con-fuentes]]

## Ampliación (2026-11-17, memoria-procesos)
La discrepancia está documentada en la bitácora 2026-11-17 03:43. La tabla de sistemas (§9.3) dice «24 armas» y la tabla de métricas (§14) dice «29 armas». En la memoria actual, la Tabla~\ref{tab:juego-sistemas} (04b-juego.tex) usa 24 y la Tabla~\ref{tab:metricas} (05-evaluacion.tex) usa 24. Hay que unificar. Lo ideal es contar en `public/js/game/config.js` el array `ARMAS` y usar esa cifra real.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
