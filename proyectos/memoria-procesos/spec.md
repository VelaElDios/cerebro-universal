# Spec: memoria completa de La Grada Colchonera (Sprints 1 y 2) con la plantilla oficial del TFG

## Qué es

La memoria del trabajo de la asignatura Procesos de Ingeniería del Software (PIS), curso 2026-2027,
con la **plantilla oficial del TFG de la ESIIAB-UCLM** (la que pidió el profesor). Cuenta el proyecto
*La Grada Colchonera* entero:

- **Sprint 1** (29/09–27/10/2026, Hitos 1–4, 19 PBIs P1–P19, 32 tareas T1–T32): la base SaaS en capas
  (cuentas, sesión, roles, PostgreSQL, correo, Google, errores, logs, CI/CD y despliegue en Cloud Run).
- **Sprint 2** (23/10–29/10/2026, 29 PBIs P20–P48, 50 tareas T33–T82): **la lógica del juego**, un
  *survivor* en pixel art construido sobre esa base (concepto, sistemas, arquitectura, anti-trampas,
  logros y evolución por fases).
- Y sobre todo el **proceso**: Scrum en DoneTonic, historias de usuario, DoD, GitHub Flow, CI/CD,
  trazabilidad requisito → PBI → tarea → PR y evolución de cada sprint.

**Versión 3.** El borrador tiene una memoria de los Hitos 1–3 escrita con fuentes antiguas. Ahora el
proyecto está cerrado (dos sprints) y **el juego SÍ se explica** (antes no). Se aprovecha lo que esté
bien, pero casi todo hay que reescribirlo y ampliarlo: la memoria final debe ser **lo más completa
posible** (orientativamente 80–120 páginas).

## Fuentes: la única verdad

Se te pasan en cada mensaje. Las del repositorio (`repo:saas/...`) son siempre la última versión:

| Fuente | Contenido |
|---|---|
| `repo:saas/docs/documentacion-tecnica.md` | **La base de la memoria.** §2 contexto, objetivos y alcance; §3 requisitos (RF-01–RF-13, RJ-01–RJ-20, RNF-01–RNF-12); §4 metodología y gestión; §5 arquitectura y decisiones; §6 diseño (módulos, modelo de datos, frontend, API); §7 los 13 flujos con diagramas de secuencia (Mermaid); §8 seguridad; §9 el juego; §10 pruebas; §11 CI/CD; §12 logs y errores; §13 problemas y soluciones; §14 métricas; §15 conclusiones y trabajo futuro; §16 índice de capturas |
| `repo:saas/docs/gestion/README.md` | DoneTonic: backlog de los dos sprints, DoD, las 29 historias de usuario del Sprint 2 con criterios, trazabilidad tarea → rama → PR, fechas de los PR y evolución de cada sprint |
| `repo:saas/docs/revision-entrega.md` | Revisión del enunciado del Sprint 1, requisito a requisito, con su evidencia |
| `repo:saas/docs/hito4-configuracion.md` | Configuración del Hito 4 (correo y Google) |
| `repo:saas/CONTRIBUTING.md` | Flujo de trabajo con ramas, commits y PR |
| `repo:saas/@arbol` | Lista de archivos del repositorio |
| `repo:saas/memoria/...` | Otra estructura de memoria que hay en el repo (`main.tex`, capítulos, `bibliografia.bib`). **Solo como guía** de qué contar; la plantilla que manda es la oficial del borrador |
| `fuentes/estructura-memoria.md` | Qué debe tener cada capítulo según el profesor |
| `fuentes/uso-ia.md` | Hechos para el anexo de uso de la IA |
| `fuentes/bibliografia-extra.md` | Referencias comprobadas que no están en el repo (OAuth 2.0, bcrypt, *Vampire Survivors*) |
| imágenes disponibles | Capturas copiadas del repo a `figs/capturas/<carpeta>/` con lo que muestra cada una (y §16 de la documentación técnica) |

