---
tipo: "decision"
titulo: "Solución a correo no salía desde Cloud Run: SMTP Gmail puerto 465 con contraseña de aplicación"
temas: ["cloud-run", "email", "grada-colchonera", "saas"]
claves: ["SMTP", "puerto 465", "Gmail", "Secret Manager"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[cloud-run]] · [[email]] · [[grada-colchonera]] · [[saas]]

Problema: emails no se enviaban desde Cloud Run. Causa: puertos SMTP estándar (25, 587) bloqueados en Cloud Run. Solución: usar SMTP de Gmail en puerto 465 (SSL/TLS implícito) con contraseña de aplicación (no contraseña de cuenta). La contraseña se almacena en Secret Manager y se inyecta como variable de entorno en Cloud Run. Configurado en `scripts/gcp/configurar-hito4.sh`.

> El correo no salía desde Cloud Run. El SMTP sin cifrar (puerto 25/587) suele estar bloqueado. SMTP de Gmail por el puerto 465 con contraseña de aplicación, guardada en Secret Manager
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
