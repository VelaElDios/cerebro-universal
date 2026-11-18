---
tipo: "concepto"
titulo: "Audio 100% sintetizado con Web Audio (ondas pulso, triángulo, ruido, secuenciador, formantes vocales para grada)"
temas: ["audio", "game-engine", "grada-colchonera", "saas"]
claves: ["audio.js", "musica.js", "Web Audio", "pulse 12.5% 25% 50%", "triangle", "noise", "secuenciador propio", "notas programadas adelantado", "grada formantes vocales palmas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[audio]] · [[game-engine]] · [[grada-colchonera]] · [[saas]]

**Motor de audio sin samples:**
- **Síntesis**: Web Audio API. Generadores: onda pulso (duty cycle 12,5%, 25%, 50%), triángulo, ruido blanco/rosa.
- **Música**: secuenciador propio (`musica.js`) que programa las notas con antelación (schedule) para timing preciso. Una canción por ambiente que evoluciona con el tiempo y la presencia de jefes; fanfarria distinta por competición.
- **Grada**: síntesis de voces mediante formantes de vocales (A, E, I, O, U) + muestras de palmas; volumen y densidad según distancia a las gradas del mapa.
- **Efectos**: todos sintetizados (disparos, impactos, menús, ultis). Sin archivos de audio → peso cero, latencia nula, determinismo total.

> **Audio.** Todo sintetizado con Web Audio: ondas de pulso (12,5 %, 25 % y 50 %), triángulo y ruido. La música es un secuenciador propio que programa las notas por adelantado; la grada usa voces con formantes de vocales y palmas.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[arquitectura-del-juego-simulacion-determinista-presentacion]] · [[generacion-de-mundo-procedural-infinito-con-distritos-estadi]] · [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]] · [[musica-100-sintetizada-web-audio-con-fanfarrias-por-competic]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
