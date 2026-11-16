---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-16 19:43"
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
Versión 4 de la spec (16/11/2026): la memoria compila y `verificar.py` pasa, pero `revisar_maquetacion.py` falla por:
- Regla 8: 4 páginas con una sola imagen (páginas 42, 43, 44, 48) — **en corrección: Paso 3 reescribe manuales con subfigure (hecho parcial en 04-descripcion.tex), Paso 4 hará lo mismo en 04b-juego.tex**.
- Regla 9: página 100 casi vacía (8 palabras) — para Paso 6.
- Regla 10: **resuelto** (duplicado tablero Sprint 1 eliminado del anexo, referencia a canónica).
- Regla 12: **en corrección** (frases «La figura X muestra…» eliminadas en 04-descripcion.tex; queda 04b-juego.tex).

## Siguiente
1. Paso 4: reescribir el manual del juego en `chapters/04b-juego.tex` como prosa con `subfigure` (dos por fila, `height=0.42\textheight`), eliminando frases sueltas.
2. Paso 5: repasar capítulos 01, 03, 05, 06 y anexos: fusionar secciones cortas, eliminar repeticiones, mejorar estilo.
3. Paso 6: corregir páginas sueltas (Regla 8) y página casi vacía (Regla 9).
4. Ejecutar `comando_prueba` hasta que `verificar.py` y `revisar_maquetacion.py` pasen en verde.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
