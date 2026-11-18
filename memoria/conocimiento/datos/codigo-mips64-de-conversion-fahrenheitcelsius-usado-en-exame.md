---
tipo: "dato"
titulo: "Código MIPS64 de conversión Fahrenheit→Celsius usado en examen AC June 2020"
temas: ["ac", "exam-code", "floating-point", "loop", "mips64", "temperature-conversion"]
claves: ["convT", "L.S", "SUB.S", "MUL.S", "S.S", "DADDUI", "BNE", "F0", "F2", "F3", "R1", "R2", "R3"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[exam-code]] · [[floating-point]] · [[loop]] · [[mips64]] · [[temperature-conversion]]

Bucle de 7 instrucciones que procesa array de 10 floats °F en R1, guarda °C en R3. Registros: F0=temp trabajo, F2=5/9 (constante), F3=32 (constante), R1=puntero origen, R2=fin array, R3=puntero destino. Patrón clásico: load FP → FP op → FP op → store FP → address update ×2 → branch. 1 resultado por iteración. Dependencias RAW: I1→I2 (F0), I2→I3 (F0), I3→I4 (F0), I5→I7 (R1), I6→I4 siguiente iteración (R3).

> Exercise 1. The following MIPS64 code converts a set of temperature values expressed in Fahrenheit degrees to Celsius degrees, according to the expression: (32 °F − 32) × 5 / 9 = 0 °C. convT: L.S F0, 0(R1) #I1 F0= temperature read in °F SUB.S F0, F0,F3 #I2 F0= T in °F – 32 MUL.S F0, F0,F2 #I3 F0= (T in °F − 32) × 5 / 9 = T in °C S.S F0, 0(R3) #I4 Stores T in °C in memory DADDUI R1, R1, #4 #I5 R1=address of the next temperature in °F DADDUI R3, R3, #4 #I6 R3=address to store the next temperature in °C BNE R1, R2, convT #I7 If R1<>R2 convert the next temperature
> — `repo:datos/temarios/AC/examenes/June2020.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]]
