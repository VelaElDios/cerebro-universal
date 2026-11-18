---
tipo: "receta"
titulo: "Pasos para resolver Exercise 3 Processor A (superscalar in-order sin renombrado)"
temas: ["ac", "pipeline", "superscalar"]
claves: ["in-order issue", "no register renaming", "forwarding", "2-way", "issue window unlimited"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Metodología para rellenar tabla Processor A (ciclos 1-12):
1. Listar instrucciones en orden con sus etapas: IF, ID, EX, MEM, WB (asumiendo MIPS-like de 5 etapas).
2. Ciclo a ciclo, intentar emitir hasta 2 instrucciones en orden (la siguiente no emitida + la siguiente a esa).
3. Comprobar hazards:
   - RAW: forwarding resuelve si resultado listo en EX/MEM/WB anterior; si no, stall en ID.
   - WAR/WAW: SIN renombrado → son hazards reales. Una instrucción que escribe un registro frena a instrucciones posteriores que leen/escriben ese registro hasta que la escritura completa (WB).
   - Estructurales: 2 vías, unidades totalmente segmentadas → no hay conflictos estructurales salvo puertos de banco de registros (ID leer 2, WB escribir 2).
4. Cargas: MEM 2 ciclos → resultado listo al final del 2º ciclo MEM; forwarding desde fin de MEM.
5. Multiplicaciones: EX 2 ciclos → resultado listo al final del 2º ciclo EX; forwarding desde fin de EX.
6. Resto: EX 1 ciclo → forwarding desde fin de EX.
7. Delay branch: no hay saltos en el código, ignorar.
8. Rellenar tabla marcando etapa por ciclo para cada instrucción (burbujas = stall).

> Processor A is a 2-way superscalar processor with in-order issue and an issue window large enough for considering all the instructions. The processor does not support register renaming.
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs]] · [[latencias-de-instrucciones-y-supuestos-de-pipeline-en-exerci]]
