---
tipo: "concepto"
titulo: "Números en diagramas de secuencia deben coincidir con la especificación"
temas: ["codigos estado", "http", "latex", "pgf-umlsd", "sequencediagram"]
claves: ["400", "422", "409", "200", "fig:sec-partida", "fig:sec-contratar"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/lecciones.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[codigos estado]] · [[http]] · [[latex]] · [[pgf-umlsd]] · [[sequencediagram]]

Al escribir diagramas de secuencia, copiar los códigos de estado exactos de la documentación técnica (documentacion-tecnica.md §7.10 y §7.11). Si la fuente dice 400, usar 400; si dice 409, usar 409. No inventar códigos. Ejemplo: en el diagrama, la línea \begin{call}{api}{finalizarPartida}{srv}{200 o 400} debe reflejar los códigos reales (400, no 422).

> En el diagrama de secuencia fig:sec-partida se usó el código de estado 422 para «resultado imposible», pero la documentación técnica (§7.10) especifica 400. El test de verificación detecta números no presentes en las fuentes.
> — `memoria/lecciones.md` (cita sin comprobar)

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[estrategia-de-pruebas-error-first-y-ci-como-requisito-de-mer]] · [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[diagramas-de-secuencia-con-pgf-umlsd]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]] · [[diagramas-de-secuencia-pgf-umlsd-sintaxis-correcta]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
