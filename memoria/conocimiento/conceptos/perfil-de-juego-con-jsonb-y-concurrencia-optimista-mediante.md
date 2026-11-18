---
tipo: "concepto"
titulo: "Perfil de juego con JSONB y concurrencia optimista mediante versión"
temas: ["grada-colchonera", "juego", "modelo-datos", "saas"]
claves: ["juego_perfiles", "JSONB", "version", "concurrencia optimista", "datos", "plantilla", "contadores", "logros", "partidaActual"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[juego]] · [[modelo-datos]] · [[saas]]

Tabla `juego_perfiles`: `user_id` PK/FK a `users`. `datos` JSONB contiene: plantilla (`jugadores` con jefes, bajas, partidas, stats entrenamiento), contadores (`jefesTotal`, `partidas`, `contratos`), logros con fecha, y `partidaActual` en curso. `version` integer que incrementa en cada escritura para concurrencia optimista: dos peticiones simultáneas no pueden sobrescribirse; la que llega segunda falla y debe reintentar con datos frescos. `updated_at` timestamp.

> juego_perfiles.datos (JSONB): plantilla (jugadores con jefes, bajas, partidas y estadísticas de entrenamiento), contadores (jefesTotal, partidas, contratos), logros con su fecha y la partida en curso (partidaActual). version sube en cada escritura (concurrencia optimista).
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[tabla-users-con-indice-parcial-unico-para-email-entre-cuenta]] · [[gestion-de-sesiones-con-cookies-httponly-y-almacenamiento-en]] · [[maquina-de-estados-de-la-cuenta-de-usuario]] · [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]] · [[contratacion-de-jugador-con-ficha-y-concurrencia-optimista-d]] · [[esquema-de-progreso-guardado-en-servidor-migracion-003-tabla]] · [[validacion-anti-trampas-en-el-servidor-reloj-propio-formulas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
