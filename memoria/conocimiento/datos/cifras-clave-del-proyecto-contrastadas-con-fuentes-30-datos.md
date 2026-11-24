---
tipo: "dato"
titulo: "Cifras clave del proyecto contrastadas con fuentes (30 datos)"
temas: ["metricas", "trazabilidad", "verificacion", "memoria-procesos", "memoria"]
claves: ["19 PBIs", "32 tareas", "29 PBIs", "50 tareas", "276 pruebas", "322 pruebas", "5 migraciones", "23 endpoints", "36 jugadores", "10 jefes", "29 logros", "10 equipaciones"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md, repo:saas/docs/procesos.md, repo:saas/docs/requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/arquitectura.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-24"
---

Temas: [[metricas]] · [[trazabilidad]] · [[verificacion]]

|
  1. Sprint 1: 19 PBIs P1–P19, 32 tareas T1–T32 → sprint-1.md §Backlog
  2. Sprint 2: 29 PBIs P20–P48, 50 tareas T33–T82 → sprint-2.md §Backlog
  3. Fechas Sprint 1: 29/09–27/10/2026 → sprint-1.md
  4. Fechas Sprint 2: 23/10–29/10/2026 → sprint-2.md
  5. Cambio de alcance P19 (Cloud Run) a mitad del Sprint 1 → decisiones.md D-16
  6. Backlog Sprint 2 registrado en DoneTonic al cerrar el sprint (29/10) → decisiones.md D-19
  7. 276 pruebas automáticas al cierre Sprint 2, 322 tras Fase 7 → procesos.md §Pruebas
  8. 5 migraciones SQL (001–005) → arquitectura.md §Modelo de datos
  9. Arquitectura en capas: API, lógica, datos, integraciones → arquitectura.md §Vista general
  10. Modelo de datos: users, session, juego_perfiles, juego_records → arquitectura.md §Modelo de datos
  11. Seguridad: bcrypt coste 10, cookie httpOnly/secure/sameSite, regeneración sesión → arquitectura.md §Seguridad
  12. OAuth 2.0 con state anti-CSRF, intercambio código en servidor → arquitectura.md §Flujos
  13. Juego: género survivor, cita Vampire Survivors → juego.md §Concepto
  14. 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras → sprint-2.md §Métricas
  15. 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones → sprint-2.md §Métricas
  16. Concurrencia optimista en juego_perfiles.version → arquitectura.md §Servidor del juego
  17. Validación anti-trampas: reloj servidor, límites creíbles → arquitectura.md §Servidor del juego
  18. Despliegue: Cloud Run principal, Render alternativo, WIF, Secret Manager → procesos.md §CI/CD
  19. CI: GitHub Actions con PostgreSQL 17, Docker build, health check → procesos.md §Workflows
  20. GitHub Flow: Sprint 1 rama por tarea → hito-N/integracion; Sprint 2 un PR por fase → CONTRIBUTING.md
  21. DoD: código en PR, CI verde, desplegado, documentación actualizada → procesos.md §DoD
  22. Burndown Sprint 1: 16 PBIs del alcance (P1–P14, P18, P19) → sprint-1.md §Evolución
  23. Burndown real Sprint 2: 29 PBIs en 7 días (23/10–29/10) → sprint-2.md §Evolución
  24. Capturas DoneTonic tomadas 29/10/2026 con dos sprints cerrados → sprint-1.md §Capturas
  25. Prueba técnica RF-13: endpoint POST /api/prueba/dominio, 13 pruebas → requisitos.md §RF-13
  26. Correo real recibido en Gmail (producción) → sprint-1.md §Revisión
  27. Google OAuth publicada en producción para usuarios externos → sprint-1.md §Revisión
  28. 23 endpoints API → sprint-2.md §Métricas
  29. ~2.300 líneas backend, ~14.800 líneas juego, ~5.050 líneas pruebas → sprint-2.md §Métricas
  30. 6 dependencias producción (express, express-session, connect-pg-simple, pg, bcryptjs, nodemailer) → sprint-2.md §Métricas
relacionado: Inventario de capturas de pantalla con trazabilidad a requisitos y fechas, Inventario de capturas DoneTonic requeridas y disponibles

> Ver bitácora reciente (2026-11-23 04:09) donde se listan 30 comprobaciones con sección de la fuente.
> — `repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md, repo:saas/docs/procesos.md, repo:saas/docs/requisitos.md` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
Cada cifra del texto sale de las fuentes, copiada tal cual. El test comprueba números >20; el revisor comprueba los pequeños. Ojo con los que se parecen: 19 PBIs en Sprint 1, pero burndown de la entrega cuenta 16 (P1–P14, P18, P19).

Relacionado: [[cifras-clave-del-proyecto-contrastadas-con-fuentes-38-datos]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-31-datos]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-para-comp]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-35-datos]]

## Ampliación (2026-11-24, memoria-procesos)
Todas las cifras del proyecto (PBIs, tareas, pruebas, endpoints, migraciones, líneas de código, dependencias, contenido del juego) han sido contrastadas con las fuentes del repositorio y coinciden exactamente. No se inventa ningún número.

## Ampliación (2026-11-24, memoria-procesos)
|
  - Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32). Burndown de entrega: 16 PBIs (P1–P14, P18, P19).
  - Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82).
  - Total: 48 PBIs, 82 tareas.
  - Pruebas: 276 al cierre Sprint 2, 322 tras Fase 7.
  - API: 23 endpoints.
  - Migraciones: 5.
  - Código backend: ~2.300 líneas; juego: ~14.800 líneas; pruebas: ~5.050 líneas.
  - Contenido juego: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
