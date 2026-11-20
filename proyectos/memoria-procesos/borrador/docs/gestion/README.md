# Gestión del proyecto: backlog, trazabilidad y evolución

Este documento recoge la información de DoneTonic (espacio de trabajo **TFG**, equipo **Colchoneros**) exportada para la memoria. Fecha de captura: 29/10/2026 (dos sprints cerrados).

---

## Backlog Sprint 1 (19 PBIs, 32 tareas)

| PBI | Hito | Título | Tareas | Prioridad | Etiquetas |
|-----|------|--------|--------|-----------|-----------|
| P1 | Hito 1 | Repositorio GitHub y flujo GitHub Flow | T1, T2 | MUST | Hito 1 |
| P2 | Hito 1 | Integración continua (CI) | T3 | MUST | Hito 1 |
| P3 | Hito 1 | Despliegue continuo en URL pública | T4 | MUST | Hito 1 |
| P4 | Hito 1 | Lógica de gestión de usuarios (en memoria) | T5, T6 | MUST | Hito 1 |
| P5 | Hito 1 | Pruebas unitarias automatizadas de la lógica | T7 | MUST | Hito 1 |
| P6 | Hito 1 | Capa API de usuarios | T8 | MUST | Hito 1 |
| P7 | Hito 2 | Frontend: interfaz y cliente de comunicación separados | T9, T10 | MUST | Hito 2 |
| P8 | Hito 2 | Registro e inicio de sesión locales | T11, T12 | MUST | Hito 2 |
| P9 | Hito 2 | Cierre de sesión y mantenimiento de la sesión | T13 | MUST | Hito 2 |
| P10 | Hito 2 | Rutas protegidas en el servidor | T14 | MUST | Hito 2 |
| P11 | Hito 3 | Persistencia en base de datos real | T15, T16 | MUST | Hito 3 |
| P12 | Hito 3 | Gestión de secretos con variables de entorno | T17 | MUST | Hito 3 |
| P13 | Hito 3 | Roles de usuario y administrador | T18, T19 | MUST | Hito 3 |
| P14 | Hito 3 | Registro (log) de la actividad | T20 | MUST | Hito 3 |
| P15 | Hito 4 | Inicio de sesión con proveedor externo (OAuth) | T21, T22 | MUST | Hito 4 |
| P16 | Hito 4 | Confirmación de cuenta por correo electrónico | T23, T24 | MUST | Hito 4 |
| P17 | Hito 4 | Manejo de errores y feedback al usuario | T25, T26 | MUST | Hito 4 |
| P18 | Hito 4 | README completo y revisión de la entrega | T27, T28, T31, T32 | MUST | Hito 4 |
| P19 | Hito 4 | Despliegue continuo en Google Cloud Run | T29, T30 | MUST | Hito 4 |

**Total Sprint 1:** 19 PBIs, 32 tareas. Todos MUST (requisitos obligatorios del enunciado).

---

## Backlog Sprint 2 (29 PBIs, 50 tareas)

