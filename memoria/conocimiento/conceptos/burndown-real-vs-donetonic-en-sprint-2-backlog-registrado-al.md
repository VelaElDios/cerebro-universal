---
tipo: "concepto"
titulo: "Burndown real vs DoneTonic en Sprint 2 (backlog registrado al cerrar)"
temas: ["burndown", "donetonic", "métricas", "scrum"]
claves: ["burndown", "DoneTonic", "recta", "backlog registrado al cerrar"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
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

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
