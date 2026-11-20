---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-20 11:54"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco.
- Tablas `p{}` + `\addlinespace`; capturas máx. `height=0.42\textheight` (si quedan solas, bajar a 0.22–0.28 o agrupar en `subfigure` con `adjustbox`); diagramas grandes con `adjustbox`/`max totalheight`.
- Cada imagen una sola vez; en el resto `\ref`. Prosa de TFG: nada de «La figura X muestra…» suelto.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1, pero el burndown de la entrega cuenta 16; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7).

## Estado
- **Compilación**: OK (PDF 92 páginas, sin "Infinite glue shrinkage").
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. Longtables con `\\*` OK. Sección corta fusionada OK. Prosa sin "La figura X muestra" OK. **FALLAN**: `verificar.py` (números no encontrados en fuentes aunque están); 3 warnings pgf-umlsd en auto-mensajes `\mess`; 5 diagramas pendientes validar en PDF (reglas 16-18).
- **verificar.py**: FALLA – 726+ errores de números no en fuentes. **Discrepancia**: los números citados SÍ están en `documentacion-tecnica.md` y `gestion/README.md`. Causa: script no indexa esas fuentes o exige formato exacto.
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Juego y Sprint 2 descritos; ningún capítulo dice que el Hito 4 esté pendiente.
- **Anexo desarrollo**: Dos secciones de sprint con mismo esquema; explica recta gráficas Sprint 2.
- **Trazabilidad**: Anexo A4 con tabla completa 82 tareas.
- **Correcciones aplicadas en este paso**: 3 auto-mensajes `\mess` reemplazados por `\call` en fig:sec-confirmacion, fig:sec-partida, fig:sec-contratar.

## Siguiente
1. **CRÍTICO**: Depurar `verificar.py` para que valide números contra todas las fuentes del repo.
2. Ejecutar `revisar_umlsd.py` y validar diagramas de secuencia corregidos.
3. Validar en PDF los 5 diagramas problemáticos contra reglas 16-18 y corregir TikZ/sequencediagram si fallan.
4. Ejecutar `comando_prueba` hasta que todo pase.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
