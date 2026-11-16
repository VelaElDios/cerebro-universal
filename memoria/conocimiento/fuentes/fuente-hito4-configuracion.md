---
tipo: "fuente"
titulo: "hito4 configuracion"
temas: ["oauth", "correo", "grada-colchonera"]
claves: []
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/hito4-configuracion.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[oauth]] · [[correo]] · [[grada-colchonera]]

Documento aprendido: `repo:saas/docs/hito4-configuracion.md`.

## Resumen
Este trozo documenta la configuración única de dos servicios externos para el Hito 4: cliente OAuth de Google (inicio de sesión) y correo saliente SMTP con Gmail. Incluye pasos exactos en Google Cloud Console (pantalla de consentimiento, usuarios de prueba, URIs de redirección autorizadas), formato de la URL SMTP con contraseña de aplicación, prueba local con `.env`, despliegue a Cloud Run mediante script `configurar-hito4.sh` y una tabla de decisiones sobre comportamiento de cuentas según caso de registro/autenticación.

## Lo que se sacó de él (7)
- [[como-configurar-smtp-saliente-con-gmail-contrasena-de-aplica]]
- [[como-crear-cliente-oauth-de-google-para-la-grada-colchonera]]
- [[como-desplegar-secretos-de-hito-4-a-cloud-run-produccion]]
- [[como-probar-la-configuracion-en-local-hito-4]]
- [[comportamiento-de-cuentas-segun-metodo-de-registro-y-estado]]
- [[script-de-configuracion-de-secretos-hito-4-en-gcp]]
- [[url-base-de-la-aplicacion-la-grada-colchonera-en-cloud-run]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
