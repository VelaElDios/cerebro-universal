---
tipo: "fuente"
titulo: "documentacion tecnica"
temas: ["saas", "grada-colchonera"]
claves: []
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[saas]] · [[grada-colchonera]]

Documento aprendido: `repo:saas/docs/documentacion-tecnica.md`.

## Resumen
Este trozo es la cabecera de la documentación técnica del proyecto «La Grada Colchonera»: un juego web tipo *survivor* en pixel art construido sobre una base SaaS. Incluye metadatos del proyecto (autor, repositorio, URL en producción, fechas de los dos sprints), una tabla que mapea cada sección de este documento a los capítulos de la memoria TFG, el contexto y objetivos de la asignatura PIS, el alcance detallado por hitos y la justificación del cambio de enfoque (de red social a juego), y los requisitos funcionales completos del Sprint 1 (13 RF) y del Sprint 2 (20 RJ de juego) con sus PBIs, ub
Este trozo documenta los 12 requisitos no funcionales (RNF-01 a RNF-12) del proyecto La Grada Colchonera, la metodología Scrum con DoneTonic para dos sprints (Sprint 1: 29/09–27/10/2026 con 4 hitos; Sprint 2: 23/10–29/10/2026 con 6 fases de juego), la Definición de Hecho, el flujo GitHub Flow por hitos con ramas protegidas y CI obligatorio, tablas de trazabilidad completas PBI→tarea→rama→PR→release para ambos sprints, gráficas de burndown, cronología detallada y la arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL Neon + integraciones SMTP/Google OAuth) con diagrama Mermaid.
Este trozo detalla la arquitectura en capas del sistema (presentación, cliente API, API, lógica, datos, integraciones, composición), 14 decisiones de diseño con sus alternativas y justificaciones (Express 5 sin frontend, repositorio dual, inyección de dependencias, sesiones en servidor, bajas lógicas, tokens HMAC, OAuth propio, admin por variables de entorno, migraciones SQL, Cloud Run/Render, reglas compartidas, concurrencia optimista, simulación determinista, gráficos por código), los módulos del backend y sus responsabilidades, el modelo de datos (users con índice parcial único, session, ju
Este trozo documenta los flujos de autenticación y autorización (confirmación de correo, login local, OAuth Google, recuperación de sesión, peticiones protegidas, cambio de rol, baja de usuario), el arranque de la aplicación (migraciones y primer administrador), la partida del juego con validación anti-trampas, la contratación con concurrencia optimista, el pipeline de CI/CD (GitHub Actions → Cloud Run con WIF) y una prueba de dominio permitido. Incluye una tabla de amenazas y medidas de seguridad, y comienza la descripción del concepto del juego.
Este trozo describe el diseño completo del juego «La Grada Colchonera»: género survivor chibi con jugadores históricos del Atlético de Madrid, manual de usuario (menús, controles, oleadas, ambientes, fin de partida), tabla de sistemas (36 jugadores, 4 rarezas, 2 entrenadores, 24 armas, 14 pasivas, 24 combinaciones, 6 ultras, 16 equipos rivales, 10 jefes, dificultad escalonada, movimiento con inercia, mundo procedural, club persistente, 29 logros, audio sintetizado), arquitectura separada en simulación determinista (paso fijo 1/60 s, semilla), presentación (Canvas 2D, sprites chibi 32×32 genera
Este trozo detalla la estrategia de prueba

## Lo que se sacó de él (65)
- [[arquitectura-del-juego-simulacion-determinista-presentacion]]
- [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]]
- [[arquitectura-en-capas-con-inyeccion-de-dependencias-permitio]]
- [[arranque-de-la-aplicacion-configuracion-migraciones-y-primer]]
- [[audio-100-sintetizado-con-web-audio-ondas-pulso-triangulo-ru]]
- [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]]
- [[cambio-de-alcance-de-red-social-a-juego-survivor-justificaci]]
- [[cambio-de-alcance-durante-sprint-1-anadido-p19-cloud-run-por]]
- [[catalogo-de-sistemas-del-juego-jugadores-rarezas-entrenadore]]
- [[cliente-api-con-timeout-de-15-s-y-manejo-de-apierror]]
- [[como-exportar-diagramas-mermaid-para-la-memoria-latex]]
- [[como-mapear-este-documento-a-los-capitulos-de-la-memoria-tfg]]
- [[como-referenciar-capturas-de-pantalla-en-la-memoria-sin-copi]]
- [[contratacion-de-jugador-con-ficha-y-concurrencia-optimista-d]]
- [[correccion-de-unicidad-de-email-tras-baja-logica-indice-parc]]
- [[cronologia-detallada-del-proyecto-septiembre-octubre-2026]]
- [[decisiones-de-diseno-del-backend-con-alternativas-y-justific]]
- [[definicion-de-hecho-dod-para-tareas-e-hitos]]
- [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]]
- [[estado-de-completitud-de-sprints-y-trazabilidad]]
- [[estrategia-de-pruebas-error-first-y-ci-como-requisito-de-mer]]
- [[estrategia-de-pruebas-niveles-y-enfoque-error-first]]
- [[evolucion-por-fases-del-sprint-2-etiquetas-donetonic-adicion]]
- [[fechas-y-estructura-del-sprint-1-4-hitos-19-pbis-32-tareas]]
- [[fechas-y-estructura-del-sprint-2-6-fases-de-juego-calidad-29]]
- [[flujo-de-confirmacion-de-cuenta-por-correo-get-api-auth-conf]]
- [[flujo-de-registro-con-email-y-contrasena]]
- [[formato-de-logs-json-y-eventos-registrados]]
- [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]]
- [[generacion-de-mundo-procedural-infinito-con-distritos-estadi]]
- [[genero-y-bucle-principal-del-juego-survivor-chibi-atletico]]
- [[github-flow-por-hitos-con-ramas-protegidas-y-ci-obligatorio]]
- [[glosario-tecnico-del-proyecto-22-terminos-definidos]]
- [[grupos-de-rutas-de-la-api-y-sus-accesos]]
- [[inventario-de-capturas-de-pantalla-con-trazabilidad-a-requis]]
- [[lecciones-aprendidas-tareas-pequenas-deploy-dia-1-documentar]]
- [[lista-de-29-logros-con-datos-historicos-verificados-y-10-equ]]
- [[login-con-google-oauth-2-0-codigo-de-autorizacion-state-en-s]]
- [[login-local-con-cuenta-pendiente-y-reenvio-de-confirmacion-p]]
- [[manejo-de-errores-de-principio-a-fin-de-errores-tipados-a-ui]]
- [[manual-de-usuario-entrada-menus-controles-oleadas-ambientes]]
- [[maquina-de-estados-de-la-cuenta-de-usuario]]
- [[metadatos-del-proyecto-la-grada-colchonera]]
- [[metricas-del-proyecto-codigo-pruebas-endpoints-y-contenido-d]]
- [[modulos-del-backend-y-sus-responsabilidades]]
- [[optimizaciones-de-rendimiento-busqueda-por-radio-con-claves]]
- [[partida-del-juego-inicio-bucle-de-simulacion-60-hz-y-fin-con]]
- [[perfil-de-juego-con-jsonb-y-concurrencia-optimista-mediante]]
- [[pipeline-ci-cd-github-actions-cloud-run-con-workload-identit]]
- [[pipeline-ci-cd-github-actions-docker-cloud-run-y-render]]
- [[pivote-de-red-social-a-juego-survivor-reutilizando-base-del]]
- [[proteccion-del-ultimo-administrador-al-cambiar-rol-patch-api]]
- [[recuperacion-de-sesion-al-cargar-get-api-auth-me-y-logout-po]]
- [[renderizado-de-sprites-chibi-3232-por-capas-y-pixel-a-pixel]]
- [[requisitos-funcionales-del-juego-sprint-2-20-rj-con-trazabil]]
- [[requisitos-funcionales-del-sprint-1-13-rf-con-trazabilidad]]
- [[requisitos-no-funcionales-rnf-01-a-rnf-12-del-proyecto]]
- [[resumen-de-pruebas-por-fichero-322-totales]]
- [[roadmap-de-trabajo-futuro-priorizado]]
- [[solucion-a-correo-no-salia-desde-cloud-run-smtp-gmail-puerto]]
- [[solucion-a-json-mal-formado-que-devolvia-html-de-error-de-ex]]
- [[tabla-de-trazabilidad-sprint-1-pbi-hito-titulo-tareas-prs-re]]
- [[tabla-de-trazabilidad-sprint-2-pbi-etiqueta-titulo-tareas-pr]]
- [[tabla-users-con-indice-parcial-unico-para-email-entre-cuenta]]
- [[validacion-anti-trampas-en-el-servidor-reloj-propio-formulas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
