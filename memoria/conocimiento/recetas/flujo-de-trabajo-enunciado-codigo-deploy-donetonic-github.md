---
tipo: "receta"
titulo: "Flujo de trabajo enunciado → código → deploy (DoneTonic + GitHub)"
temas: ["donetonic", "grada-colchonera", "saas", "scrum", "github", "memoria-procesos"]
claves: ["flujo trabajo", "PBI", "tarea", "rama", "PR", "CI", "deploy", "Cloud Run"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[grada-colchonera]] · [[saas]] · [[scrum]]

Proceso estandarizado en 5 pasos:
1. **Enunciado → Backlog**: Cada requisito → PBI con historia de usuario ("Como… quiero… para…") + criterios de aceptación. Sprint 1: requisitos del enunciado. Sprint 2: lógica del juego agrupada por fases.
2. **PBI → Tareas**: Cada PBI se divide en 1–3 tareas (mínimo necesario).
3. **Tarea → Código**:
   - Sprint 1: una rama por tarea `hito-N/Tx-descripcion` → PR titulado `[Tx] ...` → integra en rama del hito.
   - Sprint 2: un PR por fase de juego (#36, #44–#54) → integra en `main`. Cada tarea en DoneTonic referencia su PR con `PR: #nn` en la descripción.
4. **Integración → Deploy**: Todos los PRs requieren CI verde. Al fusionar en `main`, deploy automático en Google Cloud Run (URL: https://la-grada-colchonera-1081564062572.europe-southwest1.run.app).
5. **Seguimiento automático**: Merge de PR → tarea a HECHO en DoneTonic. Todas las tareas de un PBI hechas → PBI a HECHO automático. Gráficas se actualizan solas.

> 5. **Seguimiento.** Al fusionar cada PR, su tarea pasa a *HECHO* en el tablero. Cuando todas las tareas de un PBI están hechas, el PBI pasa a *HECHO* automáticamente.
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[estrategia-de-pruebas-error-first-y-ci-como-requisito-de-mer]]

## Ampliación (2026-11-16, memoria-procesos)
Proceso estandarizado en 5 pasos: 1) **Enunciado → Backlog**: Cada requisito → PBI con historia de usuario ("Como… quiero… para…") + criterios de aceptación. Sprint 1: requisitos del enunciado. Sprint 2: lógica del juego agrupada por fases. 2) **PBI → Tareas**: Cada PBI se divide en 1–3 tareas (mínimo necesario). 3) **Tarea → Código**: Sprint 1: una rama por tarea `hito-N/Tx-descripcion` → PR titulado `[Tx] ...` → integra en rama del hito. Sprint 2: un PR por fase de juego (#36, #44–#54) → integra en `main`. Cada tarea en DoneTonic referencia su PR con `PR: #nn` en la descripción. 4) **Integración → Deploy**: Todos los PRs requieren CI verde. Al fusionar en `main`, deploy automático en Google Cloud Run (URL: https://la-grada-colchonera-1081564062572.europe-southwest1.run.app). 5) **Seguimiento automático**: Merge de PR → tarea a HECHO en DoneTonic. Todas las tareas de un PBI hechas → PBI a HECHO automático. Gráficas se actualizan solas.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
