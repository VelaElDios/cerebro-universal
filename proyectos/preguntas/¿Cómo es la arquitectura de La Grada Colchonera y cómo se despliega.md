Pregunta de prueba (la dejó Claude para comprobar que funciona): explica la arquitectura de La Grada Colchonera y cómo se despliega.


## Respuesta del cerebro (2026-11-17 14:18 · nvidia-revisor · nvidia/nemotron-3-ultra-550b-a55b)

# Arquitectura y despliegue de La Grada Colchonera

## Respuesta corta
**Arquitectura:** Cliente-servidor en capas (navegador → API Express → servicios → repositorios → PostgreSQL Neon) con el frontend servido desde el mismo origen. El juego separa **simulación determinista** (bucle fijo 1/60 s, RNG con semilla) de **presentación por eventos** (canvas 2D, Web Audio 100 % sintetizado).  
**Despliegue:** Cloud Run (región `europe-southwest1`), URL pública `https://la-grada-colchonera-1081564062572.europe-southwest1.run.app`. Ramificación **GitHub Flow**: `main` = estable y se despliega automático; hitos en ramas `hito-N/integración` y tareas en `hito-N/Tx-descripción`.

---

## Detalle

### 1. Arquitectura general (capas backend + frontend mismo origen)
- **Navegador (cliente):**  
  - UI: `ui.js` + `ui/` + `vistas/` → cliente API único `api.js` (fetch, timeout 15 s, errores `ApiError`, renovación de sesión) [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].  
  - GAME: `game/` (canvas, Web Audio) → mismo `api.js`.  
  - Comunicación: HTTP + JSON + cookie de sesión (mismo origen → sin CORS) [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].

- **Servidor Node.js + Express (7 capas con prohibiciones explícitas):**  
  1. **Presentación** (`public/`): pinta vistas, valida formularios, gestiona juego; **no** accede a BD ni decide permisos [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].  
  2. **Cliente API** (`public/js/api.js`): único `fetch`; **no** pinta nada [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].  
  3. **API** (`src/api/`): rutas, sesión, auth/roles, logs, formato errores; **no** reglas de negocio [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].  
  4. **Lógica** (`src/services/`): reglas puras (usuarios, confirmación, tokens, juego); **no** conoce HTTP ni SQL [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].  
  5. **Datos** (`src/repositories/`): guardar/leer en memoria o PostgreSQL (Neon) con mismo contrato; **no** valida reglas [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].  
  6. **Integraciones** (`src/integrations/`): correo (SMTP Gmail) y Google OAuth 2.0; **no** decide nada [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].  
  7. **Composición** (`src/app.js`, `src/bootstrap.js`): conecta capas, elige BD, migra, crea primer admin [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].

- **Verificación de capas:** `src/api/` → `src/services/` → `src/repositories/`; la lógica recibe el repo por parámetro (testable en memoria) [[arquitectura-en-capas-cliente-servidor-verificada-api-logica|Arquitectura en capas cliente-servidor verificada (API → lógica → datos)]].

- **Base de datos:** PostgreSQL en **Neon** [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].

- **Reglas compartidas (juego):** `club.js`, `config.js`, `logros.js` usadas tanto en servidor como en cliente [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].

### 2. Arquitectura del juego (simulación / presentación / servidor)
- **Simulación pura (`mundo.js`):**  
  - Bucle de paso fijo **1/60 s** con **RNG semilla** → determinista y reproducible [[arquitectura-del-juego-simulacion-determinista-presentacion|Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi]].  
  - Módulos: `armas.js`, `combate.js`, `jefes.js`, `oleadas.js`/`rivales.js`, `terreno.js`, `ultras.js`/`ulti.js`, `mejoras.js`, `config.js` (equilibrio) [[arquitectura-del-juego-simulacion-determinista-presentacion|Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi]].

- **Presentación (`juego.js`):**  
  - Pantallas, bucle de render, `render.js`/`render-mundo.js`/`render-ultras.js`, `sprites.js` (chibi 32×32), `hud.js`, `audio.js`+`musica.js`, `club-ui.js`/`fin-ui.js`/`firma.js`, `entrada.js` [[arquitectura-del-juego-simulacion-determinista-presentacion|Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi]].

- **Servidor de juego:** `juegoService.js` → `club.js`, `config.js`, `logros.js`; expuesto vía `api.js` → `/api/juego` [[arquitectura-del-juego-simulacion-determinista-presentacion|Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi]].

- **Eventos (desacoplamiento):** la simulación **no toca DOM ni audio**; emite eventos (`oleada`, `aviso`, `jefe-derrotado`, `ambiente`, `ultra`…) que `juego.js` traduce a sonido, avisos visuales y anuncios para lectores de pantalla [[arquitectura-del-juego-simulacion-determinista-presentacion|Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi]].

- **Rendimiento:** búsqueda de obstáculos por celdas con claves numéricas (~4,5× más rápido), una textura de suelo por celda, ambiente pintada máx. 1 vez/fotograma y por adelantado, muñecos cacheados [[arquitectura-del-juego-simulacion-determinista-presentacion|Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi]].

