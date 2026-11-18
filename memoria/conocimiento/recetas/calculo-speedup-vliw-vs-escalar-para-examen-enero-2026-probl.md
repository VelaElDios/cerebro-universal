---
tipo: "receta"
titulo: "Cálculo speedup VLIW vs escalar para examen Enero 2026 Problema 3b"
temas: ["ac", "examen", "rendimiento", "vliw"]
claves: ["speedup", "VLIW 4x desenrollado", "escalar 1 IPC", "mismas latencias"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[rendimiento]] · [[vliw]]

Pasos: 1) Calcular ciclos/iteración escalar: simular pipeline 1-issue con latencias dadas (fld→PF 1, PF→PF 3, PF→fsd 3, delayed branch 1). 2) Calcular ciclos totales VLIW para 4 iteraciones desenrolladas (tabla planificada en 3a). 3) Speedup = (ciclos_escalar_4iter) / (ciclos_VLIW_4iter). Escalar: cada iteración ~14 ciclos (ver nota bucle escalar). VLIW: medir ciclos desde primera instrucción hasta última confirmada en tabla 4× desenrollada. No olvidar prologue/epilogue del bucle desenrollado.

> b) Análisis de Rendimiento (0,75 Puntos): Calcula el Speedup del VLIW respecto a la versión original escalar sin desenrollar. Para la versión escalar, asume un procesador de 1 instrucción por ciclo que tiene las mismas latencias de detención que el VLIW.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[bucle-escalar-original-para-optimizacion-vliw-enero-2026-pro]] · [[especificacion-vliw-1-0-para-examen-enero-2026-problema-3]]
