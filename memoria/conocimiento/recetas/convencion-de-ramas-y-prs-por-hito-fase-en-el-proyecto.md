---
tipo: "receta"
titulo: "Convención de ramas y PRs por hito/fase en el proyecto"
temas: ["donetonic", "git", "grada-colchonera", "saas", "scrum", "sprint"]
claves: ["hito-1", "hito-2", "hito-3", "hito-4", "T1-T32", "T33-T82", "nomenclatura ramas", "GitHub Flow"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[git]] · [[grada-colchonera]] · [[saas]] · [[scrum]] · [[sprint]]

Patrón de nomenclatura de ramas extraído de las tablas: Sprint 1 usa `hito-X/TXX-descripcion` (ej. `hito-1/T1-estructura-base`, `hito-2/T9-cliente-api`, `hito-3/T15-configurar-bd`, `hito-4/T22-google-oauth`). Sprint 2 (fases de juego) usa PRs directos sin prefijo de hito en la tabla, pero los números de PR continúan (#36–#56). Hitos de cierre a `main`: #9 (Hito 1), #17 (Hito 2), #24 (Hito 3), #29 (cierre Sprint 1), #32 (revisión final). Cada tarea/PBI tiene PR(s) trazables. En Hito 4, una tarea DoneTonic puede mapear a varias ramas repo (P17 → 5 ramas).

> | PBI | Tarea | Descripción | Rama | Pull request | Estado | |---|---|---|---|---|---| | P1 | T1 | Crear repositorio y estructura base | `hito-1/T1-estructura-base` | [#1](https://github.com/VelaElDios/la-grada-colchonera-saas/pull/1) | Hecho | ... | P21 | Base del juego | Motor de la partida survivor | T35, T36 | #36 | 23/10/2026 | Hecho |
> — `repo:saas/docs/gestion/README.md` (cita sin comprobar)

Relacionado: [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]] · [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
