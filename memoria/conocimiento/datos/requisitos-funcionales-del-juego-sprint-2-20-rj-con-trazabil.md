---
tipo: "dato"
titulo: "Requisitos funcionales del juego (Sprint 2) — 20 RJ con trazabilidad"
temas: ["grada-colchonera", "juego", "requisitos", "saas", "sprint"]
claves: ["RJ-01 a RJ-20", "PBI", "mundo.js", "oleadas.js", "sprites.js", "rivales.js", "jefes.js", "club.js", "ultras.js", "logros.js"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[juego]] · [[requisitos]] · [[saas]] · [[sprint]]

Tabla completa de 20 requisitos funcionales del juego (Sprint 2) con trazabilidad a PBIs, archivos de implementación y suites de prueba. Cubre: entrada al juego ligada a sesión (RJ-01), bucle survivor infinito con oleadas/XP/mejoras (RJ-02), pixel art generado por código y cámara isométrica 3/4 (RJ-03), 36 jugadores + 2 entrenadores con stats/habilidades/rareza/ulti (RJ-04), armas automáticas 5 niveles + pasivas + skills por minuto (RJ-05), rivales con IA variada (RJ-06), jefes 3 fases con mecánicas especiales (RJ-07), mundo procedural con colisiones exactas (RJ-08), ambientes dinámicos cada 5 min (RJ-09), input multiplataforma + pausa/pantalla completa/ajustes (RJ-10), guardado de club con anti-cheat servidor (RJ-11), fichaje por fichas de contrato sorteadas por rareza (RJ-12), entrenamiento con puntos (RJ-13), ranking anonimizado (RJ-14), combinaciones/ULTRAS con pantalla dedicada (RJ-15), modo pruebas solo admin (RJ-16), mote+avatar único (RJ-17), logros históricos validados en servidor + equipaciones (RJ-18), pantalla fin con stats detalladas (RJ-19), audio chiptune sintetizado con controles (RJ-20). Los PBIs y criterios de aceptación completos están en `docs/gestion/README.md`.

> | Id | Requisito | PBI | Dónde se cumple | Pruebas |
|---|---|---|---|---|---|
| RJ-01 | Con sesión, el inicio es el menú del juego; sin sesión no se juega y el progreso va ligado a la cuenta | P20, P29 | `ui.js` (ruta `#/jugar`), `requireAuth` en `/api/juego`, tablas `juego_perfiles` y `juego_records` | `api.juego`, `frontend` |
| RJ-02 | Partida *survivor* infinita: oleadas, experiencia, mejoras al subir de nivel y dificultad creciente | P21, P24, P34 | `mundo.js`, `oleadas.js`, `mejoras.js`, `config.js` | `game`, `juego-personajes`, `juego-club` |
| RJ-03 | Gráficos pixel art generados por código y cámara 3/4 | P22, P45 | `sprites.js`, `render.js`, `render-mundo.js` | `juego-movilidad`, `juego-habilidades` |
| RJ-04 | Elegir jugador (36, con estadísticas por posición, habilidades propias y rareza por historia) y entrenador (2, con ulti) | P23, P38 | Vestuario y Dirección (`juego.js`), `config.js`, `ulti.js` | `juego-personajes`, `juego-club` |
| RJ-05 | Armas automáticas con 5 niveles, pasivas y habilidades que solo suben a partir de cierto minuto | P24, P39 | `armas.js`, `mejoras.js`, `combate.js` | `juego-habilidades` |
| RJ-06 | Rivales con comportamiento propio (embisten, disparan, rodean obstáculos, élites) | P25 | `rivales.js`, `oleadas.js` | `juego-movilidad`, `juego-personajes` |
| RJ-07 | Jefes con tres fases, avisos de ataque, escolta, furia y jugada estrella | P26, P46 | `jefes.js`, `oleadas.js` | `juego-movilidad`, `juego-logros` |
| RJ-08 | Mundo procedural con terreno, obstáculos macizos y colisiones exactas | P27, P35, P41 | `terreno.js`, `mundo.js` | `juego-movilidad` |
| RJ-09 | Ambientes que cambian cada 5 minutos (de la pretemporada a la Final del Mundial) | P36 | `config.js`, `render-mundo.js`, `musica.js` | `juego-movilidad` |
| RJ-10 | Jugable con teclado, ratón y pantalla táctil; pausa, pantalla completa y ajustes | P28 | `entrada.js`, `ajustes.js`, `juego.js` | `game`, `frontend` |
| RJ-11 | Club guardado en el servidor con validación anti-trampas de cada partida | P29 | `juegoService.finalizarPartida`, migración `003` | `api.juego`, `juegoRepository` |
| RJ-12 | Fichar jugadores con fichas de contrato (una por cada 3 jefes), sorteadas por rareza | P30, P38 | `club.js`, `POST /api/juego/contratar`, `firma.js` | `juego-club`, `api.juego`, `frontend` |
| RJ-13 | Entrenar a los jugadores con puntos ganados por bajas y jefes | P31 | `club.js`, `POST /api/juego/entrenar` | `juego-club`, `api.juego` |
| RJ-14 | Ranking de la grada con la mejor partida de cada usuario (sin mostrar el correo) | P32 | `juego_records`, `GET /api/juego/ranking` | `api.juego`, `juegoRepository` |
| RJ-15 | Combinaciones y ULTRAS, con una pantalla que muestra lo que pide cada una | P33, P40 | `ultras.js`, `render-ultras.js`, pantalla Combinaciones | `juego-ultras`, `juego-habilidades`, `frontend` |
| RJ-16 | Modo pruebas solo para administradores | P34 | `POST /api/juego/desbloquear`, `scripts/desbloquear-juego.js` | `api.juego` |
| RJ-17 | Mote único y avatar, en la cabecera, Mi cuenta y el ranking | P37 | `PUT /api/juego/identidad`, migración `004` | `api.juego`, `juegoRepository`, `frontend` |
| RJ-18 | Logros con datos de la historia del Atleti, validados en el servidor, y equipaciones desbloqueables | P42 | `logros.js`, `juegoService` | `juego-logros`, `api.juego` |
| RJ-19 | Pantalla de fin con estadísticas y daño por habilidad | P43 | `fin-ui.js`, `combate.js` | `juego-logros` |
| RJ-20 | Música chiptune, efectos y la grada, con ajustes de volumen | P44 | `audio.js`, `musica.js`, `ajustes.js` | `juego-logros` |
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]] · Diagramas de secuencia con pgf-umlsd · [[tabla-de-trazabilidad-sprint-2-pbi-etiqueta-titulo-tareas-pr]] · [[estructura-sprint-2-6-fases-calidad-29-pbis-50-tareas-fechas]] · [[evolucion-por-fases-del-sprint-2-etiquetas-donetonic-adicion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
