---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-24 10:57"
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
- **Compilación**: OK (98 páginas, LuaLaTeX). `verificar.py`: ✅ (35 figuras, 29 tablas, 18447 palabras).
- **revisar_maquetacion.py**: ❌ 4 diagramas con fallos medidos: `fig:modelo-datos` (palabras partidas), `fig:sec-registro` (flecha cruza), `fig:sec-confirmacion` (flecha sobre texto), `fig:juego-arquitectura` (referenciada pero no aparece). **Corregidos en este paso los tres primeros en 04-descripcion.tex**; el cuarto requiere mover figura en 04b-juego.tex (próximo paso).
- **Overfull hbox**: 2 en `a4-trazabilidad.tex` (líneas 206-207 y 377-378) → **intentado corregir ensanchando columna PR y ajustando anchos**; pendiente verificación en próxima compilación.
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…» en caps. 4 y 4b; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2.
- **Corregido en este paso**: 3 diagramas replanteados (modelo-datos, sec-registro, sec-confirmacion) en 04-descripcion.tex; tabla trazabilidad ajustada.
- **Pendiente**: (1) Mover fig:juego-arquitectura antes de su referencia en 04b-juego.tex. (2) Ejecutar `revisar_umlsd.py` y corregir 11 diagramas. (3) Verificar que overfull hbox desaparece. (4) Añadir cita a `fig:sec-google` en texto. (5) Revisión visual de 11 diagramas en PDF. (6) Revisión visual final página a página. (7) Re-ejecutar `comando_prueba` hasta verde total.

## Siguiente
1. Mover `fig:juego-arquitectura` en `chapters/04b-juego.tex` antes de su primera referencia.
2. Ejecutar `revisar_umlsd.py` sobre los 11 diagramas de secuencia y corregir errores reportados.
3. Verificar overfull hbox en `a4-trazabilidad.tex` tras recompilar; si persiste, reducir fuente o usar `\sloppy` local.
4. Añadir cita faltante a `fig:sec-google` en 04-descripcion.tex (sección 4.5).
5. Revisión visual de los 11 diagramas en PDF compilado (letras ≥ 7,5 pt, sin cruces, sin palabras partidas, codos).
6. Revisión visual final del PDF página a página.
7. Re-ejecutar `comando_prueba` hasta verde total.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
