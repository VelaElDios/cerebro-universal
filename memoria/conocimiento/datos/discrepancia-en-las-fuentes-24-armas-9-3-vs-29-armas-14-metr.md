---
tipo: "dato"
titulo: "Discrepancia en las fuentes: 24 armas (§9.3) vs 29 armas (§14 métricas)"
temas: ["datos", "fuentes", "juego", "verificar", "memoria-procesos", "metricas", "arma", "fuente"]
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

Relacionado: [[numeros-clave-del-proyecto-contrastados-con-fuentes]] · [[cada-cifra-de-un-documento-sale-de-las-fuentes-tambien-las-p]] · [[metricas-del-proyecto-codigo-pruebas-endpoints-y-contenido-d]] · [[inventario-de-capturas-donetonic-requeridas-y-disponibles]] · [[numeros-clave-del-proyecto-verificados-en-fuentes]] · [[cada-cifra-del-documento-sale-de-las-fuentes-tambien-las-peq]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-30-datos]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-35-datos]]

## Ampliación (2026-11-17, memoria-procesos)
La discrepancia está documentada en la bitácora 2026-11-17 03:43. La tabla de sistemas (§9.3) dice «24 armas» y la tabla de métricas (§14) dice «29 armas». En la memoria actual, la Tabla~\ref{tab:juego-sistemas} (04b-juego.tex) usa 24 y la Tabla~\ref{tab:metricas} (05-evaluacion.tex) usa 24. Hay que unificar. Lo ideal es contar en `public/js/game/config.js` el array `ARMAS` y usar esa cifra real.

## Ampliación (2026-11-17, memoria-procesos)
La documentación técnica tiene una discrepancia interna: en la tabla de sistemas (§9.3) se dice que hay 24 armas, mientras que en la tabla de métricas (§14) se dice 29. En la memoria se ha usado 24 en ambos sitios (tabla sistemas del Capítulo 4b y métricas del Capítulo 5) para mantener coherencia interna, pero se debe decidir cuál es el dato correcto y unificarlo en toda la memoria. Posiblemente las 29 incluyan las 5 habilidades nuevas de la Fase 7 (carambola, presión alta, la ola, fuera de juego, ruleta) que no son armas propiamente dichas.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
