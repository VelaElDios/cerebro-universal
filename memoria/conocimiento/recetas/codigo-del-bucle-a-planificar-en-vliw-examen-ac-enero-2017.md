---
tipo: "receta"
titulo: "Código del bucle a planificar en VLIW (examen AC enero 2017)"
temas: ["ac", "bucle", "examen", "planificacion", "vliw"]
claves: ["L.S", "MUL.S", "S.S", "ADD.S", "DADDUI", "BNEZ", "Loop", "F1", "F2", "F3", "F4", "F5", "R1", "R2", "R3", "R4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucle]] · [[examen]] · [[planificacion]] · [[vliw]]

Bucle completo de 12 instrucciones que procesa arrays en memoria (patrón típico de producto punto o similar):
1. L.S   F1, 0(R1)        ; carga FP desde dirección base R1
2. L.S   F2, 0(R2)        ; carga FP desde dirección base R2
3. MUL.S F4, F2, F1       ; F4 = F2 * F1  (usa FP MUL, latencia 4)
4. S.S   F4, 0(R1)        ; almacena F4 en 0(R1)  (usa MEM, latencia 3)
5. L.S   F3, 0(R3)        ; carga FP desde dirección base R3
6. ADD.S F5, F4, F3       ; F5 = F4 + F3  (usa FP ADD, latencia 4, depende de MUL.S y L.S F3)
7. S.S   F5, 0(R3)        ; almacena F5 en 0(R3)  (usa MEM, depende de ADD.S)
8. DADDUI R1, R1, #4      ; R1 += 4  (unidad entera, latencia 1)
9. DADDUI R2, R2, #4      ; R2 += 4  (unidad entera)
10. DADDUI R3, R3, #4     ; R3 += 4  (unidad entera)
11. DADDUI R4, R4, #-1    ; R4--     (unidad entera, actualiza contador de bucle)
12. BNEZ   R4, Loop       ; salto si R4 != 0 (unidad entera, slot de retardo = 1)

Dependencias clave (RAW):
- MUL.S (3) necesita F1 de L.S (1) y F2 de L.S (2) → 3 ciclos de espera por latencia de carga (3) + forwarding.
- S.S (4) necesita F4 de MUL.S (3) → 4 ciclos de espera por latencia FP MUL (4) + forwarding.
- ADD.S (6) necesita F4 de MUL.S (3) y F3 de L.S (5) → espera a MUL.S (4 ciclos) y L.S (3 ciclos).
- S.S (7) necesita F5 de ADD.S (6) → 4 ciclos por latencia FP ADD.
- BNEZ (12) necesita R4 de DADDUI (11) → 1 ciclo por latencia entera.
- Las actualizaciones de R1, R2, R3 (8-10) son independientes entre sí y de las cargas/almacenamientos de la misma iteración (usan registros base distintos).

> Loop: L.S    F1, 0(R1)      L.S    F2, 0(R2)      MUL.S F4, F2, F1      S.S    F4, 0(R1)      L.S    F3, 0(R3)      ADD.S F5, F4, F3      S.S    F5, 0(R3)      DADDUI R1, R1, #4      DADDUI R2, R2, #4      DADDUI R3, R3, #4      DADDUI R4, R4, #-1      BNEZ   R4, Loop
> — `repo:datos/temarios/AC/examenes/January2017.pdf`
