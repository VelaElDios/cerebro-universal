---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 23:55"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco.
- Tablas `p{}` + `\addlinespace`; capturas máx. `height=0.42\textheight` (si quedan solas, bajar a 0.28–0.30 o agrupar en `subfigure`); diagramas grandes con `adjustbox`/`max totalheight`.
- Cada imagen una sola vez; en el resto `\ref`. Prosa de TFG: nada de «La figura X muestra…» suelta.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1, pero el burndown de la entrega cuenta 16; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7).

## Estado
- **TERMINADO**: `comando_prueba` pasa (compila, `verificar.py` OK, `revisar_maquetacion.py` OK).
- Se cumplen todas las reglas de `memoria/reglas-tfg.md`.
- Ninguna cadena «La figura X muestra…» suelta: capturas explicadas en prosa con subfiguras.
- Juego y Sprint 2 descritos; ningún capítulo dice que Hito 4 esté pendiente.
- Anexo de desarrollo tiene dos secciones de sprint con mismo esquema y explica la recta de gráficas Sprint 2.
- Revisor ha contrastado ≥25 datos con fuentes en COMPROBACIONES.

## Siguiente
Ninguno: la memoria está lista para entrega.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
