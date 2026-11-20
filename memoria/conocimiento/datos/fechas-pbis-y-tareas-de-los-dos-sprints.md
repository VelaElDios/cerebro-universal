---
tipo: "dato"
titulo: "Fechas, PBIs, tareas y estructura detallada de los dos sprints (Sprint 1 y Sprint 2)"
temas: ["donetonic", "fases", "fechas", "grada-colchonera", "hitos", "pbi", "scrum", "sprint", "tarea", "tareas"]
claves: ["Sprint 1", "Sprint 2", "PBIs", "tareas", "fechas", "PBI", "tarea", "hito", "fase"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md", "repo:saas/docs/documentacion-tecnica.md", "repo:saas/docs/documentacion-tecnica.md §4.1, §4.4, §4.6"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-20"
---

Temas: [[donetonic]] · [[fases]] · [[fechas]] · [[grada-colchonera]] · [[hitos]] · [[pbi]] · [[scrum]] · [[sprint]] · [[tarea]] · [[tareas]]

# Fechas, PBIs, tareas y estructura de los dos sprints

**Temas:** [[donetonic]] · [[grada-colchonera]] · [[scrum]] · [[sprint]] · [[pbi]] · [[tarea]]

---

## Resumen general

| Sprint | Fechas | PBIs | Tareas | Etiquetas / Fases | Alcance | Prioridad |
|--------|--------|------|--------|-------------------|---------|-----------|
| **Sprint 1** | 29/09/2026 – 27/10/2026 | 19 (P1–P19) | 32 (T1–T32) | Hito 1 a Hito 4 | Base SaaS (Hitos 1–4 del enunciado) | Todos MUST |
| **Sprint 2** | 23/10/2026 – 29/10/2026 | 29 (P20–P48) | 50 (T33–T82) | Por fase del juego (ver detalle) | Lógica del juego | Todos MUST |

- **Product Backlog total:** 48 PBIs, 82 tareas, **todos marcados como hechos**.
- **Capturas DoneTonic:** 29/10/2026 con ambos sprints cerrados.
- **Fuente principal:** `repo:saas/docs/gestion/README.md` (citada en ambas notas; en Nota B se indica «cita sin comprobar»).

---

## Detalle Sprint 1 – Por hitos (Ampliación 2026-11-19, memoria-procesos)

| Hito | PBIs | Tareas |
|------|------|--------|
| Hito 1 | P1–P6 | T1–T7 |
| Hito 2 | P7–P10 | T8–T14 |
| Hito 3 | P11–P14 | T15–T20 |
| Hito 4 | P15–P19 | T21–T32 |

> **Nota:** La distribución de tareas en el Hito 4 (T21–T32 = 12 tareas) proviene de la Nota B. Ver **Contradicciones** al final.

---

## Detalle Sprint 2 – Por fases (Ampliación 2026-11-19, memoria-procesos)

| Fase / Etiqueta | PBIs | Tareas |
|-----------------|------|--------|
| Base del juego | P20–P28 | T33–T51 |
| Fase 2·Club | P29–P32 | T52–T56 |
| Fase 3·Ultras | P33–P34 | T57–T60 |
| Fase 4·Mundo | P35–P37 | T61–T63 |
| Fase 5·Rarezas | P38–P41 | T64–T68 |
| Fase 6·Logros y sonido | P42–P46 | T69–T76 |
| Calidad | P47–P48 | T77–T82 |

> **Nota:** Esta lista contiene **7 fases**. Ver **Contradicciones** al final.

---

## Burndown y métricas (Nota A – Ampliación 2026-11-19)

- **Sprint 1 (burndown):** 15 → 9 → 5 → 1 → 2 → 0 (16 PBIs en alcance de entrega).
- **Sprint 2 (burndown real, reconstruido por fechas de PR):** 28 → 11 → 11 → 2 → 2 → 2 → 0.
- **DoneTonic Sprint 2:** Gráfico en recta porque el backlog se registró al cerrar el sprint (29/10/2026).

---

## Fechas clave (Nota B – Ampliación 2026-11-19)

- **12/10/2026:** Primera entrega (Hitos 1–3).
- **23/10/2026:** Hito 4 en producción **e** inicio del Sprint 2.
- **29/10/2026:** Fin del Sprint 2 (y capturas DoneTonic con ambos sprints cerrados).

---

## Relacionados (unión de ambas notas)

- [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]]
- [[estado-de-completitud-de-sprints-y-trazabilidad]]
- [[estructura-sprint-2-6-fases-calidad-29-pbis-50-tareas-fechas]]
- [[backlog-sprint-2-con-prs-fechas-de-fusion-y-estado-por-pbi]]
- [[fechas-y-estructura-del-sprint-1-4-hitos-19-pbis-32-tareas]]
- [[fechas-pbis-y-tareas-de-los-dos-sprints]]
- [[trazabilidad-requisito-pbi-tarea-pr-en-donetonic-y-github]]
- [[fechas-pbis-y-tareas-de-los-dos-sprints]]
- [[fechas-y-estructura-del-sprint-2-1-semana-29-pbis-50-tareas]]
- Inventario de capturas de pantalla con trazabilidad a requisitos y fechas
- Trazabilidad requisito-PBI-tarea-PR en DoneTonic y GitHub
- Burndown real vs DoneTonic en Sprint 2 (backlog registrado al cierre)

---

## Origen

[[proyectos/memoria-procesos/estado|memoria-procesos]] — Ampliaciones fechadas el 2026-11-19 en ambas notas.

---

## Citas textuales de `repo:saas/docs/gestion/README.md`

> **Sprint 2** | Del 23/10/2026 al 29/10/2026 · 29 PBIs (P20–P48) y 50 tareas (T33–T82), etiquetas por fase del juego · **Hecho**  
> — *Nota A*

> **Sprint 1:** del 29/09/2026 al 27/10/2026 · 19 PBIs (P1–P19) y 32 tareas (T1–T32) · Hecho.  
> **Sprint 2:** del 23/10/2026 al 29/10/2026 · 29 PBIs (P20–P48) y 50 tareas (T33–T82) · Hecho.  
> — *Nota B (marcada como «cita sin comprobar»)*

---

## Problema / Solución (Nota B)

- **Problema:** Tener las fechas, PBIs y tareas exactas para la memoria.
- **Solución:** Usar estos datos tal cual en todos los capítulos y anexos.

<<<CONTRADICCION>>
1. **Número de fases en Sprint 2:** La Nota A (cuerpo principal y enlace `estructura-sprint-2-6-fases...`) describe **6 fases** (Fase 1 a Fase 6). La Ampliación de la Nota A (2026-11-19) y la Ampliación de la Nota B (2026-11-19) afirman que el Sprint 2 tuvo **7 fases** (Base del juego, Fase 2·Club, Fase 3·Ultras, Fase 4·Mundo, Fase 5·Rarezas, Fase 6·Logros y sonido, Calidad).  
2. **Tareas del Hito 4 (Sprint 1):** La Nota A (advertencia sobre [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]]) dice que el Hito 4 tiene **6 tareas (T21–T26)** marcadas hechas al cerrar el Sprint 1. La Ampliación de la Nota B dice que el Hito 4 abarca **12 tareas (T21–T32)** dentro del Sprint 1 (que cierra el 27/10/2026).

> Sprint 2 | Del 23/10/2026 al 29/10/2026 · 29 PBIs (P20–P48) y 50 tareas (T33–T82), etiquetas por fase del juego · **Hecho**
> — `repo:saas/docs/gestion/README.md`

Fusionada con: Fechas y estructura de los dos sprints con PBIs y tareas

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