| PBI | Etiqueta | Título | Tareas | Prioridad |
|-----|----------|--------|--------|-----------|
| P20 | Base del juego | Rediseño de la interfaz web y menú del juego | T33, T34 | MUST |
| P21 | Base del juego | Motor de la partida survivor | T35, T36 | MUST |
| P22 | Base del juego | Gráficos pixel art y cámara 3/4 | T37, T38 | MUST |
| P23 | Base del juego | Jugadores, entrenadores y Vestuario | T39, T40, T41 | MUST |
| P24 | Base del juego | Armas, habilidades y mejoras | T42, T43 | MUST |
| P25 | Base del juego | Rivales con comportamiento propio | T44, T45 | MUST |
| P26 | Base del juego | Jefes con fases | T46, T47 | MUST |
| P27 | Base del juego | Mapa con terreno y obstáculos | T48, T49 | MUST |
| P28 | Base del juego | Controles, pantalla completa y ajustes | T50, T51 | MUST |
| P29 | Fase 2 · Club | Progreso del juego guardado en el servidor | T52, T53 | MUST |
| P30 | Fase 2 · Club | Contratos: fichar jugadores | T54 | MUST |
| P31 | Fase 2 · Club | Entrenamiento de jugadores | T55 | MUST |
| P32 | Fase 2 · Club | Ranking de la grada | T56 | MUST |
| P33 | Fase 3 · Ultras | Combinaciones y ULTRAS | T57, T58 | MUST |
| P34 | Fase 3 · Ultras | Dificultad equilibrada y modo pruebas | T59, T60 | MUST |
| P35 | Fase 4 · Mundo | Mundo procedural natural | T61 | MUST |
| P36 | Fase 4 · Mundo | Ambientes por finales | T62 | MUST |
| P37 | Fase 4 · Mundo | Mote y avatar | T63 | MUST |
| P38 | Fase 5 · Rarezas | Rarezas por historia rojiblanca y fichajes | T64, T65 | MUST |
| P39 | Fase 5 · Rarezas | Habilidades niveladas por minuto | T66 | MUST |
| P40 | Fase 5 · Rarezas | Combinaciones y ultras a la vista | T67 | MUST |
| P41 | Fase 5 · Rarezas | Colisiones exactas | T68 | MUST |
| P42 | Fase 6 · Logros y sonido | Logros con historia y equipaciones | T69, T70 | MUST |
| P43 | Fase 6 · Logros y sonido | Pantalla de fin con estadísticas | T71 | MUST |
| P44 | Fase 6 · Logros y sonido | Música chiptune y la grada | T72, T73, T74 | MUST |
| P45 | Fase 6 · Logros y sonido | Muñecos con más detalle | T75 | MUST |
| P46 | Fase 6 · Logros y sonido | Jefes más duros | T76 | MUST |
| P47 | Calidad | Corrección de errores detectados | T77, T78, T79 | MUST |
| P48 | Calidad | Documentación y gestión del Sprint 2 | T80, T81, T82 | MUST |

**Total Sprint 2:** 29 PBIs, 50 tareas. Todos MUST (profesor fijó lógica del juego como objetivo).

---

## Definición de Hecho (DoD)

### Tarea
- Código en un Pull Request que referencia la tarea (ej. `[T5] ...`).
- Pruebas automáticas pasan en el CI (check **Pruebas** en verde).
- PR fusionado en la rama de integración del hito (Sprint 1) o en `main` (Sprint 2).
- Documentación actualizada si procede: `README.md`, carpeta `docs/`, `.env.example`.

### Hito (Sprint 1)
- Rama del hito (`hito-N/integracion`) fusionada en `main`.
- Desplegada en la URL pública y funcionando.
- Publicada como release en GitHub (`hito-1`, `hito-2`, `hito-3`, `hito-4`).

### Fase del juego (Sprint 2)
- PR de la fase fusionado en `main`.
- Desplegado en la URL pública.
- Probado a mano en el navegador (partida completa, menús, club, etc.).

---

## Historias de usuario Sprint 2 (29 HU con criterios de aceptación)

Las siguientes 29 historias de usuario están registradas en DoneTonic con sus criterios. Se corresponden 1 a 1 con los PBIs P20–P48.

