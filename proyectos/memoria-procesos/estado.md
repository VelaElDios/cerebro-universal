---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-19 17:04"
---

# memoria-procesos

Temas: [[latex]] · [[memoria]] · [[tikz]] · [[pgfplots]]

## Qué es
Memoria de PIS (curso 2026-2027) con la plantilla oficial TFG ESIIAB-UCLM. Proyecto *La Grada Colchonera*: Sprint 1 (base SaaS, P1–P19, T1–T32) y Sprint 2 (juego survivor, P20–P48, T33–T82). La única verdad son las fuentes del repo `la-grada-colchonera-saas` y `fuentes/`.

## Decisiones y convenciones
- LuaLaTeX; prueba = `verificar.py` + `revisar_maquetacion.py` (reglas de Javier en `memoria/reglas-tfg.md`).
- Una sola portada (`elements/portada.tex`); títulos negros negrita; sin páginas en blanco.
- Tablas `p{}` + `\addlinespace`; capturas máx. `height=0.42\textheight` (si quedan solas, bajar a 0.22–0.28 o agrupar en `subfigure` con `adjustbox`); diagramas grandes con `adjustbox`/`max totalheight`.
- Cada imagen una sola vez; en el resto `\ref`. Prosa de TFG: nada de «La figura X muestra…» suelta.
- Cada cifra sale de las fuentes tal cual (19 PBIs Sprint 1, pero el burndown de la entrega cuenta 16; 276 pruebas en main al cierre Sprint 2, 322 tras Fase 7).

## Estado
- **Compilación**: OK (PDF 92 páginas, sin "Infinite glue shrinkage").
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. **FALLAN**: 5 diagramas con cruces (reglas 16-18), imágenes DoneTonic duplicadas (regla 10), prosa manual capturas (regla 13), secciones cortas (regla 9), pipeline duplicado (regla 14), longtables sin `\\*` (regla 7), imágenes altas sin adjustbox (regla 8).
- **verificar.py**: FALLA - números no en fuentes (32, 23, 48, 50, 33, 82, etc.).
- **Contenido**: Todos los capítulos y anexos escritos con datos contrastados. Juego y Sprint 2 descritos; ningún capítulo dice que Hito 4 esté pendiente.
- **Anexo desarrollo**: Dos secciones sprint con mismo esquema; explica recta gráficas Sprint 2.
- **Trazabilidad**: Anexo A4 con tabla completa 82 tareas.

## Siguiente
1. Corregir los 5 diagramas en chapters/04-descripcion.tex (fig:capas, fig:modelo-datos, fig:sec-login, fig:sec-google, fig:sec-baja) separando nodos, usando codos y añadiendo espacio vertical.
2. Reemplazar números no verificados en chapters/01-introduccion.tex y chapters/03-propuesta.tex con valores de las fuentes.
3. Eliminar duplicados DoneTonic y usar \ref.
4. Reescribir prosa manuales Cap 4 y 4b con subfigures.
5. Fundir secciones cortas y unificar pipeline.
6. Añadir \\* en longtables y adjustbox en imágenes altas.
7. Solicitar fuentes faltantes para verificación completa.
8. Verificar que comando_prueba pasa todo.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
