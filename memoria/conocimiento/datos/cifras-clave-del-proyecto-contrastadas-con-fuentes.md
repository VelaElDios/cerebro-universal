---
tipo: "dato"
titulo: "Cifras clave del proyecto contrastadas con fuentes"
temas: ["memoria", "métricas", "trazabilidad", "metricas", "verificacion"]
claves: ["19 PBIs", "29 PBIs", "82 tareas", "276 pruebas", "322 pruebas", "5 migraciones", "23 endpoints"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md, repo:saas/docs/arquitectura.md"]
confianza: "propuesto"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[memoria]] · [[métricas]] · [[trazabilidad]]

19 PBIs S1 (sprint-1.md), 29 PBIs S2 (sprint-2.md), 32+50=82 tareas, 276 pruebas en main al cierre S2 (procesos.md), 322 tras Fase 7 (log.md), 5 migraciones (arquitectura.md), 23 endpoints (requisitos.md), ~14.8k líneas juego (sprint-2.md), 36 jugadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 rivales, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones (juego.md, sprint-2.md).

> Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32). Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82). Total: 48 PBIs, 82 tareas. Pruebas: 276 al cierre Sprint 2, 322 tras Fase 7."
problema: Números que se parecen pero son distintos (19 PBIs S1 vs 16 en burndown de entrega; 276 vs 322 pruebas).
solucion: Usar siempre la cifra exacta de la fuente y citarla: "19 PBIs en el backlog del Sprint 1 (sprint-1.md), pero el burndown de la entrega cuenta 16 (P1–P14, P18, P19) porque P15–P17 son del Hito 4 completado después".
> — `repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md` (cita sin comprobar)

## Ampliación (2026-11-22, memoria-procesos)
| Cifra | Valor | Fuente |
|---|---|---|
| PBIs Sprint 1 | 19 (P1–P19) | sprint-1.md §Backlog |
| PBIs Sprint 2 | 29 (P20–P48) | sprint-2.md §Backlog |
| Tareas Sprint 1 | 32 (T1–T32) | sprint-1.md §Trazabilidad |
| Tareas Sprint 2 | 50 (T33–T82) | sprint-2.md §Trazabilidad |
| Total tareas | 82 | suma |
| Pruebas en main (cierre S2) | 276 | procesos.md §Pruebas por fichero |
| Pruebas tras Fase 7 | 322 | log.md 2026-11-03 |
| Migraciones SQL | 5 (001–005) | arquitectura.md §Modelo de datos |
| Endpoints API | 23 | arquitectura.md §API |
| Líneas backend | ~2.300 | sprint-2.md §Métricas |
| Líneas juego | ~14.800 | sprint-2.md §Métricas |
| Jugadores | 36 | juego.md §Sistemas |
| Armas/habilidades | 29 | juego.md §Sistemas (24 Fase 3 + 5 Fase 7) |
| Pasivas | 16 | juego.md §Sistemas |
| Combinaciones | 29 | juego.md §Sistemas (24 Fase 3 + 5 Fase 7) |
| Ultras | 6 | juego.md §Sistemas |
| Equipos rivales | 16 | juego.md §Sistemas |
| Jefes | 10 | juego.md §Sistemas |
| Ambientes | 5 | juego.md §Sistemas |
| Selecciones | 26 | juego.md §Sistemas |
| Logros | 29 | juego.md §Logros |
| Equipaciones | 10 | juego.md §Logros |
| URL Cloud Run | https://la-grada-colchonera-1081564062572.europe-southwest1.run.app | README.md |
| Repo GitHub | https://github.com/VelaElDios/la-grada-colchonera-saas | README.md |
| Fechas Sprint 1 | 29/09–27/10/2026 | sprint-1.md |
| Fechas Sprint 2 | 23/10–29/10/2026 | sprint-2.md |
| P19 cambio alcance | Cloud Run (créditos educación) | decisiones.md D-16 |
| Backlog S2 registrado al cierre | 29/10/2026 | decisiones.md D-19 |

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
