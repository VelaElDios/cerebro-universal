---
tipo: "receta"
titulo: "Secuencia de instrucciones del problema 3 (examen AC Junio 2014) para simulación Tomasulo"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ADD.D F0 F0 F2", "L.D F2 0(R1)", "L.D F4 8(R1)", "MUL.D F8 F2 F4", "L.D F6 16(R1)", "MUL.D F10 F2 F6", "ADD.D F12 F4 F2", "ADD.D F10 F2 F6", "L.D F12 32(R1)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Secuencia exacta de 9 instrucciones para rellenar tabla de ciclos (Emisión, Ejecución, Escritura resultado, Terminación). Dependencias clave:
1. ADD.D F0,F0,F2 → escribe F0
2. L.D F2,0(R1) → escribe F2 (RAW con MUL.D F8 y MUL.D F10 y ADD.D F12 y ADD.D F10)
3. L.D F4,8(R1) → escribe F4 (RAW con MUL.D F8 y ADD.D F12)
4. MUL.D F8,F2,F4 → RAW con #2 y #3, escribe F8
5. L.D F6,16(R1) → escribe F6 (RAW con MUL.D F10)
6. MUL.D F10,F2,F6 → RAW con #2 y #5, escribe F10
7. ADD.D F12,F4,F2 → RAW con #2 y #3, escribe F12 (WAR con #9 L.D F12)
8. ADD.D F10,F2,F6 → RAW con #2 y #5, escribe F10 (WAW con #6 MUL.D F10)
9. L.D F12,32(R1) → escribe F12 (WAR con #7 ADD.D F12)
Notar: F10 tiene WAW entre MUL.D (#6) y ADD.D (#8); F12 tiene WAR entre ADD.D (#7) y L.D (#9). ROB de 4 entradas limita instrucciones en vuelo.

> ADD.D    F0, F0, F2                L.D      F2, 0(R1)                L.D      F4, 8(R1)                MUL.D    F8, F2, F4                L.D      F6, 16(R1)                MUL.D    F10, F2, F6                ADD.D    F12, F4, F2                ADD.D    F10, F2, F6                L.D      F12, 32(R1)
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
