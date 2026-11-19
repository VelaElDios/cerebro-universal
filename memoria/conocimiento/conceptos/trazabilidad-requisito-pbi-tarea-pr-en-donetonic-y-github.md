---
tipo: "concepto"
titulo: "Trazabilidad requisito → PBI → tarea → PR en DoneTonic y GitHub"
temas: ["gestión", "github flow", "scrum", "trazabilidad", "donetonic", "github", "pr", "pbi", "pull-request", "tarea"]
claves: ["PBI", "tarea", "PR", "DoneTonic", "GitHub Flow", "problema: La memoria debe mostrar trazabilidad completa desde requisito hasta pull request.", "solucion: Usar tablas de trazabilidad por sprint (Anexo A4). En Sprint 1 cada tarea tiene rama y PR individual; en Sprint 2 cada tarea indica PR en su descripción DoneTonic (un PR por fase). Las fuentes son docs/gestion/README.md (tablas trazabilidad) y docs/documentacion-tecnica.md (§3 requisitos → PBI)."]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md", "repo:saas/docs/gestion/README.md §4.4, §4.5"]
confianza: "verificado"
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

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
