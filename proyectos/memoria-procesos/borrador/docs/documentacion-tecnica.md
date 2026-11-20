# Documentación técnica de La Grada Colchonera

Versión correspondiente al cierre del Sprint 2 (29/10/2026). Esta documentación es la fuente única para la memoria.

---

## 2. Contexto, objetivos y alcance

### 2.1 Contexto
Asignatura: Procesos de Ingeniería del Software (PIS), curso 2026-2027, Grado en Ingeniería Informática, ESIIAB-UCLM.
El enunciado del Sprint 1 fija cuatro hitos comunes: gestión de usuarios, autenticación, persistencia, roles, seguridad y despliegue. Sobre esa base, cada proyecto construye su producto.

### 2.2 Objetivos
- **Principal:** Construir y desplegar una aplicación web pública donde los aficionados del Atlético de Madrid se registran, entran (email o Google) y juegan a un juego *survivor* con progreso guardado en el servidor, siguiendo un proceso de ingeniería revisable.
- **Específicos:**
  1. Producto: base SaaS (cuentas, sesión, roles, persistencia, correo, Google, errores) + juego (partida *survivor*, club, ranking, fichajes, entrenamiento, logros).
  2. Proceso: Scrum con backlog en DoneTonic, GitHub Flow (rama y PR por tarea), CI obligatorio, despliegue continuo.
  3. Calidad: arquitectura en capas, pruebas de error, seguridad desde el diseño (bcrypt, secretos fuera, permisos en servidor), interfaz accesible y responsive.
  4. Documentación: todo revisable desde el repositorio (README, docs/, memoria).

### 2.3 Alcance y cambio de enfoque
- **Sprint 1** (29/09/2026 – 27/10/2026): 4 hitos, 19 PBIs (P1–P19), 32 tareas (T1–T32). Hitos 1–3 entregados 12/10/2026; Hito 4 completado 23/10/2026. Añadido P19 (Cloud Run) por créditos de educación.
- **Sprint 2** (23/10/2026 – 29/10/2026): lógica del juego, 29 PBIs (P20–P48), 50 tareas (T33–T82), 6 fases + calidad.
- **Total:** 48 PBIs, 82 tareas, todos completados.
- **Cambio de enfoque:** Inicialmente red social; se cambió a juego *survivor* por: (1) más original, (2) problemas técnicos más ricos (simulación determinista, rendimiento canvas, mapa procedural, audio sintetizado, validación servidor anti-trampas), (3) reutiliza toda la base del Sprint 1.
- **Fuera de alcance:** multijugador tiempo real, amigos/partidas en grupo, apps nativas.

---

## 3. Requisitos

### 3.1 Requisitos funcionales Sprint 1 (RF-01 a RF-13)

| Id | Requisito | Hito | PBI | Dónde se cumple | Pruebas |
|----|-----------|------|-----|-----------------|---------|
| RF-01 | Registro email+contraseña (validación, email único, ≥8 chars) | 2 | P8 | `userService.register`, `POST /api/auth/register`, `registro.js` | `userService`, `api.auth` |
| RF-02 | Login local, mismo mensaje si email no existe o contraseña incorrecta | 2 | P8 | `userService.authenticate`, `POST /api/auth/login` | `api.auth` |
| RF-03 | Mantener sesión al recargar y cerrarla en servidor | 2 | P9 | `express-session` + tabla `session`, `GET /api/auth/me`, `POST /api/auth/logout` | `api.auth`, `api.database` (CI) |
| RF-04 | Rutas protegidas en servidor (401 sin sesión) | 2 | P10 | `requireAuth` | `api.users`, `api.auth` |
| RF-05 | Persistencia en BD real | 3 | P11 | PostgreSQL (Neon), `postgresUserRepository`, migraciones | `userRepository`, `migrate`, `api.database` |
| RF-06 | Roles usuario/admin, primer admin | 3 | P13 | `requireRole`, `requireSelfOrRole`, `userService.ensureAdmin` | `userService`, `api.users`, `bootstrap` |
| RF-07 | Listar usuarios, ver si activo, cambiar roles (solo admin) | 3 | P13 | `GET /api/users`, `GET /api/users/:id/active`, `PATCH /api/users/:id/role`, `admin.js` | `api.users` |
| RF-08 | Baja (y admin elimina); nunca último admin; email libre tras baja | 3 | P13 | `DELETE /api/users/:id` (baja lógica), `perfil.js`, `admin.js` | `userService`, `api.users` |
| RF-09 | Registro actividad relevante | 3 | P14 | `src/logger.js`, `requestLogger` | `logger` |
| RF-10 | Confirmación cuenta por correo, con reenvío | 4 | P16 | `accountConfirmationService`, `tokenSigner`, `mailer`, `GET /api/auth/confirm`, `POST /api/auth/resend-confirmation` | `accountConfirmation`, `tokenSigner`, `mailer`, `api.auth` |
| RF-11 | Login proveedor externo (Google, OAuth 2.0) | 4 | P15 | `googleOAuth.js`, `GET /api/auth/google`, `GET /api/auth/google/callback`, `userService.loginWithOAuth` | `googleOAuth`, `userService` |
| RF-12 | Manejo errores con info clara al usuario | 4 | P17 | `errorHandler.js`, `componentes.js`, `avisos.js`, `api.js` (timeout) | `api.*`, `frontend` |
| RF-13 | Prueba técnica: solo dominios permitidos | Prueba | — | `domainPolicy.js`, `POST /api/prueba/dominio` | `domainPolicy` (13 pruebas) |

### 3.2 Requisitos funcionales juego Sprint 2 (RJ-01 a RJ-20)

