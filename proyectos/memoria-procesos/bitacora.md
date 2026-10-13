# Bitácora del proyecto

Registro de lo que hace cada IA, paso a paso.

## 2026-10-13 · Preparación (Claude, a petición de Javier)

- `borrador/` parte de la plantilla oficial del TFG de la ESIIAB-UCLM (la que pasó Javier), ya compilando
  con LuaLaTeX: capítulos renombrados sin espacios, estructura según las recomendaciones del profesor
  (con Evaluación y anexos de material adicional y uso de la IA), tutor opcional en la segunda portada,
  una llave sin cerrar del índice corregida, `include/extra.tex` para paquetes nuevos y `latexmkrc`.
- Capturas reales de la aplicación y de DoneTonic en `borrador/figs/capturas/` (del repositorio del SaaS).
- Fuentes en `fuentes/`: la guía del proyecto, la documentación del repositorio y la estructura pedida.
- Test: `verificar.py`. Ahora falla a propósito (todo es texto de relleno): el trabajo es rellenarlo.

## 2026-10-13 02:21 · Constructor (gemini · gemini-3.5-flash-lite)

Se han configurado los metadatos iniciales en `include/opciones.tex` con el título y la fecha correctos, se ha adaptado la segunda portada, la declaración de autoría y el resumen (con más de 120 palabras y palabras clave) en `elements/preambulo.tex`, eliminando la dedicatoria, los agradecimientos y los datos de ejemplo, y se ha preparado la bibliografía en `bib/ref.bib` con las referencias requeridas.

**Archivos:** `include/opciones.tex`, `elements/preambulo.tex`, `bib/ref.bib`

**Intentos:**
- intento 1: ❌ VERIFICACIÓN FALLIDA: 28 problema(s)
- intento 2: no se hace, el fallo es por trabajo pendiente (no cumple «reintentar_si»); lo revisa el revisor

**Siguiente:** Configurar `include/extra.tex` con los paquetes TikZ y pgfplots (cargando la librería babel de TikZ según las lecciones aprendidas) y redactar los capítulos `01-introduccion.tex` y `03-propuesta.tex`.

## 2026-10-13 02:22 · Revisor (openrouter-grandes · nvidia/nemotron-3-ultra-550b-a55b:free)

**Veredicto:** cambios · **Prueba:** ❌ falla la prueba

**Comprobaciones:**
- Título en opciones.tex: "La Grada Colchonera: base SaaS y proceso de desarrollo" → coincide con guia.md §1 y spec
- Fecha en opciones.tex: "Octubre, 2026" → coincide con fin del Sprint 1 (27/10/2026) en guia.md
- Autor en opciones.tex: "Javier Vela González-Román" → coincide con guia.md
- Segunda portada en preambulo.tex: "TRABAJO DE PROCESOS DE INGENIERÍA DEL SOFTWARE" → cumple spec (cambia "TRABAJO FIN DE GRADO")
- Dedicatoria y agradecimientos eliminados en preambulo.tex → cumple spec (son personales)
- Declaración de autoría: estructura correcta (autor, título, atribución, mención anexo IA), sin DNI ni huecos → cumple spec
- Resumen en preambulo.tex: ~137 palabras (≥ 120) → cumple spec
- Línea "Palabras clave:" presente en preambulo.tex → cumple spec
- Bibliografía en bib/ref.bib: 9 referencias @misc con howpublished=\url{} (8 con URL, enunciado sin URL) → coincide exactamente con guia.md §10
- Referencias cubren: Express, GitHub Flow, Node.js, PostgreSQL, Cloud Run, GitHub Actions, Scrum Guide, Neon limits, Enunciado → todas en guia.md §10
- Espec en opciones.tex: "Ingeniería del Software" → coincide con guia.md

El constructor ha completado correctamente el primer paso (3 archivos de configuración). Los datos de título, fecha, autor y bibliografía coinciden con las fuentes. Se han eliminado dedicatoria y agradecimientos, y la segunda portada tiene el texto correcto.

