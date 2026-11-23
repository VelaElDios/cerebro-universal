---
tipo: "decision"
titulo: "Trazabilidad completa requisito → PBI → tarea → PR en anexo A4"
temas: ["anexo", "longtable", "trazabilidad", "memoria"]
claves: ["anexo A4", "trazabilidad", "longtable", "requisito PBI tarea PR"]
proyectos: ["memoria-procesos"]
fuentes: ["spec del proyecto (tabla anexos)", "spec del proyecto §Anexos y docs/requisitos.md, docs/sprint-1.md, docs/sprint-2.md", "memoria/chapters/a4-trazabilidad.tex\ncaption: Tabla~\\ref{tab:trazabilidad-completa} con 82 filas (una por tarea) + requisitos no funcionales transversales."]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-23"
---

Temas: [[anexo]] · [[longtable]] · [[trazabilidad]]

El anexo A4 (chapters/a4-trazabilidad.tex) contiene una longtable con 5 columnas: Requisito, PBI, Tarea, Descripción de la tarea, PR. Incluye primero los RNF transversales, luego una fila por cada una de las 82 tareas (32 Sprint 1 + 50 Sprint 2). Los datos salen de docs/documentacion-tecnica.md §3 (requisito→PBI) y docs/gestion/README.md (PBI→tarea→PR). El test verificar.py comprueba que todos los PBIs y tareas aparecen.

> Anexo nuevo: «Trazabilidad» con \label{anx:trazabilidad}. Tabla completa (longtable) requisito → PBI → tarea → PR de los dos sprints: todos los PBIs P1–P48 y todas las tareas T1–T82.
> — `spec del proyecto (tabla anexos)` (cita sin comprobar)

Relacionado: [[trazabilidad-completa-requisito-pbi-tarea-pr-en-anexo-a4-tra]] · [[tabla-de-trazabilidad-sprint-1-pbi-hito-titulo-tareas-prs-re]] · [[tabla-de-trazabilidad-sprint-2-pbi-etiqueta-titulo-tareas-pr]] · [[trazabilidad-completa-requisito-pbi-tarea-pr-82-tareas]]

## Ampliación (2026-11-23, memoria-procesos)
|
  El anexo a4-trazabilidad.tex contiene una longtable con:
  - Filas iniciales para RNF-01 a RNF-12 (transversales) con sus PBIs/tareas/PRs.
  - Una fila por cada una de las 32 tareas del Sprint 1 (con requisito, PBI, tarea, descripción, PR).
  - Una fila por cada una de las 50 tareas del Sprint 2 (con requisito, PBI, tarea, descripción, PR).
  - Total: 12 + 32 + 50 = 94 filas de datos + cabecera.
  - Columnas: Requisito (1.5cm), PBI (0.8cm), Tarea (1.3cm), Descripción (7.0cm), PR (2.9cm).
  - Usa \allowbreak en rutas/largos para evitar overfull hbox.
  - Cierres de hito y releases documentados al final.

## Ampliación (2026-11-23, memoria-procesos)
El anexo a4-trazabilidad.tex contiene la matriz completa en longtable:
- Primeras filas: RNF-01 a RNF-12 con sus PBIs, tareas y PRs asociados.
- Después: una fila por cada una de las 82 tareas (T1–T82) con Requisito (RF/RJ o —), PBI, Tarea, Descripción, PR.
- Cierres de hito y releases indicados al final.
- Compilado y verificado por verificar.py (comprueba que están todos los PBIs P1–P48 y tareas T1–T82).

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
