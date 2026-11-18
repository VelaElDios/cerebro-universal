---
tipo: "dato"
titulo: "Valores de registros y flujo de control en ejemplo DDIV* especulativo con dos condiciones iniciales"
temas: ["ac", "pipeline", "prediccion-saltos", "tomasulo"]
claves: ["DDIV*", "BNE", "R1", "R2", "R3", "R4", "R5", "division by zero", "speculative"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]]

El examen evalúa el mismo código especulativo con dos estados iniciales distintos:
- Caso 1 (R2=1): DADDI R1←1; DDIV* R5,R1,R5 (divide por cero, excepción); BNE R1,R2,end → no salta (R1=R2=1); DDIV R5,R2,R1 (1/1=1); DADDI R3←3; DADD R4←6. Resultado final: R1=1,R2=1,R3=3,R4=6,R5=1 (o dirty/undefined según mecanismo).
- Caso 2 (R2=0): DADDI R1←1; DDIV* R5,R1,R5 (excepción); BNE R1,R2,end → salta (R1≠R2); DADD R4,R4,R3 (5); fin. Instrucciones DDIV y DADDI R3 no se ejecutan. Resultado final: R1=1,R2=0,R3=2,R4=5,R5=0/dirty/undefined según mecanismo.

> R1    R2    R3    R4    R5\n 0     1     2     3     0" y "R1       R2     R3    R4    R5\n 0       0       2     3     0
> — `repo:datos/temarios/AC/examenes/January2024.pdf` (cita sin comprobar)

Relacionado: [[tres-mecanismos-de-manejo-de-excepciones-para-instrucciones]] · [[funcionamiento-detallado-de-bits-de-veneno-poison-bits-en-es]]
