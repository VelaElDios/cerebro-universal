---
tipo: "dato"
titulo: "Cifras clave del proyecto contrastadas con fuentes (38+ datos)"
temas: ["cifras", "despliegue", "endpoints", "fuentes", "grada-colchonera", "juego", "memoria", "memoria-procesos", "metricas", "migraciones", "pbis", "pruebas", "requisitos", "sprints", "tareas", "tfg", "trazabilidad", "verificacion"]
claves: ["19 PBIs", "32 tareas", "29 PBIs", "50 tareas", "276 pruebas", "322 pruebas", "5 migraciones", "23 endpoints", "36 jugadores", "10 jefes", "29 logros", "10 equipaciones"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md, repo:saas/docs/procesos.md, repo:saas/docs/requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/arquitectura.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md, repo:saas/docs/requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md", "repo:saas/docs/requisitos.md, repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/requisitos.md, repo:saas/docs/procesos.md, repo:saas/docs/juego.md, repo:saas/docs/decisiones.md", "repo:saas/docs/requisitos.md, repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/procesos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/log.md, repo:saas/docs/requisitos.md", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md, repo:saas/docs/juego.md, repo:saas/docs/procesos.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-25"
---

Temas: [[cifras]] · [[despliegue]] · [[endpoints]] · [[fuentes]] · [[grada-colchonera]] · [[juego]] · [[memoria]] · [[memoria-procesos]] · [[metricas]] · [[migraciones]] · [[pbis]] · [[pruebas]] · [[requisitos]] · [[sprints]] · [[tareas]] · [[tfg]] · [[trazabilidad]] · [[verificacion]]

# Cifras clave del proyecto contrastadas con fuentes

**Temas:** `[[metricas]]` `[[trazabilidad]]` `[[verificacion]]` `[[requisitos]]` `[[sprints]]`

---

## 1. Métricas de Sprints

| Métrica | Sprint 1 | Sprint 2 | Total / Nota |
|---------|----------|----------|--------------|
| **PBIs** | 19 (P1–P19) | 29 (P20–P48) | 48 PBIs totales |
| **Tareas** | 32 (T1–T32) | 50 (T33–T82) | 82 tareas totales |
| **Fechas** | 29/09–27/10/2026 | 23/10–29/10/2026 | — |
| **HUs / Historias** | — | 29 | sprint-2.md §Historias |
| **Etiquetas de fase** | 4 hitos | 7 etiquetas | — |
| **Burndown entrega (alcance real)** | 16 PBIs (P1–P14, P18, P19) | 29 PBIs en 7 días (reconstruido con fechas de PR) | sprint-1.md §Evolución; sprint-2.md §Evolución |
| **PRs fusionados** | — | ≥50 (50 registrados en tabla) | sprint-2.md §Tabla PRs; ampliaciones |
| **Backlog DoneTonic** | — | Registrado al cerrar el sprint (29/10) → gráficas en recta | decisiones.md D-19 |
| **Cambio de alcance** | P19 (Cloud Run) añadido a mitad del Sprint 1 | — | decisiones.md D-16 |

**Detalle evolución Sprint 2 (fechas de PR):** 23/10 (1), 24/10 (17), 26/10 (9), 29/10 (2).

---

## 2. Código y arquitectura

| Componente | Líneas aprox. | Detalle | Fuente |
|------------|---------------|---------|--------|
| Backend (src/) | ~2.300 | — | sprint-2.md §Métricas |
| Interfaz web (frontend) | ~1.150 | — | ampliación 2026-11-25 |
| CSS | ~950 | — | ampliación 2026-11-25 |
| Juego (public/js/game/) | ~14.800 | 35 módulos | sprint-2.md §Métricas; ampliación |
| Pruebas automáticas | ~5.050 | — | sprint-2.md §Métricas |
| **Total backend + juego + pruebas** | ~22.150 | — | suma |

**Arquitectura en capas:** API, lógica, datos, integraciones → `arquitectura.md §Vista general`  
**Modelo de datos:** `users`, `session`, `juego_perfiles`, `juego_records` → `arquitectura.md §Modelo de datos`  
**Migraciones SQL:** 5 (001–005) → `arquitectura.md §Modelo de datos`  
**Concurrencia optimista:** `juego_perfiles.version` → `arquitectura.md §Servidor del juego`  
**Validación anti-trampas:** reloj servidor, límites creíbles → `arquitectura.md §Servidor del juego`  
**Dependencias producción (6):** `express`, `express-session`, `connect-pg-simple`, `pg`, `bcryptjs`, `nodemailer` → `sprint-2.md §Métricas`  
**Endpoints API:** 23 → `arquitectura.md §Tabla API` / `sprint-2.md §Métricas`

---

## 3. Pruebas automáticas

| Momento | Cantidad | Fuente |
|---------|----------|--------|
| Cierre Sprint 2 (main) | 276 | `procesos.md §Pruebas` (tabla por fichero, total 276) |
| Tras Fase 7 | 322 (276 + 46 nuevas) | `sprint-2.md §Métricas` |
| Prueba técnica RF-13 | 13 pruebas (endpoint `POST /api/prueba/dominio`) | `requisitos.md §RF-13` |

**Calidad:** 0 regresiones en `main` gracias a CI obligatorio; 100 % requisitos cubiertos.

---

## 4. Contenido del juego (survivor, ref. Vampire Survivors)

| Elemento | Cantidad | Fuente |
|----------|----------|--------|
| Jugadores | 36 | `juego.md §Sistemas` |
| Entrenadores | 2 | `juego.md §Sistemas` |
| Armas | 29 | `juego.md §Sistemas` |
| Pasivas | 16 | `juego.md §Sistemas` |
| Combinaciones | 29 | `juego.md §Sistemas` |
| Ultras | 6 | `juego.md §Sistemas` |
| Equipos rivales | 16 | `juego.md §Sistemas` |
| Jefes | 10 | `juego.md §Sistemas` |
| Ambientes | 5 | `juego.md §Sistemas` |
| Selecciones | 26 | `juego.md §Sistemas` |
| Logros | 29 | `juego.md §Tabla logros` |
| Equipaciones | 10 | `juego.md §Tabla logros` |

**Género:** survivor, cita *Vampire Survivors* → `juego.md §Concepto`  
**Rendimiento:** 60 FPS, paso fijo 1/60 s, búsqueda espacial por celdas (4,5× más rápido), texturas cacheadas.  
**Accesibilidad:** HTML semántico, `aria-live`, `aria-describedby`, `prefers-reduced-motion`, joystick táctil.

---

## 5. Despliegue e infraestructura

| Aspecto | Valor | Fuente |
|---------|-------|--------|
| Principal | Cloud Run (región `europe-southwest1`) | `procesos.md §Cloud Run` |
| Alternativo | Render | `procesos.md §CI/CD` |
| Base de datos | Neon (PostgreSQL, Frankfurt) | `procesos.md §BD` |
| Secret Manager | 8 secretos | `procesos.md §Configuración` |
| WIF (Workload Identity Federation) | Sí | `procesos.md §CI/CD` |
| CI | GitHub Actions con PostgreSQL 17, Docker build (Node 22 Alpine), health check | `procesos.md §Workflows` |
| Docker base | Node 22 Alpine | `procesos.md §Docker` |

---

## 6. Seguridad

- **bcrypt** coste 10 → `arquitectura.md §Seguridad`
- **Cookies:** `httpOnly`, `secure`, `sameSite`, regeneración de sesión → `arquitectura.md §Seguridad`
- **OAuth 2.0:** `state` anti-CSRF, intercambio de código en servidor → `arquitectura.md §Flujos` / RFC 6749
- **HMAC-SHA256** para firmas → ampliación
- **Consultas parametrizadas** (prevención SQLi) → ampliación

---

## 7. Procesos y definición de hecho (DoD)

- **GitHub Flow:** Sprint 1 → rama por tarea (`hito-N/integracion`); Sprint 2 → un PR por fase → `CONTRIBUTING.md`
- **DoD:** código en PR, CI verde, desplegado, documentación actualizada → `procesos.md §DoD`
- **Capturas DoneTonic:** tomadas 29/10/2026 con dos sprints cerrados (espacio TFG, equipo *Colchoneros*) → `sprint-1.md §Capturas`
- **Correo real en Gmail (producción)** → `sprint-1.md §Revisión`
- **Google OAuth publicada en producción para usuarios externos** → `sprint-1.md §Revisión`

---

## 8. Trazabilidad y documentación de la memoria

- **Cadena completa:** requisito → PBI → tarea → rama → PR → release (Anexo B completo) → `a4-trazabilidad.tex`
- **Anexo desarrollo:** dos sprints con mismo esquema → `a1-desarrollo.tex`
- **Retrospectiva Sprint 2:** explicación de la recta en burndown → `a1-desarrollo.tex §Retrospectiva`
- **Requisitos formales memoria:**
  - Resumen ≥150 palabras → `preambulo.tex`
  - Abstract ≥120 palabras → `preambulo.tex`
  - Declaración de autoría presente → `preambulo.tex`
  - Hito 4 no pendiente (capítulos 4, 5, anexos) → estructura de la memoria

---

## 9. Uso de IA y bibliografía

- **IA para código/docs/PRs:** Claude (modo *Cowork*)
- **IA para memoria (con test automático):** Gemini, NVIDIA, OpenRouter (gratuitas)
- **Bibliografía (12 entradas):** Express, GitHub Flow, Node.js, PostgreSQL, Cloud Run, GitHub Actions, Scrum Guide, enunciado TFG, RFC 6749, bcrypt, *Vampire Survivors*, DoneTonic.

---

## 10. Metodología de verificación

- **Cada cifra** se ha extraído literalmente de las fuentes del repositorio (`docs/sprint-1.md`, `docs/sprint-2.md`, `docs/arquitectura.md`, `docs/procesos.md`, `docs/requisitos.md`, `docs/juego.md`, `docs/decisiones.md`, `CONTRIBUTING.md`, `preambulo.tex`, `a4-trazabilidad.tex`, `a1-desarrollo.tex`).
- **Test automático `verificar.py`:** comprueba que todo número >20 del texto aparece en las fuentes.
- **Revisor humano:** contrasta los números pequeños (≤20) a mano.
- **Ejemplos de contraste:**
  - 19 PBIs Sprint 1 → `sprint-1.md` tabla backlog
  - 16 PBIs en burndown entrega → `sprint-1.md` tabla evolución (P1–P14, P18, P19)
  - 276 pruebas → `procesos.md` tabla pruebas por fichero (total 276)
  - 322 pruebas → `sprint-2.md` métricas (276 + 46 Fase 7)
  - 50 PRs fusionados → `sprint-2.md` tabla PRs
  - 8 secretos → `procesos.md` configuración
  - Región `europe-southwest1` → `procesos.md` Cloud Run

---

## Fuentes principales (repositorio `saas`)

- `docs/sprint-1.md` — Backlog, fechas, burndown, capturas, revisión
- `docs/sprint-2.md` — Backlog, métricas, trazabilidad, PRs, historias
- `docs/arquitectura.md` — Vista general, modelo de datos, seguridad, flujos, servidor de juego, tabla API
- `docs/procesos.md` — CI/CD, workflows, DoD, pruebas, configuración, Docker, Cloud Run, BD
- `docs/requisitos.md` — RF-13
- `docs/juego.md` — Concepto, sistemas, tabla logros
- `docs/decisiones.md` — D-16 (cambio alcance P19), D-19 (Backlog DoneTonic)
- `CONTRIBUTING.md` — GitHub Flow
- `preambulo.tex` — Resumen, abstract, declaración autoría
- `a4-trazabilidad.tex` — Trazabilidad completa (Anexo B)
- `a1-desarrollo.tex` — Desarrollo dos sprints, retrospectiva

---

**Relacionado:**  
`[[inventario-de-capturas-de-pantalla-con-trazabilidad-a-requisitos-y-fechas]]` · `[[inventario-de-capturas-donetonicas-requeridas-y-disponibles]]` · `[[inventario-de-diagramas-obligatorios-y-su-estado-actualizado]]` · `[[cifras-clave-del-proyecto-contrastadas-con-fuentes-31-datos]]` · `[[cifras-clave-del-proyecto-contrastadas-con-fuentes-35-datos]]` · `[[numeros-clave-del-proyecto-contrastados-con-fuentes]]`

**Origen:** `[[proyectos/memoria-procesos/estado|memoria-procesos]]`

> Ver bitácora reciente (2026-11-23 04:09) donde se listan 30 comprobaciones con sección de la fuente.
> — `repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md, repo:saas/docs/procesos.md, repo:saas/docs/requisitos.md` (cita sin comprobar)
> PBIs y tareas del Sprint 1: 19 / 32 ... PBIs y tareas del Sprint 2: 29 / 50 ... Pruebas automáticas totales: 276 ... Endpoints expuestos en la API: 23 ... Migraciones SQL aplicadas: 5 ... Contenido jugable: 36 jugadores ... 29 logros
> — `repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md, repo:saas/docs/arquitectura.md, repo:saas/docs/juego.md, repo:saas/docs/procesos.md` (cita sin comprobar)

Fusionada con: Cifras clave del proyecto contrastadas con fuentes (38 datos)

Relacionado: [[cifras-clave-del-proyecto-contrastadas-con-fuentes-para-comp]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
