---
tipo: "concepto"
titulo: "GitHub Flow como modelo de ramificación del proyecto"
temas: ["git", "github-flow", "grada-colchonera"]
claves: ["GitHub Flow", "main", "hito-N/integracion", "hito-N/Tx-descripcion"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/CONTRIBUTING.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[git]] · [[github-flow]] · [[grada-colchonera]]

El proyecto adopta GitHub Flow como estrategia de ramificación. La rama `main` es la versión estable que se despliega automáticamente. Cada hito tiene una rama de integración (`hito-N/integracion`) creada desde `main` y que se fusiona de vuelta a `main` al cerrar el hito. Las tareas individuales se desarrollan en ramas `hito-N/Tx-descripcion` que nacen de la rama de integración del hito y se integran en ella mediante PR.

> Este repositorio sigue **GitHub Flow**, organizado según los hitos y las tareas del backlog en DoneTonic (proyecto *Colchoneros*).
> — `repo:saas/CONTRIBUTING.md`

Relacionado: [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
