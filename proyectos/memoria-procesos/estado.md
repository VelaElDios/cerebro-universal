---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-24 09:55"
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
- **Compilación**: OK (98 páginas, LuaLaTeX). `verificar.py`: ✅ (35 figuras, 29 tablas, 18425 palabras).
- **revisar_maquetacion.py**: ❌ 1 error crítico: `fig:modelo-datos` 102 pt más ancha que la página. **Corregida en este paso con replanteo de cajas y flechas con codos**.
- **Diagramas con fallos medidos**: `fig:sec-registro`, `fig:sec-confirmacion`, `fig:sec-login`, `fig:sec-google`, `fig:sec-baja`, `fig:sec-partida`, `fig:sec-contratar` (cruces y etiquetas sobre líneas) → replanteados con participantes ≤3, etiquetas cortas, sin paréntesis en \mess. `fig:juego-arquitectura` referenciada pero no aparecía → movida antes de la referencia y reducido text width.
- **Overfull hbox**: 2 en `a4-trazabilidad.tex` (pendientes).
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…» en caps. 4 y 4b; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2.
- **Corregido en este paso**: 8 diagramas replanteados (modelo-datos, 5 de secuencia en 04-descripcion, 3 en 04b-juego) y colocación de fig:juego-arquitectura.
- **Pendiente**: (1) Ejecutar `revisar_umlsd.py` y corregir 11 diagramas. (2) Corregir overfull hbox en a4-trazabilidad.tex. (3) Añadir cita a `fig:sec-google` en texto. (4) Revisión visual de 11 diagramas en PDF. (5) Revisión visual final página a página. (6) Re-ejecutar `comando_prueba` hasta verde total.

## Siguiente
1. Ejecutar `revisar_umlsd.py` sobre los 11 diagramas de secuencia y corregir errores reportados.
2. Corregir overfull hbox en chapters/a4-trazabilidad.tex (líneas 206-207 y 377-378).
3. Añadir cita faltante a `fig:sec-google` en 04-descripcion.tex (sección 4.5).
4. Revisión visual de los 11 diagramas en PDF compilado (letras ≥ 7,5 pt, sin cruces, sin palabras partidas, codos).
5. Revisión visual final del PDF página a página.
6. Re-ejecutar `comando_prueba` hasta verde total.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
