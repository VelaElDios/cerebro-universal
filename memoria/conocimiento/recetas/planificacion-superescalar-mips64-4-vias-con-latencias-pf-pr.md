---
tipo: "receta"
titulo: "Planificación superescalar MIPS64 4 vías con latencias PF (Problema 4 Enero 2015)"
temas: ["ac", "cpi", "mips64", "planificacion", "superescalar"]
claves: ["L.D", "MUL.D", "ADD.D", "S.D", "DADDUI", "BNE", "desenrollado 6 veces", "2 enteras/mem + 2 PF por ciclo", "suma PF 2 ciclos", "mul PF 3 ciclos", "adelantamiento", "salto retardado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[mips64]] · [[planificacion]] · [[superescalar]]

**Parámetros máquina:**
- 5 etapas: IF, ID, EX, MEM, WB (o similar).
- Ancho 4: hasta 2 instrucciones enteras/de memoria (carga/almacena, ALU entera, salto) + 2 instrucciones PF por ciclo.
- Adelantamiento (forwarding) completo.
- Salto retardado (delayed branch): la instrucción en el slot de retardo se ejecuta siempre.
- Unidades segmentadas: pueden aceptar nueva operación cada ciclo.
- Latencias etapa EX: FP ADD.D = 2 ciclos, FP MUL.D = 3 ciclos, FP L.D/S.D = 1 ciclo (dir. efectiva + acceso), Enteras (DADDUI, BNE) = 1 ciclo.

**Código bucle original:**
```
Bucle: L.D   F4, 0(R1)      ; FP load
       MUL.D F6, F4, F4     ; FP mul (3 ciclos EX)
       ADD.D F6, F6, F4     ; FP add (2 ciclos EX), depende de MUL.D
       S.D   F6, 0(R1)      ; FP store, depende de ADD.D
       DADDUI R1, R1, 8     ; Entera, actualiza puntero
       BNE    R1, R2, Bucle ; Salto retardado
```

**Dependencias clave:**
- MUL.D → ADD.D (RAW en F6, latencia 3 ciclos EX mul + forwarding a add).
- ADD.D → S.D (RAW en F6, latencia 2 ciclos EX add + forwarding a store).
- L.D → MUL.D (RAW en F4, latencia 1 ciclo EX load + forwarding).
- S.D → DADDUI: independiente (distintos registros).
- DADDUI → BNE: RAW en R1 (salto usa R1 actualizado).
- BNE → siguiente iteración: salto retardado, slot de retardo útil.

**Estrategia desenrollado 6× (6 iteraciones = 6×6=36 instrucciones):**
Renombrar registros para evitar dependencias falsas (WAR/WAW) entre iteraciones: usar F4_i, F6_i por iteración i. El puntero R1 se actualiza secuencialmente (DADDUI encadenado), pero las cargas/almacenas de cada iteración usan R1 con offset 0 y R1 ya actualizado por DADDUI previas. Con adelantamiento, la dirección efectiva de L.D/S.D de iteración i usa R1 tras i-1 DADDUI.

**Planificación compacta (esquema por ciclos, 4 vías):**
Se busca llenar huecos de latencia PF con instrucciones de otras iteraciones. Como hay 2 vías PF, se pueden solapar MUL.D y ADD.D de distintas iteraciones. La vía entera/memoria sirve para L.D, S.D, DADDUI, BNE.

Ejemplo de tabla de planificación (ciclo → instrucciones lanzadas):
```
Ciclo 1: L.D F4_1,0(R1) | L.D F4_2,0(R1+8) | DADDUI R1,R1,8 | (BNE no aún)
Ciclo 2: MUL.D F6_1,F4_1,F4_1 | L.D F4_3,0(R1+16) | DADDUI R1,R1,8 | ...
...
```
La planificación exacta requiere simular ciclo a ciclo respetando:
- Máx 2 PF / ciclo.
- Máx 2 Entera/Mem / ciclo.
- Dependencias RAW con latencias dadas (forwarding al ciclo siguiente de terminar EX).
- Salto retardado: BNE se lanza en un ciclo, la instrucción en su slot de retardo (la siguiente en orden de programa) se ejecuta siempre. Al desenrollar, los BNE de cada iteración (excepto el último) saltan al siguiente BNE o al código posterior; el último BNE sale del bucle.

**Cálculo CPI:**
CPI = (Total ciclos de la planificación) / (Total instrucciones ejecutadas = 36).
Con planificación óptima, el bucle desenrollado 6× debería acercarse a CPI ≈ 1 (ideal 4 inst/ciclo → CPI 0.25, pero dependencias y recursos limitan). La respuesta numérica exacta sale de la tabla completa.

> Un procesador superescalar MIPS64 con 5 etapas puede lanzar 4 instrucciones por ciclo: dos enteras o de acceso a memoria y dos de punto flotante. Se asume que existen adelantamientos, salto retardado y que todas las unidades funcionales están segmentadas. Además, las sumas en PF requieren 2 ciclos para la etapa de ejecución, las multiplicaciones en PF 3 ciclos y el resto de operaciones 1 ciclo.
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[comparativa-tomasulo-vs-marcador-scoreboard]]
