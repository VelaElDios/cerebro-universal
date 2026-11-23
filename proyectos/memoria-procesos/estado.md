---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-24 00:57"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = compilar + `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco; hidelinks.
- Tablas `p{}` + `\small` en longtable; capturas máx. `height=0.42\textheight`, móviles `width=0.35\textwidth`; diagramas grandes con `adjustbox`.
- Cada imagen una sola vez; en el resto `\ref`. **Cada `\label`, incluidas subfiguras, debe citarse con `\ref` en el texto**.
- Prosa de TFG: nada de «La figura X muestra…» suelto; capturas integradas en párrafos y agrupadas con `subfigure`.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1 pero burndown de entrega cuenta 16; 276 pruebas al cierre Sprint 2, 322 tras Fase 7; 23 endpoints; 5 migraciones).

## Estado
- **Compilación**: OK (98 páginas, LuaLaTeX). `verificar.py`: ✅ (35 figuras, 29 tablas, 18409 palabras).
- **revisar_maquetacion.py**: ❌ 2 errores: `fig:sec-registro` 581 pt ancho (04-descripcion.tex:361), `fig:sec-login` 183 pt ancho (04-descripcion.tex:435). **Empeorados tras intento de corrección**.
- **Diagramas con fallos medidos**: `fig:modelo-datos` (palabras partidas), `fig:sec-confirmacion` (línea cruza caja), `fig:sec-login` (flechas cruzan cajas alt), `fig:sec-google` (etiquetas ajustadas, líneas cruzadas), `fig:juego-arquitectura` (referenciada pero no en página).
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…»; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2.
- **Corregido en este paso**: `fig:sec-registro` y `fig:sec-login` replanteados con 4 participantes, `\newinst[3]`, etiquetas cortas, llamadas internas anidadas.
- **Pendiente**: (1) Estrechar `fig:modelo-datos`. (2) Replantear `fig:sec-confirmacion`. (3) Replantear `fig:sec-google`. (4) Fijar `fig:juego-arquitectura`. (5) Añadir cita a `fig:sec-google` en texto. (6) Ejecutar `revisar_umlsd.py` y corregir 11 diagramas. (7) Revisión visual de esos 11 diagramas en PDF. (8) Revisión visual final página a página.

## Siguiente
1. Aplicar las 4 tareas de diagramas pendientes en 04-descripcion.tex y 04b-juego.tex.
2. Añadir cita faltante a `fig:sec-google` en 04-descripcion.tex.
3. Ejecutar `revisar_umlsd.py` sobre los 11 diagramas pendientes y corregir errores.
4. Revisión visual de los 11 diagramas en PDF (letras ≥ 7.5 pt, sin cruces, sin palabras partidas, codos).
5. Revisión visual final del PDF página a página.
6. Re-ejecutar `comando_prueba` hasta verde total.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
