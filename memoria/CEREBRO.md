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
4. **Máquinas:** `memoria/mapas/grafo.json` tiene todas las notas (nodos) y sus relaciones (aristas).

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

## Ahora mismo

415 nodos y 1486 relaciones: 3 📁 proyecto, 187 🔵 tema, 32 ⚠️ leccion, 41 💡 concepto, 69 🧪 receta, 29 ⚖️ decision, 44 📊 dato, 10 📚 fuente · actualizado 2026-11-16 19:43

## Temas principales

[[grada-colchonera]] (131) · [[saas]] (105) · [[latex]] (68) · [[scrum]] (49) · [[donetonic]] (44) · [[sprint]] (34) · [[tfg]] (29) · [[memoria]] (27) · [[cerebro]] (12) · [[sus]] (11) · [[usabilidad]] (11) · [[procesos]] (11) · [[oauth]] (11) · [[lua]] (10) · [[auth]] (10) · [[git]] (10) · [[tikz]] (9) · [[correo]] (8) · [[bibliografia]] (7) · [[figuras]] (7) · [[github-flow]] (7) · [[verificacion]] (6) · [[arquitectura]] (6) · [[backend]] (6) · [[juego]] (6) · [[trazabilidad]] (6) · [[decision]] (6) · [[pgfplots]] (5) · [[general]] (5) · [[metricas]] (5)
