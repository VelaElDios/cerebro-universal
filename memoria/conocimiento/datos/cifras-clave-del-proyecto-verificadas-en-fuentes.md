---
tipo: "dato"
titulo: "Cifras clave del proyecto verificadas en fuentes"
temas: ["metricas", "pbis", "sprints", "tareas", "fechas", "pruebas", "datos", "memoria-procesos", "verificacion"]
claves: ["19 PBIs", "32 tareas", "29 PBIs", "50 tareas", "48 PBIs", "82 tareas", "276 pruebas", "322 pruebas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md, repo:saas/docs/gestion/README.md", "repo:saas/docs/documentacion-tecnica.md y repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[metricas]] · [[pbis]] · [[sprints]] · [[tareas]]

Cifras oficiales del proyecto: Sprint 1 = 19 PBIs / 32 tareas (Hitos 1-4). Sprint 2 = 29 PBIs / 50 tareas (6 fases + calidad). Total = 48 PBIs / 82 tareas. Pruebas automáticas = 276 (Sprint 1: 140, Sprint 2 hasta Fase 6: 136); con Fase 7 = 322. El burndown de la entrega del Sprint 1 cuenta 16 PBIs (P1–P14, P18, P19) porque P15-P17 son del Hito 4 que se entregó después.

> Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32). Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82). Total: 48 PBIs, 82 tareas. Pruebas: 276 en main al cierre Sprint 2, 322 tras Fase 7.
> — `repo:saas/docs/documentacion-tecnica.md, repo:saas/docs/gestion/README.md` (cita sin comprobar)

## Ampliación (2026-11-19, memoria-procesos)
|
  Cifras oficiales del proyecto (copiar tal cual, no redondear ni sumar de memoria):
  
  **Sprint 1 (29/09–27/10/2026):**
  - 19 PBIs (P1–P19)
  - 32 tareas (T1–T32)
  - 4 hitos (Hito 1–4)
  - Todos prioridad MUST
  - Burndown alcance entrega: 16 PBIs (P1–P14, P18, P19)
  - Cambio de alcance: +P19 (Cloud Run) a mitad de sprint
  - Releases: hito-1, hito-2, hito-3, hito-4, sprint-1
  - Cierres de hito: PR #9, #17, #24, #29, #32
  
  **Sprint 2 (23/10–29/10/2026):**
  - 29 PBIs (P20–P48)
  - 50 tareas (T33–T82)
  - 7 etiquetas de fase (Base, Fase 2–6, Calidad)
  - Todos MUST
  - Backlog registrado en DoneTonic al cerrar (29/10) → gráficas en recta
  - Evolución real por PRs: 23/10 (1 PBI), 24/10 (17 PBIs), 26/10 (9 PBIs), 29/10 (2 PBIs)
  - PRs principales: #36, #44–#54, #51, #55, #56
  
  **Totales proyecto:**
  - 48 PBIs (P1–P48)
  - 82 tareas (T1–T82)
  - >50 PRs fusionados
  - 5 migraciones SQL (001–005)
  - 23 endpoints API
  - 276 pruebas automáticas (main cierre Sprint 2)
  - 322 pruebas (tras Fase 7)
  - ~2.300 líneas backend, ~1.150 frontend, ~14.800 juego, ~5.050 tests
  - 6 dependencias directas producción
  - Contenido jugable: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones
  
  **Fechas clave:**
  - 29/09/2026: inicio Sprint 1
  - 12/10/2026: primera entrega (Hitos 1–3, P18, P19)
  - 23/10/2026: Hito 4 en producción + inicio Sprint 2
  - 27/10/2026: fin Sprint 1
  - 29/10/2026: fin Sprint 2 + backlog DoneTonic

## Ampliación (2026-11-19, memoria-procesos)
|
  Valores confirmados para usar en la memoria (copiar tal cual):
  - Sprint 1: 19 PBIs, 32 tareas, 4 hitos, fechas 29/09–27/10/2026.
  - Sprint 2: 29 PBIs, 50 tareas, fechas 23/10–29/10/2026.
  - Total PBIs: 48. Total tareas: 82.
  - Pruebas automáticas: 276 (main cierre Sprint 2), 322 (tras Fase 7).
  - Burndown Sprint 1: 16 PBIs en alcance de entrega (P1–P14, P18, P19).
  - Releases: hito-1, hito-2, hito-3, hito-4, sprint-1.
  - Endpoints API: 23. Migraciones SQL: 5.
  - Líneas backend: ~2.300; frontend: ~1.150; CSS: ~950; juego: ~14.800; tests: ~5.050.
  - Contenido jugable: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.

## Ampliación (2026-11-19, memoria-procesos)
Cifras confirmadas en las fuentes del repositorio (documentacion-tecnica.md §4 y gestion/README.md):
- Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32). Fechas: 29/09/2026 – 27/10/2026.
- Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82). Fechas: 23/10/2026 – 29/10/2026.
- Total proyecto: 48 PBIs, 82 tareas.
- Pruebas: 276 en main al cierre Sprint 2; 322 tras Fase 7 (46 pruebas añadidas).
- Burndown Sprint 1 (entrega): 16 PBIs (P1–P14, P18, P19) — P15–P17 son Hito 4, completado después de la primera entrega.
- Releases: hito-1, hito-2, hito-3, hito-4, sprint-1.
- PRs fusionados: más de 50.
- Endpoints API: 23.
- Migraciones SQL: 5.
- Líneas backend: ~2.300; frontend: ~1.150; CSS: ~950; juego: ~14.800; tests: ~5.050.
- Contenido jugable: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.

Relacionado: [[numeros-clave-del-proyecto-verificados-en-fuentes]] · [[numeros-clave-del-proyecto-contrastados-con-fuentes]] · [[metricas-del-proyecto-codigo-pruebas-endpoints-y-contenido-d]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
