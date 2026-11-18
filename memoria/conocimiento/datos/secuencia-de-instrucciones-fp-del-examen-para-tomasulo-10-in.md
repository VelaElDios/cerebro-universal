---
tipo: "dato"
titulo: "Secuencia de instrucciones FP del examen para Tomasulo (10 instrucciones)"
temas: ["ac", "instruction mix", "tomasulo"]
claves: ["DIV.D", "ADD.D", "SUB.D", "S.D", "MUL.D", "L.D", "reservation stations", "FP registers"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[instruction mix]] · [[tomasulo]]

Secuencia exacta de 10 instrucciones del ejercicio 1 (parte a y b):
1. DIV.D F0, F2, F4        ; F0 = F2 / F4
2. ADD.D F2, F4, F8        ; F2 = F4 + F8  (WAW con #1 en F0? No, #1 escribe F0, #2 escribe F2. RAW: #2 lee F4,F8)
3. SUB.D F0, F4, F8        ; F0 = F4 - F8  (WAW con #1 en F0; RAW con #1? #1 escribe F0, #3 lee F4,F8 → sin RAW con #1)
4. S.D   F0, 0(R1)         ; store F0 → mem  (RAW con #1 y #3 en F0; debe esperar a que F0 esté listo)
5. MUL.D F2, F4, F0        ; F2 = F4 * F0  (WAW con #2 en F2; RAW con #1/#3 en F0, con #2 en F4)
6. DIV.D F6, F8, F0        ; F6 = F8 / F0  (RAW con #1/#3/#5 en F0)
7. L.D   F6, 0(R2)         ; load F6 ← mem  (WAW con #6 en F6; RAW con #6? #6 escribe F6, #7 escribe F6 → WAW)
8. ADD.D F0, F6, F2        ; F0 = F6 + F2  (WAW con #1/#3 en F0; RAW con #7 en F6, con #2/#5 en F2)
9. MUL.D F2, F0, F8        ; F2 = F0 * F8  (WAW con #2/#5 en F2; RAW con #8 en F0)
10. ADD.D F2, F0, F6       ; F2 = F0 + F6  (WAW con #2/#5/#9 en F2; RAW con #8/#9 en F0, con #7 en F6)

Dependencias clave (RAW verdaderas):
- #4 (S.D) espera a #1 o #3 (último escritor de F0 antes del store).
- #5 (MUL.D) espera a #1/#3 (F0) y #2 (F4).
- #6 (DIV.D) espera a #1/#3/#5 (F0).
- #8 (ADD.D) espera a #7 (F6) y #2/#5 (F2).
- #9 (MUL.D) espera a #8 (F0).
- #10 (ADD.D) espera a #8/#9 (F0) y #7 (F6).

WAW en registros FP: F0 escrito por #1, #3, #8; F2 por #2, #5, #9, #10; F6 por #6, #7. En Tomasulo sin renombrado arquitectónico, las estaciones de reserva renombran implícitamente, pero el store (#4) y la carga (#7) acceden a memoria y registros arquitectónicos → hay que gestionar orden de memoria.

> DIV.D F0, F2, F4 / ADD.D F2, F4, F8 / SUB.D F0, F4, F8 / S.D F0, 0(R1) / MUL.D F2, F4, F0 / DIV.D F6, F8, F0 / L.D F6, 0(R2) / ADD.D F0, F6, F2 / MUL.D F2, F0, F8 / ADD.D F2, F0, F6
> — `repo:datos/temarios/AC/examenes/January2020.pdf` (cita sin comprobar)

Relacionado: [[como-rellenar-la-tabla-de-estado-de-instrucciones-en-tomasul]] · [[como-rellenar-la-tabla-de-estado-en-tomasulo-con-especulacio]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]]