| PBI | Historia de usuario | Criterios de aceptación (resumidos) |
|-----|---------------------|--------------------------------------|
| P20 | **Rediseño interfaz y menú juego**. Como aficionado quiero una web con aspecto de juego, clara en móvil y ordenador, para que entrar a jugar sea lo primero que vea al iniciar sesión. | Sistema diseño propio (colores, espacios, tipografía Plus Jakarta Sans) en tokens CSS reutilizables; Modo oscuro rojiblanco toda la web y responsive; Con sesión iniciada el inicio es el menú del juego; cabecera solo muestra Jugar y Mi cuenta (y Administración al admin); Pantallas cuentas Sprint 1 siguen funcionando (pruebas verdes). |
| P21 | **Motor partida survivor**. Como jugador quiero una partida de supervivencia contra oleadas infinitas, en la que mis armas ataquen solas y yo solo tenga que moverme y elegir mejoras. | Simulación pura (sin DOM) paso fijo 1/60s y azar con semilla: misma semilla = misma partida; Oleadas cada 30s, XP al eliminar rivales, elección 1 de 3 mejoras al subir nivel; Dificultad crece sin parar (vida, daño, velocidad rivales); Pausa, fin partida, vuelta menú; partida se pausa al cambiar pestaña. |
| P22 | **Gráficos pixel art y cámara 3/4**. Como jugador quiero un estilo visual propio y reconocible, con muñecos «chibi» del Atleti, para que el juego tenga personalidad sin usar imágenes oficiales. | Muñecos 16×20 píxeles dibujados con código (sin imágenes), con caché fotogramas; Cámara 3/4 con inercia, inclinación al correr, destellos y aplastado al recibir golpes; Respeta `prefers-reduced-motion` (sin sacudidas ni partículas). |
| P23 | **Jugadores, entrenadores y Vestuario**. Como jugador quiero elegir entre leyendas del Atleti y un entrenador, cada uno con su estilo, para que cada partida se juegue distinta. | Stats por posición (portero, defensa, medio, delantero) retocadas por rasgos cada jugador; Cada jugador solo aprende habilidades que encajan con su forma de jugar; Dos entrenadores (Simeone y Luis Aragonés) con bonificaciones y ulti propia; Vestuario con filtro posición y ficha jugador. |
| P24 | **Armas, habilidades y mejoras**. Como jugador quiero muchas armas y habilidades que suban de nivel y se puedan combinar, para construir una estrategia distinta en cada partida. | Armas disparo y cuerpo a cuerpo que atacan solas, 5 niveles; Pasivas (botas, imán, pasión…) y mejoras extra sin límite cuando todo al máximo; Porteros no aprenden armas disparo. |
| P25 | **Rivales con comportamiento propio**. Como jugador quiero rivales variados que me obliguen a moverme, para que la partida no sea solo aguantar en un sitio. | 16 equipos con jugadores genéricos que se desbloquean por oleadas; Unos embisten avisando con «!» y otros disparan balones; Rivales rodean gradas y paredes para llegar al jugador. |
| P26 | **Jefes con fases**. Como jugador quiero jefes famosos con ataques propios cada pocas oleadas, para tener retos claros dentro de la partida. | Un jefe cada 4 oleadas, al azar entre disponibles y sin repetir hasta que salgan todos; 3 fases por vida (66% y 33%): más ataques, menos espera, más velocidad; Cada ataque fuerte se avisa en suelo antes de golpear. |
| P27 | **Mapa con terreno y obstáculos**. Como jugador quiero un campo con barro, lluvia, gradas y estructuras, para que moverse por el mapa sea parte del juego. | Barro frena, lluvia acelera balones, gradas no se atraviesan; Mapa procedural con biomas y estructuras distinto cada partida; Premios por campo señalados con flechas en borde pantalla. |
| P28 | **Controles, pantalla completa y ajustes**. Como jugador quiero jugar con teclado o con el dedo y ajustar el sonido y los gráficos, para jugar cómodo en cualquier dispositivo. | Teclado (WASD/flechas) y joystick táctil flotante en móvil; Pantalla completa (botón y tecla F) y menú pausa con ajustes dentro partida; Ajustes guardados en navegador: volumen, efectos, números daño, zoom, joystick. |
| P29 | **Progreso juego guardado en servidor**. Como jugador quiero que mi club y mis partidas se guarden en mi cuenta, para no perder el progreso al cambiar de dispositivo. | Tablas `juego_perfiles` y `juego_records` (migración 003) ligadas al usuario; API `/api/juego` protegida con sesión: perfil, empezar y terminar partida; Servidor valida cada resultado con su reloj (anti-trampas) y rechaza imposibles; Concurrencia optimista: dos peticiones a la vez no se pisan. |
| P30 | **Contratos: fichar jugadores**. Como jugador quiero ganar fichas de contrato venciendo jefes y canjearlas por jugadores nuevos, para ampliar mi plantilla. | Plantilla inicial 4 jugadores comunes (uno por posición); 1 ficha por cada 3 jefes vencidos en la cuenta; contrato nunca repite jugador; Probabilidad depende rareza jugador. |
| P31 | **Entrenamiento de jugadores**. Como jugador quiero entrenar a mis jugadores con los puntos que ganan, para que mejoren partida a partida. | Puntos por jefes (1 cada 3 con ese jugador) y por bajas (cada vez más caros); 4 stats (Vida, Defensa, Disparo, Suerte) hasta 20 puntos; Solo se gastan puntos libres; validado en servidor. |
| P32 | **Ranking de la grada**. Como jugador quiero compararme con el resto de aficionados, para tener un motivo para mejorar mi marca. | Una fila por usuario con su mejor partida (tiempo; en empate, nivel); Nunca se muestra el correo de nadie; Pestañas Mis partidas y La grada. |
| P33 | **Combinaciones y ULTRAS**. Como jugador quiero que juntar ciertas habilidades desbloquee combinaciones y poderes definitivos, para premiar las estrategias pensadas. | 24 combinaciones con nombre propio y bonus; 6 ULTRAS que se consiguen solas al completar combinaciones (Premio Puskás, Balón de Oro, Zamora…); Efecto visual propio y daño en parte porcentual (reducido contra jefes). |
| P34 | **Dificultad equilibrada y modo pruebas**. Como jugador quiero que el juego sea difícil pero justo, y como administrador quiero poder probarlo todo sin jugar horas. | Tramo final más duro desde minuto 9 y rivales curtidos desde 12; Ayuda inicial que se apaga en 8 minutos para poder vencer al primer jefe; Modo pruebas (solo admin): todos los jugadores y puntos sin tocar el ranking. |
| P35 | **Mundo procedural natural**. Como jugador quiero un mundo distinto en cada partida, con barrios, estadios, parques y mesetas, para que explorar tenga gracia. | Ruidos suaves para distrito, altura y humedad: todo encaja sin cortes; Estadios con gradas que miran al campo, plazas con tiendas, mesetas con escaleras; Casi todo el mapa alcanzable desde la salida (con pruebas). |
| P36 | **Ambientes por finales**. Como jugador quiero que cada 5 minutos la partida cambie de escenario, para sentir que avanzo de final en final. | Pretemporada → Copa del Rey → Liga → Champions → Mundial; Cambian luz, césped, afición y carteles; rivales salen más fuertes; En el Mundial todos llevan camiseta de su selección. |
| P37 | **Mote y avatar**. Como jugador quiero un mote y una cara propios, para que en el ranking y en la cabecera no salga mi correo. | Mote 3-16 caracteres, único sin distinguir mayúsculas ni tildes (409 si cogido); Avatar con cara de jugador fichado o entrenador; Migración 004 y `PUT /api/juego/identidad`. |
| P38 | **Rarezas por historia rojiblanca y fichajes**. Como aficionado quiero que la rareza de cada jugador refleje lo que fue en el Atleti, y que fichar se sienta especial. | 36 jugadores en 4 rarezas (Común, Raro, Épico, Leyenda) según historia en club; Más rareza = más habilidades aprendibles y menos probabilidad en contrato; Animación firma contrato en pixel art. |
| P39 | **Habilidades niveladas por minuto**. Como jugador quiero que las habilidades más fuertes no rompan la partida al principio. | Niveles que no salen hasta cierto minuto (`desdeMinuto`) y recarga mínima (`cdMin`); Regate, entrada rasante y contragolpe reequilibrados. |
| P40 | **Combinaciones y ultras a la vista**. Como jugador quiero ver qué combinaciones y ultras existen y qué me falta, para planificar la partida. | Pantalla Combinaciones con nombre, bonus, requisitos y ultra a la que cuentan; Filtros Todas / Con tu jugador / Conseguidas. |
| P41 | **Colisiones exactas**. Como jugador quiero que lo que veo sea lo que choca, para que nadie se esconda detrás de un tejado. | Edificios, gradas y bancos chocan en todo su dibujo; Muñecos chocan por los pies (vista 3/4); copa árboles se vuelve transparente. |
| P42 | **Logros con historia y equipaciones**. Como aficionado quiero logros con datos curiosos del Atleti que desbloqueen equipaciones, para tener objetivos a largo plazo. | 29 logros con un dato real que se descubre al conseguirlo; Servidor solo apunta logros que puede comprobar; 10 equipaciones que se eligen en el Vestuario. |
| P43 | **Pantalla de fin con estadísticas**. Como jugador quiero ver al final de la partida qué ha funcionado, para mejorar en la siguiente. | Tiempo, ambiente, bajas, jefes, daño total, golpe máximo, críticos, daño recibido, vida recuperada; Barras daño por habilidad (armas, ultras, ulti, quemaduras); Jefes vencidos con lo que costaron y logros nuevos. |
| P44 | **Música chiptune y la grada**. Como jugador quiero música y ambiente de estadio, para que la partida emocione. | Fanfarria propia por competición y canción fondo que se anima con tiempo y jefes; Grada murmura y canta cuando te acercas; Volumen música aparte de efectos; todo sintetizado (sin ficheros). |
| P45 | **Muñecos con más detalle**. Como aficionado quiero reconocer a los jugadores y a los jefes en el campo. | Sombreado, orejas, nariz y peinados nuevos; Rasgos propios: brazalete capitán, cinta, pecas, barba, pendientes, tatuajes. |
| P46 | **Jefes más duros**. Como jugador quiero que los jefes sean un reto de verdad a partir del segundo. | Escolta élites desde segundo jefe y refuerzos al cambiar fase; Furia si tardas en ganarles; Una jugada estrella por jefe en fase 3; primero sigue asequible. |
| P47 | **Corrección errores detectados**. Como usuario quiero que los errores que encuentren los probadores se arreglen con pruebas que eviten que vuelvan. | Cada error se reproduce con prueba antes de arreglarlo; Arreglos pasan CI y se despliegan. |
| P48 | **Documentación y gestión Sprint 2**. Como responsable del proyecto quiero que todo el Sprint 2 se pueda revisar desde el repositorio. | README con capturas juego y DoneTonic; Documentación técnica para memoria con diagramas; Backlog, tablero y gráficas Sprint 2 en DoneTonic. |

