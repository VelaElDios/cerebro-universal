---
tipo: "concepto"
titulo: "Concurrencia optimista en perfil del juego (version en juego_perfiles)"
temas: ["base de datos", "concurrencia", "juego", "postgresql", "saas"]
claves: ["concurrencia optimista", "version", "juego_perfiles", "UPDATE WHERE version"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/arquitectura.md"]
confianza: "verificado"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[base de datos]] · [[concurrencia]] · [[juego]]

Al contratar, dos peticiones simultáneas leen la misma versión; la primera escribe y la segunda falla (0 filas), se reintenta con datos nuevos (ya sin fichas) y devuelve 409. Esto evita bloqueos y permite escalar.
relacionado: Servidor del juego y anti-trampas, Diagrama de secuencia contratar (fig:sec-contratar)

> Cada cambio del perfil usa concurrencia optimista (UPDATE … WHERE version = $n) con reintentos.
> — `repo:saas/docs/arquitectura.md`

## Ampliación (2026-11-22, memoria-procesos)
Implementado en juegoService.js para contratar, entrenar, identidad, finalizarPartida. El diagrama de secuencia fig:sec-contratar muestra el caso de doble clic: P1 escribe v7→v8, P2 falla en v7, reintenta con v8 (sin fichas) y recibe 409.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
