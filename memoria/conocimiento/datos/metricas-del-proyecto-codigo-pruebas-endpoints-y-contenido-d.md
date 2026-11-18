---
tipo: "dato"
titulo: "Métricas del proyecto: código, pruebas, endpoints y contenido del juego"
temas: ["grada-colchonera", "metricas", "saas", "sprint"]
claves: ["PBIs", "tareas", "PRs", "releases", "322 pruebas", "23 endpoints", "5 migraciones", "2300 líneas backend", "1150 frontend", "950 CSS", "14800 juego", "5050 pruebas", "6 dependencias", "36 jugadores", "29 armas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[metricas]] · [[saas]] · [[sprint]]

Resumen cuantitativo del proyecto: Sprint 1: 19 PBIs, 32 tareas; Sprint 2: 29 PBIs, 50 tareas. >50 PRs (1 por tarea + cierres de hito + fases de juego). 5 releases: `hito-1` a `hito-4` y `sprint-1`. 322 tests automáticos + test DB real en CI. 23 endpoints API. 5 migraciones SQL. Código: backend ~2.3k líneas (src/ + SQL), frontend web ~1.15k (ui.js, api.js, ui/), CSS ~950, juego ~14.8k (35 módulos en public/js/game/), tests ~5.05k. 6 dependencias producción: express, express-session, connect-pg-simple, pg, bcryptjs, nodemailer. Contenido juego: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.

> Métrica Valor PBIs / tareas del Sprint 1 19 / 32 PBIs / tareas del Sprint 2 29 / 50 Pull requests Más de 50 (uno por tarea, uno por cierre de hito y uno por fase del juego) Releases hito-1, hito-2, hito-3, hito-4, sprint-1 Pruebas automáticas 322 (+ el recorrido con PostgreSQL real en el CI) Endpoints de la API 23 Migraciones 5 Líneas de código del backend (src/, con SQL) ~2.300 Líneas de la interfaz web (ui.js, api.js, ui/) ~1.150 Líneas de CSS ~950 Líneas del juego (public/js/game/, 35 módulos) ~14.800 Líneas de pruebas ~5.050 Dependencias de producción 6 (express, express-session, connect-pg-simple, pg, bcryptjs, nodemailer) Contenido del juego 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]] · [[requisitos-funcionales-del-juego-sprint-2-20-rj-con-trazabil]] · [[numeros-clave-del-proyecto-contrastados-con-fuentes]] · [[estado-de-completitud-de-sprints-y-trazabilidad]] · [[metricas-comparativas-sprint-1-vs-sprint-2]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
