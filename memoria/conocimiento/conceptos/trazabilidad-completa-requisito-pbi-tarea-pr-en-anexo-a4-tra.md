---
tipo: "concepto"
titulo: "Trazabilidad completa requisito → PBI → tarea → PR en anexo a4-trazabilidad.tex"
temas: ["anexo", "longtable", "trazabilidad"]
claves: ["requisito", "PBI", "tarea", "PR", "longtable", "82 tareas"]
proyectos: ["memoria-procesos"]
fuentes: ["spec del proyecto (tabla Anexos), repo:saas/docs/documentacion-tecnica.md §3, repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[anexo]] · [[longtable]] · [[trazabilidad]]

El anexo a4-trazabilidad.tex debe contener una `longtable` con 5 columnas: Requisito, PBI, Tarea, Descripción de la tarea, PR. Filas: (1) RNF transversales (12 filas, una por RNF con sus PBIs/tareas/PRs); (2) Sprint 1: 32 filas (una por tarea T1–T32) con su requisito/PBI; (3) Sprint 2: 50 filas (T33–T82) con su RJ/PBI. Total ~94 filas. Usar `\small` y `longtable` para que parta por páginas. Citar PRs con `#nn` (linkable si se usa hyperref). Al final, nota con cierres de hito y releases.

> Tabla completa (longtable) requisito → PBI → tarea → PR de los dos sprints: todos los PBIs P1–P48 y todas las tareas T1–T82.
> — `spec del proyecto (tabla Anexos), repo:saas/docs/documentacion-tecnica.md §3, repo:saas/docs/gestion/README.md` (cita sin comprobar)

Relacionado: [[estado-de-completitud-de-sprints-y-trazabilidad]] · [[historias-de-usuario-y-criterios-de-aceptacion-en-donetonic]] · [[burndown-real-vs-burndown-de-donetonic-en-sprint-2]] · [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
