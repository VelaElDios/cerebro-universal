---
tipo: "dato"
titulo: "Esquema de progreso guardado en servidor (migración 003, tablas y API)"
temas: ["api", "backend", "base-datos", "donetonic", "grada-colchonera", "scrum", "seguridad"]
claves: ["juego_perfiles", "juego_records", "migracion 003", "/api/juego", "anti-cheat", "optimistic concurrency", "P29"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[api]] · [[backend]] · [[base-datos]] · [[donetonic]] · [[grada-colchonera]] · [[scrum]] · [[seguridad]]

- Migración 003 crea:
  - juego_perfiles: perfil de club del usuario (plantilla, puntos, stats, identidad).
  - juego_records: cada partida terminada (tiempo, nivel, bajas, jefes, daño, ambiente, semilla, etc.).
- Endpoints protegidos con requireAuth:
  - GET /api/juego/perfil → devuelve perfil completo.
  - POST /api/juego/empezar → devuelve semilla y estado inicial (servidor genera semilla).
  - POST /api/juego/terminar → recibe resultado, valida con reloj servidor (anti-cheat: tiempo mínimo, stats máximos teóricos), guarda en juego_records y actualiza perfil.
- Concurrencia optimista: cada fila tiene version (integer); UPDATE ... WHERE version = X; si falla, reintenta con versión fresca.

> Tablas juego_perfiles y juego_records (migración 003) ligadas al usuario. API /api/juego protegida con sesión: perfil, empezar y terminar partida. El servidor valida cada resultado con su propio reloj (anti-trampas) y rechaza resultados imposibles. Concurrencia optimista: dos peticiones a la vez no se pisan.
> — `repo:saas/docs/gestion/README.md` (cita sin comprobar)

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[validacion-anti-trampas-en-el-servidor-reloj-propio-formulas]] · [[api-del-juego-con-validacion-anti-trampas]] · [[validacion-anti-trampas-en-servidor-con-reloj-propio-y-recha]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
