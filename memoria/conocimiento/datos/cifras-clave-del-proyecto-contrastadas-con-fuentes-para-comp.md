---
tipo: "dato"
titulo: "Cifras clave del proyecto contrastadas con fuentes (fusionada)"
temas: ["datos", "fuentes", "grada-colchonera", "juego", "memoria", "metricas", "métricas", "proyecto", "pruebas", "saas", "scrum", "sprints", "trazabilidad", "verificacion"]
claves: ["19 PBIs", "29 PBIs", "82 tareas", "276 pruebas", "322 pruebas", "5 migraciones", "23 endpoints", "36 jugadores", "29 logros"]
proyectos: ["memoria-procesos"]
fuentes: ["sprint-1.md, sprint-2.md, procesos.md, log.md, juego.md, arquitectura.md", "sprint-1.md, sprint-2.md, log.md, requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md, repo:saas/docs/arquitectura.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/log.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md, repo:saas/docs/juego.md, repo:saas/docs/procesos.md, repo:saas/@arbol", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/arquitectura.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[datos]] · [[fuentes]] · [[grada-colchonera]] · [[juego]] · [[memoria]] · [[metricas]] · [[métricas]] · [[proyecto]] · [[pruebas]] · [[saas]] · [[scrum]] · [[sprints]] · [[trazabilidad]] · [[verificacion]]

# Cifras clave del proyecto contrastadas con fuentes
Temas: [[fuentes]] · [[métricas]] · [[verificación]] · [[memoria]] · [[trazabilidad]]

## Tabla maestra de cifras

| Cifra | Valor | Fuente | Sección memoria / Nota |
|---|---|---|---|
| PBIs Sprint 1 | 19 (P1–P19) | sprint-1.md §Backlog / tabla backlog | 01-introduccion, 03-propuesta, a1-desarrollo |
| PBIs alcance entrega Sprint 1 (burndown) | 16 (P1–P14, P18, P19) | sprint-1.md evolución | a1-desarrollo (burndown) |
| PBIs Sprint 2 | 29 (P20–P48) | sprint-2.md §Backlog / tabla backlog | 01-introduccion, 04b-juego, a1-desarrollo |
| Tareas Sprint 1 | 32 (T1–T32) | sprint-1.md §Trazabilidad / trazabilidad | a1-desarrollo, a4-trazabilidad |
| Tareas Sprint 2 | 50 (T33–T82) | sprint-2.md §Trazabilidad / trazabilidad | a1-desarrollo, a4-trazabilidad |
| **Total tareas** | **82** | suma anterior | a4-trazabilidad (82 filas) |
| Pruebas en main (cierre Sprint 2) | 276 | procesos.md §Pruebas por fichero / tabla pruebas | 05-evaluacion, a1-desarrollo |
| Pruebas tras Fase 7 | 322 | log.md 2026-11-03 | 05-evaluacion (nota) |
| Migraciones SQL | 5 (001–005) | arquitectura.md §Modelo de datos / db/migrations | 04-descripcion, 05-evaluacion |
| Endpoints API | 23 | arquitectura.md §API / tabla API | 04-descripcion, 05-evaluacion |
| Líneas backend | ~2.300 | sprint-2.md §Métricas | 05-evaluacion |
| Líneas interfaz (frontend) | ~1.150 | sprint-2.md §Métricas | — |
| Líneas CSS | ~950 | sprint-2.md §Métricas | — |
| Líneas juego | ~14.800 | sprint-2.md §Métricas | 04b-juego, 05-evaluacion |
| Líneas pruebas | ~5.050 | sprint-2.md §Métricas | — |
| Jugadores | 36 | juego.md §Sistemas / sistemas | 04b-juego, 05-evaluacion |
| Entrenadores | 2 | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Armas/habilidades | 29 (24 Fase 3 + 5 Fase 7) | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Pasivas | 16 (14 + 2 Fase 7) | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Combinaciones | 29 (24 Fase 3 + 5 Fase 7) | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Ultras | 6 | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Equipos rivales | 16 | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Jefes | 10 | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Ambientes | 5 | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Selecciones | 26 | juego.md §Sistemas | 04b-juego, 05-evaluacion |
| Logros | 29 | juego.md §Logros | 04b-juego, 05-evaluacion |
| Equipaciones | 10 | juego.md §Logros | 04b-juego, 05-evaluacion |
| URL producción (Cloud Run) | https://la-grada-colchonera-1081564062572.europe-southwest1.run.app | sprint-1.md, README.md | a2-material, 01-introduccion |
| Repositorio GitHub | https://github.com/VelaElDios/la-grada-colchonera-saas | sprint-1.md, README.md | a2-material, 01-introduccion |
| Fechas Sprint 1 | 29/09–27/10/2026 | sprint-1.md | 01-introduccion, 03-propuesta |
| Fechas Sprint 2 | 23/10–29/10/2026 | sprint-2.md | 01-introduccion, 04b-juego |
| Cambio alcance P19 | Cloud Run (créditos educación) | decisiones.md D-16 | 01-introduccion, 03-propuesta, a1-desarrollo |
| Backlog S2 registrado al cierre | 29/10/2026 | decisiones.md D-19 | a1-desarrollo (retrospectiva S2) |
| Dependencias producción | 6 (express, express-session, connect-pg-simple, pg, bcryptjs, nodemailer) | arquitectura.md / package.json | 04-descripcion, 05-evaluacion |
| Despliegue: secretos | 8 en Secret Manager | — | 05-evaluacion |
| Despliegue: BD CI | PostgreSQL 17 | — | 05-evaluacion |
| Despliegue: runtime | Node 22 Alpine | — | 05-evaluacion |
| Despliegue: región | europe-southwest1 (Madrid) | — | 05-evaluacion |
| Despliegue: BD gestionada | Neon (Frankfurt) | — | 05-evaluacion |
| DoneTonic | Espacio TFG, equipo Colchoneros | — | a1-desarrollo |
| DoneTonic HUs Sprint 2 | 29 | capturas 29/10/2026 | a1-desarrollo |
| Capturas anexos | app/ 13, hito4/ 11, juego/ 16, donetonic/ 8, produccion/ 3, prueba-tecnica/ 2, fase7/ 12 | — | a2-material |
| Resumen (memoria) | 198 palabras (≥150) | — | 01-introduccion |
| Abstract (memoria) | 156 palabras (≥120) | — | 01-introduccion |
| Declaración autoría | Sí | — | 01-introduccion |
| Trazabilidad anexo | Completa P1–P48 / T1–T82 (82 filas) | a4-trazabilidad.tex | a4-trazabilidad |

