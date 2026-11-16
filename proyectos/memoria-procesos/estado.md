---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-16 18:57"
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
- Regla 10: 1 imagen repetida (`01-tablero-sprint.png` en chapters/03-propuesta.tex y chapters/a1-desarrollo.tex) — **en corrección con el CAMBIAR de arriba**.
- Regla 8: 5 páginas con una sola imagen (páginas 42, 43, 44, 48, 95) — para Paso 6.
- Regla 9: página 101 casi vacía (6 palabras) — para Paso 6.

## Siguiente
1. Aplicar el CAMBIAR en `a1-desarrollo.tex` para eliminar el duplicado del tablero del Sprint 1 y referenciar la figura canónica del capítulo 3.
2. Paso 3: Reescribir la sección «La aplicación: manual de usuario (SaaS)» en `chapters/04-descripcion.tex` como prosa explicativa con `subfigure` (dos por fila), eliminando las frases sueltas «La figura X muestra…».
3. Paso 4: Lo mismo en `chapters/04b-juego.tex` para el manual del juego.
4. Paso 5: Repasar capítulos 01, 03, 05, 06 y anexos: fusionar secciones de 1–2 líneas, eliminar párrafos repetidos entre capítulos, mejorar estilo (sin adornos, frases cortas, explicar el porqué).
5. Paso 6: Corregir páginas con una sola imagen (Regla 8) y página casi vacía (Regla 9).
6. Ejecutar `comando_prueba` hasta que `verificar.py` y `revisar_maquetacion.py` pasen en verde.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
