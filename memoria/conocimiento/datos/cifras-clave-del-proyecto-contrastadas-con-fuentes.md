---
tipo: "dato"
titulo: "Cifras clave del proyecto verificadas en fuentes"
temas: ["datos", "fechas", "memoria-procesos", "metricas", "pbis", "pruebas", "sprints", "tareas", "verificacion"]
claves: ["19 PBIs", "32 tareas", "29 PBIs", "50 tareas", "276 pruebas", "322 pruebas", "82 tareas", "48 PBIs"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md", "repo:saas/docs/documentacion-tecnica.md, repo:saas/docs/gestion/README.md", "repo:saas/docs/documentacion-tecnica.md y repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-22"
---

Temas: [[datos]] · [[fechas]] · [[memoria-procesos]] · [[metricas]] · [[pbis]] · [[pruebas]] · [[sprints]] · [[tareas]] · [[verificacion]]

# Cifras clave del proyecto verificadas en fuentes

**Temas:** [[metricas]] · [[pbis]] · [[pruebas]] · [[sprints]] · [[tareas]]

---

## Resumen ejecutivo

| Concepto | Valor |
|----------|-------|
| **Sprint 1** | 19 PBIs (P1–P19), 32 tareas (T1–T32), 4 hitos, fechas 29/09–27/10/2026 |
| **Sprint 2** | 29 PBIs (P20–P48), 50 tareas (T33–T82), 7 etiquetas de fase, fechas 23/10–29/10/2026 |
| **Total proyecto** | 48 PBIs, 82 tareas, >50 PRs fusionados |
| **Pruebas automáticas** | 276 (main al cierre Sprint 2), 322 (tras Fase 7) |
| **Burndown Sprint 1 (entrega)** | 16 PBIs (P1–P14, P18, P19) |
| **Burndown real Sprint 2** | 23/10 (1), 24/10 (17), 26/10 (9), 29/10 (2) |
| **Releases** | hito-1, hito-2, hito-3, hito-4, sprint-1 |
| **Endpoints API** | 23 |
| **Migraciones SQL** | 5 (001–005) |
| **Dependencias producción** | 6 directas |
| **Líneas de código** | Backend ~2.300, Frontend ~1.150, CSS ~950, Juego ~14.800, Tests ~5.050 |
| **Contenido jugable** | 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones, 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones |

---

## Sprint 1 (29/09–27/10/2026)

- **19 PBIs** (P1–P19), todos prioridad **MUST**
- **32 tareas** (T1–T32)
- **4 hitos** (Hito 1–4)
- **Burndown alcance entrega:** 16 PBIs (P1–P14, P18, P19) — *P15–P17 pertenecen al Hito 4, completado después de la primera entrega*
- **Cambio de alcance:** +P19 (Cloud Run) a mitad de sprint
- **Releases:** hito-1, hito-2, hito-3, hito-4, sprint-1
- **Cierres de hito (PRs):** #9, #17, #24, #29, #32

---

## Sprint 2 (23/10–29/10/2026)

- **29 PBIs** (P20–P48), todos prioridad **MUST**
- **50 tareas** (T33–T82)
- **7 etiquetas de fase:** Base, Fase 2, Fase 3, Fase 4, Fase 5, Fase 6, Calidad
- **Backlog registrado en DoneTonic** al cerrar (29/10) → gráficas en recta
- **Evolución real por PRs (burndown):**
  - 23/10: 1 PBI
  - 24/10: 17 PBIs
  - 26/10: 9 PBIs
  - 29/10: 2 PBIs
- **PRs principales:** #36, #44–#54, #51, #55, #56

---

## Totales del proyecto

- **48 PBIs** (P1–P48)
- **82 tareas** (T1–T82)
- **>50 PRs fusionados**
- **5 migraciones SQL** (001–005)
- **23 endpoints API**
- **276 pruebas automáticas** en `main` al cierre del Sprint 2 (140 Sprint 1 + 136 juego hasta Fase 6)
- **322 pruebas** tras Fase 7 (+46 pruebas)
- **Líneas de código:**
  - Backend: ~2.300
  - Frontend: ~1.150
  - CSS: ~950
  - Juego: ~14.800
  - Tests: ~5.050
- **6 dependencias directas de producción**
- **Contenido jugable:**
  - 36 jugadores
  - 2 entrenadores
  - 29 armas
  - 16 pasivas
  - 29 combinaciones
  - 6 ultras
  - 16 equipos
  - 10 jefes
  - 5 ambientes
  - 26 selecciones
  - 29 logros
  - 10 equipaciones

---

## Fechas clave

| Fecha | Evento |
|-------|--------|
| 29/09/2026 | Inicio Sprint 1 |
| 12/10/2026 | Primera entrega (Hitos 1–3, P18, P19) |
| 23/10/2026 | Hito 4 en producción + inicio Sprint 2 |
| 27/10/2026 | Fin Sprint 1 |
| 29/10/2026 | Fin Sprint 2 + backlog DoneTonic |

---

## Releases y PRs de referencia

- **Releases:** `hito-1`, `hito-2`, `hito-3`, `hito-4`, `sprint-1`
- **PRs de cierre de hito (Sprint 1):** #9, #17, #24, #29, #32
- **PRs principales (Sprint 2):** #36, #44–#54, #51, #55, #56
- **Total PRs fusionados:** >50

---

## Fuentes (citas sin comprobar)

- `repo:saas/docs/sprint-1.md`
- `repo:saas/docs/sprint-2.md`
- `repo:saas/docs/procesos.md`
- `repo:saas/docs/documentacion-tecnica.md` (§4)
- `repo:saas/docs/gestion/README.md`

---

## Notas relacionadas

- [[cifras-clave-del-proyecto-contrastadas-con-fuentes]]
- [[numeros-clave-del-proyecto-verificados-en-fuentes]]
- [[numeros-clave-del-proyecto-contrastados-con-fuentes]]
- [[metricas-del-proyecto-codigo-pruebas-endpoints-y-contenido-d]]

**Origen:** [[proyectos/memoria-procesos/estado|memoria-procesos]]

> Sprint 1: 19 PBIs (P1–P19) y 32 tareas (T1–T32). Sprint 2: 29 PBIs (P20–P48) y 50 tareas (T33–T82). Pruebas automáticas en main al cerrar Sprint 2: 276 (140 Sprint 1 + 136 juego hasta Fase 6). Tras Fase 7: 322 pruebas.
> — `repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md` (cita sin comprobar)
> Sprint 1: 19 PBIs (P1–P19), 32 tareas (T1–T32). Sprint 2: 29 PBIs (P20–P48), 50 tareas (T33–T82). Total: 48 PBIs, 82 tareas. Pruebas: 276 en main al cierre Sprint 2, 322 tras Fase 7.
> — `repo:saas/docs/documentacion-tecnica.md, repo:saas/docs/gestion/README.md` (cita sin comprobar)

Fusionada con: Cifras clave del proyecto verificadas en fuentes

Relacionado: [[cifras-clave-del-proyecto-la-grada-colchonera-contrastadas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
