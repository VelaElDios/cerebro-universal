---
tipo: "decision"
titulo: "Comportamiento de cuentas según método de registro y estado previo"
temas: ["correo", "grada-colchonera", "oauth", "saas"]
claves: ["pending", "authProvider: google", "ACCOUNT_PENDING", "ADMIN_EMAIL", "ADMIN_PASSWORD"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/hito4-configuracion.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[correo]] · [[grada-colchonera]] · [[oauth]] · [[saas]]

Tabla de decisiones implementada en el backend para resolver colisiones entre registro local y OAuth:
- **Registro email+pass**: cuenta `pending` 24 h, login devuelve `ACCOUNT_PENDING` hasta confirmar vía enlace.
- **Google OAuth email nuevo**: cuenta activa directa con `authProvider: google`.
- **Google OAuth email ya registrado pendiente**: cuenta pasa a activa (Google valida propiedad del email).
- **Google OAuth email de cuenta eliminada**: acceso rechazado (no se resucita).
- **Admin inicial**: se crea activo desde variables `ADMIN_EMAIL` / `ADMIN_PASSWORD` (sin flujo pendiente).

> | Caso | Resultado | |---|---| | Registro con email y contraseña | Cuenta `pending` + correo con enlace (24 h). Hasta confirmar, el login devuelve `ACCOUNT_PENDING` | | Entrar con Google, email nuevo | Cuenta creada ya activa (`authProvider: google`) | | Entrar con Google, email de una cuenta local pendiente | La cuenta queda confirmada (Google ya verificó el correo) | | Entrar con Google, email de una cuenta eliminada | Rechazado | | Administrador inicial | Se crea activo desde `ADMIN_EMAIL` / `ADMIN_PASSWORD` |
> — `repo:saas/docs/hito4-configuracion.md`

Relacionado: [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
