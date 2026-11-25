---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-25 13:47"
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
- **verificar.py**: ✅ (35 figuras, 29 tablas, 18374 palabras, estructura, trazabilidad completa, cifras contrastadas).
- **revisar_maquetacion.py**: ✅ cumple todas las reglas de maquetación (incluidos los 3 diagramas de secuencia medidos y revisados).
- **Figuras**: 35 figuras y 29 tablas con caption, label y \ref; figuras fijas obligatorias presentes.
- **Capturas**: ≥4 app/, ≥4 hito4/, ≥8 juego/, ≥5 donetonic/, ≥2 produccion/, ≥1 prueba-tecnica/.
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…» en caps. 4 y 4b; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2.
- **Hito 4**: descrito como completado en todos los capítulos.

## Siguiente
Proyecto terminado. La memoria está lista para entrega y actualización de `final/`.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
