---
tipo: "dato"
titulo: "Código de instrucciones para Ejercicio 2 (Tomasulo especulativo) y Ejercicio 3 (Superscalar)"
temas: ["ac", "pipeline", "superscalar", "tomasulo"]
claves: ["MUL.D", "SUB.D", "L.D", "DIV.D", "ADD.D", "LW", "DADD", "DSUB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]] · [[tomasulo]]

Listado exacto de instrucciones para copiar/pegar en simulador o tabla:
**Ejercicio 2 (8 instrucciones FP/load):**
1. MUL.D F4, F6, F12
2. SUB.D F6, F4, F10
3. L.D   F4, 10(R2)
4. DIV.D F0, F14, F16
5. SUB.D F12, F14, F0
6. ADD.D F20, F28, F24
7. L.D   F0, 10(R2)
8. MUL.D F18, F28, F24

**Ejercicio 3 (7 instrucciones enteras):**
I1: LW      R1, 0(R2)
I2: DADD R4, R1, R3
I3: DSUB R6, R7, R8
I4: LW      R3, 0(R9)
I5: DSUB R10, R10, R12
I6: DADD R8, R8, R1
I7: DSUB R3, R3, R1

> MUL.D F4,F6,F12 SUB.D F6,F4,F10 L.D   F4,10(R2) DIV.D F0,F14,F16 SUB.D F12,F14,F0 ADD.D F20,F28,F24 L.D   F0,10(R2) MUL.D F18,F28,F24
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[parametros-de-simulacion-tomasulo-especulativo-para-mips64-e]] · [[configuracion-superscalar-4-issue-para-diagramas-de-pipeline]] · [[secuencia-de-10-instrucciones-mips64-fp-para-ejercicio-3-tom]] · [[secuencia-de-instrucciones-para-simulacion-tomasulo-examen-e]]
