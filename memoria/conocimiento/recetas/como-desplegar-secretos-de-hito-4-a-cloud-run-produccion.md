---
tipo: "receta"
titulo: "Cómo desplegar secretos de Hito 4 a Cloud Run (producción)"
temas: ["correo", "grada-colchonera", "oauth", "saas"]
claves: ["configurar-hito4.sh", "Secret Manager", "Cloud Shell", "PROJECT_ID", "PR T25"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/hito4-configuracion.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[correo]] · [[grada-colchonera]] · [[oauth]] · [[saas]]

1. Abre Cloud Shell y ve a la carpeta `scripts/gcp` del repositorio.
2. Ejecuta: `PROJECT_ID=tu-proyecto bash configurar-hito4.sh`.
3. El script pide interactivamente los cuatro valores (`SMTP_URL`, `MAIL_FROM`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`) y los almacena en **Secret Manager**.
4. Fusiona la PR de despliegue (T25); a partir de ahí Cloud Run inyecta esos secretos como variables de entorno en el contenedor.
5. Verifica en la web: registro → llega correo → enlace → entrar, y botón "Entrar con Google".

> En Cloud Shell, desde la carpeta `scripts/gcp`: `PROJECT_ID=tu-proyecto bash configurar-hito4.sh` (pide los cuatro valores y los guarda en Secret Manager).
> — `repo:saas/docs/hito4-configuracion.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]] · [[como-crear-cliente-oauth-de-google-para-la-grada-colchonera]] · [[como-configurar-smtp-saliente-con-gmail-contrasena-de-aplica]] · [[script-de-configuracion-de-secretos-hito-4-en-gcp]] · [[como-probar-la-configuracion-en-local-hito-4]] · [[solucion-a-correo-no-salia-desde-cloud-run-smtp-gmail-puerto]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
