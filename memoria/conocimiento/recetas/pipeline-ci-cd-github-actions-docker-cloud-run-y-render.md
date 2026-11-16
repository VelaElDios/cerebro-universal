---
tipo: "receta"
titulo: "Pipeline CI/CD: GitHub Actions, Docker, Cloud Run y Render"
temas: ["despliegue", "devops", "grada-colchonera", "saas"]
claves: ["ci.yml", "deploy-cloud-run.yml", "memoria.yml", "Cloud Run", "Neon", "Workload Identity Federation", "Artifact Registry", "Secret Manager"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[despliegue]] · [[devops]] · [[grada-colchonera]] · [[saas]]

Cuatro workflows: 1) `ci.yml` se dispara en PR/push a `main` y `hito-*/integracion`; ejecuta `npm ci` + `npm test` con PostgreSQL 17 y construye/arranca imagen Docker comprobando `/api/health`. 2) `deploy-cloud-run.yml` se lanza tras CI exitoso en `main` (`workflow_run`); usa Workload Identity Federation para autenticar en Google Cloud, sube imagen a Artifact Registry y despliega en Cloud Run (región `europe-southwest1`, escala a cero, secretos como variables de entorno, service account con acceso mínimo). 3) `memoria.yml` compila la memoria LaTeX (LuaLaTeX + latexmk + biber) y publica PDF como artefacto. 4) Render despliega alternativamente según `render.yaml`. Imagen Docker: Node 22 Alpine, solo dependencias de producción, usuario no root, puerto 8080. Base de datos Neon (PostgreSQL gestionado, Frankfurt) compartida. Scripts de preparación única: `scripts/gcp/preparar-cloud-run.sh` (proyecto, APIs, Artifact Registry, secretos, service accounts, WIF) y `scripts/gcp/configurar-hito4.sh` (secretos correo y Google). Resiliencia: revisiones fallidas no rompen servicio anterior.

> Workflow ci.yml (CI): Cada PR y cada push a main y a hito-*/integración. Trabajo Pruebas: npm ci + npm test con un servicio PostgreSQL 17. Trabajo Imagen Docker: construye la imagen, la arranca y comprueba /api/health. deploy-cloud-run.yml: Cuando el CI termina bien en main (workflow_run). Autentica en Google Cloud con Workload Identity Federation, construye y sube la imagen a Artifact Registry y despliega en Cloud Run con las variables (NODE_ENV, ALLOWED_DOMAINS) y los 8 secretos de Secret Manager. Imagen Docker: Node 22 (Alpine), solo dependencias de producción, usuario sin privilegios, escucha en el 8080. Cloud Run: región europe-southwest1 (Madrid), escala a cero, secretos montados como variables de entorno, cuenta de servicio de ejecución con acceso solo a sus secretos. Base de datos: Neon (PostgreSQL gestionado, región Frankfurt), compartida por Cloud Run y Render. Seguridad del despliegue: GitHub no guarda ninguna clave de Google Cloud; obtiene un token temporal por federación de identidad. Resiliencia: si una revisión no arranca (por ejemplo, falta un secreto), Cloud Run y Render siguen sirviendo la anterior. Preparación única: scripts/gcp/preparar-cloud-run.sh (proyecto, APIs, Artifact Registry, secretos, cuentas de servicio, WIF) y scripts/gcp/configurar-hito4.sh (secretos de correo y Google).
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
