---
tipo: "concepto"
titulo: "Qué resuelve el renombrado de registros (register renaming)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["register renaming", "dependencias de nombre", "WAR", "WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

El renombrado de registros resuelve las dependencias de nombre (name dependencies), que son las antidependencias (WAR) y dependencias de salida (WAW). No resuelve dependencias de control ni fallos de caché. Permite que instrucciones que usan el mismo registro arquitectónico pero son independientes se ejecuten en paralelo asignándoles registros físicos distintos.

> What problem does "register renaming" solve? a) Control dependencies b) Cache misses c) Name dependencies d) All are correct
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
