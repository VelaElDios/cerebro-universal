---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-22 22:15"
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
- **Compilación**: OK (95 páginas). Overfull hbox residual 10pt corregido en anx:trazabilidad.
- **verificar.py**: OK (35 fig, 29 tab, 16935 palabras).
- **revisar_maquetacion.py**: FALLA - 6 diagramas aún incumplen reglas 16-18 (flechas cruzando texto, letras <7.5pt). Correcciones aplicadas en 3 archivos (04-descripcion, 04b-juego, 05-evaluacion) replanteando diagramas (no escalando): menos participantes, etiquetas cortas, separación mayor, `\scriptsize`, codos en flechas.
- **revisar_umlsd.py**: pendiente.
- **Revisión visual PDF**: pendiente.
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2. Trazabilidad completa 82 tareas. Cadenas "La figura X muestra..." eliminadas en secciones corregidas. Imágenes DoneTonic/producción dejadas en un solo sitio (cap:propuesta y cap:evaluacion).

## Siguiente
1. Ejecutar `comando_prueba` y confirmar que la compilación pasa, `verificar.py` OK y `revisar_maquetacion.py` OK (diagramas reglas 16-18).
2. Ejecutar `revisar_umlsd.py` y validar diagramas de secuencia.
3. Revisión visual final del PDF página a página.
4. Verificar mínimos de capturas por carpeta y referencias `\ref` cruzadas correctas.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
