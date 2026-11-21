---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-21 22:55"
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
- **Compilación**: OK (PDF 95 páginas, sin "Infinite glue shrinkage").
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. Longtables con `\\*` OK. Sección corta fusionada OK. Prosa sin "La figura X muestra" OK. Imágenes no repetidas OK. Subfiguras OK. Trazabilidad completa OK.
- **verificar.py**: FALLABA por 2 overfull hbox → **corregidos en este paso** reduciendo anchos de columna y añadiendo \allowbreak en las dos longtables problemáticas (RJ en 04-descripcion y logros en 04b-juego).
- **revisar_maquetacion.py**: no ejecutado (fallo previo de verificar.py).
- **revisar_umlsd.py**: no ejecutado.
- **Revisión visual PDF**: pendiente (diagramas incumplen reglas 16-18).
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2. Trazabilidad 82 tareas completa.
- **Correcciones aplicadas**: 2 longtables ajustadas (anchos reducidos + \allowbreak en rutas largas).
- **Pendiente**: Ejecutar `comando_prueba` para confirmar corrección; rehacer diagramas para reglas 16-18; pasar toda la suite de pruebas.

## Siguiente
1. Ejecutar `comando_prueba` y confirmar que `verificar.py` pasa.
2. Ejecutar `revisar_maquetacion.py` y `revisar_umlsd.py`.
3. Rehacer diagramas problemáticos (fig:capas, fig:modelo-datos, fig:juego-arquitectura, fig:pipeline, fig:burndown-s1, fig:burndown-s2, y los 7 sequencediagram) para que quepan a tamaño real SIN escalar.
4. Revisión visual final del PDF página a página.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
