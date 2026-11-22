---
tipo: "decision"
titulo: "Motor de partida determinista a paso fijo 1/60 s con semilla"
temas: ["arquitectura", "donetonic", "grada-colchonera", "scrum", "simulacion"]
claves: ["fixed timestep", "seeded random", "1/60 s", "determinista", "P21"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[arquitectura]] · [[donetonic]] · [[grada-colchonera]] · [[scrum]] · [[simulacion]]

La partida se simula en un bucle fijo de 1/60 s (≈16,67 ms) sin depender del DOM ni de requestAnimationFrame. El generador de números aleatorios usa una semilla inicial; dada la misma semilla, la partida es idéntica (determinismo total). Esto permite:
- Reproducción exacta de partidas para debugging, replays o validación servidor.
- Sincronización cliente-servidor sin desvíos.
- Pausa automática al cambiar de pestaña (Page Visibility API) sin romper la simulación.
El paso fijo también simplifica la física y la IA de rivales/jefes.

> Simulación pura (sin DOM) con paso fijo de 1/60 s y azar con semilla: misma semilla, misma partida.
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[simulacion-de-paso-fijo-con-semilla-mundo-js]] · [[arquitectura-del-juego-simulacion-determinista-presentacion]] · [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]] · [[simulacion-determinista-del-juego-paso-fijo-1-60-s-semilla]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
