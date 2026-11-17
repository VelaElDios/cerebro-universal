---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 15:48"
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
- Compila (94 páginas) y `verificar.py` OK (35 figuras, 29 tablas, 16819 palabras).
- `revisar_maquetacion.py` fallaba en **Regla 9** (página 88 casi vacía) — **he fusionado el párrafo final del anexo de trazabilidad con el introductorio para resolverlo**.
- He corregido: 4 frases «La figura X muestra…» en `04b-juego.tex` reescritas como prosa con cita integrada; párrafo duplicado del menú de pausa eliminado en `04b-juego.tex`; nota añadida en tablas de `04b-juego.tex` sobre combinaciones (24 en Fase 3 + 5 en Fase 7 = 29 total).
- Pendiente: confirmar que Regla 9 y 13 se resuelven tras recompilar; barrer resto de frases prohibidas en todos los capítulos; verificar imágenes no repetidas; repaso estilo global.

## Siguiente
1. Ejecutar `comando_prueba`; si falla Regla 9 o 13, localizar el problema en el PDF y corregir.
2. Barrer todos los capítulos eliminando frases «La figura X muestra…» y reescribirlas como prosa con cita integrada.
3. Verificar que ninguna imagen se repite (cada captura una sola vez, el resto con `\ref`).
4. Repaso final de estilo en `01`, `06` y anexos: frases cortas, sin adornos, coherencia entre capítulos.
5. Cuando todo pase en verde y el revisor haya contrastado ≥25 datos, marcar TERMINADO.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
