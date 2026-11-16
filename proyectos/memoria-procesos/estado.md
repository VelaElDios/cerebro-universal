---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-16 12:21"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de la asignatura Procesos de Ingeniería del Software (curso 2026-2027) con la plantilla oficial del TFG de la ESIIAB-UCLM. Cuenta el proyecto *La Grada Colchonera* entero: el Sprint 1 (la base SaaS, P1–P19 y T1–T32) y el Sprint 2 (el juego, P20–P48 y T33–T82). La única verdad son las fuentes: el repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- Se compila con LuaLaTeX; el test es `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en [[reglas-tfg]]).
- Solo la portada oficial (`elements/portada.tex`). Títulos en negro y negrita. Sin páginas en blanco.
- Tablas con columnas `p{}` y `\addlinespace` entre filas. Capturas a `height=0.42\textheight` como mucho, agrupadas con `subfigure`.
- Cada imagen, una sola vez; en el resto, `\ref`.
- Archivos largos: se tocan con CAMBIAR, nunca reescritos enteros.
- Cada cifra sale de las fuentes, copiada tal cual (19 PBIs en el Sprint 1, pero el burndown de la entrega cuenta 16).

## Estado
Versión 4 de la spec (16/11/2026): la memoria está entera (unas 128 páginas, `verificar.py` OK), pero a Javier no le parece profesional. Hay que rehacer cómo se cuenta y cómo se ve:
- quitar la segunda portada de `preambulo.tex`;
- quitar las imágenes repetidas;
- quitar las unas 45 frases sueltas «La figura X muestra…»;
- quitar las páginas con una sola imagen.

## Siguiente
Seguir el orden de trabajo de la spec (versión 4): primero `elements/preambulo.tex` y las imágenes repetidas.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
