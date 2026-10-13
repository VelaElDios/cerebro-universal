# Spec: memoria de La Grada Colchonera (Procesos de Ingeniería del Software)

## Qué es

La memoria del trabajo de la asignatura Procesos de Ingeniería del Software (PIS), curso 2026-2027,
con el formato de un TFG de la ESIIAB-UCLM. Describe el **Sprint 1** de *La Grada Colchonera*: la base
de una aplicación SaaS con gestión de usuarios, su arquitectura y, sobre todo, el **proceso**
(Scrum en DoneTonic, GitHub Flow, CI/CD y despliegue en Google Cloud Run).

El borrador ya tiene la plantilla oficial de la escuela adaptada y compilando, con los capítulos
vacíos (texto `\lipsum` de relleno) y las capturas reales en `figs/capturas/`. Hay que rellenarla.

## Fuentes: la única verdad

Las fuentes se te pasan en cada mensaje (`fuentes/`, fuera del borrador, no se pueden cambiar):

| Fuente | Contenido |
|---|---|
| `guia.md` | Guía completa del proyecto: objetivo, requisitos, decisiones, arquitectura, procesos, herramientas, cifras, problemas, pendiente y referencias. **Es la fuente principal.** |
| `gestion.md` | Gestión en DoneTonic: backlog, definición de hecho, trazabilidad tarea → rama → PR y evolución del sprint (tabla para el burndown) |
| `revision-entrega.md` | Revisión de los requisitos del enunciado, uno a uno, con su evidencia |
| `contributing.md` | Flujo de trabajo con ramas, commits y PR |
| `estructura-memoria.md` | Qué debe tener cada capítulo según el profesor |
| `figuras.md` | Qué muestra cada captura de `figs/capturas/` |
| `uso-ia.md` | Hechos para el anexo de uso de la IA |

**Regla de oro:** cada dato (cifras, fechas, nombres, versiones, URLs, números de PR) sale de las
fuentes, copiado tal cual. Si algo no está en las fuentes, **no se escribe** (ni horas, ni puntos de
historia, ni usuarios, ni opiniones de terceros). El test comprueba que todo número mayor que 20 del
texto aparece en las fuentes.

## Qué no se toca

- `include/configuracion.tex`, `include/colores.tex` y `elements/portada.tex`: son de la plantilla.
  Los paquetes nuevos (TikZ, pgfplots, booktabs...) van en `include/extra.tex`.
- `latexmkrc`, `figs/` (logos y capturas) y `Memoria.tex` (ya incluye todos los capítulos).
- `\espec` en `include/opciones.tex`: lo confirma Javier.

## Qué hay que hacer

### Datos y páginas iniciales
- `include/opciones.tex`: `\titulo` = `La Grada Colchonera: base SaaS y proceso de desarrollo\,`;
  `\fecha` = `Octubre, 2026\,`. El autor ya está puesto. Sin director ni codirector.
- `elements/preambulo.tex`:
  - Segunda portada: «TRABAJO FIN DE GRADO» pasa a ser «TRABAJO DE PROCESOS DE INGENIERÍA DEL SOFTWARE».
  - Quitar la dedicatoria y los agradecimientos (son personales: si los quiere, los escribe Javier).
  - Declaración de autoría sin DNI ni huecos: «Yo, \autor, declaro que soy el autor del trabajo
    titulado “\titulo”…», que el material no original está atribuido y que el uso de la IA se detalla
    en el Anexo C (`\ref{anx:ia}`). Lugar y fecha: «Albacete, \fecha».
  - **Resumen** (≥ 120 palabras) seguido de una línea *Palabras clave*.

### Capítulos (en `chapters/`)

| Archivo | Contenido (sección de la guía) | Mínimo |
|---|---|---|
| `01-introduccion.tex` | Motivación (§1: la asignatura evalúa la aplicación y el proceso; la aplicación). Objetivo principal y objetivos específicos (sacados de los hitos y requisitos). Alcance de la entrega (Hitos 1–3). Estructura de la memoria (capítulos y anexos con `\ref`). | 350 palabras |
| `03-propuesta.tex` | Propuesta de solución sin detalles técnicos (§1). Metodología: Scrum en DoneTonic (sprint, backlog, definición de hecho) y GitHub Flow por hitos (§3 Proceso, §5, contributing). Herramientas (§6) en una tabla, agrupadas en gestión, desarrollo, despliegue y documentación. | 500 palabras |
| `04-descripcion.tex` | Requisitos (§2) como tabla RF/RNF con su estado. Arquitectura (§4): figura TikZ de las capas, modelo de datos, flujo de la sesión y tabla de la API. Decisiones técnicas y de diseño (§3) justificadas. Desarrollo del proyecto: tabla resumen del sprint (fechas, objetivo, PBIs, estado) remitiendo al Anexo A. La aplicación tipo manual de usuario con las capturas `app-*`. | 900 palabras |
| `05-evaluacion.tex` | Diseño de la evaluación: pruebas automatizadas, CI en cada PR contra PostgreSQL 17, revisión frase a frase contra el enunciado y comprobación del despliegue (§5.2, §7, revision-entrega). Resultados con las cifras de §7. Discusión: qué garantiza todo esto y qué no (historial concentrado en un día, §7 «Observación»). | 300 palabras |
| `06-conclusiones.tex` | Conclusiones en el orden de los objetivos del capítulo 1, diciendo cómo se ha cumplido cada uno. Trabajo futuro: 3 ideas de §9 (Hito 4: OAuth y confirmación por correo; manejo de errores; rediseño visual). | 250 palabras |

