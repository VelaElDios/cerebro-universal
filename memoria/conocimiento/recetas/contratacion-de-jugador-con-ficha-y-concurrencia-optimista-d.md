---
tipo: "receta"
titulo: "Contratación de jugador con ficha y concurrencia optimista (doble clic → 409)"
temas: ["concurrencia-optimista", "fichas", "grada-colchonera", "juego", "saas"]
claves: ["contratar", "juego_perfiles", "version", "UPDATE WHERE version", "409", "reintento"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[concurrencia-optimista]] · [[fichas]] · [[grada-colchonera]] · [[juego]] · [[saas]]

Dos peticiones simultáneas (doble clic) llaman a `juegoService.contratar()`.
1. Ambas leen `SELECT datos, version` → obtienen versión 7.
2. Cada una gasta 1 ficha y sortea jugador.
3. P1 ejecuta `UPDATE … WHERE version = 7` → 1 fila afectada, versión pasa a 8.
4. P2 ejecuta mismo `UPDATE WHERE version = 7` → 0 filas (versión cambió).
5. P2 reintenta: `SELECT` nuevo → versión 8, 0 fichas.
6. P2 recibe 409 «No tienes fichas de contrato»; P1 recibe 200 con fichado, logros nuevos y perfil actualizado.

> P1->>JS: contratar() P2->>JS: contratar() JS->>DB: SELECT datos, version (v = 7) JS->>DB: SELECT datos, version (v = 7) JS->>JS: P1: 1 ficha → sortea jugador JS->>JS: P2: 1 ficha → sortea jugador JS->>DB: P1: UPDATE … WHERE version = 7 → 1 fila (v = 8) JS->>DB: P2: UPDATE … WHERE version = 7 → 0 filas JS->>DB: P2 reintenta: SELECT (v = 8, 0 fichas) JS-->>P2: 409 «No tienes fichas de contrato» JS-->>P1: 200 {fichado, logrosNuevos, perfil}
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[perfil-de-juego-con-jsonb-y-concurrencia-optimista-mediante]] · [[validacion-anti-trampas-en-el-servidor-reloj-propio-formulas]] · [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]] · [[concurrencia-optimista-en-perfil-del-juego-version-en-juego]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
