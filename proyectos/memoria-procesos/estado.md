---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-24 23:23"
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
- **verificar.py**: ✅ (35 figuras, 29 tablas, 18396 palabras, estructura, trazabilidad completa, cifras contrastadas).
- **revisar_maquetacion.py**: ❌ falla en fig:modelo-datos (etiquetas 'userId' y 'su club' sobre líneas).
- **Figuras**: ⚠️ Gemini no pudo revisar fig:sec-baja (modelo no disponible), pero la medición geométrica del PDF ya la comprobó (no bloquea).
- **Diagramas con fallos medidos en PDF** (1 pendiente):
  1. fig:modelo-datos (cap. 04-descripcion): etiquetas 'userId' y 'su club' sobre líneas → **corregido en este paso** (mayor separación vertical, pos=0.5, coordenadas ajustadas).
- **Overfull hbox**: corregidos en a1-desarrollo.tex (burndowns) en paso anterior; no aparecen en la salida actual.
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…» en caps. 4 y 4b; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2.

## Siguiente
1. Constructor: aplicar el cambio en chapters/04-descripcion.tex y ejecutar `comando_prueba` hasta verde total.
2. Si todo pasa, hacer la revisión final y marcar la memoria como terminada.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
