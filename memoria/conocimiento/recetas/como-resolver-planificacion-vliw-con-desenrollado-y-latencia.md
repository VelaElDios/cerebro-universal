---
tipo: "receta"
titulo: "Cómo resolver planificación VLIW con desenrollado y latencias dadas"
temas: ["ac", "desenrollado-bucle", "planificacion", "receta", "vliw"]
claves: ["VLIW scheduling", "loop unrolling", "latency hiding", "forwarding", "delayed branch", "slot filling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollado-bucle]] · [[planificacion]] · [[receta]] · [[vliw]]

Pasos para resolver este tipo de problemas:
1. Identificar latencias por etapa: MEM=2 (L.D, S.D), EX=2 (ADD.D, MUL.D, DIV.D), IF/ID/WB=1 (DADDUI, BNEZ).
2. Dibujar diagrama de dependencias del bucle original (RAW: F2/F4 entre L.D→ADD.D/MUL.D; F8/F6 entre MUL.D/ADD.D→DIV.D; F0 entre DIV.D→S.D; R1/R2/R10 entre DADDUI→siguiente iteración).
3. Desenrollar N veces (aquí N=4), renombrando registros si hace falta (aquí no hay renombrado por ser VLIW estático, se usan mismos registros pero offsets distintos).
4. Planificar ciclo a ciclo colocando hasta 4 ops/ciclo, respetando:
   - Una operación no puede emitirse hasta que sus operandos estén listos (latencia del productor).
   - Forwarding permite usar resultado al ciclo siguiente de terminar EX/MEM.
   - Delayed branch: la instrucción en el "delay slot" tras BNEZ se ejecuta siempre.
5. Rellenar huecos con instrucciones de iteraciones posteriores (software pipelining manual).
6. Contar operaciones totales emitidas / ciclos usados para parte (b).

> Assume the following timing parameters: 2 cycles for the MEM step of loads and stores, 2 cycles for the EX step of arithmetic operations, and 1 cycle for the rest of steps.
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]] · [[planificacion-vliw-para-bucle-con-latencias-mem-2-add-d-1-mu]] · [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]]
