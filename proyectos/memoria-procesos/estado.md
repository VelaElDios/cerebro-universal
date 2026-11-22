---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-22 21:34"
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
- **Compilación**: corregidos overfull hbox en fig:sec-registro (54pt) y 8 diagramas con flechas sobre texto / palabras partidas en chapters/04-descripcion.tex y chapters/04b-juego.tex. Pendiente ejecutar `comando_prueba`.
- **verificar.py**: pendiente (ejecutar tras esta corrección).
- **revisar_maquetacion.py**: no ejecutado (pendiente tras corregir overfull).
- **revisar_umlsd.py**: no ejecutado (pendiente).
- **Revisión visual PDF**: pendiente (diagramas incumplían reglas 16-18, ahora corregidos en 2 archivos).
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2. Trazabilidad completa 82 tareas.

## Siguiente
1. Ejecutar `comando_prueba` y confirmar que la compilación pasa, `verificar.py` OK (sin overfull hbox) y `revisar_maquetacion.py` OK.
2. Ejecutar `revisar_umlsd.py` y validar diagramas de secuencia.
3. Revisión visual final del PDF página a página.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
