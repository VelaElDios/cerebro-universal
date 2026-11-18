---
tipo: "decision"
titulo: "Arquitectura en capas con inyección de dependencias permitió cambios sin tocar lógica"
temas: ["arquitectura", "grada-colchonera", "saas"]
claves: ["arquitectura en capas", "inyección de dependencias", "PostgreSQL", "correo", "Google", "juego"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[arquitectura]] · [[grada-colchonera]] · [[saas]]

Decisión: usar arquitectura en capas con inyección de dependencias (DI).
Beneficio demostrado: permitió 3 cambios mayores sin modificar lógica de negocio:
1. Cambio de almacenamiento en memoria a PostgreSQL.
2. Añadir autenticación por correo (confirmación, reenvío, HMAC) y OAuth 2.0 con Google.
3. Montar el juego completo (simulación determinista, procedural, audio) sobre la misma base.
La DI desacopla implementaciones concretas (repositorios, servicios de email, auth) de los casos de uso.

> La **arquitectura en capas con inyección de dependencias** permitió cambiar de memoria a PostgreSQL, añadir correo y Google o montar un juego entero encima sin tocar la lógica existente.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]] · [[decisiones-de-diseno-del-backend-con-alternativas-y-justific]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
