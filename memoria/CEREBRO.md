---
tipo: "guia"
titulo: "CEREBRO: cómo usar esta memoria"
---

# CEREBRO — léeme primero (para IAs)

Este vault es la **memoria compartida** de todas las IAs que trabajan para Javier: da igual qué modelo o qué
empresa esté conectada, aquí está lo que ya se sabe, cómo se hacen las cosas y por qué. Sirve también para
buscar con RAG y, en el futuro, para entrenar una IA local. (este archivo se genera solo)

## Cómo encontrar algo

1. **Por proyecto:** `proyectos/<nombre>/estado.md` es la ficha corta (qué es, decisiones, convenciones,
   estado y siguiente). La bitácora entera está al lado.
2. **Por tema:** `memoria/temas/<tema>.md` enlaza todo lo de ese tema: recetas, decisiones, conceptos,
   datos, lecciones y proyectos.
3. **Por tipo:** `memoria/conocimiento/<tipo>/` y `memoria/lecciones/` (todo listado en [[indice]]).
4. **Máquinas:** `memoria/mapas/grafo.json` tiene todas las notas (nodos) y sus relaciones (aristas), y
   `memoria/mapas/embeddings.json` sus vectores para buscar por significado.
5. **Desde un chat (Claude, ChatGPT...):** el servidor MCP `scripts/mcp_cerebro.py` deja buscar, leer y
   guardar notas. Para preguntar al cerebro sin chat: una nota en `proyectos/preguntas/`.

## Tipos de nota

| Tipo | Carpeta | Para qué |
|---|---|---|
| 💡 concepto | `conocimiento/conceptos/` | Qué es algo (término, pieza de la arquitectura, tema del temario) |
| 🧪 receta | `conocimiento/recetas/` | **Cómo lo hacemos** en nuestros proyectos: pasos y código que funcionó. Si existe, se hace igual |
| ⚖️ decisión | `conocimiento/decisiones/` | Qué se eligió y por qué: no se vuelve a discutir sin motivo nuevo |
| 📊 dato | `conocimiento/datos/` | Hechos concretos de un proyecto (cifras, fechas, nombres), con su fuente |
| 📚 fuente | `conocimiento/fuentes/` | Un documento aprendido (temario, documentación) y todo lo que se sacó de él |
| ⚠️ lección | `lecciones/` | Errores que ya se resolvieron: no repetirlos |

## Reglas para usarla

- `confianza: "verificado"` → la cita está comprobada literalmente en su fuente: úsalo sin volver a deducirlo.
  `"propuesto"` → probablemente bien, pero compruébalo antes de dar nada por cierto.
- Si lo que necesitas no está, **apréndelo y guárdalo** (bloque `<<<CONOCIMIENTO>>>`) con su fuente y una cita
  literal. Nunca inventes datos: lo que no está en una fuente no se escribe.
- Reglas fijas de Javier: [[reglas-tfg]] (memorias con formato de TFG).
- El jardinero (`proyectos/jardinero`) pasa cada día: comprueba citas, fusiona notas repetidas, marca
  contradicciones y enlaza lo parecido. Qué notas ayudan de verdad: [[ESTADISTICAS]].

## Ahora mismo

680 nodos y 3726 relaciones: 6 📁 proyecto, 297 🔵 tema, 43 ⚠️ leccion, 53 💡 concepto, 137 🧪 receta, 71 ⚖️ decision, 62 📊 dato, 11 📚 fuente · actualizado 2026-11-24 08:38

## Temas principales

[[latex]] (185) · [[grada-colchonera]] (132) · [[saas]] (107) · [[tfg]] (74) · [[memoria]] (73) · [[scrum]] (59) · [[donetonic]] (50) · [[sprint]] (38) · [[maquetacion]] (33) · [[tikz]] (32) · [[pgf-umlsd]] (32) · [[memoria-procesos]] (28) · [[verificacion]] (26) · [[figuras]] (26) · [[trazabilidad]] (20) · [[metricas]] (17) · [[diagramas]] (16) · [[juego]] (13) · [[fuentes]] (13) · [[lua]] (12) · [[bibliografia]] (12) · [[cerebro]] (12) · [[longtable]] (11) · [[sus]] (11) · [[usabilidad]] (11) · [[procesos]] (11) · [[sprints]] (11) · [[oauth]] (11) · [[pgfplots]] (10) · [[subcaption]] (10)
