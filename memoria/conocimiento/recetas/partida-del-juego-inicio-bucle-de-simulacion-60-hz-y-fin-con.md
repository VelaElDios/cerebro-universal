---
tipo: "receta"
titulo: "Partida del juego: inicio, bucle de simulación (60 Hz) y fin con validación anti-trampas (servidor)"
temas: ["anti-cheat", "concurrencia-optimista", "grada-colchonera", "juego", "saas", "simulación"]
claves: ["iniciarPartida", "finalizarPartida", "juegoService", "juegoRepository", "perfil + version", "reloj del servidor", "límites creíbles", "logros verificables", "concurrencia optimista", "guardarPerfil", "guardarRecord"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[anti-cheat]] · [[concurrencia-optimista]] · [[grada-colchonera]] · [[juego]] · [[saas]] · [[simulación]]

1. **Inicio**: Jugador elige personaje y entrenador. Frontend (`juego.js`) llama `api.iniciar()` → `POST /partidas`. `juegoService.iniciarPartida()` lee `perfil + version` del repo, verifica que el personaje está en la plantilla, crea `partidaActual = {id, inicio = reloj del servidor}`, guarda perfil con versión (optimista) y devuelve 201 con `partidaId` y stats de entrenamiento.
2. **Bucle**: Cada fotograma (paso fijo 1/60 s) el frontend pasa la entrada a `mundo.js` (simulación), recibe eventos (oleada, jefe, mejora, logro…), dibuja HUD, sonido y música.
3. **Fin**: Simulación emite estado fin. Frontend llama `terminar(id, tiempo, nivel, jefes, bajas, logros)` → `POST /partidas/:id/fin`. `juegoService.finalizarPartida()` valida:
   - ¿Es la partida en curso?
   - ¿`tiempo ≤ transcurrido + 15 s` (margen de red)?
   - ¿Jefes, nivel y bajas son creíbles?
   Si no → 400 «El resultado no es creíble».
   Si válido: reparte jefes, bajas, puntos, fichas; logros creíbles + logros de plantilla; `guardarPerfil(version)` con reintento si otra petición ganó (optimista); `guardarRecord()` si es su mejor partida. Devuelve 200 con recompensas, logros nuevos, record y perfil actualizado.

> J->>G: Jugar (jugador y entrenador elegidos) G->>C: iniciar(personaje, entrenador) C->>A: POST /partidas A->>JS: iniciarPartida() JS->>R: perfil + version JS->>JS: ¿Está en tu plantilla? partidaActual = {id, inicio = reloj del servidor} JS->>R: guardarPerfil(version) A-->>G: 201 {partidaId, stats de entrenamiento} loop Cada fotograma (paso fijo 1/60 s) G->>SIM: avanzar(entrada) SIM-->>G: eventos (oleada, jefe, mejora, logro…) G->>G: Dibujo, HUD, sonido y música end SIM-->>G: estado fin (te eliminan) G->>C: terminar(id, tiempo, nivel, jefes, bajas, logros) C->>A: POST /partidas/:id/fin A->>JS: finalizarPartida() JS->>JS: ¿Es la partida en curso? ¿tiempo ≤ transcurrido + 15 s? ¿jefes, nivel y bajas creíbles? alt Resultado imposible JS-->>A: 400 «El resultado no es creíble» else Válido JS->>JS: Reparte jefes, bajas, puntos y fichas logros creíbles + logros de plantilla JS->>R: guardarPerfil(version) (reintenta si otra petición ganó) JS->>R: guardarRecord() si es su mejor partida A-->>G: 200 {recompensas, logrosNuevos, record, perfil} G->>J: Pantalla de fin con estadísticas y logros
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[perfil-de-juego-con-jsonb-y-concurrencia-optimista-mediante]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
