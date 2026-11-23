---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-23 17:05"
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
- **Compilación**: OK (98 páginas, LuaLaTeX). `verificar.py`: ✅ (35 figuras, 29 tablas, 18391 palabras).
- **revisar_maquetacion.py**: ❌ Tres diagramas con fallos medidos (fig:sec-registro, fig:sec-confirmacion, fig:sec-google); 11 diagramas con Gemini 404 (requieren revisión visual regla 19).
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…»; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación de la recta del Sprint 2.
- **Corregido en este paso**: eliminada `\ref.` mal formada en 04-descripcion.tex; ajustados tres diagramas de secuencia (aumentado espaciado de participantes de 1.5 a 2) para intentar mejorar tamaño de fuente.
- **Pendiente**: (1) Replantear 3 diagramas de secuencia con fallos medidos. (2) Ejecutar `revisar_umlsd.py` y corregir 11 diagramas pendientes. (3) Revisión visual de esos 11 diagramas en PDF (reglas 16-19). (4) Revisión visual final página a página (regla 15).

## Siguiente
1. Replantear fig:sec-registro, fig:sec-confirmacion, fig:sec-google en chapters/04-descripcion.tex (menos participantes, etiquetas limpias, codos, text width).
2. Ejecutar `revisar_umlsd.py` sobre los 11 diagramas pendientes y corregir errores.
3. Revisión visual de los 11 diagramas en PDF (letras ≥ 7.5 pt, sin cruces, sin palabras partidas, codos).
4. Revisión visual final del PDF página a página.
5. Re-ejecutar `comando_prueba` hasta verde total.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