---

## Trazabilidad tarea → rama → PR (Sprint 1)

| PBI | Tarea | Descripción | Rama | PR |
|-----|-------|-------------|------|----|
| P1 | T1 | Crear repositorio y estructura base | `hito-1/T1-estructura-base` | #1 |
| P1 | T2 | Configurar GitHub Flow | `hito-1/T2-github-flow` | #2 |
| P2 | T3 | Workflow de CI con GitHub Actions | `hito-1/T3-integracion-continua` | #3 |
| P3 | T4 | Despliegue automático en proveedor cloud gratuito | `hito-1/T4-despliegue-continuo`, `hito-1/T4-url-publica` | #4, #10 |
| P4 | T5 | Modelo de usuario y repositorio en memoria | `hito-1/T5-modelo-repositorio-memoria` | #5 |
| P4 | T6 | Servicio de gestión de usuarios | `hito-1/T6-servicio-usuarios` | #6 |
| P5 | T7 | Framework de pruebas y al menos 5 pruebas | `hito-1/T7-pruebas-unitarias` | #7 |
| P6 | T8 | Endpoints de la API de usuarios | `hito-1/T8-api-usuarios` | #8 |
| P7 | T9 | Cliente de comunicación con la API | `hito-2/T9-cliente-api` | #11 |
| P7 | T10 | Interfaz de usuario: vistas y navegación | `hito-2/T10-vistas-navegacion` | #12 |
| P8 | T11 | Registro y login en el backend (con hash) | `hito-2/T11-registro-login-backend` | #13 |
| P8 | T12 | Formularios de registro y login en el frontend | `hito-2/T12-formularios-frontend` | #14 |
| P9 | T13 | Mantener la sesión al recargar y cerrar sesión | `hito-2/T13-gestion-sesion` | #15 |
| P10 | T14 | Middleware de autenticación y protección de rutas | `hito-2/T14-rutas-protegidas` | #16 |
| P11 | T15 | Elegir y configurar la base de datos | `hito-3/T15-configurar-bd` | #18 |
| P11 | T16 | Repositorio de BD sustituyendo al de memoria | `hito-3/T16-repositorio-postgres` | #19 |
| P12 | T17 | Sacar los secretos a variables de entorno | `hito-3/T17-secretos-entorno` | #20 |
| P13 | T18 | Roles, autorización y primer administrador (backend) | `hito-3/T18-roles-autorizacion` | #21 |
| P13 | T19 | Panel de administración y baja de cuenta (frontend) | `hito-3/T19-panel-admin` | #22 |
| P14 | T20 | Configurar el logging de la actividad relevante | `hito-3/T20-logging` | #23 |
| P15 | T21 | Registrar la aplicación OAuth en Google | `hito-4/T22-google-oauth` | #40 |
| P15 | T22 | Flujo de inicio de sesión con OAuth | `hito-4/T22-google-oauth` | #40 |
| P16 | T23 | Servicio de correo | `hito-4/T23-correo` | #38 |
| P16 | T24 | Flujo de confirmación de la cuenta | `hito-4/T24-confirmacion` | #39 |
| P17 | T25 | Errores en el backend | `hito-4/T25-secretos-hito4` y resto ramas hito | #37–#41 |
| P17 | T26 | Mensajes de error en el frontend | `hito-4/T26-privacidad` y resto ramas hito | #37–#41 |
| P18 | T27 | Completar el README | `hito-4/T27-readme-completo` | #25 |
| P18 | T28 | Etiquetas de hito y revisión final | `hito-4/T28-revision-entrega` | #26 |
| P18 | T31 | Revisión frase a frase contra el enunciado y README final | `hito-4/T31-revision-enunciado` | #30 |
| P18 | T32 | Carpeta de la memoria en LuaLaTeX | `hito-4/T32-carpeta-memoria` | #31 |
| P19 | T29 | Contenerizar la aplicación con Docker | `hito-4/T29-docker` | #27 |
| P19 | T30 | Despliegue continuo en Cloud Run con GitHub Actions | `hito-4/T30-cloud-run` | #28 |

