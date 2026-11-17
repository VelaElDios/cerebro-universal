---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 16:42"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco.
- Tablas `p{}` + `\addlinespace`; capturas máx. `height=0.42\textheight` (si quedan solas, bajar a 0.30–0.32 o agrupar en `subfigure`); diagramas grandes con `adjustbox`/`max totalheight`.
- Cada imagen una sola vez; en el resto `\ref`. Prosa de TFG: nada de «La figura X muestra…» suelta.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1, pero el burndown de la entrega cuenta 16; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7).

## Estado
- Compila (93 páginas) y `verificar.py` OK (35 figuras, 29 tablas, 16798 palabras).
- `revisar_maquetacion.py` OK (reglas de maquetación cumplidas).
- Paso 1 completado: `elements/preambulo.tex` ya cumplía regla 1 (sin segunda portada).
- Pendiente: paso 2 (imágenes repetidas), paso 3 (prosa en manual de uso SaaS), paso 4 (prosa en manual del juego), paso 5 (repaso estilo global), paso 6 (barrido final hasta todo verde).

## Siguiente
Paso 2: eliminar imágenes repetidas entre `04-descripcion.tex`, `05-evaluacion.tex`, `a1-desarrollo.tex` y `a2-material.tex`. Cada captura una sola vez, el resto con `\ref`.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