| Id | Requisito | PBI | Dónde se cumple | Pruebas |
|----|-----------|-----|-----------------|---------|
| RJ-01 | Con sesión inicio es menú juego; sin sesión no se juega; progreso ligado a cuenta | P20, P29 | `ui.js` (ruta `#/jugar`), `requireAuth` en `/api/juego`, tablas `juego_perfiles`, `juego_records` | `api.juego`, `frontend` |
| RJ-02 | Partida *survivor* infinita: oleadas, XP, mejoras, dificultad creciente | P21, P24, P34 | `mundo.js`, `oleadas.js`, `mejoras.js`, `config.js` | `game`, `juego-personajes`, `juego-club` |
| RJ-03 | Gráficos pixel art por código, cámara 3/4 | P22, P45 | `sprites.js`, `render.js`, `render-mundo.js` | `juego-movilidad`, `juego-habilidades` |
| RJ-04 | Elegir jugador (36, stats por posición, habilidades, rareza) y entrenador (2, ulti) | P23, P38 | Vestuario y Dirección (`juego.js`), `config.js`, `ulti.js` | `juego-personajes`, `juego-club` |
| RJ-05 | Armas automáticas 5 niveles, pasivas, habilidades desde cierto minuto | P24, P39 | `armas.js`, `mejoras.js`, `combate.js` | `juego-habilidades` |
| RJ-06 | Rivales con comportamiento propio (embisten, disparan, rodean, élites) | P25 | `rivales.js`, `oleadas.js` | `juego-movilidad`, `juego-personajes` |
| RJ-07 | Jefes 3 fases, avisos, escolta, furia, jugada estrella | P26, P46 | `jefes.js`, `oleadas.js` | `juego-movilidad`, `juego-logros` |
| RJ-08 | Mundo procedural: terreno, obstáculos macizos, colisiones exactas | P27, P35, P41 | `terreno.js`, `mundo.js` | `juego-movilidad` |
| RJ-09 | Ambientes cambian cada 5 min (pretemporada a Final Mundial) | P36 | `config.js`, `render-mundo.js`, `musica.js` | `juego-movilidad` |
| RJ-10 | Jugable teclado, ratón, táctil; pausa, pantalla completa, ajustes | P28 | `entrada.js`, `ajustes.js`, `juego.js` | `game`, `frontend` |
| RJ-11 | Club guardado en servidor con validación anti-trampas | P29 | `juegoService.finalizarPartida`, migración 003 | `api.juego`, `juegoRepository` |
| RJ-12 | Fichar jugadores con fichas contrato (1 por 3 jefes), sorteo por rareza | P30, P38 | `club.js`, `POST /api/juego/contratar`, `firma.js` | `juego-club`, `api.juego`, `frontend` |
| RJ-13 | Entrenar jugadores con puntos por bajas y jefes | P31 | `club.js`, `POST /api/juego/entrenar` | `juego-club`, `api.juego` |
| RJ-14 | Ranking grada: mejor partida por usuario (sin correo) | P32 | `juego_records`, `GET /api/juego/ranking` | `api.juego`, `juegoRepository` |
| RJ-15 | Combinaciones y ULTRAS, pantalla con requisitos | P33, P40 | `ultras.js`, `render-ultras.js`, pantalla Combinaciones | `juego-ultras`, `juego-habilidades`, `frontend` |
| RJ-16 | Modo pruebas solo admin | P34 | `POST /api/juego/desbloquear`, `scripts/desbloquear-juego.js` | `api.juego` |
| RJ-17 | Mote único y avatar en cabecera, Mi cuenta, ranking | P37 | `PUT /api/juego/identidad`, migración 004 | `api.juego`, `juegoRepository`, `frontend` |
| RJ-18 | Logros con historia Atleti, validados en servidor, equipaciones | P42 | `logros.js`, `juegoService` | `juego-logros`, `api.juego` |
| RJ-19 | Pantalla fin con stats y daño por habilidad | P43 | `fin-ui.js`, `combate.js` | `juego-logros` |
| RJ-20 | Música chiptune, efectos, grada, ajustes volumen | P44 | `audio.js`, `musica.js`, `ajustes.js` | `juego-logros` |

### 3.3 Requisitos no funcionales (RNF-01 a RNF-12)

| Id | Requisito | Cómo se cumple |
|----|-----------|----------------|
| RNF-01 | Seguridad credenciales y sesiones | Hash bcrypt, cookie httpOnly+secure+sameSite, regeneración sesión, permisos servidor, consultas parametrizadas |
| RNF-02 | Secretos fuera del código | Variables entorno; Secret Manager en producción; app no arranca sin secreto obligatorio |
| RNF-03 | Separación en capas | API → lógica → datos/integraciones, inyección dependencias |
| RNF-04 | Pruebas automáticas y CI obligatorio | 322 pruebas con `node:test`; ramas protegidas exigen CI verde |
| RNF-05 | Despliegue continuo URL pública | Cloud Run (principal) y Render (alternativo), sin intervención manual |
| RNF-06 | Disponibilidad y coste | Escala a cero (capas gratuitas y créditos educación); si versión no arranca, sirve la anterior |
| RNF-07 | Accesibilidad | HTML semántico, foco gestionado, `aria-live` avisos, errores `aria-describedby`, teclado, `prefers-reduced-motion` |
| RNF-08 | Responsive | Panel admin → tarjetas en móvil; joystick táctil en juego |
| RNF-09 | Rendimiento juego | 60 FPS portátil normal: paso fijo, búsqueda espacial celdas, texturas por celda cacheadas y precargadas |
| RNF-10 | Trazabilidad | Requisito → PBI → tarea → rama → PR → release |
| RNF-11 | Privacidad | Política pública; ranking sin correo; logs ocultan datos sensibles |
| RNF-12 | Mantenibilidad | Sin frameworks ni compilación frontend; equilibrio en `config.js`; módulos pequeños y comentados |

---

## 4. Metodología y gestión

### 4.1 Scrum adaptado en DoneTonic
- Espacio de trabajo: **TFG**, equipo: **Colchoneros**.
- Backlog, sprints, tablero y gráficas en DoneTonic.
- Dos sprints:
  - **Sprint 1** (29/09–27/10/2026): 19 PBIs (P1–P19), 32 tareas (T1–T32), etiquetas *Hito 1* a *Hito 4*, prioridad MUST.
  - **Sprint 2** (23/10–29/10/2026): 29 PBIs (P20–P48), 50 tareas (T33–T82), etiquetas por fase (*Base del juego*, *Fase 2·Club*, *Fase 3·Ultras*, *Fase 4·Mundo*, *Fase 5·Rarezas*, *Fase 6·Logros y sonido*, *Calidad*), prioridad MUST.
