---
tipo: "dato"
titulo: "Números clave del proyecto contrastados con fuentes"
temas: ["metricas", "trazabilidad", "verificacion", "métricas", "verificación"]
claves: ["19 PBIs", "32 tareas", "29 PBIs", "50 tareas", "276 pruebas", "322 pruebas", "82 tareas", "5 migraciones", "23 endpoints"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md, repo:saas/docs/gestion/README.md", "repo:saas/docs/documentacion-tecnica.md §14 y repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[metricas]] · [[trazabilidad]] · [[verificacion]]

Cifras verificadas contra las fuentes para usar en la memoria sin inventar: 19 PBIs Sprint 1 (pero burndown entrega cuenta 16: P1–P14, P18, P19); 29 PBIs Sprint 2; 32+50=82 tareas; 13 RF, 20 RJ, 12 RNF; 5 migraciones; 23 endpoints; 6 dependencias producción; ~2.300 LOC backend, ~1.150 frontend, ~950 CSS, ~14.800 juego, ~5.050 tests; 36 jugadores, 2 entrenadores, 24 armas, 14 pasivas, 24 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.

> Sprint 1: 19 PBIs (P1–P19) y 32 tareas (T1–T32). Sprint 2: 29 PBIs (P20–P48) y 50 tareas (T33–T82). Pruebas: 276 (140 Sprint 1 + 136 juego) + CI con PostgreSQL real = 322 totales. Migraciones: 5. Endpoints API: 23.
> — `repo:saas/docs/documentacion-tecnica.md, repo:saas/docs/gestion/README.md` (cita sin comprobar)

Relacionado: [[estado-de-completitud-de-sprints-y-trazabilidad]] · [[metricas-comparativas-sprint-1-vs-sprint-2]] · [[metricas-del-proyecto-codigo-pruebas-endpoints-y-contenido-d]] · [[cifras-clave-del-proyecto-verificadas-en-fuentes]] · [[numeros-clave-del-proyecto-verificados-en-fuentes]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes]]

## Ampliación (2026-11-16, memoria-procesos)
Todos los números mayores que 20 aparecen en las fuentes. Los pequeños (19, 29, 32, 50, 5, 23, 6, 10, 14, 16, 24, 26) también se han contrastado con las tablas de la documentación técnica y la gestión. El burndown de la entrega del Sprint 1 cuenta 16 PBIs (P1–P14, P18, P19) porque P15–P17 son del Hito 4 y se entregaron después.

## Ampliación (2026-11-16, memoria-procesos)
|
  - Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32). Burndown de la entrega cuenta 16 PBIs (P1–P14, P18, P19).
  - Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82).
  - Total tareas: 82.
  - Pruebas: 322 totales (276 + CI con PostgreSQL real).
  - Migraciones: 5 (001 usuarios, 002 sesiones, 003 juego, 004 identidad, 005 email libre tras baja).
  - API: 23 endpoints.
  - Juego: 36 jugadores, 2 entrenadores, 24 armas, 14 pasivas, 24 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.
  - Dependencias producción: 6.
  - LOC: backend ~2.300, frontend ~1.150, CSS ~950, juego ~14.800, tests ~5.050.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
