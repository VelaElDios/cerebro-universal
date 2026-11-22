---
tipo: "concepto"
titulo: "Convención de ramas y PRs por sprint (Sprint 1 vs Sprint 2)"
temas: ["donetonic", "grada-colchonera", "saas", "scrum"]
claves: ["rama", "PR", "hito-N/Tx", "main", "fase", "convención nombres"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
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

Relacionado: [[flujo-de-trabajo-enunciado-codigo-deploy-donetonic-github]] · [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]] · [[backlog-sprint-2-con-prs-fechas-de-fusion-y-estado-por-pbi]] · [[convencion-de-ramas-y-prs-por-hito-fase-en-el-proyecto]] · [[metricas-comparativas-sprint-1-vs-sprint-2]] · [[burndown-real-del-sprint-2-vs-graficas-donetonic-en-recta]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[fases-del-sprint-2-y-prs-asociados]]: La nota A afirma que en el Sprint 2 hubo «un PR por fase de juego (#36, #44–#54)», implicando que cada uno de esos 11 PRs (#44 a #54) corresponde a una fase. La nota B lista los mismos PRs pero muestra que solo #36, #49, #50, #52, #53 y #54 están etiquetados como «Fase 1» a «Fase 6»; #44–#48 y #51 son mejoras/arreglos sueltos, no fases.

> ⚠️ Posible contradicción con [[backlog-sprint-2-con-prs-fechas-de-fusion-y-estado-por-pbi]]: La Nota A afirma que en el Sprint 2 hubo «un único PR por fase de juego (#36, #44–#54)», implicando que cada uno de esos 11 PRs corresponde a una fase. La Nota B muestra que solo 6 PRs (#36, #49, #50, #52, #53, #54) se asocian a las fases 1–6; los PRs #44–#48 y #51 son mejoras/arreglos de «Base del juego» o «Calidad», no fases de juego.

> ⚠️ Posible contradicción con [[sprint-2-recoge-juego-ya-hecho-6-fases-preexistentes-como-ba]]: La Nota A describe el Sprint 2 como el periodo de **integración/desarrollo de la lógica de juego** mediante «un PR por fase» (11 PRs #36, #44–#54 fusionados en `main`). La Nota B afirma que el Sprint 2 **no desarrolló lógica nueva**, sino que solo documentó como backlog 6 fases **ya implementadas** antes del sprint; las fusiones de esos 6 PRs de fase ocurrieron en la semana del sprint, pero el código ya existía.

> ⚠️ Posible contradicción con [[evolucion-por-fases-del-sprint-2-etiquetas-donetonic-adicion]]: La Nota A afirma que en el Sprint 2 hubo «un único PR por fase de juego» listando 12 PRs (#36, #44–#54), implicando 12 fases. La Nota B enumera 8 fases/etiquetas DoneTonic para el Sprint 2 (Rediseño, Fases 1 a 7). Además, la Nota A encuadra el Sprint 2 como «lógica juego», mientras que la Nota B incluye una fase inicial de «Rediseño» (interfaz/UX) ajena a la lógica de juego.
