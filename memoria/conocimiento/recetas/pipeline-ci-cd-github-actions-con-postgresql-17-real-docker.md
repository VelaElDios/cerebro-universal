---
tipo: "receta"
titulo: "Pipeline CI/CD: GitHub Actions con PostgreSQL 17, Docker, Cloud Run, Render y compilación LaTeX"
temas: ["ci-cd", "cloud-run", "despliegue", "devops", "docker", "github-actions", "grada-colchonera", "postgresql", "procesos", "saas"]
claves: ["ci.yml", "deploy-cloud-run.yml", "PostgreSQL 17", "Workload Identity Federation", "main protegida", "memoria.yml", "Cloud Run", "Neon", "Artifact Registry", "Secret Manager"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md", "repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-19"
---

Temas: [[ci-cd]] · [[cloud-run]] · [[despliegue]] · [[devops]] · [[docker]] · [[github-actions]] · [[grada-colchonera]] · [[postgresql]] · [[procesos]] · [[saas]]

# Pipeline CI/CD: GitHub Actions con PostgreSQL 17, Docker, Cloud Run, Render y compilación LaTeX

Temas: [[ci-cd]] · [[cloud-run]] · [[docker]] · [[github-actions]] · [[grada-colchonera]] · [[postgresql]] · [[procesos]] · [[saas]] · [[despliegue]] · [[devops]]

## Workflows en `.github/workflows/`

1. **`ci.yml`** (dispara en PR, push a `main` y a ramas `hito-*/integracion`):
   - `npm ci` + `npm test` (80 tests con `node:test`) usando un **contenedor de servicio PostgreSQL 17 real**.
   - Construye la imagen Docker (`Dockerfile`), la arranca y comprueba el endpoint `/api/health`.
   - La rama `main` tiene **branch protection** que exige el status check **"Pruebas"** en verde.

2. **`deploy-cloud-run.yml`** (dispara mediante `workflow_run` tras CI exitoso en `main`):
   - Autentica en Google Cloud mediante **Workload Identity Federation** (token OIDC, sin claves JSON).
   - `gcloud builds submit` → sube la imagen a **Artifact Registry**.
   - `gcloud run deploy` → despliega en **Cloud Run** (región `europe-southwest1` / Madrid):
     - Servicio: `la-grada-colchonera` (URL fija).
     - Escala a cero.
     - Variables de runtime (`NODE_ENV`, `ALLOWED_DOMAINS`) y **8 secretos** montados como variables de entorno desde **Secret Manager**.
     - Cuenta de servicio de ejecución con acceso mínimo (solo a sus secretos).
   - **Resiliencia**: las revisiones fallidas no rompen el servicio anterior.

3. **`memoria.yml`**:
   - Compila la memoria LaTeX (LuaLaTeX + `latexmk` + `biber`) y publica el PDF como artefacto.

4. **Render** (despliegue alternativo, definido en `render.yaml`):
   - Usa la misma imagen Docker y la base de datos compartida.

## Imagen Docker
- **Base**: Node 22 Alpine.
- Solo dependencias de producción.
- Usuario no root.
- Escucha en el puerto **8080**.

## Base de datos
- **CI**: PostgreSQL 17 real (contenedor de servicio en GitHub Actions).
- **Producción**: **Neon** (PostgreSQL gestionado, región Frankfurt), compartida por Cloud Run y Render.

## Infraestructura como código y scripts de preparación única
- `render.yaml` → define el servicio en Render.
- `scripts/gcp/preparar-cloud-run.sh` → proyecto, APIs, Artifact Registry, secretos, cuentas de servicio, WIF.
- `scripts/gcp/configurar-hito4.sh` → secretos de correo y Google.

## Seguridad del despliegue
- GitHub **no guarda ninguna clave de Google Cloud**; obtiene un token temporal por federación de identidad (Workload Identity Federation).

## Citas de referencia
> GitHub Actions (*Pruebas* con PostgreSQL 17 real e *Imagen Docker*). `main` está protegida y exige el check en verde [...] Cuando el CI pasa en `main`, [`deploy-cloud-run.yml`](../.github/workflows/deploy-cloud-run.yml) construye la imagen y la despliega en Cloud Run (Workload Identity Federation, sin claves)
> — `repo:saas/docs/revision-entrega.md` (cita sin comprobar)

> Workflow ci.yml (CI): Cada PR y cada push a main y a hito-*/integración. Trabajo Pruebas: npm ci + npm test con un servicio PostgreSQL 17. Trabajo Imagen Docker: construye la imagen, la arranca y comprueba /api/health. deploy-cloud-run.yml: Cuando el CI termina bien en main (workflow_run). Autentica en Google Cloud con Workload Identity Federation, construye y sube la imagen a Artifact Registry y despliega en Cloud Run con las variables (NODE_ENV, ALLOWED_DOMAINS) y los 8 secretos de Secret Manager. Imagen Docker: Node 22 (Alpine), solo dependencias de producción, usuario sin privilegios, escucha en el 8080. Cloud Run: región europe-southwest1 (Madrid), escala a cero, secretos montados como variables de entorno, cuenta de servicio de ejecución con acceso solo a sus secretos. Base de datos: Neon (PostgreSQL gestionado, región Frankfurt), compartida por Cloud Run y Render. Seguridad del despliegue: GitHub no guarda ninguna clave de Google Cloud; obtiene un token temporal por federación de identidad. Resiliencia: si una revisión no arranca (por ejemplo, falta un secreto), Cloud Run y Render siguen sirviendo la anterior. Preparación única: scripts/gcp/preparar-cloud-run.sh (proyecto, APIs, Artifact Registry, secretos, cuentas de servicio, WIF) y scripts/gcp/configurar-hito4.sh (secretos de correo y Google).
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

## Relacionado
[[pipeline-ci-cd-github-actions-con-postgresql-17-real-docker]] · [[pipeline-ci-cd-github-actions-cloud-run-con-workload-identit]] · [[url-publica-de-despliegue-continuo-google-cloud-run]] · [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[pipeline-ci-cd-github-actions-con-postgresql-17-real-docker]] · [[seguridad-bcrypt-coste-10-sin-secretos-en-repo-secret-manage]]

## Origen
[[proyectos/memoria-procesos/estado|memoria-procesos]]

> GitHub Actions (*Pruebas* con PostgreSQL 17 real e *Imagen Docker*). `main` está protegida y exige el check en verde [...] Cuando el CI pasa en `main`, [`deploy-cloud-run.yml`](../.github/workflows/deploy-cloud-run.yml) construye la imagen y la despliega en Cloud Run (Workload Identity Federation, sin claves)
> — `repo:saas/docs/revision-entrega.md` (cita sin comprobar)
> Workflow ci.yml (CI): Cada PR y cada push a main y a hito-*/integración. Trabajo Pruebas: npm ci + npm test con un servicio PostgreSQL 17. Trabajo Imagen Docker: construye la imagen, la arranca y comprueba /api/health. deploy-cloud-run.yml: Cuando el CI termina bien en main (workflow_run). Autentica en Google Cloud con Workload Identity Federation, construye y sube la imagen a Artifact Registry y despliega en Cloud Run con las variables (NODE_ENV, ALLOWED_DOMAINS) y los 8 secretos de Secret Manager. Imagen Docker: Node 22 (Alpine), solo dependencias de producción, usuario sin privilegios, escucha en el 8080. Cloud Run: región europe-southwest1 (Madrid), escala a cero, secretos montados como variables de entorno, cuenta de servicio de ejecución con acceso solo a sus secretos. Base de datos: Neon (PostgreSQL gestionado, región Frankfurt), compartida por Cloud Run y Render. Seguridad del despliegue: GitHub no guarda ninguna clave de Google Cloud; obtiene un token temporal por federación de identidad. Resiliencia: si una revisión no arranca (por ejemplo, falta un secreto), Cloud Run y Render siguen sirviendo la anterior. Preparación única: scripts/gcp/preparar-cloud-run.sh (proyecto, APIs, Artifact Registry, secretos, cuentas de servicio, WIF) y scripts/gcp/configurar-hito4.sh (secretos de correo y Google).
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: - Nota A menciona **dos workflows** (`ci.yml` y `deploy-cloud-run.yml`); Nota B habla de **cuatro workflows** incluyendo `memoria.yml` y cuenta a Render como un workflow (Render es un servicio externo, no un workflow de GitHub Actions).
- Nota A: `ci.yml` dispara solo en PR y push a `main`; Nota B añade ramas `hito-*/integracion`.
- Nota A: el trabajo "Imagen Docker" solo construye; Nota B dice que **construye, arranca y comprueba `/api/health`**.
- Nota A: branch protection en `main` requiere check "Pruebas"; Nota B no lo menciona.
- Nota A: `deploy-cloud-run.yml` dispara en "push a `main` tras CI verde"; Nota B usa explícitamente `workflow_run` tras CI exitoso en `main`.
- Nota A: servicio Cloud Run `la-grada-colchonera` con URL fija; Nota B no nombra el servicio ni la URL fija.
- Nota B detalla **imagen Docker** (Node 22 Alpine, usuario no root, puerto 8080), **base de datos Neon** (Frankfurt), script `configurar-hito4.sh`, **resiliencia** y workflow `memoria.yml`; Nota A no los incluye.
- Nota A cita `repo:saas/docs/revision-entrega.md`; Nota B cita `repo:saas/docs/documentacion-tecnica.md`.

Fusionada con: Pipeline CI/CD: GitHub Actions, Docker, Cloud Run y Render

Relacionado: [[pipeline-ci-cd-descrito-una-sola-vez-en-cap-5-regla-14-javie]] · [[pipeline-ci-cd-descrito-una-sola-vez-en-cap-5]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
