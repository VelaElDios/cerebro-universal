---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 05:17"
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
- Compila (95 páginas) y `verificar.py` OK (37 figuras, 29 tablas, 16473 palabras).
- `revisar_maquetacion.py` falla: Regla 8 (página 43, solo una imagen, 22 palabras) y Regla 9 (página 89, casi vacía, 8 palabras).
- El constructor corrigió la cita faltante de `fig:hito4-admin-estados-privacidad` y reescribió 3 frases prohibidas en `04b-juego.tex` (pendiente verificación en código).
- He reducido a `0.30\textheight` cuatro figuras sueltas en `04-descripcion.tex` (app-entrar, app-sin-permiso, app-404, dt-pbi-detalle) para que no queden solas en página.
- He acortado el párrafo final de `a1-desarrollo.tex` para evitar cola suelta en página 89.
- Pendiente: verificar 3 frases prohibidas en `04b-juego.tex`; unificar 24/29 armas; repaso estilo global.

## Siguiente
1. Ejecutar `comando_prueba`; si falla Regla 8/9, localizar la página en el PDF y agrupar/reducir la figura suelta.
2. Verificar y corregir las 3 frases prohibidas en `04b-juego.tex` si no están ya.
3. Buscar en todos los capítulos más cadenas «La figura X muestra/ilustra/demuestra».
4. Decidir unificación de armas (24 vs 29) y aplicar en 04b y 05.
5. Repaso final de estilo en 01, 06 y anexos.
6. Cuando todo pase en verde y el revisor haya contrastado ≥25 datos, marcar TERMINADO.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
