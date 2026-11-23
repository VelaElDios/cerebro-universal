---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-23 07:45"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = compilar + `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco; hidelinks.
- Tablas `p{}` (redefinido en include/extra.tex) + `\small` en longtable; capturas máx. `height=0.42\textheight`, móviles `width=0.35\textwidth`; diagramas grandes con `adjustbox`.
- Cada imagen una sola vez; en el resto `\ref`. **Cada `\label`, incluidas las subfiguras de `\subcaption`, debe citarse con `\ref` en el texto** (verificar.py lo exige).
- Prosa de TFG: nada de «La figura X muestra…» suelto; las capturas se integran en párrafos y se agrupan con `subfigure`.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1 pero burndown de entrega cuenta 16; 276 pruebas al cierre del Sprint 2, 322 tras Fase 7; 23 endpoints; 5 migraciones).

## Estado
- **Compilación**: OK (98 páginas, LuaLaTeX). `revisar_maquetacion.py`: ✅ reglas cumplidas; 13 diagramas medidos en PDF sin fallos; 9 diagramas con aviso 404 de Gemini (no bloquean).
- **verificar.py**: ✅ pasa (35 figuras, 29 tablas, 18029 palabras). Subfiguras de prueba técnica ya citadas.
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…»; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación de la recta del Sprint 2; duplicado de lecciones Sprint 2 eliminado de la retrospectiva Sprint 1.
- **Pendiente**: validación `revisar_umlsd.py` + visual de 9 diagramas (fig:modelo-datos, fig:sec-registro, fig:sec-confirmacion, fig:sec-google, fig:sec-partida, fig:sec-contratar, fig:pipeline, fig:burndown-s1, fig:burndown-s2); fusión de secciones cortas y quitar repeticiones entre capítulos; revisión visual página a página del PDF.

## Siguiente
1. Reejecutar `comando_prueba` y confirmar verde.
2. Validar los 9 diagramas pendientes (umlsd + revisión a ojo; replantear los que fallen).
3. Fusionar secciones cortas y quitar repeticiones entre capítulos.
4. Revisión visual final del PDF página a página y contrastar ≥25 datos con las fuentes en COMPROBACIONES.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
