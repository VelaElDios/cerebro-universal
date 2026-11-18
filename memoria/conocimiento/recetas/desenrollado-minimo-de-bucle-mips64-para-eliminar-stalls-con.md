---
tipo: "receta"
titulo: "Desenrollado mínimo de bucle MIPS64 para eliminar stalls con FP mul (3 ciclos) y div (4 ciclos)"
temas: ["ac", "loop-unrolling", "mips64", "pipeline"]
claves: ["MUL.D 3 ciclos", "DIV.D 4 ciclos", "forwarding", "delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[mips64]] · [[pipeline]]

Latencias: MUL.D=3, DIV.D=4. Dependencias: I3 (MUL) → I4 (DIV) → I5 (S.D). Con forwarding, resultado de MUL disponible tras 3 ciclos (ciclo de emisión + 3). DIV necesita operandos listos. Para evitar stalls, desenrollar N veces de forma que las instrucciones de iteraciones distintas se entrelacen cubriendo latencias. Mínimo N = techo(latencia_total / ancho_emisión) pero aquí es escalar. Análisis clásico: distancia entre MUL y DIV = 3 ciclos, entre DIV y S.D = 4 ciclos. Desenrollar 4 veces permite reordenar: emitir MUL_i, MUL_i+1, MUL_i+2, MUL_i+3, luego DIV_i (tras 3 ciclos), etc. Verificar con diagrama de tiempo.

> The FP multiplier requires 3 cycles, and the FP divisor requires 4 cycles. ... b) Unroll the loop the minimum number of times to schedule it without stalls. Assume delayed branch.
> — `repo:datos/temarios/AC/examenes/June2018.pdf` (cita sin comprobar)

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]]
