---
tipo: "receta"
titulo: "Simulación de paso fijo con semilla (mundo.js)"
temas: ["donetonic", "grada-colchonera", "saas", "scrum"]
claves: ["simulación", "paso fijo", "semilla", "mundo.js", "P21", "T35"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[donetonic]] · [[grada-colchonera]] · [[saas]] · [[scrum]]

Tarea T35 (PBI P21) implementa el bucle de simulación determinista con paso de tiempo fijo y semilla para reproducibilidad. El código reside en `mundo.js` y se fusionó en PR #36 (Fase 1, 23/10/2026). Permite que la lógica del juego (movimiento, colisiones, IA) sea idéntica en cliente y servidor, facilitando la validación anti-trampas y el rebobinado.

> P21 | T35 | Simulación de paso fijo con semilla (mundo.js) | [#36](https://github.com/VelaElDios/la-grada-colchonera-saas/pull/36) | Hecho
> — `repo:saas/docs/gestion/README.md`

Relacionado: [[generacion-de-terreno-por-ruidos-terreno-js]] · [[motor-de-partida-determinista-a-paso-fijo-1-60-s-con-semilla]] · [[generacion-de-mundo-procedural-infinito-con-distritos-estadi]] · [[simulacion-determinista-del-juego-paso-fijo-1-60-s-semilla]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
