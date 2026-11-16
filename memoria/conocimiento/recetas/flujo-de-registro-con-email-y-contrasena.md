---
tipo: "receta"
titulo: "Flujo de registro con email y contraseña"
temas: ["autenticación", "grada-colchonera", "registro", "saas"]
claves: ["registro", "userService", "passwordHasher", "userRepository", "accountConfirmation", "mailer", "HMAC token", "24h"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[autenticación]] · [[grada-colchonera]] · [[registro]] · [[saas]]

Secuencia: 1) Usuario escribe email/contraseña en vista registro. 2) Vista valida formato email y longitud >= 8. 3) Vista llama `api.register(email, password)`. 4) `api.js` POST a `/api/auth/register`. 5) `api/auth.js` delega a `userService.register()`. 6) Servicio normaliza email, valida, busca en repo (`findByEmail`). 7) Si existe -> `ConflictError` -> 409 -> mensaje en formulario. 8) Si nuevo: hashea contraseña con bcrypt (coste 10, en tests 4). 9) Crea usuario en repo con `role=user`, `status=pending`, `provider=local`. 10) Llama `accountConfirmationService.enviarConfirmacion(user)`. 11) Servicio genera token HMAC-SHA256 con payload `{userId, propósito, caducidad 24h}`. 12) Envía email vía `mailer` (SMTP o log) con enlace `/api/auth/confirm?token=...`. 13) Si falla email: log `mail.failed`, responde 201 con aviso "no se ha podido enviar, pide otro". 14) Si ok: responde 201 con "te hemos enviado un correo". 15) Vista muestra aviso éxito y redirige a Entrar.

> U->>V: Escribe email y contraseña / V->>C: register(email, password) / C->>A: POST {email, password} / A->>S: register() / S->>H: hash(password) (bcrypt) / S->>R: create(role user, status pending, provider local) / A->>AC: enviarConfirmacion(user) / AC->>AC: token = firma HMAC {userId, propósito, caducidad 24 h} / AC->>M: send(to, asunto, enlace /api/auth/confirm?token=…)
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[decisiones-de-diseno-del-backend-con-alternativas-y-justific]] · [[cliente-api-con-timeout-de-15-s-y-manejo-de-apierror]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
