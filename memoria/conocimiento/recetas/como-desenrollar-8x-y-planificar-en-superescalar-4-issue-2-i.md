---
tipo: "receta"
titulo: "Cómo desenrollar 8x y planificar en superescalar 4-issue (2 int + 2 PF) con sumas PF 2 ciclos"
temas: ["ac", "loop-unrolling", "mips64", "planificacion", "superescalar"]
claves: ["superescalar grado 4", "2 enteros 2 punto flotante", "desenrollado 8 veces", "ADD.D 2 ciclos", "adelantamiento", "salto retardado", "unidades segmentadas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[mips64]] · [[planificacion]] · [[superescalar]]

Bucle original: L.D F10,0(R2) | ADD.D F8,F10,F4 | S.D F8,0(R2) | DADDUI R2,R2,-8 | BNE R2,R3,Bucle. Desenrollar 8 veces → 40 instrucciones (8×5). Superescalar: emite hasta 4/ciclo (máx 2 enteras + 2 PF). Unidades segmentadas → pueden iniciar nueva op cada ciclo. ADD.D latencia 2 ciclos EX (resultado listo tras 2). Adelantamiento disponible. Salto retardado → slot de retardo se rellena. Planificación: objetivo maximizar throughput, minimizar ciclos. Estrategia: agrupar instrucciones independientes de distintas iteraciones. Ejemplo ciclo 1: L.D iter1, L.D iter2, DADDUI iter1, DADDUI iter2 (2 PF + 2 int). Ciclo 2: L.D iter3, L.D iter4, DADDUI iter3, DADDUI iter4. Ciclo 3: ADD.D iter1, ADD.D iter2, S.D iter1, S.D iter2 (pero ADD.D usa F10 de L.D → con adelantamiento, ADD.D puede iniciar en ciclo 3 si L.D terminó MEM en ciclo 2). Continuar hasta emitir todas. BNE final en slot de retardo de último salto.

> Desenrolla el código 8 veces y planifícalo lo más compactamente posible para el superescalar planteado indicando las instrucciones emitidas en cada ciclo.
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf`