**Dos correcciones menores en `elements/preambulo.tex`:**
1. La declaración de autoría dice "en el anexo correspondiente" pero la spec pide explícitamente "en el Anexo C (\ref{anx:ia})".
2. La fecha en la firma dice "Albacete, a \fecha" y la spec dice "Albacete, \fecha" (sin la preposición "a").

El resto de errores del test (capítulos con lipsum, 0 figuras/tablas, bibliografía sin citas, conteos de palabras) son esperables porque solo se han tocado estos 3 archivos; los capítulos se redactarán en los siguientes pasos.

**Correcciones del revisor:** `elements/preambulo.tex`

**Tareas para el constructor:**
- Configurar `include/extra.tex` con los paquetes necesarios: TikZ (con librería `babel`), pgfplots, booktabs, placeins, csquotes, icomma y cualquier otro que vaya a usarse en figuras y tablas.
- Redactar `chapters/01-introduccion.tex`: motivación (asignatura evalúa aplicación y proceso), objetivo principal y específicos (sacados de hitos/requisitos), alcance (Hitos 1–3), estructura de la memoria (capítulos y anexos con `\ref`). Mínimo 350 palabras. Incluir la frase «proyecto de aficionado sin relación oficial con el Club Atlético de Madrid».
- Redactar `chapters/03-propuesta.tex`: propuesta de solución sin detalles técnicos (§1 guía), metodología (Scrum en DoneTonic, GitHub Flow por hitos, §3, §5, contributing), herramientas en tabla agrupadas (gestión, desarrollo, despliegue, documentación, §6). Mínimo 500 palabras. Citar referencias con `\cite`.

## 2026-10-13 03:01 · Constructor (gemini · gemini-flash-latest)

He configurado `include/extra.tex` con los paquetes necesarios (TikZ con soporte babel, pgfplots, booktabs, placeins, csquotes e icomma). He redactado íntegramente `chapters/01-introduccion.tex` cubriendo motivación, objetivos específicos, alcance de la entrega (Hitos 1–3) y estructura de la memoria con referencias cruzadas. Asimismo, he redactado `chapters/03-propuesta.tex` detallando la propuesta de solución, la metodología ágil (Scrum en DoneTonic y GitHub Flow) y la tabla de herramientas clasificadas por categoría, enlazando todas las referencias bibliográficas.

**Archivos:** `include/extra.tex`, `chapters/01-introduccion.tex`, `chapters/03-propuesta.tex`

**Intentos:**
- intento 1: ❌ VERIFICACIÓN FALLIDA: 16 problema(s)
- intento 2: no se hace, el fallo es por trabajo pendiente (no cumple «reintentar_si»); lo revisa el revisor

**Siguiente:** Redactar `chapters/04-descripcion.tex` con los requisitos (tabla RF/RNF), arquitectura (diagrama TikZ de capas, modelo de datos, flujo de sesión, tabla de API), decisiones técnicas justificadas, tabla resumen del sprint y manual de la aplicación con las capturas `app-*`.

## 2026-10-13 03:04 · Revisor (openrouter-grandes · nvidia/nemotron-3-ultra-550b-a55b:free)

**Veredicto:** cambios · **Prueba:** ❌ falla la prueba

