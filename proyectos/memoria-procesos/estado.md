---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-20 08:10"
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
- **Compilación**: OK (PDF 91 páginas, sin "Infinite glue shrinkage") tras correcciones de longtables.
- **Reglas Javier**: Portada única OK; declaraciones, resumen, abstract OK; índices OK. **FALLAN**: 5 diagramas con cruces pendientes de validar (reglas 16-18), longtables de anexos sin `\\*` (regla 7 – corregidas 2 en este paso, pendiente verificación del resto), imágenes repetidas DoneTonic/producción (regla 10).
- **verificar.py**: FALLA – 726+ errores de números no en fuentes. **Causa raíz**: 2 fuentes principales aún no existen en el repo (`revision-entrega.md`, `hito4-configuracion.md`); las dos creadas (`documentacion-tecnica.md`, `gestion/README.md`) no contienen todas las cifras.
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Juego y Sprint 2 descritos; ningún capítulo dice que el Hito 4 esté pendiente.
- **Anexo desarrollo**: Dos secciones de sprint con mismo esquema; explica recta gráficas Sprint 2.
- **Trazabilidad**: Anexo A4 con tabla completa 82 tareas.
- **Correcciones aplicadas en este paso**: 2 longtables en `a1-desarrollo.tex` (`tab:sprint1-backlog` y `tab:prob-desarrollo`) ahora llevan `\\*`; fundida sección "Validación y gestión" en cap 4 con "Hito 4: correo y Google".

## Siguiente
1. **CRÍTICO**: Crear las 2 fuentes faltantes en el repo para que `verificar.py` pueda validar TODOS los números.
2. Reemplazar cualquier número por valores confirmados en fuentes.
3. Verificar en PDF los 5 diagramas (fig:capas, fig:modelo-datos, fig:sec-login, fig:sec-google, fig:sec-baja) para reglas 16-18.
4. Confirmar `\\*` en todas las longtables (incluidas anexos).
5. Confirmar no duplicados de imágenes (especialmente DoneTonic y producción).
6. Ejecutar `comando_prueba` hasta que todo pase.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
