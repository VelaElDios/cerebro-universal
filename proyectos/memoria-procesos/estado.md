---
tipo: "proyecto"
titulo: "memoria-procesos"
temas: ["latex", "memoria", "tikz", "pgfplots"]
actualizado: "2026-11-23 00:57"
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
- **Compilación**: OK (96 páginas). Overfull hbox residual corregido en anx:trazabilidad.
- **verificar.py**: FALLA - 2 referencias sin resolver (`. ` y `)` página 31).
- **revisar_maquetacion.py**: FALLA - 6 diagramas incumplen reglas 16-18 (fig:capas 55pt ancho, fig:juego-arquitectura 68pt ancho, fig:sec-login letras 6.9pt + flechas cruzan, fig:sec-baja letras 7.5pt + flechas cruzan, fig:sec-registro y fig:sec-google pendientes).
- **revisar_umlsd.py**: pendiente.
- **Revisión visual PDF**: pendiente.
- **Contenido**: Todos los capítulos y anexos escritos con datos del spec. Anexo desarrollo con dos sprints mismo esquema y explicación recta Sprint 2. Trazabilidad completa 82 tareas. Cadenas "La figura X muestra..." eliminadas en secciones corregidas (04-descripcion, 04b-juego). Imágenes DoneTonic/producción dejadas en un solo sitio (cap:propuesta y cap:evaluacion).

## Siguiente
1. Corregir referencias rotas en 04-descripcion.tex (línea ~794).
2. Replantear 4 diagramas problemáticos restantes (fig:sec-login, fig:sec-baja, fig:sec-google, fig:pipeline) sin escalar: menos participantes, etiquetas ≤2 líneas, más separación, codos en flechas, fuente ≥`\scriptsize`.
3. Validar 5 diagramas no revisados (fig:sec-partida, fig:sec-contratar, fig:pipeline, fig:burndown-s1, fig:burndown-s2) con `revisar_umlsd.py` y ojo.
4. Ejecutar `comando_prueba` y confirmar compilación, `verificar.py` OK y `revisar_maquetacion.py` OK.
5. Revisión visual final del PDF página a página.
6. Verificar mínimos de capturas por carpeta y referencias `\ref` cruzadas correctas.

Bitácora completa: [[proyectos/memoria-procesos/bitacora|bitácora]] · Spec: [[proyectos/memoria-procesos/spec|spec]]
