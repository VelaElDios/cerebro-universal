---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-16 16:06"
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
- Regla 10: 8 imágenes repetidas en varios capítulos (se corrige en este paso con CAMBIAR para a2-material.tex y 04-descripcion.tex; queda a1-desarrollo.tex).
- Regla 8: 5 páginas con una sola imagen (páginas 42, 43, 44, 48, 96).
- Regla 9: página 102 casi vacía (8 palabras).
- Error en a1-desarrollo.tex: figura `fig:donetonic-s2-tablero` usa imagen errónea (01-tablero-sprint en vez de 04-tablero-sprint2).

## Siguiente
1. Terminar Paso 2: corregir `a1-desarrollo.tex` (imagen errónea y duplicados restantes).
2. Paso 3: reescribir «La aplicación» en `04-descripcion.tex` como prosa con `subfigure`.
3. Paso 4: reescribir manual del juego en `04b-juego.tex` con `subfigure`.
4. Paso 5: repasar capítulos y anexos (secciones cortas, párrafos repetidos, estilo).
5. Paso 6: corregir maquetación (Reglas 8 y 9) y ejecutar `comando_prueba` hasta verde.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