**Regla de oro:** cada dato (cifras, fechas, nombres, versiones, URLs, números de PR, nombres de
módulos) sale de las fuentes, copiado tal cual. Si algo no está en las fuentes, **no se escribe**.
El test comprueba que todo número mayor que 20 del texto aparece en las fuentes; los pequeños los
comprueba el revisor. Ojo con los que se parecen: 19 PBIs en el Sprint 1, pero el burndown de la
entrega cuenta 16 (P1–P14, P18 y P19); 32 + 50 = 82 tareas; 276 pruebas.

## Qué no se toca

- Archivos protegidos (se ignoran si se intentan escribir): `Memoria.tex`, `latexmkrc`,
  `include/configuracion.tex`, `include/colores.tex`, `include/opciones.tex` (título, autor,
  `\espec`), `elements/portada.tex` y `figs/*`.
- `Memoria.tex` ya incluye, en este orden: `01-introduccion`, `03-propuesta`, `04-descripcion`,
  **`04b-juego`** (capítulo nuevo, entre la descripción y la evaluación), `05-evaluacion`,
  `06-conclusiones` y los anexos `a1-desarrollo`, **`a4-trazabilidad`** (nuevo), `a2-material` y
  `a3-uso-ia`.
- Los paquetes nuevos van en `include/extra.tex`. Ya están `tikz`, `pgfplots`, `longtable`,
  `booktabs` y **`pgf-umlsd`** (diagramas de secuencia: `sequencediagram`, `\newthread`, `\newinst`,
  `call`, `\mess`).
- La bibliografía es BibTeX con `apalike` (`bib/ref.bib`), como manda la plantilla.

## Qué hay que hacer

### Capítulos (en `chapters/`)

| Archivo | Contenido | Fuente | Mínimo |
|---|---|---|---|
| `01-introduccion.tex` | Motivación y contexto; objetivo principal y específicos; alcance de los dos sprints y **cambio de enfoque** de red social a juego, con su porqué; estructura de la memoria con `\ref` a cada capítulo y anexo | §2 | 600 palabras |
| `03-propuesta.tex` | Problema y propuesta (sin detalles técnicos). **Metodología**: Scrum adaptado en DoneTonic con los dos sprints (fechas, PBIs, historias de usuario, prioridad MUST, etiquetas), DoD, GitHub Flow (Sprint 1: rama por tarea → rama del hito; Sprint 2: un PR por fase), CI obligatorio y planificación (alcance §2.3, cronología §4.6). Herramientas (tabla). Captura del backlog de DoneTonic | §4, gestión, CONTRIBUTING | 900 palabras |
| `04-descripcion.tex` | **Requisitos** en tablas (`longtable`): RF-01–RF-13, RJ-01–RJ-20 y RNF-01–RNF-12, con PBI y dónde se cumple. **Arquitectura**: diagrama de capas en TikZ (`fig:capas`) y decisiones de diseño explicando el porqué (§5.2). **Diseño**: módulos del backend, **modelo de datos entidad-relación en TikZ** (`fig:modelo-datos`, con las tablas del juego), frontend y API (tabla). **Flujos** (§7.1–7.9) con diagramas de secuencia: registro (`fig:sec-registro`), confirmación por correo (`fig:sec-confirmacion`), login local (`fig:sec-login`), Google OAuth (`fig:sec-google`) y baja (`fig:sec-baja`); los demás, en texto o con más diagramas. **Seguridad** (§8, tabla). **Resumen de los sprints** (tabla, el detalle en el Anexo A). **La aplicación** tipo manual de usuario (cuentas, administración, Hito 4) con capturas de `app/` y `hito4/` | §3, 5, 6, 7.1–7.9, 8, 16 | 3000 palabras |
| `04b-juego.tex` | **Capítulo nuevo: «El juego (Sprint 2)»** con `\label{cap:juego}`. Concepto (género *survivor*, cita a *Vampire Survivors*); cómo se juega, tipo manual, con capturas de `juego/`; sistemas (§9.3); arquitectura del juego (§9.4, mejor con un dibujo); servidor y anti-trampas (§9.5) con los diagramas de secuencia de una partida (`fig:sec-partida`, §7.10) y de contratar con concurrencia optimista (`fig:sec-contratar`, §7.11); logros (§9.6); evolución por fases (§9.7, tabla) | §7.10–7.11, 9, 16 | 1800 palabras |
| `05-evaluacion.tex` | Diseño de la evaluación. Pruebas (§10: estrategia, tabla por fichero, 276 pruebas, comprobaciones manuales). CI/CD (§11) con el pipeline en TikZ (`fig:pipeline`, §7.12) y la captura del CI en verde. Registro de actividad y manejo de errores (§12). Revisión frente al enunciado (revision-entrega). Prueba técnica (§7.13 y RF-13) con sus capturas. Comprobación en producción (capturas de `produccion/`). **Métricas** (§14, tabla). Resultados y discusión | §7.12–7.13, 10–12, 14 | 1200 palabras |
| `06-conclusiones.tex` | Conclusiones en el orden de los objetivos del capítulo 1, diciendo cómo se ha cumplido cada uno; lecciones aprendidas (§15.1); **trabajo futuro** (§15.2: multijugador con *party* de hasta 4 y amigos, y el resto) | §15 | 500 palabras |

