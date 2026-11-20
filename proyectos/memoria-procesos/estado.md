---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-21 00:45"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco.
- Tablas `p{}` + `\addlinespace`; capturas máx. `height=0.42\textheight` (si quedan solas, bajar a 0.15–0.20 o agrupar en `subfigure` con `adjustbox`); diagramas grandes con `adjustbox`/`max totalheight`.
- Cada imagen una sola vez; en el resto `\ref`. Prosa de TFG: nada de «La figura X muestra…» suelto.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1, pero el burndown de la entrega cuenta 16; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7).

## Estado
- **Compilación**: OK (PDF 91 páginas, sin "Infinite glue shrinkage").
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. Longtables con `\\*` OK. Sección corta fusionada OK. Prosa sin "La figura X muestra" OK. Juego y Sprint 2 descritos; ningún capítulo dice que el Hito 4 esté pendiente.
- **verificar.py**: OK (35 figuras, 29 tablas, 17045 palabras, todas las cifras >20 en fuentes, sin huecos, referencias correctas).
- **revisar_maquetacion.py**: OK (fig:modelo-datos corregido, fig:sec-login corregido, resto de diagramas OK).
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2. Trazabilidad 82 tareas completa.
- **Correcciones aplicadas**: Diagrama `fig:modelo-datos` corregido (cajas separadas, etiquetas en huecos, texto legible). Diagrama `fig:sec-login` corregido (flechas sueltas eliminadas, respuestas fuera de bloques alt).
- **Pendiente**: Actualizar rutas `docs/` antiguas en 3 archivos (`a3-uso-ia.tex`, `a4-trazabilidad.tex`, `05-evaluacion.tex`).

## Siguiente
1. Aplicar cambios de rutas en `a3-uso-ia.tex` y `a4-trazabilidad.tex` (hecho en este paso).
2. Ejecutar `comando_prueba` para confirmar que compila y tests pasan.
3. Actualizar rutas en `05-evaluacion.tex`.
4. Ejecutar `revisar_umlsd.py` sobre los 7 diagramas de secuencia.
5. Revisión final PDF página a página.
6. Marcar TERMINADO solo si todo pasa.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
