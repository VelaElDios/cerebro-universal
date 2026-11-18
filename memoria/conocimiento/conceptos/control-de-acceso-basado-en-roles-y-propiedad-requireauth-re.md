---
tipo: "concepto"
titulo: "Control de acceso basado en roles y propiedad (requireAuth, requireRole, requireSelfOrRole)"
temas: ["auth", "autorizacion", "grada-colchonera", "middlewares", "procesos", "saas"]
claves: ["requireAuth", "requireRole", "requireSelfOrRole", "401 UNAUTHENTICATED", "403 FORBIDDEN", "último administrador"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[autorizacion]] · [[grada-colchonera]] · [[middlewares]] · [[procesos]] · [[saas]]

Tres middlewares en cadena (definidos en `src/api/currentUser.js`):
1. `requireAuth` → verifica sesión válida (`req.user` existe). Si no: `401 { code: 'UNAUTHENTICATED' }`.
2. `requireRole('admin')` → exige `req.user.role === 'admin'`. Si no: `403 { code: 'FORBIDDEN' }`.
3. `requireSelfOrRole('admin')` → permite si `req.user.id === params.id` O `role === 'admin'`. Usado en `DELETE /api/users/:id`.
Regla de negocio adicional en `userService.deleteUser`: nunca se elimina al último admin (cuenta y lanza error).
Frontend (`ui.js`) solo oculta botones/enlaces; la seguridad real está en el servidor.

> `requireAuth` (`401`), `requireRole` y `requireSelfOrRole` (`403`). La interfaz solo oculta los enlaces
> — `repo:saas/docs/revision-entrega.md`

Relacionado: [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[gestion-de-sesiones-con-cookies-httponly-y-almacenamiento-en]] · [[modulos-del-backend-y-sus-responsabilidades]] · [[proteccion-del-ultimo-administrador-al-cambiar-rol-patch-api]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
