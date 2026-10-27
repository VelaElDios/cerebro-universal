# Spec: memoria de La Grada Colchonera, Sprint 1 completo (Procesos de Ingeniería del Software)

## Qué es

La memoria del trabajo de la asignatura Procesos de Ingeniería del Software (PIS), curso 2026-2027,
con el formato de un TFG de la ESIIAB-UCLM. Describe el **Sprint 1 completo (Hitos 1 a 4)** de
*La Grada Colchonera*: la base de una aplicación SaaS en capas (cuentas, sesión, roles, persistencia,
correo, inicio de sesión con Google, manejo de errores, despliegue), y sobre todo el **proceso**
(Scrum en DoneTonic, GitHub Flow, CI/CD y despliegue en Google Cloud Run).

**Versión 2.** El borrador ya tiene una memoria completa de los Hitos 1–3 escrita con fuentes antiguas
(una guía del 12/10/2026). Ahora el Sprint 1 está cerrado y la fuente es **el repositorio del proyecto**,
que el cerebro descarga en cada paso. Hay que **actualizar** la memoria, no rehacerla desde cero:
corregir lo que haya cambiado, añadir el Hito 4 y la prueba técnica, y usar las capturas nuevas.

**El juego no se explica en esta memoria.** El producto evolucionó a un juego después del Sprint 1;
como mucho se menciona en una frase en el trabajo futuro, sin describirlo.

## Fuentes: la única verdad

Se te pasan en cada mensaje. Las del repositorio (`repo:saas/...`) son siempre la última versión:

| Fuente | Contenido |
|---|---|
| `repo:saas/docs/documentacion-tecnica.md` | **Fuente principal.** Escrita para la memoria: requisitos (RF/RNF), metodología, arquitectura, diseño, flujos con diagramas de secuencia (Mermaid), seguridad, pruebas, CI/CD, errores, problemas, métricas y conclusiones. Su §1 dice qué sección alimenta cada capítulo. |
| `repo:saas/docs/gestion/README.md` | Gestión en DoneTonic: backlog, trazabilidad tarea → rama → PR y evolución del sprint |
| `repo:saas/docs/revision-entrega.md` | Revisión de los requisitos del enunciado, uno a uno, con su evidencia |
| `repo:saas/docs/hito4-configuracion.md` | Configuración del Hito 4 (correo y Google) |
| `repo:saas/CONTRIBUTING.md` | Flujo de trabajo con ramas, commits y PR |
| `repo:saas/@arbol` | Lista de archivos del repositorio (estructura del código) |
| `repo:saas/memoria/bibliografia.bib` | Referencias bibliográficas del proyecto (las únicas URLs que valen en `bib/ref.bib`) |
| `fuentes/estructura-memoria.md` | Qué debe tener cada capítulo según el profesor |
| `fuentes/uso-ia.md` | Hechos para el anexo de uso de la IA |
| imágenes disponibles | Lista de capturas copiadas del repo a `figs/capturas/` con lo que muestra cada una |

**Regla de oro:** cada dato (cifras, fechas, nombres, versiones, URLs, números de PR) sale de las
fuentes, copiado tal cual. Si algo no está en las fuentes, **no se escribe**. Si el borrador tiene un
dato de la versión anterior que ya no aparece en las fuentes (por ejemplo, número de pruebas o líneas
de código, o «el Hito 4 queda pendiente»), se actualiza con el de las fuentes. El test comprueba que
todo número mayor que 20 del texto aparece en las fuentes; los pequeños los comprueba el revisor.

## Qué no se toca

- Archivos protegidos (se ignoran si se intentan escribir): `Memoria.tex`, `latexmkrc`,
  `include/configuracion.tex`, `include/colores.tex`, `elements/portada.tex` y `figs/*`.
- Los paquetes nuevos van en `include/extra.tex`.
- `\espec` en `include/opciones.tex`: lo confirma Javier.

## Qué hay que hacer

### Capturas
- Las capturas buenas son las nuevas: `figs/capturas/app/`, `figs/capturas/hito4/`,
  `figs/capturas/donetonic/`, `figs/capturas/produccion/` y `figs/capturas/prueba-tecnica/`.
  Las antiguas (`figs/capturas/app-*.png`, `figs/capturas/donetonic-*.png`) se sustituyen por las nuevas
  equivalentes en todos los capítulos.
- Imágenes verticales (móvil): `width=0.35\textwidth`. El resto: `width=0.9\textwidth` como máximo.

### Diagramas
- Los diagramas de la documentación técnica están en Mermaid: se redibujan en **TikZ** (no se pueden
  usar imágenes de Mermaid). Hacen falta al menos: arquitectura en capas (actualizada), pipeline de CI/CD
  (actualizado con §11), burndown con pgfplots (con los datos de la evolución del sprint) y **al menos dos
  diagramas de secuencia**: confirmación de la cuenta por correo (§7.1–7.2) e inicio de sesión con Google
  (§7.4). Un diagrama de secuencia en TikZ: participantes como nodos arriba, líneas de vida discontinuas
  y flechas horizontales con etiqueta, de arriba abajo.

### Datos y páginas iniciales
- `include/opciones.tex`: título y fecha se mantienen salvo que las fuentes digan otra cosa del Sprint 1.
- `elements/preambulo.tex`: actualizar el **Resumen** (≥ 120 palabras) y las *Palabras clave* con el
  Sprint 1 completo.

