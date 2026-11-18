---
tipo: "dato"
titulo: "Secuencia de instrucciones MIPS64 del examen Junio 2012 (Tomasulo especulativo)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["L.D F0", "L.D F2", "ADD.D F4", "L.D F6", "MUL.D F8", "ADD.D F10", "S.D F8", "S.D F10"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Secuencia exacta de 8 instrucciones del problema:
1. L.D  F0,  0(R1)    ; carga F0 desde memoria
2. L.D  F2,  0(R2)    ; carga F2 desde memoria
3. ADD.D F4, F0, F2   ; F4 = F0 + F2 (depende de 1 y 2)
4. L.D  F6,  0(R3)    ; carga F6 desde memoria
5. MUL.D F8, F4, F6   ; F8 = F4 * F6 (depende de 3 y 4)
6. ADD.D F10, F6, F12 ; F10 = F6 + F12 (depende de 4, F12 ya disponible)
7. S.D  F8,  8(R1)    ; almacena F8 (depende de 5)
8. S.D  F10, 8(R2)    ; almacena F10 (depende de 6)
Patrón de dependencias: RAW en 3→5, 4→5, 4→6, 5→7, 6→8. WAW potencial en F6 (instr 4 vs uso en 5,6).

> L.D F0, 0(R1) / L.D F2, 0(R2) / ADD.D F4, F0, F2 / L.D F6, 0(R3) / MUL.D F8, F4, F6 / ADD.D F10, F6, F12 / S.D F8, 8(R1) / S.D F10, 8(R2)
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[secuencia-de-instrucciones-del-problema-3-examen-ac-junio-20]] · [[secuencia-de-instrucciones-mips64-para-simulacion-tomasulo-p]] · [[secuencia-de-instrucciones-para-simulacion-tomasulo-con-div]]
