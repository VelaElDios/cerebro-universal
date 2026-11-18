---
tipo: "receta"
titulo: "Flujo de confirmación de cuenta por correo (GET /api/auth/confirm)"
temas: ["auth", "grada-colchonera", "saas", "secuencia"]
claves: ["confirmar", "tokenSigner", "accountConfirmation", "userService", "303", "aviso"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[grada-colchonera]] · [[saas]] · [[secuencia]]

El usuario abre el enlace de confirmación que lleva un token. La API `GET /api/auth/confirm` delega en `accountConfirmation.confirmar(token)`, que usa `tokenSigner.verify(token, propósito)` para validar firma, caducidad y propósito. Si el token es inválido, devuelve `null` y la API redirige con `303` a `/?aviso=enlace-no-valido#/entrar` registrando `user.confirm_failed`. Si es válido, obtiene `{userId}` y llama a `userService.activar(userId)` solo si la cuenta está en estado `pending`. Finalmente redirige con `303` a `/?aviso=cuenta-confirmada#/entrar` registrando `user.confirmed`. La interfaz (`ui.js`) lee el parámetro `aviso`, lo muestra y lo elimina de la URL.

> U->>A: Abre el enlace (token) A->>AC: confirmar(token) AC->>T: verify(token, propósito) alt Firma mala, caducado o propósito distinto T-->>AC: null A-->>U: 303 → /?aviso=enlace-no-valido#/entrar (log user.confirm_failed) else Válido T-->>AC: {userId} AC->>S: activar(userId) (si está pending) A-->>U: 303 → /?aviso=cuenta-confirmada#/entrar (log user.confirmed)
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[maquina-de-estados-de-la-cuenta-de-usuario]] · [[perfil-de-juego-con-jsonb-y-concurrencia-optimista-mediante]] · [[registro-de-usuario-con-confirmacion-por-correo-hmac-24-h-y]] · [[flujo-de-registro-con-email-y-contrasena]] · [[login-local-con-cuenta-pendiente-y-reenvio-de-confirmacion-p]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
