---
tipo: "receta"
titulo: "Cálculo de detenciones (stalls) y CPR en pipeline RISC-V con FP segmentado"
temas: ["ac", "adelantamiento", "cpr", "paralelismo-instruccion", "pipeline", "riscv", "stalls", "unidad-funcional-segmentada"]
claves: ["CPR", "ciclos por resultado", "stalls", "burbujas", "adelantamiento", "forwarding", "latencia", "iniciación", "fmul.d", "fdiv.d", "fld", "fsd", "bne", "ID", "EX", "MEM", "WB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[adelantamiento]] · [[cpr]] · [[paralelismo-instruccion]] · [[pipeline]] · [[riscv]] · [[stalls]] · [[unidad-funcional-segmentada]]

Procedimiento para calcular stalls y CPR en pipeline RISC-V con FP segmentado (Ej.8 y Ej.10):
Supuestos del enunciado: adelantamiento (forwarding) activo, saltos resueltos en ID, unidad entera 1 ciclo, fld/fsd etapa EX 1 ciclo, FP multiplicador 3 ciclos (latencia), FP divisor 4 ciclos (Ej.8) o 6 ciclos (Ej.10), ambos totalmente segmentados (iniciación = 1 ciclo).
Pasos:
1. Dibuja diagrama de espacio-tiempo (instrucciones × ciclos) para una iteración en estado estacionario.
2. Detecta dependencias RAW que no resuelve forwarding:
   - Ej.8: i3 `fmul.d f0,f0,f2` (latencia 3) → i4 `fdiv.d f0,f0,f4` usa f0. Forwarding desde salida de multiplicador (ciclo 3) a entrada de divisor → sin stall si divisor acepta operando cada ciclo (segmentado). Pero i4 escribe f0, i5 `fsd f0,0(x1)` necesita f0 en MEM. Divisor latencia 4 → resultado listo ciclo 4 tras inicio. fsd en MEM necesita dato → stall si MEM antes de WB del divisor.
   - Ej.10: `fdiv.d f0,f0,f10` (latencia 6) → `fsd f0,0(x1)` necesita f0 en MEM. Con forwarding desde WB de divisor a MEM de fsd: si divisor termina WB en ciclo 6, fsd MEM en ciclo 7 → 0 stalls si pipeline permite. Pero hay dos divisiones por iteración.
3. Considera dependencias de control: `bne` resuelto en ID → si salto tomado, 1 ciclo de penalización (flush IF) salvo predicción. En estado estacionario, bne tomado cada iteración → 1 stall por iteración por control.
4. CPR = ciclos totales en estado estacionario / resultados por iteración.
   - Ej.8: 1 resultado (área) por iteración. Instrucciones: 9. Con stalls por FP y control, CPR típico ≈ 9-11 ciclos.
   - Ej.10: 2 resultados (normaliza 2 vectores) por iteración. Dos divisiones en serie (usa mismo f0). CPR = (ciclos iteración) / 2.
Fórmula general: CPR = (instrucciones_por_iteración + stalls_por_iteración) / resultados_por_iteración.

> Indica las detenciones que se producen al ejecutar el código y calcula el CPR (Ciclos Por Resultado).
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf`

Relacionado: [[identificacion-de-dependencias-loop-carried-en-bucles-c-styl]] · [[parametros-de-pipeline-risc-v-fp-para-ejercicios-tema-2-mult]] · [[analisis-de-paradas-en-bucle-con-unidades-fp-de-latencias-2]] · [[analisis-de-detenciones-stalls-en-bucle-con-media-ponderada]]
