---
tipo: "receta"
titulo: "Pipeline CI/CD: GitHub Actions → Cloud Run con Workload Identity Federation (WIF) y despliegue alternativo en Render"
temas: ["artifact-registry", "ci-cd", "cloud-run", "despliegue", "github-actions", "grada-colchonera", "saas", "wif"]
claves: ["CI", "deploy-cloud-run", "Workload Identity Federation", "Artifact Registry", "gcloud run deploy", "Secret Manager", "migraciones", "primer admin", "revisión anterior"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[artifact-registry]] · [[ci-cd]] · [[cloud-run]] · [[despliegue]] · [[github-actions]] · [[grada-colchonera]] · [[saas]] · [[wif]]

1. **Pull Request**: GitHub Actions ejecuta CI (pruebas con PostgreSQL 17 + build imagen Docker). Check «Pruebas» debe pasar para permitir merge.
2. **Merge a main**: CI en main; al éxito dispara workflow `deploy-cloud-run`.
3. **Deploy**: `deploy-cloud-run` obtiene token temporal vía Workload Identity Federation (sin claves), hace `docker build + push` a Artifact Registry (etiqueta = commit SHA), y `gcloud run deploy` pasando variables y secretos desde Secret Manager.
4. **Arranque en Cloud Run**: la nueva revisión ejecuta migraciones y `ensureAdmin`. Si arranca bien → tráfico a la nueva revisión; si falla → sigue la revisión anterior (rollout automático).
5. **Despliegue alternativo**: Webhook de main a Render para despliegue paralelo.

> D->>GH: Pull request GH->>CI: Pruebas (PostgreSQL 17) + imagen Docker CI-->>GH: Check «Pruebas» verde (obligatorio para fusionar) D->>GH: Fusión en main GH->>CI: CI en main CI-->>CD: workflow_run: success CD->>GC: Token temporal con Workload Identity Federation CD->>AR: docker build + push (etiqueta = commit) CD->>CR: gcloud run deploy (variables + secretos de Secret Manager) CR->>CR: Arranca la revisión: migraciones y primer admin alt Arranca bien CR-->>D: Tráfico a la nueva revisión else Falla CR-->>D: Sigue la revisión anterior end GH->>RE: Webhook de main → despliegue alternativo
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[pipeline-ci-cd-github-actions-docker-cloud-run-y-render]] · [[pipeline-ci-cd-github-actions-con-postgresql-17-real-docker]] · [[url-publica-de-despliegue-continuo-google-cloud-run]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
