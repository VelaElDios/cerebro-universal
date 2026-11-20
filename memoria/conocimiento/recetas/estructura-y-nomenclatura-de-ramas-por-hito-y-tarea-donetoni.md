---
tipo: "receta"
titulo: "Estructura y nomenclatura de ramas por hito y tarea DoneTonic"
temas: ["donetonic", "git", "github-flow", "grada-colchonera"]
claves: ["hito-N/integracion", "hito-N/Tx-descripcion", "Tx", "Px", "DoneTonic"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/CONTRIBUTING.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[git]] · [[github-flow]] · [[grada-colchonera]]

- Rama principal: `main` (estable, despliegue automático)
- Rama de integración por hito: `hito-N/integracion` (se crea desde `main`, se integra en `main` al cerrar hito)
- Rama de tarea: `hito-N/Tx-descripcion` (se crea desde `hito-N/integracion`, se integra en `hito-N/integracion` al terminar tarea)
- `Tx` = identificador de tarea en DoneTonic (ej. T5)
- El PR debe referenciar también el PBI (`Px`) al que pertenece la tarea
- Nunca se trabaja directamente sobre `main` ni sobre `hito-N/integracion`

> `Tx` es el identificador de la tarea en DoneTonic (por ejemplo `T5`). El PR indica también su PBI (`Px`).
> — `repo:saas/CONTRIBUTING.md`

Relacionado: [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]] · [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]] · [[github-flow-como-modelo-de-ramificacion-del-proyecto]] · [[github-flow-por-hitos-con-ramas-protegidas-y-ci-obligatorio]] · [[convencion-de-ramas-y-prs-por-hito-fase-en-el-proyecto]] · [[reglas-de-integracion-mediante-pull-requests-con-ci-obligato]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[flujo-de-trabajo-enunciado-codigo-deploy-donetonic-github]]: La nota A establece como regla general que **toda tarea** se ramifica desde `hito-N/integracion` y se fusiona en esa misma rama de integración del hito, la cual solo se une a `main` al cerrar el hito. La nota B describe que en el **Sprint 2** (que corresponde a un hito) no se usa esa rama de integración: se abren PRs por fase de juego que se fusionan **directamente en `main`** (#36, #44–#54), saltándose `hito-N/integracion`.
