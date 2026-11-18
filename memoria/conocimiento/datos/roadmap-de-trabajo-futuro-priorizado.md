---
tipo: "dato"
titulo: "Roadmap de trabajo futuro priorizado"
temas: ["grada-colchonera", "saas", "sprint"]
claves: ["multijugador", "WebSockets", "party", "PWA", "ranking", "rate limiting", "Playwright", "E2E"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[saas]] · [[sprint]]

Ítems de backlog futuro (no implementados en sprints 1-2):
1. **Multijugador cooperativo**: friends list, party (max 4), WebSockets, servidor autoritativo (extiende arquitectura actual).
2. **Contenido**: más jugadores, jefes, equipaciones, logros; sprites mejorados (Fase 7 ya inició esto).
3. **Rankings**: por temporadas y por ambiente (Final Copa, Liga, etc.).
4. **Auth hardening**: password recovery email + rate limiting en login (brute-force protection).
5. **E2E testing**: Playwright en CI + coverage reporting.
6. **PWA**: manifest, service worker, install prompt, offline-capable assets para móvil.
Prioridad sugerida: auth hardening → PWA → E2E → multijugador → rankings → contenido.

> - **Multijugador:** lista de amigos y partidas en grupo (*party*) de hasta 4 jugadores, con WebSockets y un servidor autoritativo.
- Más contenido: jugadores, jefes, equipaciones y logros; mejorar los sprites de los jugadores menos conocidos.
- Ranking por temporadas y por ambiente.
- Recuperación de contraseña por correo y limitación de intentos de inicio de sesión (*rate limiting*).
- Pruebas de extremo a extremo automatizadas en el CI (Playwright) y medición de cobertura.
- Aplicación instalable (PWA) para jugar desde el móvil como una app.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[manual-de-usuario-entrada-menus-controles-oleadas-ambientes]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