**Cierres de hito Sprint 1:** PR #9 (Hito 1 → `main`), #17 (Hito 2), #24 (Hito 3), #29 (cierre sprint), #32 (revisión final y memoria). Releases: `hito-1`, `hito-2`, `hito-3`, `hito-4`, `sprint-1`.

---

## Trazabilidad tarea → PR (Sprint 2)

En Sprint 2 cada tarea indica en su descripción de DoneTonic el PR donde está. La integración fue en `main` con un PR por fase y uno por arreglo.

| PBI | Tareas | PRs | Hecho (fecha fusión último PR) |
|-----|--------|-----|--------------------------------|
| P20 | T33, T34 | #36, #45 | 24/10/2026 |
| P21 | T35, T36 | #36 | 23/10/2026 |
| P22 | T37, T38 | #44, #46 | 24/10/2026 |
| P23 | T39–T41 | #44, #48 | 24/10/2026 |
| P24 | T42, T43 | #36, #48 | 24/10/2026 |
| P25 | T44, T45 | #44, #45, #47 | 24/10/2026 |
| P26 | T46, T47 | #45, #48 | 24/10/2026 |
| P27 | T48, T49 | #45, #47 | 24/10/2026 |
| P28 | T50, T51 | #36, #47 | 24/10/2026 |
| P29 | T52, T53 | #49 | 24/10/2026 |
| P30 | T54 | #49 | 24/10/2026 |
| P31 | T55 | #49, #50 | 24/10/2026 |
| P32 | T56 | #49 | 24/10/2026 |
| P33 | T57, T58 | #50 | 24/10/2026 |
| P34 | T59, T60 | #50 | 24/10/2026 |
| P35 | T61 | #52 | 24/10/2026 |
| P36 | T62 | #52 | 24/10/2026 |
| P37 | T63 | #52 | 24/10/2026 |
| P38 | T64, T65 | #53 | 26/10/2026 |
| P39 | T66 | #53 | 26/10/2026 |
| P40 | T67 | #53 | 26/10/2026 |
| P41 | T68 | #53 | 26/10/2026 |
| P42 | T69, T70 | #54 | 26/10/2026 |
| P43 | T71 | #54 | 26/10/2026 |
| P44 | T72–T74 | #54 | 26/10/2026 |
| P45 | T75 | #54 | 26/10/2026 |
| P46 | T76 | #54 | 26/10/2026 |
| P47 | T77–T79 | #51, #55, #56 | 29/10/2026 |
| P48 | T80–T82 | #55 | 29/10/2026 |

