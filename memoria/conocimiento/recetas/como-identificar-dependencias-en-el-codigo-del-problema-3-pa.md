---
tipo: "receta"
titulo: "Cómo identificar dependencias en el código del Problema 3 para planificación"
temas: ["ac", "dependencias", "hazards", "pipeline", "planificacion-instrucciones"]
claves: ["RAW", "WAR", "WAW", "R3", "R4", "R6", "R8", "R9", "R11", "R13", "dependencias registros"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[hazards]] · [[pipeline]] · [[planificacion-instrucciones]]

Dependencias RAW (verdaderas): 1→4 (R3), 2→5 (R4), 4→5 (R4), 1→7 (R3), 4→8 (R11), 7→8 (R8). Dependencias WAR (anti): 4→2 (R4), 5→4 (R4), 8→4 (R11), 8→5 (R11). Dependencias WAW (salida): 2→5 (R4), 4→5 (R4), 4→8 (R11). En ejecución en orden solo importan RAW (resueltos con forwarding). En fuera de orden sin renombramiento, WAR/WAW frenan emisión. Con renombramiento, WAR/WAW desaparecen.

> LW R3, 0(R1); LW R4, 0(R2); SUB R6, R7, R8; ADD R4, R3, R11; LW R11, 0(R4); SUB R9, R9, R13; ADD R8, R8, R3; SUB R11, R11, R3
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
