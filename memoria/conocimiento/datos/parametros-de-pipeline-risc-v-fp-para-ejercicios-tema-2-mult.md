---
tipo: "dato"
titulo: "Parámetros de pipeline RISC-V FP para ejercicios Tema 2 (multiplicador 3 ciclos, divisor 4/6 ciclos)"
temas: ["ac", "iniciacion", "latencia", "paralelismo-instruccion", "pipeline", "punto-flotante", "riscv"]
claves: ["fmul.d 3 ciclos", "fdiv.d 4 ciclos", "fdiv.d 6 ciclos", "completamente segmentado", "iniciación 1 ciclo", "adelantamiento", "salto resuelto ID"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[iniciacion]] · [[latencia]] · [[paralelismo-instruccion]] · [[pipeline]] · [[punto-flotante]] · [[riscv]]

Valores fijos dados en los enunciados para el modelo de pipeline:
- Ejercicio 8 (cálculo áreas triángulos):
  - FP multiplicador (fmul.d): latencia 3 ciclos, iniciación 1 ciclo (totalmente segmentado).
  - FP divisor (fdiv.d): latencia 4 ciclos, iniciación 1 ciclo (totalmente segmentado).
  - fld/fsd: etapa de ejecución (EX) 1 ciclo.
  - Unidad entera (addi, bne): 1 ciclo.
  - Saltos (bne) resueltos en etapa ID.
  - Adelantamiento de operandos (forwarding) soportado.
- Ejercicio 10 (normalización vectores):
  - FP divisor (fdiv.d): latencia 6 ciclos, iniciación 1 ciclo (totalmente segmentado).
  - Resto igual que arriba.
Estos parámetros determinan los stalls por dependencias RAW en cadenas FP (ej. fmul → fdiv → fsd) y el CPR final.

> La unidad funcional de PF de multiplicación requiere 3 ciclos y la división 4 ciclos." / "La unidad funcional de división en punto flotante está completamente segmentada y emplea 6 ciclos.
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-detenciones-stalls-y-cpr-en-pipeline-risc-v-con-f]]