**PRs por fase Sprint 2:** #36 (23/10, base), #44–#52 (24/10, Fases 1–4), #53, #54 (26/10, Fases 5–6), #55 (27/10, documentación), #51, #55, #56 (arreglos), #56 (29/10, baja Google). Total >50 PRs fusionados en proyecto completo.

---

## Evolución Sprint 1 (PBIs del alcance de la entrega: 16 PBIs = P1–P14, P18, P19)

| Momento | PBIs hechos | PBIs pendientes |
|---------|-------------|-----------------|
| Inicio Sprint 1 (29/09/2026) | 0 | 15 |
| Cierre Hito 1 (release `hito-1`) | 6 | 9 |
| Cierre Hito 2 (release `hito-2`) | 10 | 5 |
| Cierre Hito 3 (release `hito-3`) | 14 | 1 |
| Se añade P19 (Cloud Run) | 14 | 2 |
| Cierre primera entrega (12/10/2026) | 16 | 0 |

Gráfica: Figura `burndown-s1` (Anexo desarrollo). Escalón «+P19» refleja cambio de alcance.
Capturas DoneTonic Sprint 1 (29/10/2026): tablero 100% (Figura `donetonic-tablero`), gráficas burndown/burnup con 19 PBIs completados (Figura `donetonic-graficas-s1`), Product Backlog dos sprints (Figura `donetonic-backlog`).