### Anexos

| Archivo | Contenido | Mínimo |
|---|---|---|
| `a1-desarrollo.tex` | **Una sección por sprint con el mismo esquema** (lo pide el profesor): *Planificación* (objetivo, fechas, sprint backlog en tabla, historias de usuario: en el Sprint 2 las 29 con sus criterios resumidos, en `longtable`); *Desarrollo* (problema → solución de §13 en tablas, no un diario); *Revisión* (entregas, releases, cronología §4.6); *Retrospectiva* (burndown con pgfplots: `fig:burndown-s1` con la tabla de evolución del Sprint 1, y `fig:burndown-s2` con el **burndown real por fechas de los PR**; capturas de las gráficas de DoneTonic; cambio de alcance de P19). Hay que **explicar que las gráficas de DoneTonic del Sprint 2 salen en recta porque el backlog se registró al cerrar el sprint (29/10)** | 2500 palabras |
| `a4-trazabilidad.tex` | **Anexo nuevo: «Trazabilidad»** con `\label{anx:trazabilidad}`. Tabla completa (`longtable`) requisito → PBI → tarea → PR de los dos sprints: **todos los PBIs P1–P48 y todas las tareas T1–T82** (§3 da requisito → PBI; la gestión da PBI → tarea → PR) | 150 palabras + tabla |
| `a2-material.tex` | Enlaces con `\url`: repositorio, aplicación desplegada, releases `hito-1`…`hito-4`, documentación del repositorio y DoneTonic | 60 palabras |
| `a3-uso-ia.tex` | Uso responsable de la IA con los hechos de `uso-ia.md` | 250 palabras |

### Páginas iniciales
- `elements/preambulo.tex`: **Resumen** (≥ 150 palabras, de los dos sprints y el juego) con
  «Palabras clave», y una página nueva **Abstract** en inglés (≥ 120 palabras) con «Keywords», con el
  mismo formato que el Resumen (`\Large{\bft{Abstract}}`). La declaración de autoría no se toca.

### Figuras, tablas y bibliografía
- Al menos **30 figuras** y **15 tablas**, cada una con `\caption`, `\label` (`fig:…`, `tab:…`) y citada
  con `\ref` en el texto.
- Figuras con etiqueta fija (las comprueba el test y tienen que ser dibujos, no imágenes): `fig:capas`,
  `fig:modelo-datos`, `fig:sec-registro`, `fig:sec-confirmacion`, `fig:sec-login`, `fig:sec-google`,
  `fig:sec-baja`, `fig:sec-partida`, `fig:sec-contratar`, `fig:pipeline` (TikZ o `sequencediagram`) y
  `fig:burndown-s1`, `fig:burndown-s2` (pgfplots).
