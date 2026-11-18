---
tipo: "concepto"
titulo: "Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi"
temas: ["architecture", "game-engine", "grada-colchonera", "saas"]
claves: ["mundo.js", "paso fijo 1/60", "semilla", "determinismo", "eventos (oleada", "aviso", "jefe-derrotado", "ambiente", "ultra)", "mundo.stats", "celdas numéricas 4.5x", "textura suelo por celda/ambiente", "sprites cacheados", "Canvas 2D 3/4", "chibi 32x32", "capas píxel a píxel", "18 peinados", "6 barbas", "4 frames", "equipaciones 26 selecciones sin imágenes", "render-suelo.js", "render-paletas.js", "render-habilidades.js", "efectos.js RNG propio", "Web Audio pulse/triangle/noise", "secuenciador", "formantes vocales"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[architecture]] · [[game-engine]] · [[grada-colchonera]] · [[saas]]

**Separación simulación / presentación / servidor:**
- **Simulación pura (`mundo.js`):** bucle de paso fijo (1/60 s) con RNG semilla → determinista y reproducible. Si el frame tarda, ejecuta varios pasos (con tope). Módulos: `armas.js`, `combate.js`, `jefes.js`, `oleadas.js`/`rivales.js`, `terreno.js`, `ultras.js`/`ulti.js`, `mejoras.js`, `config.js` (todo el equilibrio).
- **Presentación (`juego.js`):** pantallas, bucle de render, `render.js`/`render-mundo.js`/`render-ultras.js`, `sprites.js` (chibi 32×32), `hud.js`, `audio.js`+`musica.js`, `club-ui.js`/`fin-ui.js`/`firma.js`, `entrada.js`.
- **Servidor:** `juegoService.js` → `club.js`, `config.js`, `logros.js`; expuesto vía `api.js` → `/api/juego`.
- **Eventos:** la simulación no toca DOM ni audio; emite eventos (`oleada`, `aviso`, `jefe-derrotado`, `ambiente`, `ultra`…) que `juego.js` traduce a sonido, avisos visuales y anuncios para lectores de pantalla.
- **Estadísticas:** cada fuente de daño (arma, ultra, ulti, quemaduras) se acumula en `mundo.stats` para la pantalla de fin.
- **Rendimiento:** búsqueda de obstáculos por celdas con claves numéricas (~4,5× más rápido), una textura de suelo por celda y ambiente pintada máx. una vez por fotograma y por adelantado, muñecos cacheados.
- **Dibujo chibi:** Canvas 2D cámara 3/4 (suelo aplastado vertical, muñecos de pie). Sprites generados por código en grid 32×32 (16×20 sin piernas hasta Fase 6): cabeza grande, cuerpo, zapatones. Pintado por capas píxel a píxel: zapatos, pantalón, torso, brazos, cabeza, cada una con contorno y luz superior-izquierda. 18 peinados, 6 barbas, mandíbula, complexión, estatura, gesto, gafas, cinta, guantes, brazalete… 4 frames de caminata. Equipaciones y 26 camisetas de selección generadas sin imágenes. Mapa (Fase 7) con píxeles de 2 unidades en `render-suelo.js`/`render-obstaculos.js`, paletas por ambiente en `render-paletas.js`, efectos de habilidades en `render-habilidades.js` (partículas con tope y RNG propio en `efectos.js` para que activar/desactivar no cambie la partida).
- **Audio:** todo sintetizado con Web Audio: ondas pulso (12,5%, 25%, 50%), triángulo, ruido. Música con secuenciador propio que programa notas por adelantado; grada usa voces con formantes de vocales y palmas.

> **Determinismo.** `mundo.js` avanza con un paso fijo de 1/60 s y un generador aleatorio con semilla. Si el navegador va lento, se hacen varios pasos por fotograma (con un tope); el resultado no depende de los FPS y las pruebas son reproducibles.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[modulos-del-backend-y-sus-responsabilidades]] · [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[audio-100-sintetizado-con-web-audio-ondas-pulso-triangulo-ru]] · [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]] · [[generacion-de-mundo-procedural-infinito-con-distritos-estadi]] · [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]] · [[motor-de-partida-determinista-a-paso-fijo-1-60-s-con-semilla]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
