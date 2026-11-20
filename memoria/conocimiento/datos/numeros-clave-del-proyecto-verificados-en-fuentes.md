---
tipo: "dato"
titulo: "Números clave del proyecto verificados en fuentes"
temas: ["memoria-tfg", "metricas", "sprints", "pbis", "pruebas", "tareas", "trazabilidad"]
claves: ["19 PBIs", "32 tareas", "29 PBIs", "50 tareas", "276 pruebas", "322 pruebas", "48 PBIs", "82 tareas", "problema: Necesidad de referencia rápida de cifras principales para contraste con verificar.py", "solucion: Lista de cifras con su ubicación exacta en fuentes para depuración del script"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md, repo:saas/docs/log.md, repo:saas/docs/arquitectura.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[memoria-tfg]] · [[metricas]] · [[sprints]]

|
  - Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32) → doc §2.3, gestión backlog S1
  - Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82) → doc §2.3, gestión backlog S2
  - Total: 48 PBIs, 82 tareas → doc §2.3
  - Pruebas cierre S2: 276 → doc §14 métricas
  - Pruebas tras Fase 7: 322 → doc §14 métricas
  - Entidades ER: 4 (users, session, juego_perfiles, juego_records) → doc §6.2
  - Releases: 5 (hito-1, hito-2, hito-3, hito-4, sprint-1) → gestión cierres
  - PRs fusionados: >50 → doc §14 métricas
  - Endpoints API: 23 → doc §14 métricas
  - Migraciones: 5 → doc §14 métricas
  - Jugadores: 36 → doc §9.3 sistemas
  - Armas: 29 → doc §9.3 sistemas
  - Combinaciones: 29 → doc §9.3 sistemas
  - Logros: 29 → doc §9.3 sistemas
fuente: docs/documentacion-tecnica.md §2.3, §14, §9.3; docs/gestion/README.md backlog y trazabilidad
relacionado: Cada cifra de un documento sale de las fuentes, también las pequeñas

## Ampliación (2026-11-20, memoria-procesos)
Cifras oficiales del proyecto para usar en la memoria sin redondear ni inventar. El burndown de la entrega del Sprint 1 cuenta 16 PBIs (P1–P14, P18, P19) porque P15–P17 se integraron después. Las 276 pruebas son al cierre del Sprint 2; 322 tras la Fase 7 posterior.

## Ampliación (2026-11-20, memoria-procesos)
Todos los números clave del proyecto contrastados con las fuentes oficiales del repositorio. Sprint 1: 29/09–27/10/2026, 19 PBIs, 32 tareas, 4 hitos. Sprint 2: 23/10–29/10/2026, 29 PBIs, 50 tareas, 7 fases. Burndown Sprint 1 cuenta 16 PBIs (P1–P14, P18, P19) porque P15–P17 (Hito 4) se completaron después. Pruebas: 140 Sprint 1 + 136 juego hasta Fase 6 = 276; +46 Fase 7 = 322. Migraciones: 001 usuarios, 002 sesiones, 003 juego, 004 identidad, 005 email libre tras baja.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
