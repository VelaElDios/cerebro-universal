---
tipo: "concepto"
titulo: "Convención de ramas y PRs por sprint (Sprint 1 vs Sprint 2)"
temas: ["donetonic", "grada-colchonera", "saas", "scrum"]
claves: ["rama", "PR", "hito-N/Tx", "main", "fase", "convención nombres"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-18"
---

Temas: [[donetonic]] · [[grada-colchonera]] · [[saas]] · [[scrum]]

Diferencia clave en la estrategia de branching/PR entre sprints:
- **Sprint 1 (base SaaS)**: Granularidad por tarea. Rama por tarea: `hito-N/Tx-descripcion` (ej. `hito-1/T1-repo-setup`). PR titulado `[Tx] descripción` → se fusiona en la rama del hito (`hito-1`, `hito-2`, etc.). Al cerrar el hito, su rama va a `main` y se taggea como release (`hito-1`, `hito-2`, `hito-3`, `hito-4`).
- **Sprint 2 (lógica juego)**: Granularidad por fase. Un único PR por fase de juego (#36, #44–#54) → se fusiona directamente en `main`. Las tareas de DoneTonic referencian su PR con `PR: #nn` en la descripción.
Razón implícita: Sprint 1 requería entregas parciales evaluables (hitos con releases), Sprint 2 era un bloque único de funcionalidad de juego integrada en fases.

> En el Sprint 1 cada tarea tiene una rama propia `hito-N/Tx-descripcion` que se integra en la rama del hito mediante un PR `[Tx] ...`. En el Sprint 2 el trabajo se integró en `main` con **un PR por fase** del juego (#36, #44–#54), y cada tarea de DoneTonic indica en su descripción el PR donde está (`PR: #nn`).
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[flujo-de-trabajo-enunciado-codigo-deploy-donetonic-github]] · [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]] · [[backlog-sprint-2-con-prs-fechas-de-fusion-y-estado-por-pbi]] · [[convencion-de-ramas-y-prs-por-hito-fase-en-el-proyecto]] · [[metricas-comparativas-sprint-1-vs-sprint-2]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[fases-del-sprint-2-y-prs-asociados]]: La nota A afirma que en el Sprint 2 hubo «un PR por fase de juego (#36, #44–#54)», implicando que cada uno de esos 11 PRs (#44 a #54) corresponde a una fase. La nota B lista los mismos PRs pero muestra que solo #36, #49, #50, #52, #53 y #54 están etiquetados como «Fase 1» a «Fase 6»; #44–#48 y #51 son mejoras/arreglos sueltos, no fases.
