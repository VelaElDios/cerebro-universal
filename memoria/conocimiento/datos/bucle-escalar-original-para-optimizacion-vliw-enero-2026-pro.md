---
tipo: "dato"
titulo: "Bucle escalar original para optimización VLIW Enero 2026 Problema 3"
temas: ["ac", "examen", "vliw"]
claves: ["fld f1", "0(x1)", "fadd.d f2", "f1", "f0", "fmul.d f3", "f2", "f1", "fsd f3", "0(x1)", "addi x1", "x1", "-8", "bnez x1", "Loop"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[vliw]]

6 instrucciones por iteración. Dependencias: I2 usa f1 de I1 (latencia fld→PF 1); I3 usa f2 de I2 (latencia PF→PF 3); I4 usa f3 de I3 (latencia PF→fsd 3); I5/I6 independientes de FP pero I6 (bnez) tiene delay slot 1. Puntero x1 decrementa 8 bytes (double). f0 = K constante en registro. Para versión escalar 1 IPC con mismas latencias: cada iteración tarda 1 (I1) +1 stall +1 (I2) +3 stalls +1 (I3) +3 stalls +1 (I4) +1 (I5) +1 (I6) +1 delay slot = 14 ciclos/iter (aprox, ver cálculo exacto en speedup).

> El código ensamblador RISC-V original ("escalar") es: Loop: fld f1, 0(x1) #I1 Carga X(i) fadd.d f2, f1, f0 #I2 Suma: aux= X(i) + K (f0 es constante K) fmul.d f3, f2, f1 #I3 Multiplicación: res = aux * X(i) fsd f3, 0(x1) #I4 Almacena en vector X addi x1, x1, -8 #I5 Decrementa puntero bnez x1, Loop #I6 Salta si no ha terminado
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[especificacion-vliw-1-0-para-examen-enero-2026-problema-3]] · [[latencias-vliw-1-0-para-examen-enero-2026-problema-3]] · [[codigo-del-bucle-a-planificar-en-vliw-examen-ac-enero-2017]] · [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]] · [[planificacion-vliw-de-bucle-con-6-unidades-funcionales-exame]]