> **Resumen narrativo**: 19 PBIs en el backlog del Sprint 1 (P1–P19), pero el burndown de la entrega cuenta 16 (P1–P14, P18, P19) porque P15–P17 son del Hito 4 completado después. Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82). Total: 48 PBIs, 82 tareas, >50 PRs fusionados. Pruebas: 276 al cierre Sprint 2 (140 Sprint 1 + 136 juego Fases 1–6), 322 tras Fase 7 (+46). API: 23 endpoints, 5 migraciones. Código: ~2.300 backend, ~1.150 interfaz, ~950 CSS, ~14.800 juego, ~5.050 pruebas. Juego: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.

---

## Ampliaciones cronológicas

### 2026-11-22 (memoria-procesos) — Tabla de cifras con fuentes granulares
(Incorporada en la tabla maestra arriba; se conservan las referencias de sección: §Backlog, §Trazabilidad, §Pruebas por fichero, §Modelo de datos, §API, §Métricas, §Sistemas, §Logros.)

### 2026-11-23 (memoria-procesos) — Detalle de sprints y evolución
- **Sprint 1**: 29/09–27/10/2026, 19 PBIs, 32 tareas, 4 hitos. Burndown entrega: 16 PBIs (P1–P14, P18, P19).
- **Sprint 2**: 23/10–29/10/2026, 29 PBIs, 50 tareas, 7 etiquetas de fase. Backlog registrado en DoneTonic al cierre (29/10) → gráficas en recta.
- **Evolución real Sprint 2 por fechas de PR**: 23/10 (1), 24/10 (17), 26/10 (9), 29/10 (2) = 29 PBIs.
- **Pruebas**: 140 Sprint 1 + 136 juego hasta Fase 6 = 276; +46 Fase 7 = 322.
- **Migraciones detalle**: 001 usuarios, 002 sesiones, 003 juego, 004 identidad, 005 email libre tras baja.
- **Cambio enfoque**: red social → juego (3 motivos: originalidad, problemas técnicos ricos, reutiliza base SaaS).
- **Arquitectura**: capas API → lógica → datos/integraciones, inyección de dependencias.
- **Seguridad**: bcrypt, cookie httpOnly/secure/sameSite, regeneración de sesión, permisos en servidor.
- **Concurrencia optimista**: campo `version` en `juego_perfiles`.
- **Simulación determinista**: paso fijo 1/60 s con semilla.
- **Gráficos/sonido**: generados por código (sin assets externos).
- **Muñecos chibi**: 32×32 sin piernas (Fase 7, decisión D-21).
- **Tope de bajas**: `bajasPosibles` en `config.js` (decisión D-22).

