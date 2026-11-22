---
tipo: "decision"
titulo: "Sprint 2 recoge juego ya hecho: 6 fases preexistentes como backlog"
temas: ["decision", "donetonic", "grada-colchonera", "saas", "scrum", "sprint"]
claves: ["Sprint 2", "lógica del juego", "6 fases", "backlog", "profesor", "ya estaba hecho"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[decision]] · [[donetonic]] · [[grada-colchonera]] · [[saas]] · [[scrum]] · [[sprint]]

Decisión del profesor: Sprint 2 (23/10–29/10/2026) no desarrolla nueva lógica de juego, sino que documenta y traza lo ya implementado. El juego completo existía en 6 fases (Base, Club, Ultras, Mundo, Rarezas, Logros y sonido). El sprint convierte ese trabajo previo en backlog formal: 29 PBIs, 50 tareas, etiquetas por fase. Esto explica la alta velocidad (todo "Hecho" en pocos días) y que las fechas de fusión sean 23–29/10/2026.

> Del 23/10/2026 al 29/10/2026. Cerrado el Sprint 1, el profesor fijó que el **Sprint 2 es la lógica del juego**. El juego ya estaba hecho, en seis fases, así que el sprint recoge ese trabajo como backlog: 29 PBIs (P20–P48) y 50 tareas (T33–T82), con una etiqueta por fase.
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[cronologia-detallada-del-proyecto-septiembre-octubre-2026]] · [[estructura-sprint-2-6-fases-calidad-29-pbis-50-tareas-fechas]] · [[backlog-sprint-2-con-prs-fechas-de-fusion-y-estado-por-pbi]] · [[registro-retroactivo-del-sprint-2-en-donetonic-y-efecto-en-g]] · [[fases-del-sprint-2-y-prs-asociados]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[evolucion-por-fases-del-sprint-2-etiquetas-donetonic-adicion]]: La Nota A describe 7 fases de **desarrollo nuevo** en el Sprint 2 (Rediseño + Fases 1-7) añadiendo características y resolviendo problemas. La Nota B afirma que el Sprint 2 **no desarrolla lógica nueva**, sino que documenta 6 fases preexistentes (Base, Club, Ultras, Mundo, Rarezas, Logros y sonido) como backlog formal. Además, el número de fases difiere (7 vs 6).

> ⚠️ Posible contradicción con [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]]: La Nota A describe el Sprint 2 como el periodo de **integración/desarrollo de la lógica de juego** mediante «un PR por fase» (11 PRs #36, #44–#54 fusionados en `main`). La Nota B afirma que el Sprint 2 **no desarrolló lógica nueva**, sino que solo documentó como backlog 6 fases **ya implementadas** antes del sprint; las fusiones de esos 6 PRs de fase ocurrieron en la semana del sprint, pero el código ya existía.

> ⚠️ Posible contradicción con [[burndown-real-del-sprint-2-vs-graficas-donetonic-en-recta]]: La Nota A describe el Sprint 2 como un periodo de **desarrollo nuevo e integración** (7 fases, 11 PRs fusionados en main del 23 al 29/10 añadiendo características y resolviendo problemas). La Nota B afirma que el Sprint 2 **no desarrolló lógica nueva**, sino que solo documentó como backlog 6 fases **ya implementadas antes del sprint**; las fusiones ocurrieron esa semana pero el código preexistía.
