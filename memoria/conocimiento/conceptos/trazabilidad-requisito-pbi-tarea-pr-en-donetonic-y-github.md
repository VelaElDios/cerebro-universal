---
tipo: "concepto"
titulo: "Trazabilidad requisito → PBI → tarea → PR en DoneTonic y GitHub"
temas: ["gestión", "github flow", "scrum", "trazabilidad", "donetonic", "github", "pr", "pbi", "pull-request", "tarea"]
claves: ["PBI", "tarea", "PR", "DoneTonic", "GitHub Flow", "problema: La memoria debe mostrar trazabilidad completa desde requisito hasta pull request.", "solucion: Usar tablas de trazabilidad por sprint (Anexo A4). En Sprint 1 cada tarea tiene rama y PR individual; en Sprint 2 cada tarea indica PR en su descripción DoneTonic (un PR por fase). Las fuentes son docs/gestion/README.md (tablas trazabilidad) y docs/documentacion-tecnica.md (§3 requisitos → PBI)."]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md", "repo:saas/docs/gestion/README.md §4.4, §4.5"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[gestión]] · [[github flow]] · [[scrum]] · [[trazabilidad]]

|
  - Sprint 1: 19 PBIs, 32 tareas, PRs #1–#34, #37–#41. Cierres de hito: #9, #17, #24, #29, #32.
  - Sprint 2: 29 PBIs, 50 tareas, PRs #36, #44–#56. Fechas de fusión dan evolución real.
  - Tabla Anexo A4: 82 filas (12 RNF transversales + 32 tareas S1 + 50 tareas S2).

## Ampliación (2026-11-19, memoria-procesos)
|
  Sprint 1 (32 tareas): T1–T32 → ramas hito-1/... a hito-4/... → PRs #1–#41 + cierres #9, #17, #24, #29, #32.
  Sprint 2 (50 tareas): T33–T82 → PRs #36, #44–#56 (uno por fase/arreglo).
  Total: 82 tareas, >50 PRs fusionados.
  Releases: hito-1, hito-2, hito-3, hito-4, sprint-1.

## Ampliación (2026-11-19, memoria-procesos)
Sprint 1: 32 tareas T1-T32 → ramas `hito-N/Tx-descripcion` → PRs #1-#34, #37-#41 → releases hito-1, hito-2, hito-3, hito-4, sprint-1. Sprint 2: 50 tareas T33-T82 → PRs #36, #44-#56 (uno por fase/arreglo) → main. Trazabilidad completa en Anexo A4 (tabla 82 filas). Cierres de hito: PR #9, #17, #24, #29, #32. Evolución Sprint 1: 16 PBIs alcance entrega (P1-P14, P18, P19). Evolución Sprint 2 real (fechas PR): 23/10 (1 PBI), 24/10 (17 PBIs), 26/10 (9 PBIs), 29/10 (2 PBIs). DoneTonic Sprint 2 muestra recta porque backlog registrado al cerrar sprint (29/10).
relacionado: Fechas y estructura de los dos sprints con PBIs y tareas, Inventario de capturas de pantalla con trazabilidad a requisitos y fechas, Burndown real vs DoneTonic en Sprint 2 (backlog registrado al cierre)

Relacionado: [[fechas-pbis-y-tareas-de-los-dos-sprints]] · [[trazabilidad-completa-requisito-pbi-tarea-pr-82-tareas]] · [[fechas-pbis-y-tareas-de-los-dos-sprints]] · [[backlog-completo-del-sprint-1-con-trazabilidad-a-releases]] · [[fechas-pbis-tareas-y-estructura-de-los-dos-sprints]] · [[metricas-comparativas-sprint-1-vs-sprint-2]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[datos-del-burndown-sprint-1-pbis-pendientes-por-hito]]: Nota A afirma que el Sprint 1 tuvo 19 PBIs (primer viñeta) y menciona cuatro releases de hito (hito-1 a hito-4) más sprint-1; Nota B indica que el Sprint 1 tuvo 16 PBIs totales (15 iniciales + P19 añadido) y su burndown solo registra tres hitos (hito-1, hito-2, hito-3) antes del cierre del sprint.

> ⚠️ Posible contradicción con [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]]: La **Nota A** delimita el Hito 4 en **6 tareas (T21–T26)** y afirma que esas seis se marcaron hechas al cerrar el Sprint 1. La **Nota B** establece que el Sprint 1 tiene **32 tareas (T1–T32)** e incluye la release `hito-4`, lo que implica que el Hito 4 abarca hasta la T32 (12 tareas: T21–T32), no solo hasta la T26.

> ⚠️ Posible contradicción con [[fases-del-sprint-2-y-prs-asociados]]: La Nota A describe 6 fases para el Sprint 2 (Fase 1 a Fase 6 en PRs #36, #49, #50, #52, #53, #54). La Nota B, en su bloque de advertencia ⚠️, afirma textualmente que su propia ampliación del 2026-11-19 establece que el Sprint 2 tuvo **7 fases**.

> ⚠️ Posible contradicción con [[cifras-clave-del-proyecto-la-grada-colchonera-contrastadas]]: Nota A (en su advertencia ⚠️ sobre [[fases-del-sprint-2-y-prs-asociados]]) describe 6 fases para el Sprint 2 (Fase 1 a Fase 6). Nota B (en su Ampliación 2026-11-21) afirma explícitamente que el Sprint 2 tuvo **7 fases**.
