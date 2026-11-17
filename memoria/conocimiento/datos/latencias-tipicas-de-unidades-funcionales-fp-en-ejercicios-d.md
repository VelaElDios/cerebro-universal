---
tipo: "dato"
titulo: "Latencias típicas de unidades funcionales FP en ejercicios del temario (ciclos)"
temas: ["ac", "latencia", "punto-flotante", "uf"]
claves: ["fadd.d fmul.d fdiv.d fld fsd", "ciclos ejecución", "segmentada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[latencia]] · [[punto-flotante]] · [[uf]]

Valores que aparecen en distintos ejercicios (¡usar los del enunciado concreto!):
- **Ej. 12 (implícito en diagrama)**: fmul.s: EX1-EX4 (4 ciclos EX), fld/fsd: EX+MEM (2 ciclos), addi/bne: 1 ciclo EX.
- **Ej. 13**: No da latencias explícitas → asumir "típicas" (suma 2, mul 3-4, div 4, load/store 1-2).
- **Ej. 14 (Tomasulo)**: Suma/Resta 2, Multiplicador 4, fld/fsd ejecución 2 ciclos.
- **Ej. 15**: Multiplicación 3 ciclos, División 4 ciclos, UF completamente segmentadas.
- **Ej. 16**: fld/fsd ejecución 1 ciclo, fadd.d/fsub.d 2 ciclos, fmul.d 5 ciclos.
- **Ej. 17**: Suma FP 2, Multiplicación FP 4, División FP 7, fld/fsd 1 ciclo (implícito "todas las etapas 1 ciclo excepto EX FP").
- **Ej. 18**: Solo enteras (lw, add, slt, addi, bne) → 1 ciclo por etapa, sin latencias FP.
Nota: "Completamente segmentada" = puede iniciar nueva operación cada ciclo (throughput 1), latencia = ciclos de EX.

> La unidad funcional PF de multiplicación requiere 3 ciclos y la división requiere 4 ciclos." / "Suma FP 2 / Multiplicación FP 4 / División FP 7" / "La etapa de ejecución de fld y fsd consume 2 ciclos de reloj." / "ejecución de las instrucciones fadd.d, fsub.d y fmul.d requiere 2, 2 y 5 ciclos, respectivamente.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf` (cita sin comprobar)

Relacionado: [[parametros-estandar-para-ejercicios-de-segmentacion-software]] · [[algoritmo-de-tomasulo-reglas-de-simulacion-para-ejercicios-d]]