- Capturas: solo las nuevas, con su ruta: `\includegraphics[...]{figs/capturas/juego/01-menu}`. Al menos
  4 de `app/`, 4 de `hito4/`, 8 de `juego/`, 5 de `donetonic/`, 2 de `produccion/` y 1 de
  `prueba-tecnica/`. Las antiguas (`figs/capturas/app-*.png`, `figs/capturas/donetonic-*.png`) ya no
  valen. Verticales (móvil): `width=0.35\textwidth`; el resto, `width=0.9\textwidth` como máximo.
- Diagramas de secuencia grandes: dentro de `\resizebox{\textwidth}{!}{...}` para que no se salgan.
- Tablas de más de media página con `longtable`. Nada fuera del margen.
- Bibliografía (`bib/ref.bib`, `apalike`): Scrum Guide, Express, Node.js, PostgreSQL, OAuth 2.0
  (RFC 6749), bcrypt, GitHub Flow, GitHub Actions, Google Cloud Run, *Vampire Survivors* (género
  *survivor*) y el enunciado. Solo URLs que estén en las fuentes; todas con `year` (`{s.f.}` si no hay
  fecha); autores que son organizaciones con doble llave; todas citadas.

## Estilo

- Español formal de TFG, impersonal o en tercera persona. **Explicar el porqué de cada decisión**, no
  solo el qué.
- Claro y **sin adornos**: nada de «trasciende», «exhaustivo», «riguroso», «de forma integral», «es
  fundamental subrayar». Frases cortas.
- Rutas, comandos y nombres de código en `\texttt{}`, escapando `_`, `#`, `%`, `&` y `$`.
- Proyecto de aficionado sin relación oficial con el Club Atlético de Madrid: decirlo una vez.

## Cómo se comprueba

`comando_prueba` compila con LuaLaTeX y ejecuta `verificar.py`, que comprueba contra las mismas fuentes:
estructura, sin relleno ni DNI, sin referencias ni citas rotas, bibliografía, figuras y tablas con
caption, label y `\ref`, figuras con etiqueta fija, capturas mínimas por carpeta, todos los RF/RJ/RNF en
el texto, todos los PBIs y tareas en el anexo de trazabilidad, mínimos de palabras, Resumen y
Abstract, números > 20 en las fuentes, nada fuera del margen y el PDF sin «??».

## Orden de trabajo sugerido (máximo 3 archivos por paso)

1. `04-descripcion.tex`: requisitos, arquitectura (`fig:capas`), modelo de datos (`fig:modelo-datos`) y API.
2. `04-descripcion.tex`: flujos con los 5 diagramas de secuencia, seguridad y la aplicación con capturas.
3. `04b-juego.tex` completo (con `fig:sec-partida` y `fig:sec-contratar`) y `bib/ref.bib`.
4. `a1-desarrollo.tex` (los dos sprints) y `a4-trazabilidad.tex`.
5. `05-evaluacion.tex`.
6. `01-introduccion.tex`, `03-propuesta.tex` y `06-conclusiones.tex`.
7. `elements/preambulo.tex` (Resumen y Abstract), `a2-material.tex` y `a3-uso-ia.tex`.
8. Repasar lo que diga el revisor hasta que `verificar.py` pase.

## Criterios de terminado

- [ ] `comando_prueba` pasa (compila y `verificar.py` OK).
- [ ] El juego y el Sprint 2 están descritos; ningún capítulo dice que el Hito 4 esté pendiente.
- [ ] El anexo de desarrollo tiene las dos secciones de sprint con el mismo esquema y explica la recta
      de las gráficas del Sprint 2.
- [ ] El revisor ha contrastado con las fuentes, en COMPROBACIONES, **al menos 25 datos** repartidos por
      todos los capítulos y anexos (cifra o hecho → sección de la fuente), incluidos números pequeños.
