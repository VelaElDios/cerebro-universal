---
tipo: "concepto"
titulo: "Simulación determinista del juego (paso fijo 1/60 s, semilla)"
temas: ["determinismo", "juego", "survivor"]
claves: ["paso fijo", "semilla", "mundo.js", "reproducibilidad", "pruebas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/arquitectura.md"]
confianza: "verificado"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[determinismo]] · [[juego]] · [[survivor]]

La simulación pura (sin DOM ni audio) avanza con paso fijo y semilla, lo que permite probarla en Node sin navegador. Los eventos (oleada, aviso, jefe-derrotado, ambiente, ultra) se traducen a sonido y avisos en la presentación. Estadísticas de daño por fuente se guardan en mundo.stats para la pantalla de fin.
relacionado: Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi, Rendimiento del juego: búsqueda espacial por celdas, texturas cacheadas

> Determinismo. mundo.js avanza con un paso fijo de 1/60 s y un generador aleatorio con semilla. Si el navegador va lento, se hacen varios pasos por fotograma (con un tope); el resultado no depende de los FPS y las pruebas son reproducibles.
> — `repo:saas/docs/arquitectura.md`

Relacionado: [[motor-de-partida-determinista-a-paso-fijo-1-60-s-con-semilla]] · [[arquitectura-del-juego-simulacion-determinista-presentacion]] · [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
