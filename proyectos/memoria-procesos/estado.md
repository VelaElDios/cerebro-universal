---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-19 11:04"
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
- **Compilación**: FALLA con "Infinite glue shrinkage" en 6 capítulos. Parches en `preambulo.tex` (raggedbottom persistente en @float, mainmatter, frontmatter, backmatter, chapter, longtable, figure, table, adjustbox, @startsection, @outputpage) y `\\*` en 2 longtables de `a1-desarrollo.tex` (pendiente en el resto). Imagen `donetonic/06-graficas-sprint2.png` envuelta en `adjustbox{max totalheight=0.42\textheight}` en `a1-desarrollo.tex`.
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. Pendiente: diagramas (Fig 3.1, 4.7), imágenes repetidas (DoneTonic), cadenas «La figura X muestra…», coherencia entre capítulos, secciones cortas.
- **Contenido**: Todos los capítulos y anexos escritos con datos contrastados (25+ comprobaciones). Juego y Sprint 2 descritos; ningún capítulo dice que Hito 4 esté pendiente.
- **Anexo desarrollo**: Dos secciones sprint con mismo esquema; explica recta gráficas Sprint 2.
- **Trazabilidad**: Anexo A4 con tabla completa 82 tareas.

## Siguiente
1. Ejecutar `comando_prueba` tras parches de compilación.
2. Si compila, añadir `\\*` antes de `\bottomrule` en longtables restantes y envolver `produccion/02-actions-verde.png` en `adjustbox`.
3. Corregir diagramas de secuencia (participantes no declarados).
4. Eliminar imágenes repetidas de DoneTonic (usar `\ref`).
5. Reescribir prosa de manuales (Cap 4 y 4b) eliminando frases sueltas de figuras.
6. Corregir diagramas TikZ y de secuencia según reglas 16-18.
7. Fundir secciones cortas y unificar descripción del pipeline.
8. Verificar que `verificar.py` y `revisar_maquetacion.py` pasan.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
