---
tipo: "concepto"
titulo: "Cadena de middlewares para petición protegida y autorización por roles (requireAuth, requireRole)"
temas: ["auth", "grada-colchonera", "middleware", "rbac", "saas"]
claves: ["requestLogger", "currentUser", "requireAuth", "requireRole", "401 UNAUTHENTICATED", "403 FORBIDDEN", "X-Request-Id"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[grada-colchonera]] · [[middleware]] · [[rbac]] · [[saas]]

La petición entra con cabecera `X-Request-Id`. `requestLogger` pasa a `currentUser` que carga `req.user` (usuario activo de la sesión o null). `requireAuth` verifica `req.user`: si null → 401 UNAUTHENTICATED. Si existe, pasa a `requireRole('admin')`: si rol `user` → 403 FORBIDDEN (log `auth.forbidden`); si rol `admin` → continúa al handler `GET /api/users` que llama a `userService.listUsers()` y devuelve usuarios sin datos sensibles (200). Finalmente `requestLogger` registra log `http.request` con método, ruta, estado, ms y usuario.

> C->>RL: GET /api/users (X-Request-Id) RL->>CU: siguiente CU->>CU: req.user = usuario activo de la sesión o null CU->>RA: siguiente alt req.user es null RA-->>C: 401 UNAUTHENTICATED else RA->>RR: siguiente alt rol user RR-->>C: 403 FORBIDDEN (log auth.forbidden) else rol admin RR->>H: siguiente H->>S: listUsers() S-->>H: usuarios sin datos sensibles H-->>C: 200 end end RL->>RL: log http.request (método, ruta, estado, ms, usuario)
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[control-de-acceso-basado-en-roles-y-propiedad-requireauth-re]] · [[gestion-de-sesiones-con-cookies-httponly-y-almacenamiento-en]] · [[modulos-del-backend-y-sus-responsabilidades]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
