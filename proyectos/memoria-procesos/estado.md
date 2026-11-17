---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 01:36"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de la asignatura Procesos de Ingeniería del Software (curso 2026-2027) con la plantilla oficial del TFG de la ESIIAB-UCLM. Cuenta el proyecto *La Grada Colchonera* entero: el Sprint 1 (la base SaaS, P1–P19 y T1–T32) y el Sprint 2 (el juego, P20–P48 y T33–T82). La única verdad son las fuentes: el repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- Se compila con LuaLaTeX; el test es `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en reglas-tfg).
- Solo la portada oficial (`elements/portada.tex`). Títulos en negro y negrita. Sin páginas en blanco.
- Tablas con columnas `p{}` y `\addlinespace` entre filas. Capturas a `height=0.42\textheight` como mucho, agrupadas con `subfigure`.
- Cada imagen, una sola vez; en el resto, `\ref` a la figura canónica.
- Archivos largos: se tocan con CAMBIAR, nunca reescritos enteros.
- Cada cifra sale de las fuentes, copiada tal cual (19 PBIs en el Sprint 1, pero el burndown de la entrega cuenta 16).

## Estado
Versión 4 de la spec (16/11/2026): la memoria compila y `verificar.py` pasa en estructura, pero `revisar_maquetacion.py` falla por:
- Regla 9: página 88 casi vacía (6 palabras) — **EN CORRECCIÓN** (fusionado párrafo final de `a1-desarrollo.tex` y sección «Capturas…» integrada en «Enlaces del proyecto» en `a2-material.tex`).
- Regla 12: frases «La figura X muestra…» eliminadas en 04-descripcion.tex, 04b-juego.tex, 03-propuesta.tex y 05-evaluacion.tex.
- Regla 10: duplicado tablero Sprint 1 eliminado del anexo, referencia a canónica.
- Error «Float too large» corregido reduciendo capturas a `0.42\textheight` y añadiendo `max totalheight` a diagramas TikZ.

## Siguiente
1. Ejecutar `comando_prueba` hasta que `verificar.py` y `revisar_maquetacion.py` pasen en verde.
2. Si persiste alguna página casi vacía o con una sola imagen, ajustar agrupando capturas o fusionando secciones.
3. Repaso final de estilo en capítulos 01, 06 y anexos: eliminar adornos, frases cortas, coherencia.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
