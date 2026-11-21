---
tipo: "concepto"
titulo: "Diferencia nomenclatura tareas Hito 4 entre DoneTonic y repositorio"
temas: ["donetonic", "grada-colchonera", "saas", "scrum", "sprint"]
claves: ["Hito 4", "DoneTonic", "ramas", "T21-T26", "nomenclatura"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-18"
---

Temas: [[donetonic]] · [[grada-colchonera]] · [[saas]] · [[scrum]] · [[sprint]]

Discrepancia documentada: DoneTonic usa nombres descriptivos de tarea (T21 Registrar app OAuth, T22 Flujo login OAuth, T23 Servicio correo, T24 Flujo confirmación, T25 Errores backend, T26 Mensajes frontend). El repo usa 5 ramas técnicas: `hito-4/T22-google-oauth` (#40), `T23-correo` (#38), `T24-confirmacion` (#39), `T25-secretos-hito4` (#37), `T26-privacidad` (#41). P17 (manejo errores) se reparte entre las 5 ramas. Todas marcadas hechas en DoneTonic al cerrar Sprint 1.

> > **Hito 4.** En DoneTonic las tareas del Hito 4 se llaman por lo que hacen (T21 *Registrar app OAuth*, T22 *Flujo login OAuth*, T23 *Servicio correo*, T24 *Flujo confirmación*, T25 *Errores backend* y T26 *Mensajes frontend*). En el repositorio el trabajo se repartió en cinco ramas (`hito-4/T22-google-oauth` #40, `T23-correo` #38, `T24-confirmacion` #39, `T25-secretos-hito4` #37 y `T26-privacidad` #41). El manejo de errores (P17) está repartido por las cinco. Las seis tareas se marcaron como hechas en DoneTonic al cerrar el Sprint 1.
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[convencion-de-ramas-y-prs-por-sprint-sprint-1-vs-sprint-2]] · [[historias-de-usuario-y-criterios-de-aceptacion-en-donetonic]] · [[convencion-de-ramas-y-prs-por-hito-fase-en-el-proyecto]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[backlog-completo-del-sprint-1-con-trazabilidad-a-releases]]: La nota A afirma que las seis tareas del Hito 4 se marcaron hechas en DoneTonic **al cerrar el Sprint 1**. La nota B indica una **Primera entrega el 12/10/2026** (con Hitos 1–3 + P18 + P19, estos dos del Hito 4) y que el **Hito 4 se completó el 23/10/2026**, lo que sugiere que el cierre del Sprint 1 (o su entrega principal) ocurrió el 12/10, once días antes de terminar el Hito 4.

> ⚠️ Posible contradicción con [[fechas-pbis-y-tareas-de-los-dos-sprints]]: La nota A dice que el Hito 4 tiene **6 tareas (T21–T26)** y que esas seis se marcaron hechas al cerrar el Sprint 1. La nota B dice que el Hito 4 abarca **12 tareas (T21–T32)** dentro del Sprint 1 (que cierra el 27/10/2026).

> ⚠️ Posible contradicción con [[trazabilidad-requisito-pbi-tarea-pr-en-donetonic-y-github]]: La **Nota A** delimita el Hito 4 en **6 tareas (T21–T26)** y afirma que esas seis se marcaron hechas al cerrar el Sprint 1. La **Nota B** establece que el Sprint 1 tiene **32 tareas (T1–T32)** e incluye la release `hito-4`, lo que implica que el Hito 4 abarca hasta la T32 (12 tareas: T21–T32), no solo hasta la T26.