### 2026-11-23 (memoria-procesos) — Lista de verificación
- Lista de 25+ cifras y hechos verificados contra las fuentes del repositorio, listados en COMPROBACIONES.
- Todas las cifras mayores de 20 que aparecen en la memoria están en las fuentes. Las menores (19, 29, 32, 50, 23, 5, 36, 29, 16, 6, 16, 10, 5, 26) las comprueba el revisor.
- Ojo con los que se parecen: 19 PBIs en Sprint 1 pero burndown de entrega cuenta 16 (P1–P14, P18, P19); 32 + 50 = 82 tareas totales; 276 pruebas al cierre Sprint 2, 322 tras Fase 7.

### 2026-11-23 (memoria-procesos) — Resumen final para memoria
- Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32), 4 hitos. Burndown entrega: 16 PBIs (P1–P14, P18, P19).
- Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82), 7 etiquetas de fase. 29 historias de usuario con criterios.
- Total: 48 PBIs, 82 tareas, >50 PRs fusionados.
- Pruebas: 276 al cierre Sprint 2, 322 tras Fase 7 (140 S1 + 136 juego F1–F6 + 46 F7).
- API: 23 endpoints, 5 migraciones.
- Código: ~2.300 líneas backend, ~1.150 frontend, ~950 CSS, ~14.800 juego, ~5.050 pruebas.
- Dependencias producción: 6 (express, express-session, connect-pg-simple, pg, bcryptjs, nodemailer).
- Juego: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones (24 F3 + 5 F7), 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones.
- Despliegue: 8 secretos Secret Manager, PostgreSQL 17 en CI, Node 22 Alpine, región europe-southwest1 (Madrid), Neon (Frankfurt).
- DoneTonic: 29 HUs Sprint 2, capturas 29/10/2026, gráficas Sprint 2 en recta (backlog registrado al cerrar).
- Memoria: Resumen ≥150 palabras (198), Abstract ≥120 palabras (156), declaración autoría, trazabilidad completa P1–P48/T1–T82 en a4-trazabilidad.tex.

---

## Notas de verificación (problema/solución)
**Problema**: Números que se parecen pero son distintos (19 PBIs S1 vs 16 en burndown de entrega; 276 vs 322 pruebas).  
**Solución**: Usar siempre la cifra exacta de la fuente y citarla: *"19 PBIs en el backlog del Sprint 1 (sprint-1.md), pero el burndown de la entrega cuenta 16 (P1–P14, P18, P19) porque P15–P17 son del Hito 4 completado después"*.

> — `repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/log.md, repo:saas/docs/juego.md, repo:saas/docs/arquitectura.md, repo:saas/docs/decisiones.md, repo:saas/README.md` (citas sin comprobar in situ)

---

## Relacionado
- [[Inventario de diagramas obligatorios y su estado]]
- [[Validación final del PDF antes de marcar terminado]]
- [[proyectos/memoria-procesos/estado|memoria-procesos (origen)]]

> 19 PBIs en el Sprint 1, pero el burndown de la entrega cuenta 16 (P1–P14, P18 y P19); 32 + 50 = 82 tareas; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7.
> — `sprint-1.md, sprint-2.md, procesos.md, log.md, juego.md, arquitectura.md` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: Fuente de "Endpoints API": NOTA A cita `arquitectura.md tabla API`; NOTA B en el párrafo resumen cita `requisitos.md` pero en su tabla cita `arquitectura.md §API`. Se unifica a `arquitectura.md §API / tabla API` por ser la referencia más consistente y detallada.

Fusionada con: Cifras clave del proyecto contrastadas con fuentes

Relacionado: [[cifras-clave-del-proyecto-contrastadas-con-fuentes-38-datos]] · [[cifras-clave-del-proyecto-la-grada-colchonera-contrastadas]] · [[cifras-clave-del-proyecto-la-grada-colchonera-sprints-1-y-2]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
