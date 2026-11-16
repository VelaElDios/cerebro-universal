---
tipo: "receta"
titulo: "Cómo crear cliente OAuth de Google para La Grada Colchonera"
temas: ["correo", "grada-colchonera", "oauth", "saas"]
claves: ["Google Cloud Console", "ID de cliente", "secreto del cliente", "URIs de redirección", "pantalla de consentimiento"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/hito4-configuracion.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[correo]] · [[grada-colchonera]] · [[oauth]] · [[saas]]

1. Entra en https://console.cloud.google.com/auth/overview y selecciona el proyecto `la-grada-colchonera-…`.
2. Si no existe pantalla de consentimiento: Google Auth Platform → Comenzar → Nombre: "La Grada Colchonera", correo de asistencia tuyo, Público: **Externo**, correo de contacto tuyo, acepta y crea.
3. En **Público** deja la app en *Pruebas* y añade tu correo (y el del profesor) como **usuarios de prueba**. Para abrir a cualquiera: *Publicar aplicación* (con scopes `openid`, `email`, `profile` no requiere verificación).
4. En **Clientes → Crear cliente**: tipo **Aplicación web**, nombre "La Grada Colchonera web", añade las dos URIs de redirección autorizadas (producción y local).
5. Al crear se muestran **ID de cliente** y **secreto del cliente** → son `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET`.

> En **Clientes → Crear cliente**: - Tipo de aplicación: **Aplicación web**. Nombre: `La Grada Colchonera web`. - **URIs de redireccionamiento autorizados** (añade las dos): - `https://la-grada-colchonera-1081564062572.europe-southwest1.run.app/api/auth/google/callback` - `http://localhost:3000/api/auth/google/callback`
> — `repo:saas/docs/hito4-configuracion.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
