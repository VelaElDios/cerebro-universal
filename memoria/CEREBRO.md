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

523 nodos y 2459 relaciones: 6 📁 proyecto, 242 🔵 tema, 34 ⚠️ leccion, 44 💡 concepto, 92 🧪 receta, 43 ⚖️ decision, 51 📊 dato, 11 📚 fuente · actualizado 2026-11-19 13:13

## Temas principales

[[grada-colchonera]] (131) · [[latex]] (107) · [[saas]] (105) · [[tfg]] (54) · [[scrum]] (52) · [[memoria]] (50) · [[donetonic]] (49) · [[sprint]] (36) · [[tikz]] (16) · [[figuras]] (13) · [[trazabilidad]] (13) · [[lua]] (12) · [[cerebro]] (12) · [[verificacion]] (11) · [[sus]] (11) · [[usabilidad]] (11) · [[procesos]] (11) · [[oauth]] (11) · [[auth]] (10) · [[git]] (10) · [[bibliografia]] (9) · [[maquetacion]] (9) · [[pgf-umlsd]] (8) · [[tablas]] (8) · [[juego]] (8) · [[memoria-procesos]] (8) · [[correo]] (8) · [[metricas]] (7) · [[github-flow]] (7) · [[diagramas]] (7)
