---
tipo: "receta"
titulo: "Segmentación software (software pipelining) para bucle conteo negativos RISC-V"
temas: ["ac", "modulo-scheduling", "pipeline", "riscv", "segmentacion-software", "software-pipelining"]
claves: ["segmentación software", "software pipelining", "start-up", "finish-up", "kernel", "dependencias bucle", "desenrollado", "RISC-V"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[modulo-scheduling]] · [[pipeline]] · [[riscv]] · [[segmentacion-software]] · [[software-pipelining]]

**Bucle original**: lw x5,0(x1); slt x5,x5,x0; add x3,x3,x5; sw x3,0(x2); addi x1,x1,4; addi x4,x4,-1; bne x4,x0,bucle. **Pipeline**: IF, ID, EX, MEM, WB; forward EX→EX, MEM→EX; salto resuelto en ID; load-use penalty 1 ciclo (MEM→EX). **a) Detenciones**: lw→slt: 1 (load-use); slt→add: 0 (forward EX); add→sw: 0 (forward EX); sw→addi(x1): 0 (sw MEM, addi EX, distinto reg); addi(x1)→lw(sig iter): 0 (forward MEM→EX? addi WB en ciclo 5, lw ID en ciclo 5? Requiere análisis detallado); addi(x4)→bne: 0 (forward EX→ID? bne en ID, addi en EX mismo ciclo → 1 ciclo si no hay forward ID); bne→lw(sig): 1 (control hazard, salto en ID, target en IF siguiente). **b) Kernel segmentado**: Reordenar para separar dependencias carried (x3, x1, x4). Instrucciones: lw, slt, add, sw, addi1, addi2, bne. Dependencias carried: x3 (add→add), x1 (addi1→lw), x4 (addi2→bne). Latencias: lw→slt 1, slt→add 0, add→sw 0, add→add 1 (x3), addi1→lw 1 (x1), addi2→bne 1 (x4). II (Initiation Interval) mínimo = max(RecMII, ResMII). RecMII = 1 (ciclo por dependencia carried). ResMII = ceil(instrucciones/unidades) = 7/1? Superescalar grado 1 → 7. Pero con pipeline, se solapan. **c) Start-up**: prologue con primeras instrucciones de iteraciones 1,2,3... **Finish-up**: epilogue con últimas instrucciones. (Solución completa requiere diagrama de precedencias y tabla de reservas).

> Problema 1 (2,5 puntos). El siguiente bucle se ejecuta en un procesador RISC-V segmentado... a) Indica las detenciones entre cada par de instrucciones... b) Aplica segmentación software para eliminar todas las dependencias de datos del cuerpo del bucle... c) Detalla los bloques start-up (a la izquierda) y finish-up (a la derecha).
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)
