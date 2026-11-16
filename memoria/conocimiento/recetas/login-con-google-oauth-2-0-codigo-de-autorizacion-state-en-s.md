---
tipo: "receta"
titulo: "Login con Google OAuth 2.0 (código de autorización, state en sesión)"
temas: ["auth", "google", "grada-colchonera", "oauth", "saas"]
claves: ["/api/auth/google", "state", "Workload Identity Federation", "client_secret", "loginWithOAuth", "email_verified"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[google]] · [[grada-colchonera]] · [[oauth]] · [[saas]]

1. Usuario pide `GET /api/auth/google`. Servidor genera `state` aleatorio (24 bytes hex), lo guarda en sesión (PostgreSQL) y redirige a Google con `client_id`, `redirect_uri`, `scope=email`, `state`.
2. Usuario inicia sesión en Google y acepta. Google redirige a `/api/auth/google/callback?code&state`.
3. Servidor compara `state` con el de la sesión y lo borra (un solo uso). Si falla → 303 con aviso `google-error` o `google-cancelado`.
4. Si `state` correcto: servidor intercambia `code` por token llamando a Google con `client_secret` (solo en servidor). Obtiene `email` y `email_verified`.
5. Llama a `userService.loginWithOAuth(google, email, verificado)`:
   - Si email no verificado → error → 303 `google-rechazado`.
   - Si no existía (o solo cuenta eliminada) → `create(active, provider google, sin contraseña)`.
   - Si existía pendiente → `update(status active)`.
6. Regenera sesión con `userId` y redirige a `/?aviso=google-cuenta-creada` (nueva) o `google-ok#/jugar` (existente).

> U->>A: GET /google A->>SS: state aleatorio (24 bytes en hexadecimal) A-->>U: 303 → accounts.google.com (client_id, redirect_uri, scope email, state) U->>G: Inicia sesión y acepta G-->>U: 302 → /api/auth/google/callback?code&state U->>A: GET /google/callback?code&state A->>SS: Compara el state y lo borra (un solo uso) alt state falso, ausente o reutilizado / el usuario canceló A-->>U: 303 → /?aviso=google-error | google-cancelado else state correcto A->>G: POST token (code + client_secret, desde el servidor) G-->>A: id del perfil: email y email_verified A->>S: loginWithOAuth(google, email, verificado) alt Email sin verificar S-->>A: error → 303 aviso=google-rechazado else No existía (o solo había una cuenta eliminada) S->>R: create(active, provider google, sin contraseña) else Existía pendiente S->>R: update(status active) end A->>SS: Regenera la sesión con userId A-->>U: 303 → /?aviso=google-cuenta-creada | google-ok#/jugar
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[maquina-de-estados-de-la-cuenta-de-usuario]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
