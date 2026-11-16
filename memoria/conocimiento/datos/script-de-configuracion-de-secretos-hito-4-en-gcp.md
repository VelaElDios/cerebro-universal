---
tipo: "dato"
titulo: "Script de configuración de secretos Hito 4 en GCP"
temas: ["correo", "grada-colchonera", "oauth", "saas"]
claves: ["configurar-hito4.sh", "scripts/gcp", "Secret Manager", "PROJECT_ID"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/hito4-configuracion.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[correo]] · [[grada-colchonera]] · [[oauth]] · [[saas]]

Script ubicado en `scripts/gcp/configurar-hito4.sh`. Uso: `PROJECT_ID=tu-proyecto bash configurar-hito4.sh`. Solicita interactivamente `SMTP_URL`, `MAIL_FROM`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` y los almacena en **Secret Manager** para que Cloud Run los inyecte como variables de entorno tras fusionar la PR de despliegue (T25).

> En Cloud Shell, desde la carpeta `scripts/gcp`: `PROJECT_ID=tu-proyecto bash configurar-hito4.sh` (pide los cuatro valores y los guarda en Secret Manager).
> — `repo:saas/docs/hito4-configuracion.md`

Relacionado: [[como-desplegar-secretos-de-hito-4-a-cloud-run-produccion]] · [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
