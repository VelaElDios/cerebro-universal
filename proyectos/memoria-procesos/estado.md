---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 12:00"
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
- Compila (94 páginas) y `verificar.py` OK (35 figuras, 29 tablas, 16595 palabras).
- `revisar_maquetacion.py` falla: **Regla 9** (página 88 casi vacía, 6 palabras) — **he fusionado el último párrafo de la retrospectiva Sprint 2 con el anterior en `a1-desarrollo.tex` para resolverlo**.
- He corregido: 2 frases «La figura X muestra…» en `04-descripcion.tex` reescritas como prosa; párrafo duplicado del menú de pausa eliminado en `04b-juego.tex`; nota añadida en tabla de evolución y tabla de sistemas de `04b-juego.tex` sobre combinaciones (24 en Fase 3 + 5 en Fase 7 = 29 total).
- Pendiente: confirmar que Regla 9 se resuelve tras recompilar; barrer resto de frases prohibidas en todos los capítulos; verificar imágenes no repetidas; repaso estilo global.

## Siguiente
1. Ejecutar `comando_prueba`; si falla Regla 9, localizar la página 88 en el PDF y fundir/expandir el texto suelto.
2. Barrer todos los capítulos eliminando frases «La figura X muestra…» y reescribirlas como prosa con cita integrada (Regla 13).
3. Verificar que ninguna imagen se repite (cada captura una sola vez, el resto con `\ref`).
4. Repaso final de estilo en `01`, `06` y anexos: frases cortas, sin adornos, coherencia entre capítulos.
5. Cuando todo pase en verde y el revisor haya contrastado ≥25 datos, marcar TERMINADO.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
