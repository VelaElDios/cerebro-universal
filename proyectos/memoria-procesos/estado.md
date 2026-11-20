---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-20 01:28"
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
- **Compilación**: OK (PDF 92 páginas, sin "Infinite glue shrinkage") tras correcciones de longtables.
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. **FALLAN**: 5 diagramas con cruces pendientes de validar (reglas 16-18), secciones cortas en caps 4 y 5 (regla 9), longtables de anexos sin `\\*` (regla 7 – constructor dice haber corregido 13, pendiente verificación).
- **verificar.py**: FALLA – 16+ errores de números no en fuentes (32, 23, 48, 50, 33, 82, etc. en caps 1 y 3). **Causa raíz**: 4 fuentes principales no proporcionadas (`documentacion-tecnica.md`, `gestion/README.md`, `revision-entrega.md`, `hito4-configuracion.md`).
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Juego y Sprint 2 descritos; ningún capítulo dice que el Hito 4 esté pendiente.
- **Anexo desarrollo**: Dos secciones de sprint con mismo esquema; explica recta gráficas Sprint 2.
- **Trazabilidad**: Anexo A4 con tabla completa 82 tareas.
- **Correcciones aplicadas**: 12 longtables de caps 4, 4b, 5 llevan `\\*` antes de `\bottomrule`; fundidas 3 subsecciones cortas en cap 4 y 1 en cap 5.

## Siguiente
1. **CRÍTICO**: Obtener las 4 fuentes faltantes para poder verificar TODOS los números.
2. Reemplazar cualquier número por valores confirmados en fuentes.
3. Verificar en PDF los 5 diagramas (fig:capas, fig:modelo-datos, fig:sec-login, fig:sec-google, fig:sec-baja) para reglas 16-18.
4. Confirmar `\\*` en todas las longtables (incluidas anexos).
5. Confirmar no duplicados de imágenes (especialmente DoneTonic y producción).
6. Ejecutar `comando_prueba` hasta que todo pase.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