### Anexos

| Archivo | Contenido | Mínimo |
|---|---|---|
| `a1-desarrollo.tex` | Sprint 1 con el esquema de la plantilla. Planificación: objetivo, fechas, tabla del sprint backlog (P1–P19 con hito y estado) y trazabilidad. Desarrollo del sprint: problemas y soluciones de §8 (tablas, no un diario). Revisión: qué se entregó (releases, cifras). Retrospectiva: burndown con pgfplots usando la tabla «Evolución del sprint» de `gestion.md`, el cambio de alcance (+P19) y lo aprendido. | 600 palabras |
| `a2-material.tex` | Enlaces: repositorio, aplicación (Cloud Run y Render), releases y documentación del repositorio (§10). Con `\url`. | 60 palabras |
| `a3-uso-ia.tex` | Uso responsable de la IA con los hechos de `uso-ia.md`: qué hizo la IA, qué hizo el alumno y cómo se verificó. | 200 palabras |

### Figuras y tablas
- Al menos **6 figuras** y **5 tablas**, cada una con `\caption`, `\label` (`fig:…`, `tab:…`) y citada en el
  texto con `\ref`.
- Figuras mínimas: arquitectura en capas (TikZ), pipeline de CI/CD o flujo de ramas (TikZ), burndown
  (pgfplots), al menos 3 capturas de la aplicación y 1 de DoneTonic.
- Capturas con `\includegraphics[width=0.9\textwidth]{figs/capturas/…}` (la del móvil, 0.35\textwidth).
- Nada puede salirse del margen: tablas con columnas de ancho fijo (`L{4cm}`, definidas en la plantilla)
  o `\small`.

### Bibliografía (`bib/ref.bib`, BibTeX con estilo apalike)
- Solo las referencias de §10 de la guía. Formato `@misc` con `howpublished = {\url{…}}`.
- El enunciado de la asignatura con la clave `enunciado` (sin URL, es un PDF de la asignatura).
- Cada referencia se cita al menos una vez con `\cite{…}` donde corresponda.

## Estilo

- Español, impersonal («se ha desarrollado», «se decidió»), claro y sin adornos ni frases de relleno.
- Explicar el porqué de cada decisión (la guía lo da siempre).
- Rutas, comandos y nombres de código en `\texttt{}`, escapando `_`, `#`, `%`, `&` y `$`.
- La aplicación es un proyecto de aficionado sin relación oficial con el Club Atlético de Madrid:
  decirlo así una vez (introducción) y no usar escudos ni logos.

## Cómo se comprueba

`comando_prueba` compila con LuaLaTeX y ejecuta `verificar.py` (fuera del borrador), que comprueba:
estructura, que no queda relleno ni DNI, que no hay referencias ni citas rotas, que la bibliografía
solo tiene URLs de las fuentes, figuras y tablas con caption, label y `\ref`, mínimos de palabras,
figuras y tablas, que ningún número mayor que 20 falta en las fuentes y que el PDF no tiene «??».

## Orden de trabajo sugerido (máximo 3 archivos por paso)

1. `include/opciones.tex`, `elements/preambulo.tex` (con el resumen) y `bib/ref.bib`.
2. `include/extra.tex` (TikZ y pgfplots), `01-introduccion.tex` y `03-propuesta.tex`.
3. `04-descripcion.tex`.
4. `05-evaluacion.tex` y `06-conclusiones.tex`.
5. `a1-desarrollo.tex`.
6. `a2-material.tex` y `a3-uso-ia.tex`.
7. Repasar lo que diga el revisor hasta que `verificar.py` pase.

## Criterios de terminado

- [ ] `comando_prueba` pasa (compila y `verificar.py` OK).
- [ ] El revisor ha contrastado con las fuentes, en COMPROBACIONES, al menos 10 datos repartidos por los
      capítulos (cifra o hecho → sección de la fuente).
- [ ] Todos los capítulos y anexos siguen el contenido de las tablas de arriba.
