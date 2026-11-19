---
tipo: "dato"
titulo: "Backlog completo del Sprint 1 con trazabilidad a releases"
temas: ["donetonic", "grada-colchonera", "saas", "scrum", "sprint"]
claves: ["P1–P19", "Hito 1–4", "releases GitHub", "trazabilidad"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-18"
---

Temas: [[donetonic]] · [[grada-colchonera]] · [[saas]] · [[scrum]] · [[sprint]]

Tabla de los 19 PBIs del Sprint 1 con su hito, título, estado y enlace de entrega:
- **Hito 1** (release hito-1): P1 GitHub repo + GitHub Flow, P2 CI, P3 Deploy continuo URL pública, P4 Gestión usuarios en memoria, P5 Tests unitarios lógica, P6 API usuarios.
- **Hito 2** (release hito-2): P7 Frontend interfaz/cliente separados, P8 Registro/login locales, P9 Logout + mantenimiento sesión, P10 Rutas protegidas servidor.
- **Hito 3** (release hito-3): P11 Persistencia BD real, P12 Secretos con variables entorno, P13 Roles usuario/admin, P14 Log de actividad.
- **Hito 4** (release hito-4): P15 OAuth (PR #40), P16 Confirmación cuenta email (PRs #38, #39), P17 Manejo errores + feedback (PRs #37–#41), P18 README completo + revisión, P19 Deploy Cloud Run (créditos educación).
- Primera entrega (12/10/2026): Hitos 1–3 + P18 + P19. Hito 4 completado 23/10/2026.
- Nota: P17 (manejo errores) ya tenía parte desde Hito 1: handler común formato `{"error": {"code", "message"}}` y mensajes error/éxito en UI.

> | P19 | H4 | Despliegue continuo en Google Cloud Run | Hecho | Cierre del sprint |
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]] · [[backlog-sprint-2-con-prs-fechas-de-fusion-y-estado-por-pbi]] · [[fechas-y-estructura-del-sprint-1-4-hitos-19-pbis-32-tareas]] · [[trazabilidad-completa-sprint-1-pbis-tareas-ramas-y-prs]] · [[datos-del-burndown-sprint-1-pbis-pendientes-por-hito]] · [[tabla-de-trazabilidad-sprint-1-pbi-hito-titulo-tareas-prs-re]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]]: La nota A afirma que las seis tareas del Hito 4 se marcaron hechas en DoneTonic **al cerrar el Sprint 1**. La nota B indica una **Primera entrega el 12/10/2026** (con Hitos 1–3 + P18 + P19, estos dos del Hito 4) y que el **Hito 4 se completó el 23/10/2026**, lo que sugiere que el cierre del Sprint 1 (o su entrega principal) ocurrió el 12/10, once días antes de terminar el Hito 4.
