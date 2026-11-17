---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-17 22:49"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco.
- Tablas `p{}` + `\addlinespace`; capturas máx. `height=0.42\textheight` (si quedan solas, bajar a 0.28–0.30 o agrupar en `subfigure`); diagramas grandes con `adjustbox`/`max totalheight`.
- Cada imagen una sola vez; en el resto `\ref`. Prosa de TFG: nada de «La figura X muestra…» suelta.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1, pero el burndown de la entrega cuenta 16; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7).

## Estado
- Paso 1 completado: `elements/preambulo.tex` ya cumplía regla 1 (sin segunda portada).
- Paso 2 (imágenes duplicadas y referencias): **EN PROGRESO** - Correcciones aplicadas en este veredicto para:
  1. Mover figura `fig:donetonic-graficas-s1` a `03-propuesta.tex` y referenciar desde allí (hecho por constructor).
  2. Reducir participantes en diagrama `fig:sec-registro` de 8 a 6 (agrupando Frontend y Confirmación+correo).
  3. Reducir altura de figura combinada admin-estados+privacidad a 0.28\textheight y añadir texto.
  4. Fusionar párrafo final en `a1-desarrollo.tex` con citas a `fig:donetonic-pbi-detalle` y `fig:donetonic-s2-tareas`.
- Pendiente: ejecutar `comando_prueba` para confirmar que pasan todas las comprobaciones.

## Siguiente
Ejecutar `comando_prueba` tras los cambios propuestos. Si pasa, avanzar a paso 3: reescribir sección «La aplicación» (04-descripcion.tex) como prosa integrada con subfiguras, eliminando frases sueltas «La figura X muestra…». Luego paso 4: hacer lo mismo con el manual del juego en 04b-juego.tex.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