- **Dibujo chibi:** Canvas 2D cámara 3/4 (suelo aplastado vertical, muñecos de pie). Sprites generados por código en grid 32×32 (16×20 sin piernas hasta Fase 6): cabeza grande, cuerpo, zapatones. Pintado por capas píxel a píxel (zapatos, pantalón, torso, brazos, cabeza, cada una con contorno y luz sup.-izq.). 18 peinados, 6 barbas, mandíbula, complexión, estatura, gesto, gafas, cinta, guantes, brazalete… 4 frames de caminata. Equipaciones y 26 camisetas de selección generadas sin imágenes. Mapa (Fase 7) con píxeles de 2 unidades en `render-suelo.js`/`render-obstaculos.js`, paletas por ambiente en `render-paletas.js`, efectos de habilidades en `render-habilidades.js` (partículas con tope y RNG propio en `efectos.js` para que activar/desactivar no cambie la partida) [[arquitectura-del-juego-simulacion-determinista-presentacion|Arquitectura del juego: simulación determinista, presentación por eventos, rendimiento y renderizado chibi]].

- **Audio 100 % sintetizado (Web Audio):**  
  - Síntesis: onda pulso (duty 12,5 %, 25 %, 50 %), triángulo, ruido blanco/rosa [[audio-100-sintetizado-con-web-audio-ondas-pulso-triangulo-ru|Audio 100% sintetizado con Web Audio (ondas pulso, triángulo, ruido, secuenciador, formantes vocales para grada)]].  
  - Música: secuenciador propio (`musica.js`) que programa notas con antelación (schedule) para timing preciso; una canción por ambiente que evoluciona con el tiempo y jefes; fanfarria distinta por competición [[audio-100-sintetizado-con-web-audio-ondas-pulso-triangulo-ru|Audio 100% sintetizado con Web Audio (ondas pulso, triángulo, ruido, secuenciador, formantes vocales para grada)]].  
  - Grada: síntesis de voces mediante **formantes de vocales** (A, E, I, O, U) + palmas; volumen y densidad según distancia a gradas del mapa [[audio-100-sintetizado-con-web-audio-ondas-pulso-triangulo-ru|Audio 100% sintetizado con Web Audio (ondas pulso, triángulo, ruido, secuenciador, formantes vocales para grada)]].  
  - Efectos: todos sintetizados (disparos, impactos, menús, ultis). **Sin archivos de audio** → peso cero, latencia nula, determinismo total [[audio-100-sintetizado-con-web-audio-ondas-pulso-triangulo-ru|Audio 100% sintetizado con Web Audio (ondas pulso, triángulo, ruido, secuenciador, formantes vocales para grada)]].

- **Ambientes (T62/P36):** 5 ambientes que alteran iluminación (paleta, sombras), afición (cánticos, densidad) y fuerza de rivales (stats, agresividad). Seleccionados proceduralmente al generar el mapa (`terreno.js`) y afectan a dificultad dinámica calibrada con bot (P34, T59) [[cinco-ambientes-con-cambio-de-luz-aficion-y-fuerza|Cinco ambientes con cambio de luz, afición y fuerza]].

### 3. API (endpoints principales)
| Grupo | Endpoints | Acceso |
|-------|-----------|--------|
| Salud | `GET /api/health` | Público |
| Auth | `POST /register`, `POST /login`, `POST /logout`, `GET /me`, `GET /confirm`, `POST /resend-confirmation`, `GET /providers`, `GET /google`, `GET /google/callback` | Público (salvo `/me`) |
| Usuarios | `GET /users`, `GET /users/:id/active`, `PATCH /users/:id/role`, `DELETE /users/:id` | Admin (baja propia o admin) |
| Juego | `GET /perfil`, `POST /partidas`, `POST /partidas/:id/fin`, `POST /contratar`, `POST /entrenar`, `PUT /identidad`, `GET /ranking`, `POST /desbloquear` | Sesión (`desbloquear` admin) |
| Prueba | `POST /prueba/dominio` | Público |

[[grupos-de-rutas-de-la-api-y-sus-accesos|Grupos de rutas de la API y sus accesos]]

### 4. Despliegue y flujo de trabajo
- **Plataforma:** **Cloud Run** (región `europe-southwest1`) [[url-base-de-la-aplicacion-la-grada-colchonera-en-cloud-run|URL base de la aplicación La Grada Colchonera en Cloud Run]].
- **URL producción:** `https://la-grada-colchonera-1081564062572.europe-southwest1.run.app` (usada para OAuth callback) [[url-base-de-la-aplicacion-la-grada-colchonera-en-cloud-run|URL base de la aplicación La Grada Colchonera en Cloud Run]].
- **Ramificación:** **GitHub Flow**  
  - `main` = versión estable que se despliega automáticamente.  
  - Cada hito: rama de integración `hito-N/integracion` creada desde `main` y fusionada de vuelta al cerrar el hito.  
  - Tareas: ramas `hito-N/Tx-descripcion` que nacen de la rama de integración del hito y se integran vía PR [[github-flow-como-modelo-de-ramificacion-del-proyecto|GitHub Flow como modelo de ramificación del proyecto]].
- **Frontend servido por el backend:** `express.static('public')` → mismo origen → simplifica CORS, cookies y despliegue [[arquitectura-en-capas-cliente-servidor-node-js-express-postg|Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)]].

---

## Qué NO está en el cerebro (para que lo sepas)
- Detalles del `Dockerfile` / `cloudbuild.yaml` / variables de entorno de Cloud Run.
- Configuración exacta de Neon (connection pooling, IP allowlist).
- Pipeline de CI/CD (GitHub Actions u otro) que hace el deploy a Cloud Run.
- Estrategia de migraciones de BD en producción.
- Monitorización, logs, alertas, escalado automático (min/max instancias).

Si necesitas cualquiera de esos puntos, habría que añadir al cerebro los ficheros de configuración de despliegue (`Dockerfile`, `.github/workflows/*`, `cloudbuild.yaml`, `config/entornos.json`, etc.) o la documentación de infraestructura.

*Notas consultadas: 11. Para otra pregunta, crea otra nota en esta carpeta.*
