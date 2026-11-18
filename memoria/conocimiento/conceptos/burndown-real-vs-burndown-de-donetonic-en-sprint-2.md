---
tipo: "concepto"
titulo: "Burndown real vs. burndown de DoneTonic en Sprint 2"
temas: ["donetonic", "metricas", "scrum", "burndown", "sprint"]
claves: ["burndown", "DoneTonic", "recta", "registro al cierre"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md §4.5, repo:saas/docs/gestion/README.md §Evolución Sprint 2", "repo:saas/docs/gestion/README.md §Evolución del Sprint 2"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[metricas]] · [[scrum]]

En el anexo de desarrollo (a1-desarrollo.tex) hay que mostrar DOS burndowns del Sprint 2: (1) el de DoneTonic (recta 29→0 el 29/10, Figura fig:donetonic-s2-graficas) y (2) el real reconstruido por fechas de PR (23/10: 1 PBI, 24/10: 17, 26/10: 9, 29/10: 2; Figura fig:burndown-s2 con pgfplots). Explicar explícitamente por qué la gráfica de DoneTonic sale en recta: el backlog se registró al cierre, no al inicio. Esto cumple la spec: «Hay que explicar que las gráficas de DoneTonic del Sprint 2 salen en recta porque el backlog se registró al cerrar el sprint (29/10)».

> El backlog del Sprint 2 se registró en DoneTonic al cerrar el sprint (29/10), así que DoneTonic marca todos los PBIs como hechos ese día y sus gráficas salen como una recta. La evolución real se reconstruye con las fechas de los PRs.
> — `repo:saas/docs/documentacion-tecnica.md §4.5, repo:saas/docs/gestion/README.md §Evolución Sprint 2` (cita sin comprobar)

Relacionado: [[estado-de-completitud-de-sprints-y-trazabilidad]] · [[capturas-de-donetonic-disponibles-en-el-repo]] · [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]] · [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]] · [[datos-del-burndown-sprint-2-pbis-pendientes-por-dia]] · [[registro-retroactivo-del-sprint-2-en-donetonic-y-efecto-en-g]] · [[datos-del-burndown-sprint-1-pbis-pendientes-por-hito]]

## Ampliación (2026-11-16, memoria-procesos)
En el anexo A1 (Desarrollo) se deben mostrar ambos: la gráfica de DoneTonic (recta) y el burndown real (pgfplots con fechas de fusión de PRs: 23/10, 24/10, 26/10, 29/10). Explicar explícitamente que la recta se debe al registro tardío del backlog. La tabla de evolución real usa PBIs pendientes por fecha de último PR de cada PBI.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
