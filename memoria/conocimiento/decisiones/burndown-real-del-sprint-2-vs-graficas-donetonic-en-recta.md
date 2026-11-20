---
tipo: "decision"
titulo: "Burndown real del Sprint 2 vs gráficas DoneTonic en recta"
temas: ["burndown", "donetonic", "scrum", "sprint", "metricas"]
claves: ["Sprint 2", "DoneTonic", "recta", "backlog registrado al cerrar", "fechas PR"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/sprint-2.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[burndown]] · [[donetonic]] · [[scrum]] · [[sprint]]

|
  Evolución real (fechas de fusión PR en main):
  - 23/10: PR #36 → 1 PBI (base)
  - 24/10: PRs #44–#52 → 17 PBIs (personajes, movilidad, cámara, mapa, Fases 2–4)
  - 25/10: 0
  - 26/10: PRs #53, #54 → 9 PBIs (Fases 5–6)
  - 27/10: PR #55 → 0 (documentación)
  - 28/10: 0
  - 29/10: PR #56 + docs → 2 PBIs
  Burndown real: 28 → 11 → 11 → 2 → 2 → 2 → 0.
  En el anexo de desarrollo (a1-desarrollo.tex) se incluye la Tabla~\ref{tab:evolucion-s2} y la Figura~\ref{fig:burndown-s2} con pgfplots, y la Figura~\ref{fig:donetonic-s2-graficas} con la captura de DoneTonic en recta, con la explicación correspondiente.

> El backlog del Sprint 2 se registró en DoneTonic al cerrar el sprint (29/10/2026), así que DoneTonic marca todos los PBIs como hechos ese día y sus gráficas salen en recta. La evolución real se reconstruye con las fechas de fusión de los PR.
problema: Las gráficas de DoneTonic del Sprint 2 muestran una recta vertical (29→0 el 29/10) porque el backlog se registró al final, no durante el desarrollo.
solucion: En la memoria, mostrar ambas: la captura de DoneTonic (recta) y el burndown real reconstruido con fechas de PR (Tabla~\ref{tab:evolucion-s2} y Figura~\ref{fig:burndown-s2}). Explicar explícitamente por qué DoneTonic sale en recta y dar la evolución real día a día.
> — `repo:saas/docs/sprint-2.md` (cita sin comprobar)

## Ampliación (2026-11-20, memoria-procesos)
Evolución real: 23/10 (PR #36): 1 PBI; 24/10 (PRs #44–#52): 17 PBIs; 26/10 (PRs #53, #54): 9 PBIs; 29/10 (PRs #55, #56): 2 PBIs. Total 29 PBIs en 3 días de trabajo intenso. Velocity Chart confirma pico de 17 PBIs el 24/10.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