**Comprobaciones:**
- Título en opciones.tex: "La Grada Colchonera: base SaaS y proceso de desarrollo" → coincide con guia.md §1 y spec
- Fecha en opciones.tex: "Octubre, 2026" → coincide con fin Sprint 1 (27/10/2026) en guia.md
- Autor en opciones.tex: "Javier Vela González-Román" → coincide con guia.md
- Segunda portada en preambulo.tex: "TRABAJO DE PROCESOS DE INGENIERÍA DEL SOFTWARE" → cumple spec (cambia "TRABAJO FIN DE GRADO")
- Declaración de autoría: menciona "Anexo C (\ref{anx:ia})", sin DNI ni huecos → cumple spec
- Resumen en preambulo.tex: ~137 palabras (≥120) + línea "Palabras clave:" → cumple spec
- Bibliografía bib/ref.bib: 9 referencias @misc con howpublished=\url{} (8 con URL, enunciado sin URL) → coincide exactamente con guia.md §10
- Cap.1 Motivación: asignatura evalúa aplicación y proceso → guia.md §1 "El propósito pedagógico... evaluar exhaustivamente el proceso"
- Cap.1: "proyecto de aficionado sin relación oficial con el Club Atlético de Madrid" → guia.md §1 textual
- Cap.1 Alcance: limitado a Hitos 1–3, Hito 4 pospuesto → guia.md §1 "El profesor limitó la primera entrega a los Hitos 1–3"
- Cap.1 Objetivos: 7 objetivos específicos mapeados a hitos/requisitos (arquitectura, auth, roles, BD, pruebas, CI/CD, proceso ágil) → guia.md §1 hitos y §2 requisitos
- Cap.1 Estructura: cita capítulos y anexos con \ref → estructura-memoria.md
- Cap.3 Metodología: Scrum en DoneTonic (espacio TFG, proyecto Colchoneros, Sprint 1 29/09–27/10) → guia.md §5.3, gestion.md
- Cap.3: 19 PBIs, 32 tareas, todos MUST → guia.md §5.3, gestion.md tabla
- Cap.3 DoD: 4 criterios (código en rama+PR, CI verde, PR fusionado, docs actualizadas) → guia.md §5.3 textual
- Cap.3 GitHub Flow: ramas main, hito-N/integracion, hito-N/Tx-descripcion → contributing.md, guia.md §5.1
- Cap.3 Herramientas: tabla 4 categorías (Gestión, Desarrollo, Despliegue, Documentación) con 11 herramientas → guia.md §6
- Cap.3 Citas \cite{enunciado,scrumguide,githubflow,nodejs,express,postgresql,neonlimits,cloudrun,githubactions} → todas existen en bib/ref.bib
- include/extra.tex: tikz con librería babel, pgfplots, booktabs, csquotes, icomma, placeins → lecciones aprendidas (babel para spanish, icomma para comas, placeins para FloatBarrier)

Lo bueno: Los tres archivos del paso 2 están correctos en contenido y fuentes. El capítulo 1 cubre motivación, objetivos (7 específicos bien mapeados), alcance (Hitos 1–3) y estructura con referencias cruzadas. El capítulo 3 describe la propuesta sin detalles técnicos, la metodología (Scrum en DoneTonic con DoD textual, GitHub Flow por hitos) y la tabla de herramientas clasificada en 4 categorías con 11 entradas, todas citadas. La bibliografía coincide exactamente con guia.md §10. Los paquetes en extra.tex incluyen lo necesario para figuras/tablas futuras y respetan las lecciones (babel para TikZ, icomma, placeins).

Lo malo/pendiente: La tabla de herramientas en cap.3 desborda el margen (error del test: "algo se sale 35 pt del margen en líneas 29-30"). Las columnas L{3.2cm}+L{3.5cm}+L{7.5cm}=14.2cm superan el ancho de texto útil. Hay 0 figuras y 1 tabla (se piden ≥6 y ≥5 totales, pero irán en siguientes capítulos). Los demás capítulos siguen con lipsum (esperable).

He corregido yo la anchura de la tabla en el archivo adjunto.

**Correcciones del revisor:** `chapters/03-propuesta.tex`

**Tareas para el constructor:**
- Redactar `chapters/04-descripcion.tex`: requisitos (tabla RF/RNF con estado), arquitectura (diagrama TikZ capas, modelo de datos, flujo sesión, tabla API), decisiones técnicas justificadas, tabla resumen sprint (fechas, objetivo, PBIs, estado) remitiendo a Anexo A, manual de usuario con capturas `app-*` (mínimo 3 capturas de app + 1 DoneTonic = 4 figuras, más arquitectura y burndown = 6).
- Redactar `chapters/05-evaluacion.tex`: diseño evaluación (pruebas automatizadas, CI contra PostgreSQL 17, revisión frase a frase, comprobación despliegue), resultados con cifras §7, discusión (garantías y limitaciones: historial concentrado en un día).
- Redactar `chapters/06-conclusiones.tex`: conclusiones en orden objetivos cap.1, trabajo futuro (3 ideas §9: OAuth/correo, manejo errores, rediseño visual).
