---
tipo: "dato"
titulo: "Resultados reales de saltos B1 y B2 en bucles anidados con R1=2, R2=4"
temas: ["ac", "nested loops", "prediccion-saltos"]
claves: ["BEQZ", "DADDUI", "branch outcome", "taken", "not taken", "loop iteration count"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[nested loops]] · [[prediccion-saltos]]

Código:
```
Loop1: BEQZ   R1, end        ; B1
       DADDUI R1, R1, #-1
Loop2: BEQZ   R2, next       ; B2
       DADDUI R2, R2, #-1
       DADDUI R3, R3, #1
       J      Loop2
next:  DADDUI R2, R0, #4     ; restaura R2=4
       J      Loop1
end:   SW     R3, 0(R4)
```
Valores iniciales: R1=2, R2=4, R3=0.
Ejecución:
- **B1 (BEQZ R1, end)**: se toma cuando R1==0. R1 empieza en 2 y se decrementa 1 por iteración externa. Iteraciones externas = 2 (R1=2,1 → después de 2 decrementos R1=0). En la 3ª evaluación de B1, R1=0 → **not taken** (salta a end). Las 2 primeras evaluaciones: R1≠0 → **taken** (continúa en Loop1).
- **B2 (BEQZ R2, next)**: se toma cuando R2==0. R2 se restaura a 4 al inicio de cada iteración externa (instrucción `DADDUI R2, R0, #4` en `next`). Dentro de cada iteración externa, B2 se evalúa 4 veces (R2=4,3,2,1 → taken; 5ª evaluación R2=0 → not taken). Como hay 2 iteraciones externas, B2 se ejecuta 2×5 = 10 veces: 8 **taken**, 2 **not taken** (una por iteración externa).
Secuencia dinámica de saltos (orden de ejecución):
1. B1 taken (R1=2→1)
2. B2 taken (R2=4→3)
3. B2 taken (3→2)
4. B2 taken (2→1)
5. B2 taken (1→0)
6. B2 not taken (R2=0 → salta a next)
7. B1 taken (R1=1→0)
8. B2 taken (R2=4→3)
9. B2 taken (3→2)
10. B2 taken (2→1)
11. B2 taken (1→0)
12. B2 not taken (R2=0 → next)
13. B1 not taken (R1=0 → end)
Total: B1: taken, taken, not taken (3 ejecuciones). B2: 8 taken, 2 not taken (10 ejecuciones).

> Indicate the actual outcome (taken/not taken) for branches B1 and B2, if initially R1=2, R2=4, and R3=0 (R4 contains a valid memory address).
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[resultados-reales-de-saltos-b1-y-b2-en-bucle-mips64-secuenci]] · [[comportamiento-real-de-saltos-b1-beqz-y-b2-beq-en-bucle-mips]] · [[como-determinar-la-secuencia-real-de-saltos-y-resultados-en]]
