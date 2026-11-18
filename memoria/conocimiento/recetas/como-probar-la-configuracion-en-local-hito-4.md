---
tipo: "receta"
titulo: "Cómo probar la configuración en local (Hito 4)"
temas: ["correo", "grada-colchonera", "oauth", "saas"]
claves: [".env.example", ".env", "npm start", "SMTP_URL", "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/hito4-configuracion.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[correo]] · [[grada-colchonera]] · [[oauth]] · [[saas]]

1. `cp .env.example .env`
2. Edita `.env` y rellena las cuatro variables: `SMTP_URL`, `MAIL_FROM`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`.
3. Ejecuta `npm start`.
4. Si falta `SMTP_URL`, los correos no se envían realmente; el enlace de confirmación de cuenta se imprime en la consola del servidor para probar manualmente.

> Copia `.env.example` a `.env` y rellena `SMTP_URL`, `MAIL_FROM`, `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET`, y arranca con `npm start`. Sin `SMTP_URL`, los correos no se envían: el enlace de confirmación aparece en la consola.
> — `repo:saas/docs/hito4-configuracion.md`

Relacionado: [[como-crear-cliente-oauth-de-google-para-la-grada-colchonera]] · [[como-configurar-smtp-saliente-con-gmail-contrasena-de-aplica]] · [[como-desplegar-secretos-de-hito-4-a-cloud-run-produccion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
