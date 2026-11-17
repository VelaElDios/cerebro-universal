---
tipo: "receta"
titulo: "Música 100 % sintetizada (Web Audio) con fanfarrias por competición y grada reactiva"
temas: ["audio", "chiptune", "donetonic", "grada-colchonera", "procedural-audio", "scrum", "web-audio"]
claves: ["fanfarria", "canción de fondo", "grada murmura", "volumen música separado", "P44"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-17"
---

Temas: [[audio]] · [[chiptune]] · [[donetonic]] · [[grada-colchonera]] · [[procedural-audio]] · [[scrum]] · [[web-audio]]

- Motor de audio: Web Audio API (OscillatorNode, GainNode, ScriptProcessor/AudioWorklet para secuenciación).
- Fanfarria distinta al entrar en cada final (Pretemporada, Copa, Liga, Champions, Mundial).
- Canción de fondo (loop) que añade capas/arpegios según minutos transcurridos y número de jefes vencidos.
- Grada: generador de formantes vocales (ruido filtrado + envolventes) que sube volumen y complejidad al acercarse a gradas del mapa.
- Controles: slider música independiente de slider efectos; persistido en localStorage (P28).

> - Fanfarria propia por competición y canción de fondo que se anima con el tiempo y con los jefes. - La grada murmura y canta cuando te acercas a ella. - Volumen de música aparte del de efectos; todo sintetizado (sin ficheros).
> — `repo:saas/docs/gestion/README.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
