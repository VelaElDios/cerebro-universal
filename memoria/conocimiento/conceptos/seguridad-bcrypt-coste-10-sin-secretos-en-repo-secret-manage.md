---
tipo: "concepto"
titulo: "Seguridad: bcrypt coste 10, sin secretos en repo, Secret Manager en Cloud Run"
temas: ["bcrypt", "grada-colchonera", "procesos", "saas", "secret-manager", "seguridad", "variables-entorno"]
claves: ["bcryptjs", "coste 10", "loadConfig.js", ".env.example", "Secret Manager", "Cloud Run"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[bcrypt]] · [[grada-colchonera]] · [[procesos]] · [[saas]] · [[secret-manager]] · [[seguridad]] · [[variables-entorno]]

- Contraseñas: `bcryptjs` con coste 10 (`passwordHasher.js`). Hash nunca sale por API; logs lo ocultan.
- Configuración: `src/loadConfig.js` valida variables obligatorias al arranque; lanza error si falta alguna → la app no inicia.
- `.env.example` lista nombres sin valores (comprometido en repo).
- Local: `.env` en `.gitignore`.
- Producción (Cloud Run): variables inyectadas desde Secret Manager vía Workload Identity Federation (sin claves de servicio en repo).
- Render mantenido como alternativa con `render.yaml`.

> Solo variables de entorno: Secret Manager en Cloud Run y `.env` (ignorado por git) en local. En producción la aplicación no arranca si falta un secreto
> — `repo:saas/docs/revision-entrega.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
