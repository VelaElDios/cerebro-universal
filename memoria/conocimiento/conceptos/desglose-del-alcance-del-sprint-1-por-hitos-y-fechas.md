---
tipo: "concepto"
titulo: "Desglose del alcance del Sprint 1 por hitos y fechas"
temas: ["alcance", "grada-colchonera", "saas", "sprint"]
claves: ["hito 1", "hito 2", "hito 3", "hito 4", "cierre sprint", "fechas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[alcance]] · [[grada-colchonera]] · [[saas]] · [[sprint]]

Cronograma detallado del Sprint 1 (base SaaS) en tres bloques: Hitos 1-3 (29/09–12/10) cubren repositorio, CI/CD, lógica de usuarios con tests, API REST, frontend desacoplado (interfaz + cliente), auth local, sesión, rutas protegidas, PostgreSQL (Neon), secretos, roles, panel admin y logs. Hito 4 (hasta 23/10) añade confirmación por email, OAuth Google, manejo global de errores, política de privacidad y app Google publicada. Cierre (24/10): README, capturas, revisión contra enunciado, despliegue en Cloud Run y estructura de memoria. El Sprint 2 (23/10–29/10) aborda la lógica del juego en 6 fases (29 PBIs, P20–P48).

> | Etapa | Alcance |
|---|---|
| **Sprint 1, Hitos 1–3** (29/09 – 12/10/2026) | Repositorio, CI, despliegue continuo, lógica de usuarios con pruebas, API REST, frontend separado en interfaz y cliente, registro e inicio de sesión locales, sesión, rutas protegidas, PostgreSQL, secretos, roles, panel de administración y logs |
| **Sprint 1, Hito 4** (hasta el 23/10/2026) | Confirmación de cuenta por correo, inicio de sesión con Google, manejo de errores de principio a fin, política de privacidad y aplicación de Google publicada |
| **Cierre del sprint** (24/10/2026) | README, capturas, revisión de la entrega frente al enunciado, despliegue en Google Cloud Run y estructura de la memoria |
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]] · [[backlog-completo-del-sprint-1-con-trazabilidad-a-releases]] · [[diferencia-nomenclatura-tareas-hito-4-entre-donetonic-y-repo]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[fechas-y-estructura-del-sprint-1-4-hitos-19-pbis-32-tareas]] · [[cronologia-detallada-del-proyecto-septiembre-octubre-2026]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> ⚠️ Posible contradicción con [[cambio-de-alcance-durante-sprint-1-anadido-p19-cloud-run-por]]: La Nota A sitúa el despliegue en Cloud Run en el **Cierre del sprint (24/10/2026)**, mientras que la Nota B dice que la "primera entrega 12/10/2026 (Hitos 1-3, P18, P19)" ya incluía P19 (Cloud Run) y que en la tabla del Sprint 1 P19 está en el **Hito 4 (hasta 23/10/2026)**. Tres hitos/fechas distintas para el mismo PBI.
