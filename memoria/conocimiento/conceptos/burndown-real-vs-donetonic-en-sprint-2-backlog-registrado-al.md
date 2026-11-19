---
tipo: "concepto"
titulo: "Burndown real vs DoneTonic en Sprint 2 (backlog registrado al cerrar)"
temas: ["burndown", "donetonic", "métricas", "scrum", "graficas", "metricas", "sprint2"]
claves: ["burndown", "DoneTonic", "recta", "backlog registrado al cerrar"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md", "repo:saas/docs/documentacion-tecnica.md §4.4, §4.5"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[burndown]] · [[donetonic]] · [[métricas]] · [[scrum]]

|
  - Captura DoneTonic Sprint 2: Figura~\ref{fig:donetonic-s2-graficas} (subfigura) con nota: "Gráficas en recta porque el backlog se registró al cerrar el sprint (29/10/2026)".
  - Burndown real: Tabla~\ref{tab:evolucion-s2} y Figura~\ref{fig:burndown-s2} con pgfplots usando fechas de fusión de PRs: 23/10 (1 PBI), 24/10 (17 PBIs), 26/10 (9 PBIs), 29/10 (2 PBIs).
  - Explicar en retrospectiva del Anexo A1.

> El backlog del Sprint 2 se registró en DoneTonic al cerrar el sprint (29/10/2026), así que DoneTonic marca todos los PBIs como hechos ese día y sus gráficas salen como una recta. La evolución real se reconstruye con las fechas de fusión de los PRs."
problema: Las gráficas de DoneTonic del Sprint 2 salen en recta (29 a 0 el 29/10), no reflejan la evolución real.
solucion: En la memoria, mostrar ambas: la captura de DoneTonic (Figura con subfiguras) explicando que sale en recta porque el backlog se registró al cerrar, y el burndown real reconstruido con fechas de PR (Tabla y Figura con pgfplots).
> — `repo:saas/docs/gestion/README.md` (cita sin comprobar)

## Ampliación (2026-11-19, memoria-procesos)
DoneTonic Sprint 2: gráficas en recta (29→0 el 29/10). Evolución real (Tabla 4.5 y Figura burndown-s2): 23/10 (PR #36): 1 PBI hecho, 28 pendientes; 24/10 (PRs #44-#52): 17 PBIs, 11 pendientes; 25/10: 0, 11 pendientes; 26/10 (PRs #53, #54): 9 PBIs, 2 pendientes; 27/10 (PR #55): 0, 2 pendientes; 28/10: 0, 2 pendientes; 29/10 (PR #56, docs): 2 PBIs, 0 pendientes. En memoria: Figura fig:burndown-s2 (pgfplots con datos reales) y Figura fig:donetonic-s2-graficas (captura DoneTonic en recta) con explicación explícita.
relacionado: Fechas y estructura de los dos sprints con PBIs y tareas, Trazabilidad requisito-PBI-tarea-PR en DoneTonic y GitHub

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
