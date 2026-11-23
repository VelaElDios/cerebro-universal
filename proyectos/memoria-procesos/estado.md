---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-23 14:48"
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
- **Compilación**: OK (98 páginas, LuaLaTeX). `revisar_maquetacion.py`: reglas formales ✅; 13 diagramas medidos en PDF; **1 fallo real en fig:burndown-s1** (flechas cruzan texto «pendientes», regla 17); 9 diagramas con aviso Gemini 404 (requieren revisión visual obligatoria por regla 19).
- **verificar.py**: ✅ pasa (35 figuras, 29 tablas, 17878 palabras).
- **Contenido**: 01, 03, 04, 04b, 05, 06 reescritos como prosa sin «La figura X muestra…»; pipeline descrito una vez (cap. 05, fig:pipeline); imágenes DoneTonic/producción en un solo sitio; Resumen/Abstract OK; trazabilidad completa P1–P48/T1–T82 en a4; anexo desarrollo con dos sprints mismo esquema y explicación de la recta del Sprint 2.
- **Corregido en este paso**: fig:burndown-s1 y fig:burndown-s2 (pgfplots) con `ylabel style`, `scale only axis` y `enlarge x limits` para evitar colisiones de etiquetas.
- **Pendiente**: (1) Confirmar que los burndown ya no fallan en revisar_maquetacion.py. (2) Ejecutar `revisar_umlsd.py` y corregir los 9 diagramas de secuencia pendientes. (3) Revisión visual de esos 9 diagramas en el PDF (reglas 16-19). (4) Revisión visual final página a página del PDF (regla 15).

## Siguiente
1. Ejecutar `comando_prueba` para validar la corrección de los burndown.
2. Ejecutar `revisar_umlsd.py` sobre los 9 diagramas de secuencia y corregir errores.
3. Revisión visual de los 9 diagramas en el PDF (letras ≥ 7,5 pt, sin cruces, sin palabras partidas, codos en flechas).
4. Revisión visual final del PDF página a página.
5. Re-ejecutar `comando_prueba` hasta verde total.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
