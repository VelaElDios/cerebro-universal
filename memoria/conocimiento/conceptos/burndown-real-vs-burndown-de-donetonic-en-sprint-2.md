---
tipo: "concepto"
titulo: "Burndown real vs. DoneTonic en Sprint 2 (backlog registrado al cerrar el sprint)"
temas: ["burndown", "donetonic", "graficas", "metricas", "métricas", "scrum", "sprint", "sprint2"]
claves: ["burndown", "DoneTonic", "recta", "registro al cierre", "backlog registrado al cerrar"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md §4.5, repo:saas/docs/gestion/README.md §Evolución Sprint 2", "repo:saas/docs/gestion/README.md §Evolución del Sprint 2", "repo:saas/docs/gestion/README.md", "repo:saas/docs/documentacion-tecnica.md §4.4, §4.5", "repo:saas/docs/sprint-2.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-24"
---

Temas: [[burndown]] · [[donetonic]] · [[graficas]] · [[metricas]] · [[métricas]] · [[scrum]] · [[sprint]] · [[sprint2]]

Temas: [[burndown]] · [[donetonic]] · [[métricas]] · [[metricas]] · [[scrum]]

En el **Anexo A1 (Desarrollo, `a1-desarrollo.tex`)** se deben mostrar **ambos** burndowns del Sprint 2:

1. **DoneTonic (recta)**: Captura en **Figura~\ref{fig:donetonic-s2-graficas}** (subfigura) con nota: *"Gráficas en recta porque el backlog se registró al cerrar el sprint (29/10/2026)"*. DoneTonic muestra una recta 29 → 0 el 29/10.
2. **Real reconstruido**: **Tabla~\ref{tab:evolucion-s2}** (Tabla 4.5) y **Figura~\ref{fig:burndown-s2}** (pgfplots) usando **fechas de fusión de PRs**.

### Datos del burndown real (PBIs hechos / pendientes por fecha de último PR de cada PBI)
| Fecha | PRs | PBIs hechos ese día | PBIs pendientes |
|-------|-----|---------------------|-----------------|
| 23/10/2026 | #36 | 1 | 28 |
| 24/10/2026 | #44–#52 | 17 | 11 |
| 25/10/2026 | — | 0 | 11 |
| 26/10/2026 | #53, #54 | 9 | 2 |
| 27/10/2026 | #55 | 0 | 2 |
| 28/10/2026 | — | 0 | 2 |
| 29/10/2026 | #56, docs | 2 | 0 |

> **Explicación obligatoria**: El backlog del Sprint 2 se registró en DoneTonic **al cerrar el sprint (29/10/2026)**, por eso DoneTonic marca todos los PBIs como hechos ese día y sus gráficas salen como una recta. La evolución real se reconstruye con las fechas de fusión de los PRs.
> — `repo:saas/docs/documentacion-tecnica.md §4.5`, `repo:saas/docs/gestion/README.md §Evolución Sprint 2` (citas sin comprobar)

### Problema / Solución en la memoria
- **Problema**: Las gráficas de DoneTonic del Sprint 2 salen en recta (29 a 0 el 29/10), no reflejan la evolución real.
- **Solución**: Mostrar ambas: la captura de DoneTonic (Figura con subfiguras) explicando que sale en recta porque el backlog se registró al cerrar, y el burndown real reconstruido con fechas de PR (Tabla y Figura con pgfplots). Incluir esta explicación en la retrospectiva del Anexo A1.

---

## Ampliación (2026-11-16, memoria-procesos)
En el anexo A1 (Desarrollo) se deben mostrar ambos: la gráfica de DoneTonic (recta) y el burndown real (pgfplots con fechas de fusión de PRs: 23/10, 24/10, 26/10, 29/10). Explicar explícitamente que la recta se debe al registro tardío del backlog. La tabla de evolución real usa PBIs pendientes por fecha de último PR de cada PBI.

## Ampliación (2026-11-19, memoria-procesos)
DoneTonic Sprint 2: gráficas en recta (29→0 el 29/10). Evolución real (Tabla 4.5 y Figura `burndown-s2`): desglose diario completo (ver tabla arriba). En memoria: **Figura `fig:burndown-s2`** (pgfplots con datos reales) y **Figura `fig:donetonic-s2-graficas`** (captura DoneTonic en recta) con explicación explícita.

**Relacionado**:  
[[estado-de-completitud-de-sprints-y-trazabilidad]] · [[capturas-de-donetonic-disponibles-en-el-repo]] · [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]] · [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]] · [[datos-del-burndown-sprint-2-pbis-pendientes-por-dia]] · [[registro-retroactivo-del-sprint-2-en-donetonic-y-efecto-en-g]] · [[datos-del-burndown-sprint-1-pbis-pendientes-por-hito]] · [[Fechas y estructura de los dos sprints con PBIs y tareas]] · [[Trazabilidad requisito-PBI-tarea-PR en DoneTonic y GitHub]]

Relacionado: [[burndown-real-del-sprint-2-vs-graficas-donetonic-en-recta]] · [[burndown-real-vs-donetonic-en-sprint-2-explicacion-obligator]]

## Ampliación (2026-11-24, memoria-procesos)
|
  - Desarrollo real: 23/10 (PR #36, 1 PBI), 24/10 (PRs #44–#52, 17 PBIs), 26/10 (PRs #53–#54, 9 PBIs), 27/10 (#55), 29/10 (#56, docs).
  - DoneTonic: todo registrado el 29/10 → gráficas en recta.
  - Esto se explica en la retrospectiva del Sprint 2 del Anexo A.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
<<<CONTRADICCION>>
no

> El backlog del Sprint 2 se registró en DoneTonic al cerrar el sprint (29/10), así que DoneTonic marca todos los PBIs como hechos ese día y sus gráficas salen como una recta. La evolución real se reconstruye con las fechas de los PRs.
> — `repo:saas/docs/documentacion-tecnica.md §4.5, repo:saas/docs/gestion/README.md §Evolución Sprint 2` (cita sin comprobar)

Fusionada con: Burndown real vs DoneTonic en Sprint 2 (backlog registrado al cerrar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
