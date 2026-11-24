---
tipo: "dato"
titulo: "Cifras clave del proyecto contrastadas con fuentes (31 datos)"
temas: ["fuentes", "memoria", "verificacion", "metricas", "trazabilidad", "proyecto", "sprints"]
claves: ["19 PBIs", "29 PBIs", "82 tareas", "276 pruebas", "322 pruebas", "23 endpoints", "5 migraciones", "6 dependencias", "36 jugadores", "2 entrenadores", "29 armas", "16 pasivas", "29 combinaciones", "6 ultras", "16 equipos", "10 jefes", "5 ambientes", "26 selecciones", "29 logros", "10 equipaciones"]
proyectos: ["memoria-procesos"]
fuentes: ["docs/sprint-1.md, docs/sprint-2.md, docs/juego.md, docs/arquitectura.md, docs/procesos.md, docs/log.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/arquitectura.md, repo:saas/docs/juego.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/arquitectura.md", "sprint-1.md, sprint-2.md, arquitectura.md, decisiones.md, log.md, procesos.md, juego.md, requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/procesos.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-24"
---

Temas: [[fuentes]] · [[memoria]] · [[verificacion]]

|
  31 cifras/hechos verificados contra fuentes:
  1. 19 PBIs Sprint 1 (P1–P19) → sprint-1.md tabla backlog
  2. 29 PBIs Sprint 2 (P20–P48) → sprint-2.md tabla backlog
  3. 32 tareas Sprint 1 (T1–T32) → sprint-1.md trazabilidad
  4. 50 tareas Sprint 2 (T33–T82) → sprint-2.md trazabilidad
  5. 276 pruebas automáticas al cierre Sprint 2 → sprint-2.md métricas
  6. 322 pruebas tras Fase 7 → log.md 2026-11-03
  7. 23 endpoints API → arquitectura.md §API tabla
  8. 5 migraciones SQL (001–005) → arquitectura.md §db/migrations
  9. 6 dependencias producción → sprint-2.md métricas
  10. 36 jugadores (4P, 9D, 13M, 10F) → juego.md sistemas
  11. 2 entrenadores (Simeone, Aragonés) → juego.md sistemas
  12. 29 armas (24 Fase 3 + 5 Fase 7) → juego.md sistemas
  13. 16 pasivas (14 Fase 6 + 2 Fase 7) → juego.md sistemas
  14. 29 combinaciones (24 Fase 3 + 5 Fase 7) → juego.md sistemas
  15. 6 ultras → juego.md sistemas
  16. 16 equipos rivales → juego.md sistemas
  17. 10 jefes → juego.md sistemas
  18. 5 ambientes por finales → juego.md sistemas
  19. 26 selecciones nacionales → arquitectura.md renderizado
  20. 29 logros → juego.md tabla logros
  21. 10 equipaciones desbloqueables → juego.md tabla logros
  22. Burndown S1 entrega: [15,9,5,1,2,0] → sprint-1.md evolución
  23. Burndown real S2: [28,11,11,2,2,2,0] → sprint-2.md evolución
  24. 8 secretos Secret Manager → procesos.md despliegue
  25. PostgreSQL 17 en CI → procesos.md CI
  26. Node 22 Alpine → procesos.md Docker
  27. Cloud Run region europe-southwest1 → procesos.md despliegue
  28. Neon Frankfurt → procesos.md BD
  29. Fechas PRs Sprint 2 → sprint-2.md tabla PRs
  30. Cambio alcance P19 (Cloud Run) → decisiones.md D-16
  31. Backlog S2 registrado 29/10 → decisiones.md D-19

> 19 PBIs S1 → sprint-1.md backlog; 29 PBIs S2 → sprint-2.md backlog; 32+50=82 tareas → sprint-1.md y sprint-2.md trazabilidad; 276 pruebas cierre S2 → sprint-2.md métricas; 322 tras Fase 7 → log.md 2026-11-03; 23 endpoints → arquitectura.md API; 5 migraciones → arquitectura.md db/migrations; 6 dependencias → sprint-2.md métricas; 36 jugadores → juego.md sistemas; 2 entrenadores → juego.md sistemas; 29 armas → juego.md sistemas (24+5); 16 pasivas → juego.md sistemas (14+2); 29 combinaciones → juego.md sistemas (24+5); 6 ultras → juego.md sistemas; 16 equipos → juego.md sistemas; 10 jefes → juego.md sistemas; 5 ambientes → juego.md sistemas; 26 selecciones → arquitectura.md renderizado; 29 logros → juego.md logros; 10 equipaciones → juego.md logros.
> — `docs/sprint-1.md, docs/sprint-2.md, docs/juego.md, docs/arquitectura.md, docs/procesos.md, docs/log.md` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
Lista de 31 cifras/hechos verificados contra las fuentes del repositorio en el paso de revisión anterior (2026-11-23 12:54). Cada cifra tiene su origen en los documentos de `docs/` (sprint-1.md, sprint-2.md, requisitos.md, arquitectura.md, juego.md). Ejemplos:
- 19 PBIs Sprint 1 → sprint-1.md tabla backlog
- 29 PBIs Sprint 2 → sprint-2.md tabla backlog
- 32+50=82 tareas → sprint-1.md (32) + sprint-2.md (50)
- 276 pruebas al cierre Sprint 2 → sprint-2.md métricas
- 322 pruebas tras Fase 7 → sprint-2.md trabajo posterior
- 23 endpoints → arquitectura.md tabla API
- 5 migraciones → arquitectura.md lista migraciones
- 6 dependencias → sprint-2.md métricas
- 36 jugadores, 2 entrenadores → juego.md sistemas
- 29 armas, 16 pasivas, 29 combinaciones, 6 ultras → juego.md sistemas + log.md Fase 7
- 16 equipos, 10 jefes → juego.md sistemas
- 5 ambientes → juego.md sistemas
- 26 selecciones → arquitectura.md dibujo muñecos
- 29 logros, 10 equipaciones → juego.md logros
- Burndown S1 [15,9,5,1,2,0] → sprint-1.md evolución
- Burndown real S2 [28,11,11,2,2,2,0] → sprint-2.md evolución real
- 8 secretos Secret Manager → procesos.md configuración
- PostgreSQL 17 en CI → procesos.md CI
- Node 22 Alpine → procesos.md Docker
- Región Cloud Run europe-southwest1 → procesos.md Cloud Run
- Neon Frankfurt → procesos.md base de datos
- Fechas PRs S2 → sprint-2.md tabla PRs
- Cambio alcance P19 → decisiones.md D-16
- Backlog S2 registrado 29/10 → decisiones.md D-19

## Ampliación (2026-11-23, memoria-procesos)
|
  Estas 31 cifras/hechos se han verificado contra las fuentes en pasos anteriores de revisión y aparecen en el texto de la memoria. Cada número > 20 está en las fuentes; los pequeños los comprobó el revisor. Ejemplos de contraste:
  - 19 PBIs Sprint 1 → sprint-1.md tabla backlog
  - 29 PBIs Sprint 2 → sprint-2.md tabla backlog
  - 32 tareas S1 + 50 tareas S2 = 82 → sprint-1.md y sprint-2.md
  - 276 pruebas al cierre S2 → sprint-2.md métricas
  - 322 pruebas tras Fase 7 → log.md 2026-11-03
  - 23 endpoints → arquitectura.md tabla API
  - 5 migraciones → arquitectura.md lista migraciones
  - 6 dependencias producción → sprint-2.md métricas
  - 36 jugadores, 2 entrenadores → juego.md sistemas
  - 29 armas, 16 pasivas, 29 combinaciones, 6 ultras → juego.md sistemas (incluye Fase 7)
  - 16 equipos, 10 jefes, 5 ambientes, 26 selecciones → juego.md sistemas
  - 29 logros, 10 equipaciones → juego.md logros
  - Burndown S1 [15,9,5,1,2,0] → sprint-1.md tabla evolución
  - Burndown real S2 [28,11,11,2,2,2,0] → sprint-2.md tabla evolución
  - 8 secretos Secret Manager → procesos.md configuración servicios externos
  - PostgreSQL 17 en CI → procesos.md workflow CI
  - Node 22 Alpine → procesos.md imagen Docker
  - Región Cloud Run europe-southwest1 → procesos.md despliegue
  - Neon Frankfurt → procesos.md base de datos
  - Fechas PRs S2 → sprint-2.md tabla PRs fusionados
  - Cambio alcance P19 → decisiones.md D-16
  - Backlog S2 registrado 29/10 → decisiones.md D-19, sprint-2.md retrospectiva
relacionado: Inventario de diagramas obligatorios y su estado actualizado, Trazabilidad completa requisito-PBI-tarea-PR en anexo A4

## Ampliación (2026-11-23, memoria-procesos)
31 cifras/hechos verificados contra las fuentes del repositorio en esta revisión (ver COMPROBACIONES). Cada uno mapea a una sección concreta de los documentos de `docs/`.
relacionado: Inventario de diagramas obligatorios y su estado actualizado, Cómo corregir diagramas de secuencia pgf-umlsd para pasar revisar_maquetacion.py

Relacionado: [[cifras-clave-del-proyecto-contrastadas-con-fuentes-38-datos]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-30-datos]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-para-comp]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-35-datos]]

## Ampliación (2026-11-24, memoria-procesos)
|
  - Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32). Burndown de entrega: 16 PBIs (P1–P14, P18, P19).
  - Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82).
  - Total: 48 PBIs, 82 tareas.
  - Pruebas: 276 al cierre Sprint 2, 322 tras Fase 7.
  - Endpoints API: 23.
  - Migraciones SQL: 5.
  - Líneas backend (src/): ~2.300.
  - Líneas frontend (ui.js, api.js, ui/): ~1.150.
  - Líneas CSS: ~950.
  - Líneas juego (public/js/game/): ~14.800.
  - Líneas pruebas: ~5.050.
  - Dependencias producción: 6.
  - Contenido juego: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.
relacionado: Métricas del proyecto (Tabla 5.3), Trazabilidad completa (Anexo B)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
