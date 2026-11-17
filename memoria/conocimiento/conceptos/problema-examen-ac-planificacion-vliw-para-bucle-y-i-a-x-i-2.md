---
tipo: "concepto"
titulo: "Problema examen AC: Planificación VLIW para bucle y(i)=A*x(i)² con latencias dadas"
temas: ["ac", "ilp", "planificacion", "vliw"]
claves: ["VLIW", "latencias", "LF", "SF", "MULTF", "ADDI", "BNE", "segmento", "detenciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[planificacion]] · [[vliw]]

Bucle kernel: LF F2,0(R2); MULTF F4,F2,F2; MULTF F6,F4,F1; SF 0(R4),F6; ADDI R2,R2,#4; ADDI R4,R4,#4; ADDI R3,R3,#1; BNE R3,R1,BUCLE. VLIW: 2 mem, 2 PF, 1 entera/salto por ciclo. UF PF totalmente segmentadas. Latencias: ALU PF→ALU PF=3, ALU PF→SF=2, ALU Ent→ALU Ent=0, LF→ALU PF=1, LF→SF=0. Ignora retardo salto. Objetivo: rellenar tabla ciclos 1..12+ con asignación a slots (mem1, mem2, PF1, PF2, entera/salto) minimizando stalls (burbujas).

> Planifica el código para eliminar el mayor número de detenciones posible. Rellena la siguiente tabla.
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf`

Relacionado: [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]]
