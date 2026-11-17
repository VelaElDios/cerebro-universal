---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 10:28"
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
- Compila (93 páginas) y `verificar.py` OK (35 figuras, 29 tablas, 16502 palabras).
- `revisar_maquetacion.py` falla: Regla 9 (página 87 casi vacía, 8 palabras) — **he acortado el último párrafo de la retrospectiva Sprint 2 en `a1-desarrollo.tex` para intentar resolverlo**.
- He corregido: imagen duplicada en `04b-juego.tex` (eliminada figura standalone redundante), figuras sueltas en `04-descripcion.tex` (agrupadas en subfiguras), unificación de armas (29 armas, 16 pasivas, 29 combinaciones) en `04b-juego.tex` y `05-evaluacion.tex`.
- Pendiente: resolver Regla 9 definitivamente, barrer frases prohibidas en todos los capítulos, unificar dato de combinaciones (24 en Fase 3 vs 29 total), eliminar repetición del párrafo de pausa en `04b-juego.tex`, repaso estilo global.

## Siguiente
1. Ejecutar `comando_prueba`; si falla Regla 9, localizar la página 87 en el PDF y fundir el texto suelto con el anterior.
2. Barrer todos los capítulos eliminando frases «La figura X muestra…» y reescribirlas como prosa con cita integrada (Regla 13).
3. Unificar dato de combinaciones: nota en tabla de evolución de `04b-juego.tex` explicando 24 (Fase 3) + 5 (Fase 7) = 29 total.
4. Eliminar repetición del párrafo del menú de pausa en `04b-juego.tex`.
5. Repaso final de estilo en `01`, `06` y anexos.
6. Cuando todo pase en verde y el revisor haya contrastado ≥25 datos, marcar TERMINADO.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
