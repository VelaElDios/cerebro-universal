---
tipo: "receta"
titulo: "Análisis de dependencias y planificación de bucle MIPS64 con unidades FP segmentadas (examen Junio 2013)"
temas: ["ac", "bucles", "dependencias", "mips64", "pipeline", "punto-flotante"]
claves: ["MIPS64", "L.S", "MUL.S", "ADD.S", "S.S", "DADDUI", "BNE", "dependencias RAW", "WAR", "WAW", "renombramiento", "desenrollamiento", "CPI"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[mips64]] · [[pipeline]] · [[punto-flotante]]

Pasos para resolver el problema: 1) Identificar dependencias en una iteración: RAW: S1->S2 (F0), S1->S3 (F0), S2->S5 (F2), S3->S4 (F0), S4->S5 (F0), S5->S6 (F0). WAR: S2 lee F0 antes de que S3 lo sobrescriba (WAR en F0), S3 lee F0 antes de S4 (WAR), S4 lee F0 antes de S5 (WAR). WAW: ninguna en registros FP (F0 escrito en S1,S3,S4,S5 pero S1 carga, S3,S4,S5 sobrescriben). 2) Calcular CPI con pipeline dado: latencias FP: ADD.S 2 ciclos, MUL.S 4 ciclos. Adelantamiento, dependencias resueltas en ID, salto resuelto en ID con delayed branch, no dos WB FP mismo ciclo. 3) Renombrar registros para eliminar WAR/WAW y desenrollar mínimo para ocultar latencias y evitar paradas. 4) Calcular CPI resultante.

> El código MIPS64 que se muestra calcula y(i)=x(i)2+2* x(i)+2 , con 1<=i<=18 ... loop: L.S F0, 0(R4) #S1 MUL.S F2, F0, F0 #S2 MUL.S F0, F0, F4 #S3 ADD.S F0, F0, F4 #S4 ADD.S F0, F0, F2 #S5 S.S F0, 0(R8) #S6 DADDUI R4, R4, #4 #S7 DADDUI R8, R8, #4 #S8 BNE R4, R6, loop #S9
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[como-desenrollar-8x-y-planificar-en-superescalar-4-issue-2-i]] · [[dependencias-en-bucle-mips64-de-encriptacion-asciiz-problema]] · [[tipos-de-dependencias-en-codigo-fp-mips64-para-tomasulo-raw]]
