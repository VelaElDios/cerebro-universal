---
tipo: "concepto"
titulo: "Bucle vectorial de referencia para desenrollado y planificación (examen AC June 2018)"
temas: ["ac", "loop-unrolling", "pipeline"]
claves: ["L.D", "MUL.D", "ADD.D", "S.D", "DADDUI", "SLTI", "BEQZ", "vector loop"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[pipeline]]

El bucle original recorre dos vectores A y B (índices en R1 y R2, decrementados en 8 bytes = double precision). Cada iteración: carga A(i) en F2, multiplica por constante en F0 → F4, carga B(i) en F6, suma F4+F6 → F6, almacena F6 en B(i), actualiza punteros y comprueba fin. Dependencias: L.D→MUL.D (F2), MUL.D→ADD.D (F4), L.D→ADD.D (F6), ADD.D→S.D (F6), DADDUI→SLTI (R1), SLTI→BEQZ (R4). El salto BEQZ vuelve al inicio si R4=0 (no se ha alcanzado 'end').

> Loop:     L.D    F2, 0(R1)                    ; loads A(i)                 MUL.D F4, F2, F0                    ; constant * A(i)                 L.D    F6, 0(R2)                    ; loads B(i)                 ADD.D F6, F4, F6                    ; constant * A(i) + B(i)                 S.D    F6, 0(R2)                    ; stores B(i)                 DADDUI R1, R1, #-8                  ; decrements the index for A                 DADDUI R2, R2, #-8                  ; decrements the index for B                 SLTI   R4, R1, end                  ; checks if the end of the vector has been reached                 BEQZ   R4, Loop                     ; jumps if R4 = 0
> — `repo:datos/temarios/AC/examenes/June2018.pdf`
