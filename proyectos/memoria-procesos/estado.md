---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-23 04:50"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco.
- Tablas `p{}` + `\addlinespace`; capturas máx. `height=0.42\textheight` (si quedan solas, bajar a 0.15–0.20 o agrupar en `subfigure` con `adjustbox`); diagramas grandes con `adjustbox`/`max totalheight`.
- Cada imagen una sola vez; en el resto `\ref`. Prosa de TFG: nada de «La figura X muestra…» suelto.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1, pero el burndown de la entrega cuenta 16; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7).

## Estado
- **Compilación**: OK (96 páginas). Overfull hbox residual 10pt en anexo trazabilidad.
- **verificar.py**: OK (35 fig, 29 tab, 17345 palabras, referencias resueltas).
- **revisar_maquetacion.py**: OK (reglas cumplidas; 13 diagramas medidos en PDF sin fallos; 9 diagramas con Gemini 404 no bloquean).
- **revisar_umlsd.py**: pendiente para 9 diagramas.
- **Revisión visual PDF**: pendiente.
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2. Trazabilidad completa 82 tareas. Cadenas "La figura X muestra..." eliminadas en chapters/04-descripcion.tex, 04b-juego.tex y **01-introduccion.tex** (corregido en este paso). Pendientes en 03-propuesta.tex, 05-evaluacion.tex, 06-conclusiones.tex, a1-desarrollo.tex, a3-uso-ia.tex. Imágenes DoneTonic/producción en un solo sitio (cap:propuesta y cap:evaluacion). Diagramas fig:capas, fig:juego-arquitectura, fig:sec-login, fig:sec-baja corregidos.

## Siguiente
1. Eliminar cadenas «La figura X muestra…» en chapters/03-propuesta.tex, 05-evaluacion.tex, 06-conclusiones.tex, a1-desarrollo.tex, a3-uso-ia.tex.
2. Validar 9 diagramas pendientes con `revisar_umlsd.py` y revisión visual; replantear los que fallen.
3. Fusionar secciones de 1-2 líneas y eliminar repeticiones de párrafos entre capítulos.
4. Ejecutar `comando_prueba` y confirmar compilación, `verificar.py` OK y `revisar_maquetacion.py` OK.
5. Revisión visual final del PDF página a página.
6. Verificar mínimos de capturas por carpeta y referencias `\ref` cruzadas correctas.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
