---
tipo: "receta"
titulo: "Reglas de integración mediante Pull Requests con CI obligatorio"
temas: ["git", "github-flow", "grada-colchonera", "scrum"]
claves: ["PR", "CI", "pull request", "integración", "main", "hito-N/integracion"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/CONTRIBUTING.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[git]] · [[github-flow]] · [[grada-colchonera]] · [[scrum]]

Dos niveles de PR obligatorios con CI en verde:
1. **PR de tarea**: de `hito-N/Tx-descripcion` a `hito-N/integracion` al terminar cada tarea individual.
2. **PR de hito**: de `hito-N/integracion` a `main` al cerrar el hito completo.
Ningún PR se integra si el CI está en rojo. El CI ejecuta las pruebas automáticamente en cada PR.

> PR al cerrar el hito, con el CI en verde / PR al terminar la tarea, con el CI en verde
> — `repo:saas/CONTRIBUTING.md` (cita sin comprobar)

Relacionado: [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]] · [[estructura-y-nomenclatura-de-ramas-por-hito-y-tarea-donetoni]] · [[github-flow-por-hitos-con-ramas-protegidas-y-ci-obligatorio]] · [[github-flow-como-modelo-de-ramificacion-del-proyecto]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
