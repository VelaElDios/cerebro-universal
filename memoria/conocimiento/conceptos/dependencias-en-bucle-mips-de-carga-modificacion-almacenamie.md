---
tipo: "concepto"
titulo: "Dependencias en bucle MIPS de carga-modificación-almacenamiento (LW, DADD, SW, DADDUI, BNEZ)"
temas: ["ac", "dependencias", "pipeline", "riesgos"]
claves: ["RAW", "WAR", "WAW", "antidependencia", "dependencia salida", "bucle MIPS"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]] · [[riesgos]]

Análisis de una iteración (Q5): I1→I2 RAW por R1 (I2 lee R1 escrito por I1). I2→I3 RAW por R1 (I3 usa R1). I3→I4: I3 escribe memoria 0(R2), I4 escribe R2 → no hay dependencia de registros. I5→I6 RAW por R4 (I6 lee R4 escrito por I5). Entre iteraciones consecutivas (Q6): I1(it n) y I1(it n+1) ambas leen R2 → no hay dependencia. I3(it n) escribe memoria 0(R2), I1(it n+1) lee 0(R2) → RAW por memoria. I5(it n) escribe R4, I6(it n) lee R4 → RAW. I1(it n) escribe R1, I3(it n) escribe R1 → WAW por R1 (dependencia de salida). Respuestas: Q5=c (WAW entre I2 e I3 por R1), Q6=d (WAW entre I1 e I3 por R1).

> LOOP: LW R1, 0(R2) ; I1 DADD R1, R1, R3 ; I2 SW R1, 0(R2) ; I3 DADDUI R2, R2, #4 ; I4 DADDUI R4, R4, #-1 ; I5 BNEZ R4, LOOP ; I6
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[analisis-de-dependencias-raw-war-waw-en-una-iteracion-del-bu]] · [[dependencias-en-bucle-mips64-de-encriptacion-asciiz-problema]] · [[identificacion-de-antidependencia-war-entre-store-e-incremen]]