---

## Evolución real Sprint 2 (según fecha fusión último PR de cada PBI)

| Día | Hechos ese día | Hechos (acumulado) | Pendientes |
|-----|----------------|---------------------|------------|
| Inicio (23/10/2026) | 0 | 0 | 29 |
| 23/10 (PR #36) | 1 | 1 | 28 |
| 24/10 (PRs #44–#52) | 17 | 18 | 11 |
| 25/10 | 0 | 18 | 11 |
| 26/10 (PRs #53, #54) | 9 | 27 | 2 |
| 27/10 (PR #55) | 0 | 27 | 2 |
| 28/10 | 0 | 27 | 2 |
| 29/10 (PR #56 y documentación) | 2 | 29 | 0 |

Gráfica: Figura `burndown-s2` (Anexo desarrollo).
**Explicación recta DoneTonic:** Backlog Sprint 2 (29 PBIs, 50 tareas) se registró en DoneTonic al cerrar sprint (29/10/2026) con todos los PBIs ya en *Hecho*; por eso sus gráficas Sprint Burndown y Burnup (Figura `donetonic-s2-graficas`) caen en recta de 29 a 0 ese día. La evolución real se reconstruye desde fechas de fusión PRs en `main` (Tabla anterior y Figura `burndown-s2`).
Capturas DoneTonic Sprint 2 (29/10/2026): gráficas en recta (Figura `donetonic-s2-graficas`), tablero 100% (Figura `donetonic-s2-tablero`), detalle PBI con historia, criterios y tareas (Figura `donetonic-pbi-detalle`), 50 tareas en columna Hecho (Figura `donetonic-s2-tareas`).

---

## Velocity Chart DoneTonic
Refleja concentración: 29 PBIs completados en una semana, pico 17 PBIs el 24/10. Confirma desarrollo juego en ráfagas cortas e intensivas antes de registrar backlog en herramienta.
