---
tipo: "receta"
titulo: "Análisis de dependencias RAW, WAR, WAW en una iteración del bucle secuencia 0,1,0,2"
temas: ["ac", "dependencias"]
claves: ["LW", "ANDI", "DADDUI", "BEQZ", "BEQ", "R1", "R2", "R3", "R4", "R5"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias]]

En una iteración: RAW (verdaderas): LW R2,0(R1) → BEQZ R2 (B1); LW R2,0(R1) → ANDI R4,R2,#1; ANDI R4,R2,#1 → BEQZ R4 (B2); DADDUI R5,R5,#1 no tiene consumidor en la iteración. BEQ R1,R3 (B3) usa R1 y R3. DADDUI R1,R1,#4 → BEQ R1,R3 (siguiente iteración). WAR (anti): BEQZ R2 lee R2 antes de que LW siguiente iteración lo escriba; ANDI lee R2 antes de LW siguiente; BEQ R1,R3 lee R1 antes de DADDUI R1 siguiente. WAW (salida): DADDUI R1,R1,#4 escribe R1; LW siguiente iteración no escribe R1. DADDUI R5,R5,#1 escribe R5; no hay otra escritura a R5 en la iteración.

> a) Indica las dependencias de datos, antidependencias y dependencias de salida que aparecen en el código (en una sola iteración).
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf`