- Product Backlog total: 48 PBIs, 82 tareas, todas hechas.
- Cada requisito → PBI con historia de usuario («Como… quiero… para…») y criterios de aceptación; cada PBI → 1–3 tareas; cada tarea → rama y PR.
- 29 HU del Sprint 2 con criterios en `docs/gestion/README.md` (tabla `sprint2-hu`).
- Seguimiento: tablero por estados, gráficas automáticas (Sprint Burndown/Burnup, Backlog Burndown/Burnup, Velocity Chart).
- **Cambio de alcance Sprint 1:** créditos Google Cloud → PBI P19 (Cloud Run, T29, T30), Render alternativo.
- **Sprint 2:** backlog registrado en DoneTonic al cerrar sprint (29/10/2026) → gráficas en recta; evolución real reconstruida con fechas de fusión de PRs.

### 4.2 Definición de Hecho (DoD)
- **Tarea:** código en PR referenciando tarea, pruebas CI verdes (check *Pruebas*), PR fusionado, documentación actualizada (README, `docs/`, `.env.example`).
- **Hito:** rama en `main`, desplegada en URL pública, publicada como release.
- **Fase juego:** PR en `main`, desplegado, probado a mano en navegador.

### 4.3 GitHub Flow adaptado
- `main`: versión estable, despliegue automático, solo PR con CI verde.
- `hito-N/integracion`: rama integración de cada hito Sprint 1.
- `hito-N/Tx-descripcion`: rama por tarea, desde rama hito.
- **Sprint 1:** tarea → rama `hito-N/Tx` → PR a `hito-N/integracion`; cierre hito → PR `hito-N/integracion` → `main` → release `hito-1`, `hito-2`, `hito-3`. Commits en español, imperativo, con `[Tx]`. `npm test` antes de PR. Cierres: PR #9, #17, #24, #29, #32. Hito 4: ramas reubicadas sobre `main` real → PRs #37–#41 directos.
- **Sprint 2:** integración en `main` con 1 PR por fase (#36, #44–#54) y 1 por arreglo (#51, #55, #56); cada tarea DoneTonic indica su PR.
- CI obligatorio: ni `main` ni ramas integración admiten fusión con CI rojo.
- Pipeline completo (pruebas PostgreSQL 17, imagen Docker, despliegue Cloud Run) descrito en §11.

### 4.4 Planificación
- Sprint 1: Hitos 1–3 entregados 12/10/2026 (con P18, P19); Hito 4 completado y comprobado producción 23/10/2026; fin sprint 27/10/2026.
- Sprint 2: 23/10–29/10/2026.
- Cronología fecha a fecha en Tabla `cronologia` (Anexo desarrollo).

### 4.5 Herramientas
Ver Tabla `herramientas` (Capítulo 3 memoria): DoneTonic, GitHub, Node.js 22, Express 5, PostgreSQL (Neon), Playwright, GitHub Actions, Google Cloud Run, Render, LuaLaTeX, Claude (Cowork).

### 4.6 Evolución de cada sprint
- **Sprint 1:** Tabla `evolucion-s1` y Figura `burndown-s1` (Anexo desarrollo). Escalón «+P19» por cambio de alcance.
- **Sprint 2:** Tabla `evolucion-s2` y Figura `burndown-s2` (Anexo desarrollo). Trabajo concentrado en 3 jornadas: 23/10 (PR #36), 24/10 (PRs #44–#52, 17 PBIs), 26/10 (PRs #53, #54, 9 PBIs), arreglos #55, #56 (27, 29/10). Gráficas DoneTonic en recta por registro backlog al cierre.

---

## 5. Arquitectura y decisiones de diseño

### 5.1 Visión general: arquitectura en capas
Cliente-servidor en capas (Figura `fig:capas`). Servidor (Node.js+Express) sirve frontend estático → mismo origen.
Capas (Tabla `capas`):
- Presentación (`public/`): pinta vistas, valida formularios, muestra avisos, juega. No habla con BD ni decide permisos.
- Cliente API (`public/js/api.js`): peticiones HTTP, timeout 15s, traduce errores a `ApiError`, avisa si caduca sesión. No pinta.
- API (`src/api/`): rutas HTTP, sesión, auth/autorización, registro peticiones, formato errores común. No reglas de negocio.
- Lógica (`src/services/`): reglas de negocio. No conoce HTTP ni SQL.
- Datos (`src/repositories/`): guardar/leer (memoria o PostgreSQL) mismo contrato. No valida reglas.
- Integraciones (`src/integrations/`): correo y Google. No decide.
- Composición (`src/app.js`, `src/bootstrap.js`): conecta capas, elige BD, migra, crea primer admin.

### 5.2 Decisiones de diseño (Tabla `decisiones`)
Resumen de decisiones clave con justificación:
- Express 5 sin framework frontend → capas visibles como ficheros, sin build, backend sirve frontend (sin CORS), frontera interfaz/cliente en 2 ficheros.
- Repositorio dos implementaciones (memoria y PostgreSQL) → arranque y prueba sin BD, mismas pruebas en ambas, demuestra independencia almacenamiento (Repository pattern).
- Inyección dependencias por parámetro → pruebas usan versiones falsas sin trucos.
- Sesiones servidor (`express-session` + PostgreSQL) → logout/eliminar cuenta invalida al momento; cookie httpOnly sin datos; sesiones sobreviven reinicios/despliegues.
- Bajas lógicas (`status=deleted`) con email libre → historial y auditoría; cuenta no entra, sesión no vale, email y mote libres para volver (índice único parcial).
- Token confirmación firmado (HMAC) sin guardar en BD → sin tabla ni limpieza; caduca solo; no fabricable sin secreto.
- OAuth 2.0 con `fetch` (no Passport) → flujo corto entendible (`state`, intercambio código, email verificado); menos dependencias, fácil probar con cliente falso.
- Primer admin por variables entorno → sin contraseñas en código/scripts; idempotente.
- Migraciones SQL propias → pocas tablas; SQL legible y versionado con registro aplicadas.
- Cloud Run principal, Render alternativo → Cloud Run aprovecha créditos educación, escala a cero, Secret Manager, WIF; Render primer despliegue, respaldo.
- Reglas juego compartidas cliente/servidor → servidor importa `club.js`, `config.js`, `logros.js`: una fuente verdad para fichajes, entrenamiento, logros.
- Concurrencia optimista en perfil juego (`version`) → dos peticiones simultáneas no gastan misma ficha; segunda se reintenta con datos nuevos.
- Simulación juego pura y determinista → paso fijo 1/60s, azar con semilla: se prueba en Node sin navegador, resultado no depende de FPS.
- Gráficos y sonido generados con código → sin problemas derechos (nada oficial), carga instantánea, fácil variar (equipaciones, selecciones, intensidad música).

---

## 6. Diseño

### 6.1 Módulos del backend (Tabla `modulos`)
`server.js`, `bootstrap.js`, `app.js`, `config.js`/`loadConfig.js`, `logger.js`, `api/index.js`, `api/auth.js`, `api/users.js`, `api/juego.js`, `api/currentUser.js`, `api/errorHandler.js`, `services/userService.js`, `services/accountConfirmationService.js`, `services/tokenSigner.js`, `services/passwordHasher.js`, `services/juegoService.js`, `services/domainPolicy.js`, `services/errors.js`, `repositories/*` (memoria y PostgreSQL usuarios y juego), `integrations/mailer.js`, `integrations/googleOAuth.js`, `db/migrate.js`, `db/migrations/*.sql` (001 usuarios, 002 sesiones, 003 juego, 004 identidad, 005 email libre tras baja).

### 6.2 Modelo de datos entidad-relación (Figura `fig:modelo-datos`)
Tablas: `users`, `session`, `juego_perfiles`, `juego_records`.
- `users`: id (PK), email (UK único no eliminadas), password_hash (null Google), role (user|admin), status (pending|active|deleted), auth_provider (local|google), created_at, deleted_at, apodo, apodo_clave (UK), avatar.
- `session`: sid (PK), sess (JSON), expire.
- `juego_perfiles`: user_id (PK,FK), datos (JSONB), version (optimista), updated_at.
- `juego_records`: user_id (PK,FK), alias, avatar, tiempo, nivel, jefes, bajas, created_at.
Relaciones: users → juego_perfiles (tiene su club), users → juego_records (tiene su mejor partida).

### 6.3 Frontend
SPA rutas hash (`public/js/ui.js`): `#/` inicio, `#/entrar`, `#/registro`, `#/perfil`, `#/jugar`, `#/admin`, 404 «Fuera de juego». Cada ruta declara protección (protegida, solo invitados, solo admin); interfaz redirige, protección real en servidor.
Vistas (`ui/vistas/*.js`): exportan `montar(raiz, contexto)` y devuelven limpieza. Estado (`ui/estado.js`): usuario actual. Cabecera (`ui/cabecera.js`): se repinta al cambiar (mote, avatar, enlaces según rol). Formularios (`ui/formulario.js`): validan al escribir y enviar, errores `aria-describedby`. Avisos (`ui/avisos.js`): zona `aria-live`; errores `role="alert"`. Cliente (`api.js`): único `fetch`; timeout 15s `AbortController`; convierte errores en `ApiError`.

### 6.4 API (Tabla `api`)
Grupos: Salud (`GET /api/health`), Auth (`POST register`, `POST login`, `POST logout`, `GET me`, `GET confirm`, `POST resend-confirmation`, `GET providers`, `GET google`, `GET google/callback` - público salvo `me`), Usuarios (`GET /users`, `GET /users/:id/active`, `PATCH /users/:id/role`, `DELETE /users/:id` - admin, baja propio o admin), Juego (`GET perfil`, `POST partidas`, `POST partidas/:id/fin`, `POST contratar`, `POST entrenar`, `PUT identidad`, `GET ranking`, `POST desbloquear` - sesión, `desbloquear` admin), Prueba técnica (`POST /api/prueba/dominio` - público).

---

## 7. Flujos con diagramas de secuencia

Los 13 flujos principales con diagramas (Mermaid en fuente, `sequencediagram` en memoria):

1. **Registro email+contraseña** (`fig:sec-registro`): vista valida cliente → `api.js` POST → `userService` normaliza/valida → rechaza email repetido 409 → crea cuenta pending con hash → firma token HMAC 24h → correo SMTP.
2. **Confirmación enlace correo** (`fig:sec-confirmacion`): abre enlace → API verifica firma HMAC → si válida: cuenta `active`, aviso confirmación; si manipulado/caducado: redirige error, cuenta sigue pending.
3. **Login local** (`fig:sec-login`): `userService.authenticate` mismo mensaje error (email no existe o contraseña mala); si pending → 403 con opción reenviar; si correcto → regenera sesión, cookie `grada.sid`.
4. **Google OAuth 2.0** (`fig:sec-google`): guarda `state` aleatorio en sesión → redirige Google → callback compara y borra `state` (un uso) → cambia código por perfil en servidor → según email: existe/pending/no existe → activa/crea cuenta → regenera sesión.
5. **Baja** (`fig:sec-baja`): diálogo confirmación accesible → servidor `requireSelfOrRole('admin')` → impide eliminar último admin → cuenta `deleted`, suelta mote y email, sesión deja de valer en siguiente petición.
6. **Listado usuarios admin** (texto): `GET /api/users` → `requireRole('admin')` → `userService.list` → repo → tabla.
7. **Cambio rol admin** (texto): `PATCH /api/users/:id/role` → `requireRole('admin')` → `userService.changeRole` → valida no último admin → repo.
8. **Ver usuario activo** (texto): `GET /api/users/:id/active` → `requireRole('admin')` → `userService.isActive` → repo.
9. **Reenvío confirmación** (texto): `POST /api/auth/resend-confirmation` → `accountConfirmationService.resend` → firma nuevo token → correo → 202 sin revelar existencia.
10. **Una partida juego** (`fig:sec-partida`, §7.10): empezar → servidor guarda partida en curso con reloj propio; jugar → cliente avanza simulación paso fijo, pinta mundo, suena música; terminar → servidor valida resultado (rechaza si no es partida en curso, tiempo > transcurrido+15s o 4h, jefes/nivel/bajas no creíbles: `jefes ≤ 3+t/50`, `nivel ≤ 8+t/3`, `bajas ≤ 20·t+50`) → si válido: reparte recompensas, guarda perfil.
11. **Contratar concurrencia optimista** (`fig:sec-contratar`, §7.11): gasta ficha contrato en jugador sorteado por rareza; si doble clic → dos peticiones leen misma versión → primera escribe OK, segunda falla actualizar → reintenta con datos nuevos (sin fichas) → 409.
12. **Logros** (texto): cliente manda logros → servidor solo apunta los que puede comprobar (tiempo, jefes, bajas, jugador, entrenador); los de plantilla los calcula él.
13. **Pipeline CI/CD** (`fig:pipeline`, §7.12): PR → CI (pruebas PostgreSQL 17 + Docker build) → ¿CI verde en main? → sí → Deploy Cloud Run (WIF → Artifact Registry → Cloud Run deploy → smoke test) → Producción activa; no → sin despliegue. Render webhook paralelo.

---

## 8. Seguridad (Tabla `seguridad`)

| Amenaza | Medida | Dónde |
|---------|--------|-------|
| Robo contraseñas | Solo hash bcrypt (sal, coste 10). Nunca contraseña ni cifrado reversible | `passwordHasher.js` |
| Robo/fijación sesión | Cookie httpOnly, sameSite=lax, secure en prod; regenera al entrar, destruye al salir | `app.js`, `auth.js` |
| Sesión cuenta eliminada | En cada petición recarga usuario; si no activo, sesión deja de valer | `currentUser.js` |
| Escalada privilegios | Roles comprobados servidor (401/403); siempre queda un admin | `currentUser.js`, `userService.js` |
| Enlaces falsificados | Token HMAC-SHA256 clave derivada, comparación tiempo constante, propósito y caducidad 24h | `tokenSigner.js` |
| CSRF en OAuth | `state` aleatorio, guardado en sesión, un solo uso | `auth.js` |
| Inyección SQL | Consultas parametrizadas | `postgres*Repository.js` |
| XSS | DOM con `textContent` (helper `h()`); prueba lo comprueba | `dom.js`, `frontend.test.js` |
| Secretos expuestos | Solo variables entorno; Secret Manager cuenta servicio mínimo privilegio; `.env` ignorado | `loadConfig.js`, workflows |
| Datos sensibles en logs | Contraseñas, hashes, cookies, tokens, secretos → `[oculto]` | `logger.js` |
| Trampas en juego | Reloj servidor, límites creíbles, logros verificables, concurrencia optimista | `juegoService.js` |

---

## 9. El juego (Sprint 2)

### 9.1 Concepto
Juego web género *survivor* (popularizado por *Vampire Survivors*) con estética píxeles «chibi». Jugador controla futbolista historia Atlético; armas atacan solas; tarea: moverse, esquivar, elegir mejoras para aguantar oleadas infinitas rivales y jefes. Progresión entre partidas (club, fichajes, entrenamiento, logros) guardada en servidor y validada con anti-trampas.

### 9.2 Cómo se juega (manual usuario)
Ver Capítulo 4b memoria: menú (`#/jugar`), primera visita elige mote (3-16 chars, único) y cara; menú muestra ficha izquierda (mote, avatar, mejores tiempos) y opciones derecha: Jugar, Vestuario, Entrenamiento, Contratar, Logros, Combinaciones, Dirección, Ranking, Ajustes. Controles: teclado WASD/flechas, Espacio/E ulti, Esc/P pausa, F pantalla completa, 1-3 mejoras; móvil joystick táctil flotante. Ajustes en `localStorage`.
Partida infinita: oleada cada 30s, jefe cada 4 oleadas (primero 1:30). Rivales sueltan XP; subir nivel → elige 1 de 3 mejoras (combinaciones marcadas ★). Jefes: 3 fases (66% y 33% vida), escolta élites desde 2ª, furia si tardas, jugada estrella fase 3. Ambientes cada 5 min: pretemporada → Copa Rey → Liga → Champions → Mundial (cambian luz, césped, afición, carteles, fuerza rivales; en Mundial camisetas selección). Fin: pantalla stats (tiempo, ambiente, bajas, jefes, daño por habilidad, golpe fuerte, daño recibido, vida recuperada, logros nuevos) + recompensas club. Pausa (Esc/P): ajustes sonido, gráficos, controles sin salir.
Resto menú: Entrenamiento (puntos por bajas/jefes → Vida, Defensa, Disparo, Suerte; admin modo pruebas), Contratar (fichas por 3 jefes → sorteo rareza), Logros (vitrina con dato histórico), Combinaciones (metas y ultras con requisitos), Dirección (entrenador Cholo/Luis Aragonés con ulti), Ranking (mejor partida por usuario, mote+avatar, sin correo), Tu ficha (mote+avatar), Ajustes (volumen, gráficos, cámara, controles).

### 9.3 Sistemas (Tabla `juego-sistemas`)
Jugadores (36: 4P, 9D, 13M, 10F; posición fija stats base; rasgos propios; habilidades aprendibles), Rarezas (Leyenda 8, Épico 8, Raro 8, Común 12; más rareza = más habilidades 8-16 y menos prob. contrato), Entrenadores (Cholo +daño+vida ulti «Partido a partido»; Luis Aragonés +velocidad+XP ulti «Furia Roja»), Armas/habilidades (29, 5 niveles: disparo, cuerpo a cuerpo, movilidad, especiales; fuertes no suben hasta `desdeMinuto` y `cdMin`), Pasivas (16: botas, imán, pasión, pizarra, cantera, masajista, espinilleras, pulmones, toque dorado, botas en llamas, paradón, brazalete, trébol, prórroga, visión de juego, partidos grandes), Combinaciones (29 metas: Muro rojiblanco, Tiki-taka, Pichichi, Catenaccio, Leyenda rojiblanca, Golazo otro planeta, Remontada épica, Triple Corona, Infierno Metropolitano, Capitán eterno...; 24 Fase 3 + 5 Fase 7 = 29), Ultras (6 solas al completar combinaciones: Premio Puskás, Balón de Oro, MVP Champions, Zamora, Bota Oro histórica, Mejor jugador Mundial; efecto visual propio y daño % reducido vs jefes), Rivales (16 equipos genéricos; embisten: Liverpool, Arsenal, PSG, Dortmund; disparan: Bayern, City, Chelsea, Juventus, Milan, Inter, Nápoles; élites: blindado, veloz, furioso), Jefes (10: Guardiola rondo/tiki-taka, Mourinho autobús, Cristiano Siuuu, Messi eslalon, Vinicius zigzag, Yamal rosca, Neymar lluvia bicicletas, Bale cañonazos, Benzema precisión, Suárez mordiscos; 3 fases, escolta, furia, jugada estrella; desde oleada 24 pueden salir 2 a la vez; cada vuelta completa +25% duros), Dificultad (crecimiento continuo vida/daño/velocidad; tramo final +duro min 9 y rivales «curtidos» min 12; multiplicador por ambiente; ayuda inicial se apaga 8 min), Movimiento (inercia, ritmo al correr +daño+XP, castigo quieto, premios por campo), Mundo (procedural infinito semilla, ruidos suaves: distritos ciudad/entrenamiento/parque/prado, estadios con gradas, plazas/tiendas, mesetas/escaleras, barro, lluvia, caminos; colisión por pies vista 3/4), Club (plantilla inicial 4 comunes 1 por posición; 1 ficha por 3 jefes cuenta; sorteo rareza; puntos entrenamiento por jefes 1 cada 3 y por bajas; stats Vida, Defensa, Disparo, Suerte máx 20), Logros (29 con dato curioso Atleti; 10 equipaciones desbloqueables), Sonido (efectos, música chiptune original: canción por ambiente que se anima con tiempo y jefes, fanfarria por competición; grada: murmullo y cánticos según distancia gradas).

### 9.4 Arquitectura del juego (Figura `fig:juego-arquitectura`)
Tres bloques:
- **Simulación pura** (izquierda): `mundo.js` (bucle paso fijo), `armas.js`, `combate.js`, `jefes.js`, `oleadas.js`/`rivales.js`, `terreno.js`, `ultras.js`/`ulti.js`, `mejoras.js`, `config.js` (equilibrio).
- **Presentación** (centro): `juego.js` (pantallas y bucle), `render.js`/`render-mundo.js`/`render-ultras.js`, `sprites.js` (muñecos chibi 32x32), `hud.js`, `audio.js`+`musica.js`, `club-ui.js`/`fin-ui.js`/`firma.js`, `entrada.js`.
- **Servidor** (derecha): `juegoService.js`, `club.js`, `config.js`, `logros.js`.
Conexiones: simulación interna → presentación → servidor vía `api.js` → `/api/juego`; servidor usa reglas compartidas (`club.js`, `config.js`, `logros.js`).

#### Determinismo
`mundo.js` paso fijo 1/60s, generador aleatorio con semilla. Si navegador lento, varios pasos por frame (con tope); resultado no depende de FPS, pruebas reproducibles.

#### Eventos
Simulación no toca DOM ni audio: deja eventos (`oleada`, `aviso`, `jefe-derrotado`, `ambiente`, `ultra`…) que `juego.js` traduce a sonido, avisos, anuncios lectores pantalla.

#### Estadísticas
Cada fuente daño (arma, ultra, ulti, quemaduras) en `mundo.stats` para pantalla fin.

#### Rendimiento
Búsqueda obstáculos por celdas claves numéricas (~4.5x más rápida v1), 1 textura suelo por celda y ambiente, pintada máx 1 por frame y por adelantado, muñecos cacheados.

#### Dibujo
Canvas 2D cámara 3/4 (suelo aplastado vertical, muñecos de pie). Muñecos código en cuadrícula 32×32 estilo chibi (16×20 con piernas hasta Fase 6): cabeza grande, cuerpo, zapatones, sin piernas. Capas y píxel a píxel: zapatos, pantalón, torso, brazos, cabeza, cada una con contorno color y luz arriba-izquierda. Cada persona: 18 peinados, 6 barbas, mandíbula, complexión, estatura, gesto, gafas, cinta, guantes, brazalete…; caminan 4 frames. Equipaciones y 26 selecciones sin imágenes. Mapa (Fase 7) píxeles 2 unidades en `render-suelo.js` y `render-obstaculos.js`, paletas por ambiente en `render-paletas.js`, efectos habilidades en `render-habilidades.js` (partículas con tope y azar propio en `efectos.js`, encender/apagar no cambia partida).

#### Audio
Todo sintetizado Web Audio: ondas pulso (12.5%, 25%, 50%), triángulo, ruido. Música: secuenciador propio programa notas por adelantado. Grada: voces con formantes vocales y palmas.

### 9.5 Servidor y anti-trampas
- Al empezar: servidor guarda partida en curso con reloj propio.
- Al terminar: rechaza si no es partida en curso, tiempo > transcurrido+15s o 4h, o jefes/nivel/bajas no creíbles (`jefes ≤ 3+t/50`, `nivel ≤ 8+t/3`, `bajas ≤ 20·t+50`).
- Logros cliente: solo apunta los comprobables (tiempo, jefes, bajas, jugador, entrenador); los de plantilla los calcula él.
- Cambios perfil: concurrencia optimista (`UPDATE ... WHERE version = $n`) con reintentos.
- Ranking: mejor partida por usuario con mote y avatar, nunca correo.

### 9.6 Logros (Tabla `juego-logros`)
29 logros con condición y equipación desbloqueable. Cada uno esconde dato real club (ej. Griezmann 3º Balón Oro 2018, Oblak 5 Zamoras seguidas, Atleti nació 1903 azul y blanco). Datos en `logros.js` comprobados uno a uno.

### 9.7 Evolución por fases (Tabla `juego-fases`)
| Fase | Qué se añadió | Problemas que resolvió |
|------|---------------|------------------------|
| Rediseño | Nueva interfaz (tokens, tipografía, modo oscuro rojiblanco), menú juego como inicio con sesión | Interfaz sprint funcional pero sobria |
| 1 | Survivor base: simulación, oleadas, armas, mejoras, jefes, menú con muñeco paseando | — |
| 2 | Club en servidor (plantilla, contratos, entrenamiento), ranking grada, élites, poderes nuevos | Progreso ligado a cuenta y validado |
| 3 | 6 ultras, 24 combinaciones (5 más Fase 7 = 29 total), dificultad con castigo, entrenamiento por bajas, modo pruebas | Maxear una sola cosa ya no basta |
| 4 | Mundo procedural natural, 5 ambientes por finales, mote y avatar | Mapa repetitivo; correo visible en ranking |
| 5 | Rarezas por historia rojiblanca, habilidades niveladas, combinaciones a la vista, animación firma, colisiones exactas | Regate demasiado fuerte; esconderse detrás tejados |
| 6 | 29 logros con historia y 10 equipaciones, stats fin, música chiptune y grada, muñecos más detalle, jefes con escolta, furia, jugada estrella | Falta objetivos largo plazo; sonido pobre; jefes fáciles |
| 7 | Muñecos chibi 32x32 (sin piernas) con rasgos propios, mapa más detalle y luz por ambiente, menú rediseñado (paneles translúcidos, centro despejado, botón entrada), 5 habilidades (carambola, presión alta, la ola, fuera de juego, ruleta), 2 pasivas (visión de juego, partidos grandes), 5 combinaciones, mejores efectos todas habilidades | Muñecos casi iguales; mapa plano; menú estático; efectos poco legibles |

---

## 10. Pruebas

### 10.1 Estrategia
- Unitarias lógica, API y repositorio (memoria y PostgreSQL).
- Comando único: `npm test`.
- Local: `pg-mem`; CI: PostgreSQL 17 real.

### 10.2 Pruebas unitarias lógica (casos error destacados)
Email repetido, cuenta pendiente, usuario elimina a otro, último administrador.

### 10.3 Distribución por fichero (Tabla `pruebas-por-fichero`)
Total 276 en `main` al cierre Sprint 2 (140 Sprint 1 + 136 juego hasta Fase 6); 46 Fase 7 → 322 total.
Ficheros: `userService.test.js` (27), `api.auth.test.js` (16), `userRepository.test.js` (16), `frontend.test.js` (14), `domainPolicy.test.js` (13), `api.users.test.js` (11), `googleOAuth.test.js` (11), `config.test.js` (8), `accountConfirmation.test.js` (6), `logger.test.js` (6), `tokenSigner.test.js` (3), `mailer.test.js` (3), `migrate.test.js` (3), `bootstrap.test.js` (2), `health.test.js` (1), `api.database.test.js` (CI), `juego-club.test.js` (27), `juego-movilidad.test.js` (22), `api.juego.test.js` (15), `juego-personajes.test.js` (14), `juego-habilidades.test.js` (14), `juego-ultras.test.js` (13), `juego-logros.test.js` (13), `game.test.js` (10), `juegoRepository.test.js` (8).

### 10.4 Comprobaciones manuales y visuales
Cada cambio visible comprobado en navegador con Playwright (capturas automatizadas cada pantalla/estado). Hito 4 probado a mano en producción: correo real Gmail, enlace manipulado, acceso dos cuentas Google distintas. Capturas app generadas con app real y datos ejemplo.

---

## 11. CI/CD

### 11.1 Workflows (Tabla `workflows`)
| Workflow | Cuándo | Qué hace |
|----------|--------|----------|
| `ci.yml` (CI) | Cada PR y push a main, hito-*/integracion | Job *Pruebas*: `npm ci` + `npm test` con PostgreSQL 17. Job *Imagen Docker*: construye imagen, arranca, comprueba `/api/health` |
| `deploy-cloud-run.yml` | CI verde en main (`workflow_run`) | Autentica Google Cloud con WIF, construye y sube imagen a Artifact Registry, despliega en Cloud Run con variables y 8 secretos Secret Manager |
| `memoria.yml` | Cambios en memoria/ | Compila memoria LuaLaTeX (latexmk + biber) y publica PDF como artefacto |
| Render (webhook) | Cada cambio en main | Despliegue alternativo según `render.yaml` |

### 11.2 Pipeline (Figura `fig:pipeline`)
PR → CI (pruebas PostgreSQL 17 + Docker build) → ¿CI verde en main? → sí → Deploy Cloud Run (WIF → Artifact Registry → Cloud Run deploy → smoke test) → Producción; no → sin despliegue. Render paralelo por webhook.
Evidencia: Figura `actions-verde` (Capítulo 5) muestra CI y despliegue Cloud Run en verde tras PRs Hito 4.

---

## 12. Logs y errores

### 12.1 Registro actividad (logs)
Línea JSON estructurada por evento relevante en stdout (capturado por Cloud Logging en producción): `time`, `level`, `event`, `msg`, metadatos. Cada petición HTTP: `X-Request-Id` único propagado a todas las trazas.
Eventos tipados: `app.start`, `app.stop`, `app.storage`, `app.mail`, `admin.bootstrap`, `http.request`, `http.error`, `user.registered`, `auth.login`, `auth.logout`, `auth.login_failed`, `auth.forbidden`, `mail.confirmation_sent`, `mail.failed`, `mail.not_sent`, `user.confirmed`, `user.confirm_failed`, `auth.oauth_denied`, `auth.oauth_failed`, `user.role_changed`, `user.deleted`, `juego.identidad`.
Confidencialidad: contraseñas, hashes, cookies, tokens, secretos → `[oculto]`.

### 12.2 Manejo errores
Uniforme desde lógica a interfaz:
1. Servicios lanzan excepciones tipadas: `ValidationError`, `UnauthorizedError`, `ForbiddenError`, `AccountPendingError`, `NotFoundError`, `ConflictError`, `ServiceUnavailableError`.
2. Middleware `errorHandler` mapea cada error a código HTTP y respuesta estándar `{"error": {"code", "message"}}`.
3. Cliente `api.js` transforma respuestas fallidas en `ApiError`; timeout 15s `AbortController`.
4. Vistas muestran alertas específicas por caso; usuario no ve trazas internas ni formatos crudos.

---

## 13. Problemas y soluciones

### 13.1 Sprint 1 (Tablas `prob-desarrollo`, `prob-despliegue`, `prob-git`, `prob-alcance`)
- JSON mal formado → error HTML Express: manejador propio tras parser → 400 JSON en toda API.
- Correo no salía Cloud Run: SMTP sin cifrar bloqueado → Gmail puerto 465 con contraseña app en Secret Manager.
- `redirect_uri_mismatch` Google: Cloud Run dos URLs → registrar ambas en cliente Google y usar `PUBLIC_URL`.
- Ramas Hito 4 dependían unas de otras (cadena) → reubicar (rebase) sobre `main` real antes de PRs, cada una con CI verde.
- Cambio proveedor despliegue a mitad sprint (créditos Google Cloud) → nuevo PBI P19 (cambio alcance documentado), Docker y Cloud Run principal, Render alternativo.

### 13.2 Sprint 2 (Tabla `prob-juego`)
- Juego no cargaba al entrar: variable usada antes de existir en módulo arranque → inicializar antes primer uso (PR #51).
- Primer clic «Reenviar correo» se perdía tras error: botón deshabilitado tras intento fallido → rehabilitar botón tras mostrar error (PR #55).
- No se podía volver tras eliminar cuenta con Google: flujo baja OAuth no limpiaba sesión local → cerrar sesión local tras baja federada (PR #56).

---

## 14. Métricas (Tabla `metricas`)
- PBIs/tareas Sprint 1: 19 / 32
- PBIs/tareas Sprint 2: 29 / 50
- PRs fusionados: >50
- Releases GitHub: `hito-1`, `hito-2`, `hito-3`, `hito-4`, `sprint-1`
- Pruebas automáticas totales: 276 (+ batería PostgreSQL real en CI)
- Endpoints API expuestos: 23
- Migraciones SQL aplicadas: 5
- Líneas backend (`src/`, con SQL): ~2.300
- Líneas interfaz web (`ui.js`, `api.js`, `ui/`): ~1.150
- Líneas CSS: ~950
- Líneas motor juego (`public/js/game/`, 35 módulos): ~14.800
- Líneas pruebas automatizadas: ~5.050
- Dependencias directas producción: 6
- Contenido jugable: 36 jugadores, 2 entrenadores, 29 armas, 16 pasivas, 29 combinaciones (24 Fase 3 + 5 Fase 7), 6 ultras, 16 equipos, 10 jefes, 5 ambientes, 26 selecciones, 29 logros, 10 equipaciones

---

## 15. Conclusiones y trabajo futuro

### 15.1 Conclusiones (orden objetivos Capítulo 1)
- **Objetivo principal:** Cumplido. App desplegada Cloud Run URL pública (Anexo material). Aficionados registran email/Google, juegan, club/partidas/logros guardados servidor. Dos sprints cerrados: Sprint 1 19 PBIs, Sprint 2 29 PBIs, todos hechos.
- **Producto:** 4 hitos Sprint 1 completos, desplegados, comprobados producción (Capítulo 5), trazabilidad backlog→release (Anexo trazabilidad). Juego Sprint 2 encima (Capítulo 4b). Cambio red social→juego buena decisión: reutiliza base sprint y obliga resolver problemas interesantes (determinismo simulación, rendimiento, validación servidor, generación procedural, audio sintetizado).
- **Proceso:** Todo por mismo camino: PBI DoneTonic → tarea → rama → PR CI verde → despliegue automático. Camino reversible desde cualquier PR. Gráficas DoneTonic y burndowns Anexo desarrollo muestran avance. Cambio alcance Sprint 1 (PBI P19, créditos Google Cloud) registrado como PBI más, no por fuera.
- **Calidad:** Arquitectura capas + inyección dependencias permitió cambiar memoria→PostgreSQL, añadir correo/Google, montar juego entero sin tocar lógica existente. Probar error primero y exigir CI verde para fusionar evitó regresiones: 276 pruebas automáticas al cierre.
- **Documentación:** Gestión, documentación técnica, revisión entrega, memoria en repositorio junto a código. Revisor puede ir requisito→PBI→tarea→rama→PR→pruebas sin salir GitHub ni pedir acceso herramientas.

### 15.2 Lecciones aprendidas
1. Dividir pronto en tareas pequeñas: rama y PR por tarea → cada cambio fácil revisar y deshacer.
2. Automatizar despliegue desde día 1: cada entrega es PR más, no trabajo aparte al final.
3. Documentar decisiones mientras se toman, no al final: documentación técnica y memoria salen de lo ya escrito en repo.
4. Comprobar visualmente cada cambio interfaz. Así apareció clic perdido en «Reenviar correo»: al salir campo contraseña aparecía su error, página se movía, clic caía fuera botón (Anexo desarrollo).

### 15.3 Trabajo futuro
1. **Multijugador:** lista amigos y partidas en grupo (*party*) hasta 4 jugadores, WebSockets y servidor autoritativo.
2. **Más contenido:** jugadores, jefes, equipaciones, logros, mejores sprites jugadores menos conocidos.
3. **Ranking por temporadas y por ambiente.**
4. **Seguridad cuentas:** recuperación contraseña por correo y límite intentos login (*rate limiting*).
5. **Pruebas extremo a extremo** automatizadas en CI (Playwright) y medición cobertura.
6. **Aplicación instalable (PWA)** para jugar desde móvil como app.

---

## 16. Índice de capturas

Carpetas en `docs/capturas/` (copiadas a `figs/capturas/` para memoria):
- `app/`: 13 capturas (01-inicio a 13-pagina-no-encontrada)
- `donetonic/`: 8 capturas (01-tablero-sprint a 08-pbi-detalle)
- `fase7/`: 12 capturas (01-sprites-antes a 12-pausa-salir)
- `hito4/`: 11 capturas (01-entrar-google a 11-privacidad)
- `juego/`: 16 capturas (01-menu a 16-final-copa)
- `produccion/`: 3 capturas (01-correo-confirmacion a 03-google-publicada)
- `prueba-tecnica/`: 2 capturas (01-dominio-permitido, 02-subdominio-rechazado)

Descripción de cada captura en `docs/capturas/README.md` y en la lista de imágenes disponibles del borrador de memoria.
