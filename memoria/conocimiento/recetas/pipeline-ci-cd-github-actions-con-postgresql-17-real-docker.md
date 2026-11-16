---
tipo: "receta"
titulo: "Pipeline CI/CD: GitHub Actions con PostgreSQL 17 real, Docker, despliegue automático a Cloud Run"
temas: ["ci-cd", "cloud-run", "docker", "github-actions", "grada-colchonera", "postgresql", "procesos", "saas"]
claves: ["ci.yml", "deploy-cloud-run.yml", "PostgreSQL 17", "Workload Identity Federation", "main protegida"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[ci-cd]] · [[cloud-run]] · [[docker]] · [[github-actions]] · [[grada-colchonera]] · [[postgresql]] · [[procesos]] · [[saas]]

Dos workflows en `.github/workflows/`:
1. `ci.yml` (dispara en PR y push a `main`):
   - Levanta PostgreSQL 17 real (service container).
   - Ejecuta `npm test` (80 tests con `node:test`).
   - Construye imagen Docker (`Dockerfile`).
   - `main` tiene branch protection: requiere status check "Pruebas" en verde.
2. `deploy-cloud-run.yml` (dispara en push a `main` tras CI verde):
   - Autentica con Google Cloud via Workload Identity Federation (OIDC token, sin JSON keys).
   - `gcloud builds submit` + `gcloud run deploy` a `europe-southwest1`.
   - Servicio: `la-grada-colchonera` (URL fija).
   - Variables/secrets de runtime tomados de Secret Manager.
- `render.yaml` y `scripts/gcp/preparar-cloud-run.sh` documentan infraestructura como código.

> GitHub Actions (*Pruebas* con PostgreSQL 17 real e *Imagen Docker*). `main` está protegida y exige el check en verde [...] Cuando el CI pasa en `main`, [`deploy-cloud-run.yml`](../.github/workflows/deploy-cloud-run.yml) construye la imagen y la despliega en Cloud Run (Workload Identity Federation, sin claves)
> — `repo:saas/docs/revision-entrega.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
