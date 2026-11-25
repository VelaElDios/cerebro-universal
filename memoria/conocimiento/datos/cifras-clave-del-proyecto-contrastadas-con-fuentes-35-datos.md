---
tipo: "dato"
titulo: "Cifras clave del proyecto contrastadas con fuentes (35 datos)"
temas: ["datos", "memoria", "verificacion", "metricas", "sprints", "trazabilidad"]
claves: ["19 PBIs", "32 tareas", "29 PBIs", "50 tareas", "276 pruebas", "322 pruebas", "23 endpoints", "5 migraciones", "36 jugadores", "29 armas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md, repo:saas/docs/sprint-2.md §Métricas", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md, repo:saas/docs/log.md"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[datos]] · [[memoria]] · [[verificacion]]

Lista verificada de 35 cifras (ver COMPROBACIONES en el veredicto). Cada cifra sale de las fuentes citadas. Números pequeños también verificados (ej. 16 PBIs en burndown entrega = P1–P14, P18, P19). Regla: antes de escribir cualquier cifra, buscarla en las fuentes y copiarla tal cual.

> 19 PBIs (P1–P19) y 32 tareas (T1–T32)" / "29 PBIs (P20–P48) y 50 tareas (T33–T82)" / "Total 276 pruebas" / "322 pruebas" / "23 endpoints" / "5 migraciones" / "36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones
> — `repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md, repo:saas/docs/sprint-2.md §Métricas` (cita sin comprobar)

## Ampliación (2026-11-24, memoria-procesos)
|
  - Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32) → sprint-1.md §Backlog
  - Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82) → sprint-2.md §Backlog
  - Total tareas: 82 → suma de ambos
  - Pruebas al cierre Sprint 2: 276 (140 S1 + 136 juego) → procesos.md §Pruebas por fichero
  - Pruebas tras Fase 7: 322 (+46) → log.md 2026-11-03, sprint-2.md §Métricas
  - Endpoints API: 23 → arquitectura.md §API tabla, sprint-2.md §Métricas
  - Migraciones SQL: 5 (001–005) → arquitectura.md §Backend módulos, sprint-2.md §Métricas
  - Código backend: ~2.300 líneas, frontend: ~1.150, CSS: ~950, juego: ~14.800, pruebas: ~5.050 → sprint-2.md §Métricas
  - Dependencias producción: 6 → sprint-2.md §Métricas
  - Contenido juego: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones (24+5), 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones → juego.md §Sistemas tabla, sprint-2.md §Métricas
  - Capturas DoneTonic: 29/10/2026 con dos sprints cerrados → sprint-1.md §Capturas, sprint-2.md §Capturas
  - Burndown entrega Sprint 1: 16 PBIs (P1–P14, P18, P19) → sprint-1.md §Evolución tabla
  - Backlog Sprint 2 registrado al cierre (29/10) → sprint-2.md §Evolución, decisiones.md D-19
  - Fase 7 PR #58 02/11/2026, arreglos PR #59 03/11/2026 → log.md
  - Hito 4 PRs #37–#41 23/10/2026 → sprint-1.md §Hito 4
  - PBI P19 (Cloud Run) añadido a mitad de Sprint 1 → sprint-1.md §Cambio alcance, decisiones.md D-16
  - OAuth 2.0 RFC 6749 citado en flujo Google → arquitectura.md §Flujos, bibliografia-extra.md
  - bcrypt citado en seguridad contraseñas → arquitectura.md §Seguridad tabla, bibliografia-extra.md
  - Vampire Survivors género survivor → juego.md §Concepto, bibliografia-extra.md
  - Resumen ≥150 palabras, Abstract ≥120 palabras → elements/preambulo.tex (comprobado visualmente)
  - 35 figuras, 29 tablas, 18444 palabras → verificar.py output
  - Trazabilidad completa P1–P48, T1–T82 en a4-trazabilidad.tex → chapters/a4-trazabilidad.tex tabla
  - Anexo desarrollo dos sprints mismo esquema → chapters/a1-desarrollo.tex estructura

Relacionado: [[cifras-clave-del-proyecto-contrastadas-con-fuentes-31-datos]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-30-datos]] · [[cifras-clave-del-proyecto-contrastadas-con-fuentes-30-datos]] · [[numeros-clave-del-proyecto-contrastados-con-fuentes]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
