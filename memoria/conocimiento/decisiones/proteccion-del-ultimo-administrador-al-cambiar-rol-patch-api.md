---
tipo: "decision"
titulo: "Protección del último administrador al cambiar rol (PATCH /api/users/:id/role) y al darse de baja (DELETE /api/users/:id)"
temas: ["auth", "grada-colchonera", "integridad", "rbac", "saas"]
claves: ["changeRole", "findAll", "ForbiddenError", "último administrador", "requireSelfOrRole", "deleteUser", "status deleted", "deleted_at", "baja lógica", "juegoService.olvidarCuenta"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[grada-colchonera]] · [[integridad]] · [[rbac]] · [[saas]]

Dos operaciones protegen al último administrador activo:
1. **Cambio de rol** (`PATCH /api/users/:id/role`): `userService.changeRole` cuenta administradores activos con `findAll()`. Si el objetivo es el último → `ForbiddenError` «Debe quedar al menos un administrador» → 403. Si hay más → `update(id, role user)` → 200 y log `user.role_changed`.
2. **Baja de usuario** (`DELETE /api/users/:id` con `requireSelfOrRole('admin')`): `userService.deleteUser` verifica si es el último admin → 403. Si no, marca `status = 'deleted'`, `deleted_at = now()`, suelta el mote (baja lógica), llama a `juegoService.olvidarCuenta(id)` para sacarle del ranking, devuelve 204 y log `user.deleted`. La sesión deja de ser válida en la siguiente petición porque `currentUser` no acepta usuarios no activos.

> U->>V: «Eliminar mi cuenta» V->>D: ¿Eliminar tu cuenta? U->>D: Sí, eliminar D->>A: DELETE (requireSelfOrRole('admin')) A->>S: deleteUser(actor, id) alt Es el último administrador S-->>A: 403 else S->>S: status deleted, deleted_at = ahora, suelta el mote (baja lógica) A->>A: juegoService.olvidarCuenta(id): sale del ranking A-->>V: 204 (log user.deleted) → aviso y vuelta al inicio Note over A: La sesión deja de valer en la siguiente petición (currentUser ya no la acepta)
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[maquina-de-estados-de-la-cuenta-de-usuario]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
