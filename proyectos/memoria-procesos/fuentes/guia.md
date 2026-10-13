# La Grada Colchonera: guía completa del proyecto

> Proyecto individual de **Procesos de Ingeniería del Software (PIS), curso 2026-2027**, planteado como un TFG.
> Esta guía recoge lo que se ha hecho en el **Sprint 1** hasta el 12/10/2026. Solo describe trabajo real: lo que está en el repositorio, en DoneTonic y en los servicios en la nube.

| | |
|---|---|
| **Repositorio** | https://github.com/VelaElDios/la-grada-colchonera-saas |
| **Aplicación (principal)** | https://la-grada-colchonera-1081564062572.europe-southwest1.run.app (Google Cloud Run) |
| **Aplicación (alternativa)** | https://la-grada-colchonera.onrender.com (Render) |
| **Gestión** | DoneTonic: espacio *TFG*, proyecto *Colchoneros*, *Sprint 1* |
| **Alcance de la primera entrega** | Hitos 1, 2 y 3 del enunciado |

---

## Índice

1. [Objetivo y contexto](#1-objetivo-y-contexto)
2. [Requisitos](#2-requisitos)
3. [Decisiones y por qué](#3-decisiones-y-por-qué)
4. [Arquitectura](#4-arquitectura)
5. [Procesos: flujo de trabajo, CI/CD y gestión](#5-procesos-flujo-de-trabajo-cicd-y-gestión)
6. [Herramientas](#6-herramientas)
7. [Resultados en cifras](#7-resultados-en-cifras)
8. [Problemas y cómo se resolvieron](#8-problemas-y-cómo-se-resolvieron)
9. [Pendiente](#9-pendiente)
10. [Fuentes y referencias](#10-fuentes-y-referencias)

---

## 1. Objetivo y contexto

### La asignatura
El enunciado pide diseñar e implementar, de forma individual, **la estructura base de una aplicación SaaS** organizada en capas y con gestión de usuarios. Evalúa la aplicación y también **el proceso**: cómo llega cada cambio del editor a producción (ramas, pull requests, CI y despliegue continuo).

El Sprint 1 dura un mes, del 29/09/2026 al 27/10/2026, y el enunciado lo divide en cuatro hitos semanales orientativos:

| Hito | Contenido según el enunciado |
|---|---|
| 1. Esqueleto y backend | Repositorio y flujo con ramas y PR, CI, despliegue continuo, lógica de usuarios en memoria con pruebas y API |
| 2. Frontend y sesión | Interfaz y cliente separados, registro e inicio de sesión locales con hash, sesión y rutas protegidas |
| 3. Persistencia y roles | Base de datos real, secretos fuera del código, roles usuario/administrador y registro de actividad |
| 4. Servicios externos y cierre | OAuth, confirmación por correo, manejo de errores, README completo y revisión final |

### El alcance real de esta entrega
El profesor limitó **la primera entrega a los Hitos 1–3**. El Hito 4 (OAuth, confirmación por correo y manejo de errores avanzado) queda para la siguiente.

Se entregan **dos enlaces**: el del repositorio y el de la aplicación desplegada en Google Cloud. Por eso todo, incluida la gestión hecha en DoneTonic, tiene que poder revisarse desde el repositorio.

### La aplicación
**La Grada Colchonera** es una red social tipo Twitter para la afición del Atlético de Madrid. En el Sprint 1 solo existe la parte de **gestión de usuarios**, con estética rojiblanca y sin escudo ni logo oficiales: es un *«proyecto de aficionado sin relación oficial con el Club Atlético de Madrid»*.

---

## 2. Requisitos

Resumen de los apartados 3 a 8 del enunciado y de su estado en esta entrega. La comprobación requisito a requisito, con evidencias, está en `docs/revision-entrega.md`.

| Apartado | Requisito | Estado |
|---|---|---|
| 3.1 | El backend sirve el frontend (mismo origen); el cliente no accede a la BD ni tiene lógica de negocio; toda la comunicación va por una API | ✅ |
| 3.2 | Backend en capas (API, lógica, datos) y frontend en presentación + cliente de comunicación | ✅ |
| 4.1 | Registro local | ✅ |
| 4.1 | … con confirmación por correo (cuenta *pendiente* hasta confirmar) | ⏳ Hito 4 |
| 4.1 | Inicio de sesión local, cierre de sesión que invalida la sesión y sesión que sobrevive a recargas | ✅ |
| 4.1 | Inicio de sesión con un proveedor OAuth | ⏳ Hito 4 |
| 4.2 | Roles usuario y administrador | ✅ |
| 4.2 | Listar usuarios (solo admin) con email, rol y estado | ✅ |
| 4.2 | Comprobar si un usuario está activo (solo admin) | ✅ (corregido en la revisión final) |
| 4.2 | El admin elimina a cualquiera; un usuario solo a sí mismo; un eliminado no puede volver a entrar | ✅ |
| 4.2 | Restricciones aplicadas en el servidor y primer administrador justificado | ✅ |
| 5 | Persistencia real, secretos fuera del repositorio, `.env.example`, hash seguro de contraseñas, rutas protegidas (401/403) y despliegue en un proveedor cloud con URL pública | ✅ |
| 6 | ≥5 pruebas unitarias de la lógica (al menos una de error), automatizadas y con un único comando; manejo de errores con feedback; registro de actividad; historial incremental | ✅ (manejo de errores: base hecha, el pulido es del Hito 4) |
| 7 | GitHub Flow (rama por cambio, pruebas en local y PR), CI en cada PR y en `main`, despliegue continuo sin pasos manuales | ✅ |
| 8 | URL del repo, URL pública y README con tecnologías justificadas, ejecución en local, pruebas, variables y acceso de administrador | ✅ |

---

## 3. Decisiones y por qué

### Tecnología

| Decisión | Por qué |
|---|---|
| **Node.js 22 + Express 5** | Un solo lenguaje (JavaScript) en cliente y servidor y un framework mínimo en el que las capas son módulos simples. Express 5 pasa los errores de las funciones `async` al manejador común. |
| **Frontend en HTML, CSS y JavaScript sin framework**, servido por Express | Mismo origen (sin CORS), nada que compilar, y la frontera entre interfaz (`ui.js`) y cliente (`api.js`) se ve en dos ficheros. |
| **PostgreSQL en Neon** (capa gratuita) | Base de datos relacional real, gestionada y gratuita. Las tablas se crean con migraciones SQL versionadas. |
| **Sesiones en el servidor** (`express-session` + `connect-pg-simple`) | La sesión se guarda en la tabla `session`, así sobrevive a reinicios y despliegues. Cerrar sesión la destruye **en el servidor**, que es lo que pide el apartado 4.1. |
| **bcrypt** (`bcryptjs`) | Hash seguro de contraseñas, como exige el apartado 5. Nunca se guardan en claro. |
| **`node:test`** para las pruebas, con **`pg-mem`** en local y **PostgreSQL 17 real** en el CI | No hace falta un framework externo, las pruebas corren en local sin base de datos y el CI las pasa contra un PostgreSQL de verdad. |
| **Docker** (`node:22-alpine`) | Imagen reproducible para Cloud Run: solo dependencias de producción, se ejecuta sin root y escucha en el puerto 8080. |

### Diseño

| Decisión | Por qué |
|---|---|
| **Patrón repositorio con inyección de dependencias**: dos repositorios (memoria y PostgreSQL) con el mismo contrato | El Hito 3 pide cambiar a una base de datos real **sin tocar la capa lógica**. `userService` recibe el repositorio por parámetro y las mismas pruebas de contrato se pasan a los dos. |
| **Baja lógica** (`status = 'deleted'`) | Un usuario eliminado no puede volver a entrar y la cuenta sigue en el listado del administrador. |
| **Mismo mensaje** para «email no registrado» y «contraseña incorrecta» | No revelar qué cuentas existen. |
| **Primer administrador desde `ADMIN_EMAIL` y `ADMIN_PASSWORD`** al arrancar (`ensureAdmin`) | No hay contraseñas en el código ni hace falta tocar la base de datos a mano. Es idempotente: si la cuenta existe, solo la promociona. El enunciado pide justificar esta decisión. |
| **Nunca se elimina ni se degrada al último administrador** | Evita quedarse sin nadie que pueda administrar. |
| **Permisos comprobados en el servidor** (`requireAuth` → 401, `requireRole` / `requireSelfOrRole` → 403) y otra vez en la lógica al eliminar o cambiar el rol | Ocultar un botón en la interfaz no basta (apartado 4.2). |
| **«Comprobar si está activo» solo para el administrador** | Al principio también podía consultarlo el propio usuario. En la revisión frase a frase contra el enunciado se vio que el apartado 4.2 lo reserva al administrador y se corrigió. |
| **Logs en JSON por la salida estándar** | La plataforma los recoge sola (Cloud Logging o Render) y se pueden filtrar por evento. Las contraseñas, hashes, cookies y secretos se ocultan. |
| **Secretos solo en variables de entorno**; en producción la app no arranca si falta uno | Mejor fallar al arrancar que funcionar de forma insegura. En local, `.env` (ignorado por git); en Cloud Run, Secret Manager. |
| **`REQUIRE_EMAIL_CONFIRMATION`** (por defecto `false`) | El estado `pending` y la regla «una cuenta pendiente no puede entrar» ya existen y tienen pruebas, pero el envío de correos es del Hito 4. |

### Despliegue

| Decisión | Por qué |
|---|---|
| **Render primero** (capa gratuita, configuración en `render.yaml`) | Despliegue continuo desde el primer hito, como pide el enunciado. |
| **Google Cloud Run como despliegue principal** (cambio de alcance: PBI P19) | El profesor repartió créditos de Google Cloud para educación. Se añadió P19 al sprint para aprovecharlos. Render se mantiene como alternativa. |
| **Workload Identity Federation** | GitHub Actions se identifica ante Google con un token temporal: no hay ninguna clave guardada en GitHub. |
| **Dos cuentas de servicio** (`grada-runtime` y `grada-deploy`) | Mínimo privilegio: la que ejecuta la app solo lee sus secretos y la que despliega solo puede desplegar. |
| **Despliegue tras el CI en verde** (`workflow_run`) | El enunciado no lo exige, pero así nunca se despliega un commit que no ha pasado las pruebas. |

### Proceso

| Decisión | Por qué |
|---|---|
| **GitHub Flow por hitos**: `main` ← `hito-N/integracion` ← `hito-N/Tx-…` | Una rama y un PR por tarea de DoneTonic, y un PR de cierre por hito: la trazabilidad tarea → rama → PR queda en el historial. |
| **Ramas protegidas** (`main` y `hito-*/integracion`): solo admiten PR y exigen el check *Pruebas* en verde | El enunciado dice que no se integra con el CI en rojo, y GitHub lo hace cumplir. |
| **Una release por hito** (`hito-1`, `hito-2`, `hito-3`) y `sprint-1` | Lo recomienda el enunciado para ver la evolución. |
| **19 PBIs en DoneTonic, todos MUST**, sacados del enunciado y ordenados por hito | Cada requisito obligatorio es un PBI con una o dos tareas. |
| **Memoria tipo TFG en LuaLaTeX**, en `memoria/` | Primero se aplazó. Después se dejó la estructura preparada en el repo para escribirla más adelante. |

---

## 4. Arquitectura

### 4.1 Capas

```
┌──────────────────────────── NAVEGADOR ────────────────────────────┐
│                                                                   │
│   Presentación (GUI)                Cliente de comunicación       │
│   public/js/ui.js      ───────────▶ public/js/api.js              │
│   vistas, navegación #/ruta,         único punto que hace fetch,  │
│   mensajes al usuario                convierte errores en ApiError│
└───────────────────────────────────────────┬───────────────────────┘
                                            │ HTTP + JSON
                                            │ cookie de sesión grada.sid
┌──────────────────────── SERVIDOR (Express 5) ─────────────────────┐
│                                                                   │
│   Capa API            src/api/                                    │
│   rutas, sesión, requireAuth / requireRole, logs de peticiones,   │
│   manejador de errores común { error: { code, message } }         │
│        │                                                          │
│        ▼                                                          │
│   Lógica de negocio   src/services/                               │
│   userService: registro, autenticación, roles, bajas,             │
│   último administrador, ensureAdmin  (no sabe nada de HTTP ni BD) │
│        │                                                          │
│        ▼                                                          │
│   Acceso a datos      src/repositories/                           │
│   ┌──────────────────────┐      ┌──────────────────────────────┐  │
│   │ memoryUserRepository │  ó   │ postgresUserRepository       │  │
│   │ (desarrollo/pruebas) │      │ (producción, consultas       │  │
│   └──────────────────────┘      │  parametrizadas)             │  │
│                                 └──────────────┬───────────────┘  │
│   src/app.js es el único sitio donde se conectan las capas        │
└────────────────────────────────────────────────┼──────────────────┘
                                                 ▼
                                   PostgreSQL (Neon, Frankfurt)
                                   tablas: users, session,
                                           schema_migrations
```

**Dónde está la frontera entre capas** (el enunciado avisa de que se puede preguntar en la prueba individual):

- `src/api/users.js` llama a `userService.*`: es la frontera API → lógica.
- `src/services/userService.js` llama a `userRepository.*`: es la frontera lógica → datos.
- `src/app.js` es el único fichero que conecta las tres capas.
- En el navegador, `ui.js` llama a `api.*`: es la frontera presentación → cliente.

### 4.2 Modelo de datos

```
users
├── id             UUID  (clave primaria)
├── email          TEXT  único
├── password_hash  TEXT  (bcrypt; vacío en cuentas OAuth futuras)
├── role           'user' | 'admin'
├── status         'pending' | 'active' | 'deleted'
├── auth_provider  'local' | 'google'      ← preparado para el Hito 4
├── created_at     TIMESTAMPTZ
└── deleted_at     TIMESTAMPTZ

session            (formato de connect-pg-simple)
└── sid, sess (JSON), expire

schema_migrations  (las migraciones ya aplicadas)
```

Un usuario está **activo** cuando `status = 'active'`, es decir, confirmado y no eliminado. No tiene que ver con estar conectado.

### 4.3 Inicio de sesión y sesión

```
Navegador                     API (Express)                   Lógica / Datos
   │ POST /api/auth/login        │                                │
   │ {email, password} ─────────▶│ userService.authenticate() ───▶│ busca el email
   │                             │                                │ compara el hash bcrypt
   │                             │◀─────────── usuario o error ───│
   │                             │ session.regenerate()   (evita la fijación de sesión)
   │                             │ session.userId = id   (se guarda en la tabla session)
   │◀── 200 + cookie grada.sid ──│   httpOnly, sameSite=lax, secure en producción, 7 días
   │                             │
   │ (recarga la página)         │
   │ GET /api/auth/me ──────────▶│ lee la sesión → vuelve a leer el usuario
   │◀── 200 usuario ─────────────│ (si está eliminado, la sesión deja de valer)
   │                             │
   │ POST /api/auth/logout ─────▶│ session.destroy() en el servidor + borra la cookie
   │◀── 204 ─────────────────────│
```

### 4.4 API

| Método | Ruta | Acceso | Qué hace |
|---|---|---|---|
| GET | `/api/health` | Público | Comprueba que el servidor está en marcha |
| POST | `/api/auth/register` | Público | Registro con email y contraseña (mínimo 8 caracteres) |
| POST | `/api/auth/login` | Público | Inicia sesión |
| POST | `/api/auth/logout` | Público | Cierra la sesión |
| GET | `/api/auth/me` | Sesión | Usuario con la sesión iniciada |
| GET | `/api/users` | Admin | Listado (email, rol, estado) |
| GET | `/api/users/:id/active` | Admin | ¿Está activo? |
| PATCH | `/api/users/:id/role` | Admin | Cambia el rol |
| DELETE | `/api/users/:id` | El propio usuario o un admin | Baja lógica |

### 4.5 Infraestructura desplegada

```
                 GitHub (VelaElDios/la-grada-colchonera-saas)
                 ├── workflow CI (Pruebas + Imagen Docker)
                 └── workflow Despliegue en Cloud Run
                          │  token temporal (Workload Identity Federation,
                          │  limitado a este repositorio)
                          ▼
┌─────────────── Google Cloud · proyecto la-grada-colchonera-27775 ─────────────┐
│  Artifact Registry (repo "grada")  ──imagen──▶  Cloud Run "la-grada-colchonera"│
│                                                 europe-southwest1 (Madrid)     │
│  Secret Manager                                 0–2 instancias · 512 MiB       │
│   database-url · session-secret     ──────────▶ cuenta de servicio             │
│   admin-email  · admin-password                 grada-runtime                  │
│                                                         │                      │
│  Cloud Logging ◀────────────── logs JSON ───────────────┤                      │
└─────────────────────────────────────────────────────────┼──────────────────────┘
                                                          │ DATABASE_URL
                                                          ▼
                                        Neon · PostgreSQL · proyecto la-grada-colchonera
                                        AWS Europe Central 1 (Frankfurt) · base "grada"
                                                          ▲
Render (alternativo) · render.yaml ───────────────────────┘
(las dos plataformas usan la misma base de datos, así que muestran los mismos datos)
```

---

## 5. Procesos: flujo de trabajo, CI/CD y gestión

### 5.1 Flujo de ramas (GitHub Flow por hitos)

```
main ──●──────────────────────●──────────────────●──────────────────●──────────────●──▶
       │                      ▲ PR #9  hito-1    ▲ PR #17 hito-2    ▲ PR #24 hito-3  ▲ PR #29 sprint-1
       │                      │                  │                  │                ▲ PR #32 (978098e)
       └─ hito-1/integracion ─┘                  │                  │
            ▲  ▲  ▲  ...  (PRs #1–#8 y #10)     │                  │
            │  │  └ hito-1/T3-integracion-continua                  │
            │  └ hito-1/T2-github-flow           │                  │
            └ hito-1/T1-estructura-base          │                  │
                         hito-2/integracion ─────┘ (PRs #11–#16)    │
                                    hito-3/integracion ─────────────┘ (PRs #18–#23)
                                    hito-4/integracion → PRs #25–#28, #30, #31, #33
```

Pasos de cada tarea (según `CONTRIBUTING.md`):

```
DoneTonic: tarea Tx ─▶ rama hito-N/Tx-descripcion ─▶ commits "[Tx] …"
   ─▶ npm test en local ─▶ PR "[Tx] …" hacia hito-N/integracion
   ─▶ CI en verde (obligatorio) ─▶ merge ─▶ tarea en HECHO
Cierre del hito: PR hito-N/integracion → main ─▶ CI ─▶ despliegue ─▶ release hito-N
```

### 5.2 Pipeline de CI/CD

```
 push / pull_request
        │
        ▼
 ┌──────────────── CI (.github/workflows/ci.yml) ────────────────┐
 │ Job "Pruebas"                    Job "Imagen Docker"           │
 │  · servicio postgres:17           · docker build               │
 │  · npm ci                         · docker run                 │
 │  · npm test con TEST_DATABASE_URL · curl /api/health           │
 └───────────────────────────────┬───────────────────────────────┘
                                 │ solo si es un push a main y el CI termina en verde
                                 ▼
 ┌──────── Despliegue en Cloud Run (deploy-cloud-run.yml) ────────┐
 │ 1. checkout del commit probado                                 │
 │ 2. autenticación en Google (Workload Identity Federation)      │
 │ 3. docker build + push a Artifact Registry                     │
 │ 4. gcloud run deploy --set-secrets … (0–2 instancias, 512Mi)   │
 │ 5. smoke test: hasta 20 intentos de /api/health                │
 └────────────────────────────────────────────────────────────────┘

 En paralelo: Render despliega main según render.yaml.
 Además: el workflow "Memoria" compila la memoria (LuaLaTeX) cuando cambia memoria/.
```

Si una versión no arranca, por ejemplo porque falta un secreto, ni Cloud Run ni Render la ponen en marcha y siguen sirviendo la anterior.

### 5.3 Gestión ágil en DoneTonic

- **Estructura:** espacio *TFG*, equipo y proyecto *Colchoneros*, **Sprint 1** del 29/09/2026 al 27/10/2026.
- **Backlog:** 19 PBIs (P1–P19) con 32 tareas (T1–T32), etiquetados por hito y todos MUST.
- **Definición de hecho:** el código está en su rama y en un PR con la tarea, el CI pasa, el PR está integrado y la documentación está actualizada si hace falta.
- **Seguimiento:** cuando se fusiona el PR de una tarea, esta pasa a HECHO, y cuando están todas, el PBI pasa a HECHO solo.
- **Gráficas en *Paneles Scrum*:** Sprint Burnup, Sprint Burndown, Backlog Burndown, Backlog Burnup y Velocity Chart.

| PBI | Hito | Título | Tareas | Estado |
|---|---|---|---|---|
| P1 | H1 | Repositorio GitHub y flujo GitHub Flow | T1, T2 | Hecho |
| P2 | H1 | Integración continua (CI) | T3 | Hecho |
| P3 | H1 | Despliegue continuo en URL pública | T4 | Hecho |
| P4 | H1 | Lógica de gestión de usuarios (en memoria) | T5, T6 | Hecho |
| P5 | H1 | Pruebas unitarias automatizadas | T7 | Hecho |
| P6 | H1 | Capa API de usuarios | T8 | Hecho |
| P7 | H2 | Frontend: interfaz y cliente separados | T9, T10 | Hecho |
| P8 | H2 | Registro e inicio de sesión locales | T11, T12 | Hecho |
| P9 | H2 | Cierre y mantenimiento de la sesión | T13 | Hecho |
| P10 | H2 | Rutas protegidas en el servidor | T14 | Hecho |
| P11 | H3 | Persistencia en base de datos real | T15, T16 | Hecho |
| P12 | H3 | Gestión de secretos | T17 | Hecho |
| P13 | H3 | Roles de usuario y administrador | T18, T19 | Hecho |
| P14 | H3 | Registro (log) de la actividad | T20 | Hecho |
| P15 | H4 | Login con OAuth | T21, T22 | Siguiente entrega |
| P16 | H4 | Confirmación de cuenta por correo | T23, T24 | Siguiente entrega |
| P17 | H4 | Manejo de errores y feedback | T25, T26 | Siguiente entrega |
| P18 | H4 | README y revisión de la entrega | T27, T28, T31, T32 | Hecho |
| P19 | H4 | Despliegue continuo en Google Cloud Run | T29, T30 | Hecho |

**Evolución de la entrega** (PBIs pendientes de los 16 del alcance; tabla de `docs/gestion/README.md`):

```
PBIs pendientes
15 │ ■
   │ ■
 9 │ ■  ■
   │ ■  ■
 5 │ ■  ■  ■
   │ ■  ■  ■
 2 │ ■  ■  ■     ■
 1 │ ■  ■  ■  ■  ■
 0 └─────────────────■──
   Ini H1 H2 H3 +P19 Cierre
```

El escalón «+P19» corresponde al **cambio de alcance**: se añadió el despliegue en Cloud Run cuando llegaron los créditos de Google Cloud.

---

## 6. Herramientas

| Herramienta | Para qué se usó |
|---|---|
| **GitHub** | Repositorio público, ramas protegidas, pull requests, releases y GitHub Actions |
| **GitHub Actions** | Workflows *CI*, *Despliegue en Cloud Run* y *Memoria*. Acciones: `actions/checkout@v4`, `actions/setup-node@v4`, `google-github-actions/auth@v2`, `google-github-actions/setup-gcloud@v2`, `xu-cheng/latex-action@v3` y `actions/upload-artifact@v4` |
| **VS Code** | Editor y `git push` del repositorio local |
| **DoneTonic** | Backlog, sprint, tablero de tareas y gráficas |
| **Google Cloud** | Cloud Run, Artifact Registry, Secret Manager, IAM y Workload Identity Federation, Cloud Logging y Cloud Shell. La preparación es el script `scripts/gcp/preparar-cloud-run.sh` |
| **Render** | Despliegue alternativo en la capa gratuita, con `render.yaml` |
| **Neon** | PostgreSQL gestionado en la capa gratuita |
| **Docker** | Imagen de la aplicación para Cloud Run |
| **Node.js 22** y dependencias | `express`, `express-session`, `connect-pg-simple`, `pg` y `bcryptjs`; en desarrollo, `pg-mem` |
| **Playwright + Chromium** | Generar las capturas de la aplicación (`docs/capturas/app`) contra un PostgreSQL de prueba |
| **LaTeX** | LuaLaTeX, `latexmk`, `biblatex` y `biber` para la memoria |
| **Claude (Cowork)** | Asistente que escribió el código, los documentos y los commits (con autoría del alumno y el trailer `Co-Authored-By`), y creó y fusionó los PRs y actualizó DoneTonic en el navegador. Las cuentas y las credenciales (Neon, Render y Google Cloud) las creó y configuró el alumno |

---

## 7. Resultados en cifras

### Entrega
| | |
|---|---|
| Último commit de `main` | `978098e` (PR #32, 12/10/2026) |
| Despliegue de ese commit en Cloud Run | Automático tras el CI, en 58 s. Se comprobó que `/api/health` responde 200 y `/api/users` sin sesión responde 401 |
| Releases | `hito-1`, `hito-2`, `hito-3` y `sprint-1` |

### Repositorio
| Métrica | Valor |
|---|---|
| Commits en `main` | 65 (33 de trabajo + 32 merges de PR) |
| Pull requests | 33 (#1–#33), todos integrados |
| Ramas en GitHub | 33: `main`, 4 de integración y 28 de tarea |
| Código del servidor (`src/`) | 1.128 líneas de JavaScript |
| Frontend (`public/`) | 657 líneas |
| Pruebas (`tests/`) | 992 líneas en 13 ficheros |
| Migraciones SQL | 2 (`users` y `session`) |
| Capturas en la documentación | 7 de la aplicación + 3 de DoneTonic |
| Ejecuciones de GitHub Actions | 71 al cerrar la entrega (el workflow CI iba por la #65) |

### Pruebas
| | |
|---|---|
| Total | **80 pruebas automatizadas**: 79 en local y 1 de extremo a extremo que solo se ejecuta contra PostgreSQL real (en el CI) |
| Pruebas unitarias de la lógica (`userService`) | 26: email repetido, cuenta pendiente que intenta entrar, usuario que intenta eliminar a otro, último administrador… |
| Resto | API de autenticación (10), API de usuarios (11), repositorios (12: las mismas 6 pruebas de contrato para memoria y para PostgreSQL), logger (6), configuración (5), migraciones (3), frontend (3), arranque (2), salud (1) |
| Comando | `npm test` |

### Gestión
| | |
|---|---|
| PBIs | 19, de los que 16 están hechos (los 3 restantes son del Hito 4) |
| Tareas | 32 |
| Sprint Burnup y Burndown en DoneTonic | 84 % completado y 3 PBIs pendientes |

### Consumo en Neon (12/10/2026, plan gratuito)
| | Usado | Límite gratis |
|---|---|---|
| Cómputo | 0,27 CU-h | 100 CU-h al mes por proyecto |
| Almacenamiento | 0,03 GB | 1 GB por proyecto |
| Transferencia | 0 GB | 5 GB al mes |

### Memoria
- La carpeta `memoria/` está preparada: portada, resumen y abstract, 7 capítulos con guion, 2 anexos y bibliografía. Compila con LuaLaTeX a **16 páginas**, aunque todavía no tiene texto.

### Observación sobre el historial
Los 33 commits de trabajo tienen fecha **12/10/2026**. El historial es incremental en cuanto a estructura (una rama, un commit y un PR por tarea, con el CI en cada paso), pero está concentrado en un solo día. El apartado 6 dice que se espera *«un historial de commits con mensajes representativos del progreso, no una única entrega masiva»*. Conviene tenerlo presente para la prueba individual.

---

## 8. Problemas y cómo se resolvieron

### Desarrollo y pruebas
| Problema | Solución |
|---|---|
| `pg-mem` no admitía algunas construcciones de PostgreSQL (`CREATE TABLE IF NOT EXISTS` en un caso concreto, `to_timestamp`/JSON de las sesiones) | Se cambió a una consulta a `information_schema`, y la prueba de sesiones en la base de datos solo se ejecuta contra PostgreSQL real (en el CI) |
| Con `NODE_ENV=production` sobre HTTP, el navegador no guardaba la cookie de sesión (es `secure`) | Es el comportamiento correcto. Las capturas locales se hicieron en modo desarrollo |
| `pkill -f "node src/server.js"` cerraba también la propia shell que lo lanzaba | El servidor se arrancó con `setsid` desde un script |
| La tabla del panel de administración no cabía en 640 px y el botón *Eliminar* quedaba oculto | Contenedor más ancho para esa vista y, en el móvil, cada usuario se muestra como una tarjeta |
| Las capturas de GitHub hechas con Playwright salían sin estilos (sus recursos estaban bloqueados) | Se descartaron. Las de la aplicación sí se generaron bien |
| Docker Hub estaba bloqueado en el entorno de trabajo de la nube | Se simuló la imagen (`npm ci --omit=dev` y arranque en producción) y se validó de verdad en el job *Imagen Docker* del CI, que salió en verde |

### Despliegue en Google Cloud
| Problema | Solución |
|---|---|
| El script de preparación falló en Artifact Registry con `PERMISSION_DENIED`, porque los permisos de IAM tardan en propagarse | Se relanzó con `PROJECT_ID=la-grada-colchonera-27775`. El script es idempotente y no repite lo que ya existe |
| El secreto `database-url` se introdujo mal | Se añadió una versión nueva del secreto (versión 2) con `gcloud secrets versions add` |
| La URL de Cloud Run daba 404 | Todavía no se había hecho el primer despliegue. Al ejecutarse el workflow, respondió bien |
| La cadena de conexión de Neon, con su contraseña, se pegó en el chat | Se recomendó cambiar la contraseña. Se decidió no hacerlo (ver *Pendiente*) |

### Git y GitHub
| Problema | Solución |
|---|---|
| `git push --all` rechazado en las ramas de integración (*non-fast-forward*) porque las copias locales estaban desfasadas | `git fetch` y `git branch -f hito-N/integracion origin/hito-N/integracion` |
| Desde el entorno de la nube no se puede hacer `push` a GitHub (sin permiso de escritura) | Los commits se pasan al repositorio local con `git bundle`, y el alumno hace `git push --all origin` desde VS Code |
| Un *bundle* exigía un commit que el repositorio local aún no tenía | Se regeneró tomando como base un commit que sí estaba en local (`4b16182`) |
| Al subir el *bundle* con el mismo nombre se escribía la versión anterior | Se subió con otro nombre |
| Algunos merges en el navegador fallaban o tardaban | Se esperaba a que GitHub terminara de comprobar el PR y se hacía clic en el botón real (*Merge pull request → Confirm merge*) |

### Alcance y revisión
| Problema | Solución |
|---|---|
| Al leer el PDF completo se vio que la entrega exige OAuth y confirmación por correo (apartado 4.1), que no estaban hechos | El profesor limitó la primera entrega a los Hitos 1–3. Lo que había de Hito 4 se guardó sin subir para la siguiente entrega |
| El enunciado reserva «comprobar si un usuario está activo» al administrador, pero la API dejaba consultarlo también al propio usuario | Se cambió a solo administrador y se actualizó la prueba (PR #30) |
| Los primeros documentos de revisión se habían redactado a partir de los PBIs, no del PDF | `docs/revision-entrega.md` se reescribió frase a frase siguiendo los apartados 3 a 8 |

### Memoria (LaTeX)
| Problema | Solución |
|---|---|
| Al compilar con la salida en `build/`, `\include{capitulos/…}` no podía escribir su `.aux` | `.latexmkrc` crea antes las subcarpetas (`make_path`) |
| En el entorno de pruebas faltaban paquetes de LuaLaTeX (`luaotfload`, `biber`, `biblatex`) | Se instalaron. En GitHub compila con el workflow *Memoria* |

### DoneTonic
| Problema | Solución |
|---|---|
| Menús apilados y clics por JavaScript que no se aplicaban (DoneTonic está hecho con Flutter) | Clics reales por coordenadas, comprobando después el estado en el árbol de accesibilidad |
| Al emular un tamaño de ventana mayor, Flutter dejaba de pintar bien la página | Las capturas se hicieron con el tamaño real del panel (800 px de ancho) |

---

## 9. Pendiente

- **Hito 4** (siguiente entrega): OAuth (P15), confirmación por correo (P16) y manejo de errores y feedback (P17).
  - Hay trabajo guardado sin subir en `.git/claude/hito4-wip.bundle` del repositorio local:
    - `hito-4/T23-servicio-correo`: correo por SMTP con `nodemailer` y tokens firmados con HMAC.
    - `hito-4/T24-confirmacion-correo`: completo, con pruebas.
    - `hito-4/T22-login-google`: a medias.
  - Para activarlo hará falta un cliente OAuth de Google en el proyecto de Google Cloud y una cuenta SMTP (por ejemplo, Gmail con contraseña de aplicación o Brevo), con sus secretos en Secret Manager.
- **Escribir la memoria** en `memoria/`.
- **Rediseño visual** de la web cuando haya más funcionalidad.
- **Enviar las credenciales del administrador** junto con la entrega. Son los valores de `admin-email` y `admin-password`, que no están en el repositorio.
- **Cambiar la contraseña de Neon** (recomendado, porque se compartió en el chat).
- La release `sprint-1` apunta a `4b16182`, el commit anterior a la revisión final. Si se quiere que una etiqueta marque exactamente lo entregado, falta crear una sobre `978098e`.

---

## 10. Fuentes y referencias

### Documento base
- *Especificación del Proyecto. Procesos de Ingeniería del Software, curso 2026-2027 (Sprint 1)*. PDF del enunciado de la asignatura.

### Consultadas durante el proyecto
- Neon. *What are the limits and quotas for Neon's Free plan?* https://neon.com/faqs/free-plan-limits-and-quotas

### Referencias recogidas en la bibliografía de la memoria (`memoria/bibliografia.bib`)
- Express, Node.js web application framework. https://expressjs.com/
- GitHub. *GitHub flow*. https://docs.github.com/en/get-started/using-github/github-flow
- OpenJS Foundation. *Node.js*. https://nodejs.org/
- The PostgreSQL Global Development Group. *PostgreSQL*. https://www.postgresql.org/
- Google Cloud. *Cloud Run documentation*. https://cloud.google.com/run/docs
- GitHub. *GitHub Actions documentation*. https://docs.github.com/en/actions
- Schwaber, K. y Sutherland, J. (2020). *The Scrum Guide*. https://scrumguides.org/scrum-guide.html

### Documentación del propio repositorio
- `README.md`: visión general, tecnologías, ejecución, pruebas, variables, API, despliegue y acceso de administrador.
- `CONTRIBUTING.md`: flujo de trabajo con ramas y PR.
- `docs/revision-entrega.md`: requisitos del enunciado y su evidencia.
- `docs/gestion/README.md`: backlog, trazabilidad tarea → rama → PR, burndown y capturas de DoneTonic.
- `memoria/README.md`: cómo compilar la memoria.
