---
tipo: "receta"
titulo: "Planificación VLIW para bucle con latencias MEM=2, ADD.D=1, MUL.D=2 (4 ops/ciclo)"
temas: ["ac", "ilp", "planificacion", "vliw"]
claves: ["L.D", "ADD.D", "MUL.D", "S.D", "DADDUI", "BNEZ", "latencia", "hazard", "NOP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[planificacion]] · [[vliw]]

Bucle original (10 instrucciones):
  L.D    F2, 0(R1)      # carga F2
  L.D    F4, 0(R2)      # carga F4
  ADD.D  F6, F2, F2     # F6 = F2+F2 (usa F2)
  ADD.D  F8, F4, F2     # F8 = F4+F2 (usa F4, F2)
  MUL.D  F10, F4, F6    # F10 = F4*F6 (usa F4, F6)
  S.D    F10, 0(R1)     # guarda F10 (usa F10, R1)
  DADDUI R1, R1, #8     # R1 += 8
  DADDUI R2, R2, #8     # R2 += 8
  DADDUI R3, R3, #-1    # R3--
  BNEZ   R3, Bucle      # salto si R3!=0

Latencias (ciclos hasta que resultado disponible para siguiente instrucción):
- L.D / S.D: MEM=2 → resultado listo 2 ciclos después de emitir la carga/almacenamiento.
- ADD.D: EX=1 → resultado listo 1 ciclo después.
- MUL.D: EX=2 → resultado listo 2 ciclos después.
- DADDUI / BNEZ: asumir 1 ciclo (ALU entera simple).

Reglas VLIW: 4 slots por instrucción (ciclo), sin restricciones de tipo por ALU, sin salto retardado (branch resuelto en mismo ciclo o siguiente). Se insertan NOPs (burbujas) para respetar dependencias RAW.

Estrategia de planificación (list scheduling):
1. Ciclo 1: emitir las dos cargas (L.D F2, L.D F4) + dos DADDUI independientes (R1, R2) → 4 ops.
2. Ciclo 2: las cargas en MEM1; emitir DADDUI R3 + NOPs (esperar F2,F4).
3. Ciclo 3: cargas terminan (MEM2); F2,F4 listos. Emitir ADD.D F6 (usa F2) + ADD.D F8 (usa F4,F2) + NOPs.
4. Ciclo 4: ADD.D F6 termina (EX1); F6 listo. Emitir MUL.D F10 (usa F4,F6) + NOPs.
5. Ciclo 5: MUL.D en EX1; esperar.
6. Ciclo 6: MUL.D termina (EX2); F10 listo. Emitir S.D F10 (usa F10,R1) + BNEZ R3 (usa R3) + NOPs.
7. Ciclo 7: S.D en MEM1; salto resuelto (sin delay slot). Fin de iteración.

Total ~7 ciclos por iteración. Ops útiles = 10 / 7 ≈ 1.43 ops/ciclo (máx 4).

> Considera los siguientes parámetros temporales: 2 ciclos para la etapa MEM en las cargas y en los almacenamientos, 1 ciclo para completar la etapa EX de ADD.D y 2 ciclos para completar la etapa EX de la MUL.D. Además, no se aplica salto retardado.
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]] · [[desenrollado-de-bucle-3x-y-planificacion-vliw-compactada]] · [[como-resolver-planificacion-vliw-con-desenrollado-y-latencia]]
