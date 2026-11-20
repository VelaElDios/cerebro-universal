---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-20 14:44"
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
- **Compilación**: OK (PDF 92 páginas, sin "Infinite glue shrinkage").
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. Longtables con `\\*` OK. Sección corta fusionada OK. Prosa sin "La figura X muestra" OK. **FALLA verificar.py**: 2 figuras sin `\ref` (fig:hito4-admin-estados, fig:hito4-privacidad).
- **verificar.py**: 2 errores (línea 769, figuras nuevas sin citar).
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Juego y Sprint 2 descritos; ningún capítulo dice que el Hito 4 esté pendiente.
- **Anexo desarrollo**: Dos secciones de sprint con mismo esquema; explica recta gráficas Sprint 2.
- **Trazabilidad**: Anexo A4 con tabla completa 82 tareas.
- **Correcciones aplicadas en este paso**: Preparado fix para las 2 `\ref` faltantes en `04-descripcion.tex`.

## Siguiente
1. Aplicar el CAMBIO de arriba (añadir las dos `\ref`).
2. Ejecutar `comando_prueba` para confirmar que `verificar.py` y `revisar_maquetacion.py` pasan.
3. Ejecutar `revisar_umlsd.py` y validar 7 diagramas de secuencia.
4. Validar visualmente 5 diagramas TikZ/sequencediagram problemáticos contra reglas 16-18.
5. Actualizar rutas `docs/` antiguas en 4 archivos restantes.
6. Revisión final PDF página a página.
7. Marcar TERMINADO solo si todo pasa.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
