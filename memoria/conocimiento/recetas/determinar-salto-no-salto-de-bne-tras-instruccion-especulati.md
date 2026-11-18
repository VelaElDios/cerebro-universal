---
tipo: "receta"
titulo: "Determinar salto/no salto de BNE tras instrucción especulativa con excepción"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["BNE", "branch not equal", "speculative", "DDIV*", "R1", "R2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

La instrucción BNE R1, R2, end salta a 'end' si R1 ≠ R2. Tras DADDI R1, R1, #1, R1 vale 1. Si R2 inicial era 1, BNE no salta (R1=R2) y se ejecutan las instrucciones de la etiqueta 'then' (DDIV R5,R2,R1 y DADDI R3,R3,#1). Si R2 inicial era 0, BNE salta a 'end' y solo se ejecuta DADD R4,R4,R3. La excepción en DDIV* especulativa no altera R1 ni R2, por lo que la decisión del salto depende solo de los valores iniciales.

> BNE     R1, R2, end            No                    No                             Doesn't jump" y "BNE     R1, R2, end            No                    No                             Jumps
> — `repo:datos/temarios/AC/examenes/January2024.pdf` (cita sin comprobar)

Relacionado: [[valores-de-registros-y-flujo-de-control-en-ejemplo-ddiv-espe]]