### Capítulos (en `chapters/`)

| Archivo | Contenido (sección de `documentacion-tecnica.md`) | Mínimo |
|---|---|---|
| `01-introduccion.tex` | Motivación y contexto (§2.1), objetivos (§2.2, solo los del Sprint 1), alcance: Hitos 1–4 y cierre del sprint (§2.3, sin contar el juego), estructura de la memoria con `\ref`. | 400 palabras |
| `03-propuesta.tex` | Propuesta de solución sin detalles técnicos. Metodología: Scrum en DoneTonic, definición de hecho, GitHub Flow por hitos (§4.1–4.3, gestión, CONTRIBUTING). Herramientas (tabla). Captura de DoneTonic. | 600 palabras |
| `04-descripcion.tex` | Requisitos RF/RNF del Sprint 1 (§3.1 y §3.3, sin los del juego §3.2). Arquitectura (§5) y diseño (§6: módulos, modelo de datos, frontend, API). Flujos principales con los diagramas de secuencia (§7.1–7.9, sin §7.10–7.11 del juego). Seguridad (§8). Resumen del sprint remitiendo al Anexo A. La aplicación tipo manual de usuario con las capturas de `app/` y `hito4/`. | 1500 palabras |
| `05-evaluacion.tex` | Pruebas (§10, solo las del Sprint 1 si se distinguen), CI/CD (§11), registro de actividad y manejo de errores (§12), revisión frente al enunciado (revision-entrega), prueba técnica (§7.13, capturas de `prueba-tecnica/`) y comprobación en producción (capturas de `produccion/`). Resultados con cifras y discusión. | 400 palabras |
| `06-conclusiones.tex` | Conclusiones en el orden de los objetivos del capítulo 1. Trabajo futuro (§15), sin describir el juego. | 300 palabras |

### Anexos

| Archivo | Contenido | Mínimo |
|---|---|---|
| `a1-desarrollo.tex` | Sprint 1 con el esquema de la plantilla: planificación (objetivo, fechas, sprint backlog, trazabilidad §4.4), desarrollo por hitos (problema-solución de §13, en tablas, no un diario), revisión (entregas, cronología §4.6, métricas §14) y retrospectiva (burndown §4.5, captura de las gráficas de DoneTonic, cambio de alcance). | 900 palabras |
| `a2-material.tex` | Enlaces: repositorio, aplicación, releases y documentación del repositorio. Con `\url`. | 60 palabras |
| `a3-uso-ia.tex` | Uso responsable de la IA con los hechos de `uso-ia.md` y lo que digan las fuentes del repo sobre la IA. | 200 palabras |

### Figuras, tablas y bibliografía
- Al menos **6 figuras** y **5 tablas**, cada una con `\caption`, `\label` (`fig:…`, `tab:…`) y citada con `\ref`.
- Obligatorio: 5 dibujos TikZ (los 4 de arriba + otro diagrama de secuencia o de despliegue), 3 capturas de
  `app/`, 3 de `hito4/` y 1 de DoneTonic.
- Tablas de más de media página con `longtable`. Nada fuera del margen.
- Bibliografía (`bib/ref.bib`, apalike): solo referencias cuyas URLs estén en las fuentes; todas con
  `year` (`{s.f.}` si no hay fecha) y los autores que son organizaciones con doble llave. Cada una citada.

## Estilo

- Español, impersonal, claro y **sin adornos**: nada de «trasciende», «exhaustivo», «riguroso», «de
  forma integral», «es fundamental subrayar». Frases cortas que expliquen el porqué de cada decisión.
- Rutas, comandos y nombres de código en `\texttt{}`, escapando `_`, `#`, `%`, `&` y `$`.
- Proyecto de aficionado sin relación oficial con el Club Atlético de Madrid: decirlo una vez.

## Cómo se comprueba

`comando_prueba` compila con LuaLaTeX y ejecuta `verificar.py`, que comprueba contra las mismas fuentes
(incluido el repo): estructura, sin relleno ni DNI, sin referencias ni citas rotas, bibliografía, figuras
y tablas con caption, label y `\ref`, figuras obligatorias, mínimos de palabras, números > 20 en las
fuentes, nada fuera del margen y el PDF sin «??».

## Orden de trabajo sugerido (máximo 3 archivos por paso)

1. `04-descripcion.tex` (requisitos, arquitectura y capturas nuevas).
2. `include/extra.tex` si hace falta y los diagramas de secuencia en `04-descripcion.tex`.
3. `05-evaluacion.tex` y `a1-desarrollo.tex`.
4. `01-introduccion.tex`, `03-propuesta.tex` y `06-conclusiones.tex`.
5. `elements/preambulo.tex` (resumen), `a2-material.tex` y `a3-uso-ia.tex`.
6. Repasar lo que diga el revisor hasta que `verificar.py` pase.

## Criterios de terminado

- [ ] `comando_prueba` pasa (compila y `verificar.py` OK).
- [ ] Ningún capítulo dice que el Hito 4 está pendiente; el Hito 4 y la prueba técnica están descritos.
- [ ] El revisor ha contrastado con las fuentes, en COMPROBACIONES, al menos 15 datos repartidos por los
      capítulos (cifra o hecho → sección de la fuente), incluidos números pequeños.
- [ ] El juego no se describe.
