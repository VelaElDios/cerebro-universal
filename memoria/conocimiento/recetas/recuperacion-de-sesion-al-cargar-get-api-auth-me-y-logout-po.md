---
tipo: "receta"
titulo: "Recuperación de sesión al cargar (GET /api/auth/me) y logout (POST /api/auth/logout)"
temas: ["auth", "grada-colchonera", "saas", "sesión", "ui"]
claves: ["me", "currentUser", "ponerUsuario", "cookie grada.sid", "httpOnly", "sameSite=lax", "secure"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[grada-colchonera]] · [[saas]] · [[sesión]] · [[ui]]

Al cargar la web, `ui.js` llama a `api.js.me()` → `GET /api/auth/me` (envía cookie `grada.sid`). El middleware `currentUser` lee la sesión (sid → userId), vuelve a cargar el usuario de BD y comprueba si sigue activo. Si activo → 200 con usuario; `api.js` llama a `ponerUsuario(usuario)` y la UI muestra cabecera con mote y avatar. Si no hay sesión, usuario eliminado o pendiente → 401; `ponerUsuario(null)` pone modo invitado.
En logout: `ui.js` llama `logout()` → `POST /api/auth/logout`. Servidor destruye la sesión en BD y borra la cookie. Responde 200; UI muestra aviso «Has cerrado sesión» y vuelve al inicio.

> W->>C: me() C->>A: GET /api/auth/me (cookie) A->>CU: Lee la sesión CU->>SS: sid → {userId} CU->>CU: Vuelve a cargar el usuario (¿sigue activo?) alt Activo A-->>C: 200 usuario C-->>W: ponerUsuario(usuario): cabecera con mote y avatar else Sin sesión, eliminado o pendiente A-->>C: 401 C-->>W: ponerUsuario(null): modo invitado end Note over W,A: Más tarde, «Salir» W->>C: logout() C->>A: POST /api/auth/logout A->>SS: Destruye la sesión y borra la cookie A-->>C: 200 C-->>W: Aviso «Has cerrado sesión» → inicio
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[gestion-de-sesiones-con-cookies-httponly-y-almacenamiento-en]] · [[login-local-con-cuenta-pendiente-y-reenvio-de-confirmacion-p]] · [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[control-de-acceso-basado-en-roles-y-propiedad-requireauth-re]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
