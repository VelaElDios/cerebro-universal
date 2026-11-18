---
tipo: "concepto"
titulo: "Análisis de dependencias en bucle con ADD.D y S.D (misma iteración vs entre iteraciones)"
temas: ["ac", "bucles", "dependencias", "pipeline"]
claves: ["ADD.D", "S.D", "dependencia datos", "antidependencia", "dependencia salida", "loop-carried"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[pipeline]]

En el bucle dado:
- ADD.D F2, F1, F0 escribe F2.
- S.D F2, 0(R1) lee F2.
Hay una dependencia de datos verdadera (RAW) a través de F2 **en la misma iteración** (ADD.D produce, S.D consume).
No hay dependencia entre iteraciones por F2 porque F2 se sobrescribe cada iteración (dependencia de salida WAW entre iteraciones, pero la pregunta se centra en ADD.D y S.D).
La opción correcta: "There is a data dependency, through F2, in the same iteration."

> Select the correct option for the following loop and the ADD.D and S.D instructions: Loop: L.D F1, 0(R4) ADD.D F2, F1, F0 S.D F2, 0(R1) DADDUI R4, R4, #-8 BNEZ R4, Loop
> — `repo:datos/temarios/AC/examenes/June2023.pdf`

Relacionado: [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]] · [[analisis-de-dependencias-entre-instrucciones-de-punto-flotan]] · [[analisis-de-dependencias-en-bucle-mips-con-acceso-a-memoria]]
