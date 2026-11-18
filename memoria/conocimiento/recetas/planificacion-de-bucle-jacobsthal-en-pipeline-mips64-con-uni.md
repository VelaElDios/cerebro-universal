---
tipo: "receta"
titulo: "Planificación de bucle Jacobsthal en pipeline MIPS64 con unidades FP de 2 y 3 ciclos y salto retrasado"
temas: ["ac", "mips64", "pipeline"]
claves: ["Jacobsthal sequence", "loop scheduling", "delayed branch", "floating-point pipeline", "forwarding", "stall cycles"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips64]] · [[pipeline]]

**Parte a) Stalls en bucle original:** Dependencias RAW resueltas con forwarding. L.S (1 ciclo MEM) -> MUL.S (3 ciclos EX) necesita resultado de L.S: 1 stall (MUL.S espera en ID hasta que L.S termine MEM). MUL.S -> ADD.S (2 ciclos EX): ADD.S necesita resultado de MUL.S, forwarding desde EX/MEM de MUL.S tras 3 ciclos => 2 stalls. ADD.S -> S.S (1 ciclo MEM): S.S necesita resultado de ADD.S, forwarding desde EX/MEM de ADD.S tras 2 ciclos => 1 stall. S.S -> DADDUI R2: sin dependencia. DADDUI R2 -> DADDUI R3: sin dependencia. DADDUI R3 -> BNE: BNE resuelto en ID, necesita R3 listo; DADDUI escribe en WB, forwarding a ID => 0 stalls (si WB y ID mismo ciclo). BNE -> siguiente iteración: salto retrasado (delayed branch) permite rellenar slot de retardo. **Parte b) CPR original:** Ciclos por iteración = instrucciones (8) + stalls (1+2+1=4) = 12 ciclos/iteración. **Parte c) Planificación sin stalls con desenrollado y salto retrasado:** Desenrollar 2 veces (para ocultar latencias FP). Reordenar instrucciones de ambas iteraciones intercalando operaciones independientes. Usar slot de retardo del salto para instrucción útil (ej. DADDUI de la siguiente iteración). Código resultante compacto y funcional. **Parte d) CPR resultante:** Con desenrollado 2x y planificación óptima, se logran 10 ciclos para 2 iteraciones => CPR = 5 ciclos/iteración.

> The next loop runs on a pipelined MIPS64 processor to store in memory (as floating-point numbers in simple precision) the first numbers of the Jacobsthal sequence...
> — `repo:datos/temarios/AC/examenes/January 2025.pdf` (cita sin comprobar)

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[configuracion-de-pipeline-mips64-para-problema-de-examen-lat]] · [[desenrollado-de-bucle-minimo-para-eliminar-todos-los-stalls]] · [[desenrollado-minimo-de-bucle-mips64-para-eliminar-stalls-con]]
