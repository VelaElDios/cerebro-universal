---
tipo: "dato"
titulo: "Latencias de unidades funcionales en el ejemplo de marcador (ciclos 3-9)"
temas: ["ac", "arquitectura", "fp", "latencia", "scoreboard", "unidad-funcional"]
claves: ["Entera", "Mult1", "Suma", "Divide", "latencia", "ciclos", "fmul.d", "fsub.d", "fdiv.d"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[fp]] · [[latencia]] · [[scoreboard]] · [[unidad-funcional]]

Latencias observadas en la simulación (emisión → ejecución completa):

- **UF Entera (cargas fld)**: 2 ciclos de ejecución (emite en 1, lee operandos en 2, ejecuta en 3, escribe en 4). La segunda carga emite en 5, lee en 6, ejecuta en 7, escribe en 8.
- **UF Mult1 (fmul.d)**: emite en ciclo 6, **ejecución completa en ciclo 9** → **latencia 3 ciclos** (típico para multiplicación FP doble).
- **UF Suma (fsub.d)**: emite en ciclo 7, **ejecución completa en ciclo 9** → **latencia 2 ciclos** (típico para suma/resta FP doble).
- **UF Divide (fdiv.d)**: emite en ciclo 8, **no completa en el rango mostrado** (latencia > 1 ciclo, típicamente 10-20 ciclos en FP doble).
- **UF Mult2**: no se usa en este fragmento.

Estas latencias son representativas de pipelines FP de los 90 (ej. MIPS R4000, Alpha 21064) y sirven para calcular CPI y throughput en ejercicios de planificación.

> ciclo 6 fmul.d f0, f2, f4 6 ciclo 9 fmul.d f0, f2, f4 6 9
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[como-leer-la-evolucion-ciclo-a-ciclo-de-un-marcador-con-carg]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]]
