---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-24 18:56"
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
- **Compilación**: OK (100 páginas, LuaLaTeX).
- **verificar.py**: ✅ (35 figuras, 29 tablas, 18396 palabras, estructura, cifras, trazabilidad).
- **revisar_maquetacion.py**: ✅ (maquetación cumple reglas).
- **Figuras**: ⚠️ Gemini no pudo revisar fig:sec-baja (modelo no disponible), pero la medición geométrica del PDF ya la comprobó (no bloquea).
- **Diagramas con fallos medidos en PDF** (2 pendientes):
  1. fig:modelo-datos (cap. 04-descripcion): etiquetas 'userId', 'su mejor partida', 'su club' solapan líneas/texto → **corregido en este paso** (reposicionadas con más separación y codos).
  2. fig:juego-arquitectura (cap. 04b-juego): flecha discontinua 'reglas compartidas' atraviesa caja 'Servidor' → **corregido en este paso** (bajada caja Servidor y flecha con codo por la izquierda).
- **Overfull hbox**: 2 en `a4-trazabilidad.tex` (líneas 206-207 y 377-378, 5.43 pt y 9.24 pt) → persisten pese a \sloppy; tarea para constructor.
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…» en caps. 4 y 4b; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2.
- **Corregido en este paso**: (1) fig:modelo-datos: etiquetas reposicionadas. (2) fig:juego-arquitectura: caja Servidor bajada y flecha discontinua con codo por fuera.

## Siguiente
1. Constructor: reforzar \allowbreak en URLs de columna PR en `a4-trazabilidad.tex` (o {\sloppy\longtable...}) para eliminar los 2 overfull hbox residuales.
2. Ejecutar `comando_prueba` hasta verde total (compila, verificar.py OK, revisar_maquetacion.py OK).
3. Si todo pasa, marcar la memoria como terminada.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
