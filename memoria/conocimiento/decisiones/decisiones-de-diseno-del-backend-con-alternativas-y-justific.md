---
tipo: "decision"
titulo: "Decisiones de diseño del backend con alternativas y justificación"
temas: ["decisiones", "grada-colchonera", "saas"]
claves: ["express 5", "repositorio dual", "inyección dependencias", "sesiones servidor", "bajas lógicas", "token HMAC", "OAuth fetch", "admin variables entorno", "migraciones SQL", "Cloud Run Render", "reglas compartidas", "concurrencia optimista", "simulación determinista", "gráficos código"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[decisiones]] · [[grada-colchonera]] · [[saas]]

Se documentan 14 decisiones clave: 1) Express 5 sin framework frontend (React/Vue/Next) para ver capas como ficheros, sin build, sin CORS, frontera interfaz/cliente en dos ficheros. 2) Repositorio con dos implementaciones (memoria y PostgreSQL) para arrancar sin BD y pasar mismas pruebas, demostrando independencia del almacenamiento (patrón Repository). 3) Inyección de dependencias por parámetro (cada servicio recibe `userRepository`, `passwordHasher`, `mailer`, `tokenSigner`, reloj, azar) para probar con dobles sin trucos. 4) Sesiones en servidor (`express-session` + PostgreSQL) frente a JWT: logout/borrado invalida al momento, cookie `httpOnly`, sobreviven a reinicios/despliegues. 5) Bajas lógicas (`status = deleted`) con email libre frente a borrado físico o bloqueo eterno: conserva historial/auditoría, cuenta no entra, sesión invalida, email y mote libres para nueva cuenta (índice único parcial). 6) Token de confirmación firmado (HMAC) sin guardar en BD: sin tabla ni limpieza, caduca solo, infalsificable sin secreto. 7) OAuth 2.0 escrito con `fetch` frente a Passport.js: flujo corto entendible (`state`, intercambio código, email verificado), menos dependencias, fácil de probar con cliente falso. 8) Primer administrador por variables de entorno: sin contraseñas en código/scripts, idempotente. 9) Migraciones SQL propias: pocas tablas, SQL legible y versionado con registro de aplicadas. 10) Cloud Run principal y Render alternativo: Cloud Run usa créditos educación, escala a cero, Secret Manager, WIF; Render fue primer despliegue y queda de respaldo. 11) Reglas del juego compartidas cliente/servidor: servidor importa `club.js`, `config.js`, `logros.js` (única fuente de verdad). 12) Concurrencia optimista en perfil de juego (`version`): dos peticiones simultáneas no gastan dos veces la misma ficha; la segunda reintenta con datos nuevos. 13) Simulación del juego pura y determinista: paso fijo 1/60 s, azar con semilla, probables en Node sin navegador, resultado independiente de FPS. 14) Gráficos y sonido generados con código: sin problemas de derechos, carga instantánea, fácil variar equipaciones, selecciones, intensidad música.

> Express 5 sin framework de frontend | React, Vue, Next.js | Proyecto individual y didáctico: las capas se ven como ficheros, no hay paso de compilación, el backend sirve el frontend (sin CORS) y la frontera interfaz/cliente que pide el Hito 2 queda en dos ficheros.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
