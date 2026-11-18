---
tipo: "dato"
titulo: "Código de 10 instrucciones del Exercise 3 AC June 2019"
temas: ["ac", "pipeline", "superscalar", "vliw"]
claves: ["L.D F1", "L.D F2", "SUB.D F7", "MUL.D F3", "L.D F4", "ADD.D F1", "LSH R12", "SUB.D F2", "ADD.D F4", "ADD.D F20"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]] · [[vliw]]

Lista exacta de instrucciones en orden de programa:
1. L.D   F1, 0(R1)        ; carga FP, MEM=2
2. L.D   F2, 0(R2)        ; carga FP, MEM=2
3. SUB.D F7, F1, F2       ; FP sub, EX=1, RAW con 1 y 2
4. MUL.D F3, F8, F4       ; FP mul, EX=2, RAW con F4 (inicial)
5. L.D   F4, 0(R10)       ; carga FP, MEM=2, escribe F4 (WAW con 4, WAR con 6)
6. ADD.D F1, F3, F5       ; FP add, EX=1, RAW con 4 (F3), escribe F1 (WAW con 1, WAR con 3)
7. LSH   R12, R13, R14    ; entero shift, EX=1, registros enteros (independiente)
8. SUB.D F2, F2, F7       ; FP sub, EX=1, RAW con 2 (F2) y 3 (F7), escribe F2 (WAW con 2)
9. ADD.D F4, F14, F6      ; FP add, EX=1, escribe F4 (WAW con 5)
10. ADD.D F20, F10, F6    ; FP add, EX=1, independiente (F20 nuevo)

Dependencias RAW clave:
- 3 necesita 1 (F1) y 2 (F2)
- 4 necesita F4 inicial (antes de 5)
- 6 necesita 4 (F3)
- 8 necesita 2 (F2) y 3 (F7)
- 5,6,8,9 escriben registros que se leen antes → WAR/WAW sin renombrado.

> L.D   F1, 0(R1) L.D   F2, 0(R2) SUB.D F7, F1, F2 MUL.D F3, F8, F4 L.D   F4, 0(R10) ADD.D F1, F3, F5 LSH   R12, R13, R14 SUB.D F2, F2, F7 ADD.D F4, F14, F6 ADD.D F20, F10, F6
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs]] · [[secuencia-de-instrucciones-fp-del-examen-para-tomasulo-10-in]] · [[codigo-y-parametros-superescalar-examen-ac-junio-2013-p3]]
