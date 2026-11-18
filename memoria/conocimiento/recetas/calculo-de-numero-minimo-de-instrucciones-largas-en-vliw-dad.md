---
tipo: "receta"
titulo: "Cálculo de número mínimo de instrucciones largas en VLIW dado eficiencia media"
temas: ["ac", "vliw"]
claves: ["VLIW", "long instructions", "NOP", "efficiency", "operations per cycle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[vliw]]

Procesador VLIW emite 4 instrucciones/ciclo (instrucción larga = 4 operaciones). Eficiencia media = 3 ops/ciclo => 75% de ocupación. Programa original: 36 instrucciones (operaciones). Ciclos necesarios = 36 ops / 3 ops por ciclo = 12 ciclos. Cada ciclo emite 1 instrucción larga => mínimo 12 instrucciones largas. Opción correcta: (c) The minimum number of long instructions in the compiler output is 12.

> We have a VLIW processor that can issue four instructions per cycle. A compiler receives as input a program with 36 instructions and provides as output a program for this VLIW processor with an average efficiency of 3 operations per cycle. We can state that...
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`
