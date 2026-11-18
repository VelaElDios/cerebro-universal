---
tipo: "receta"
titulo: "Desenrollamiento de bucle mínimo para eliminar detenciones en RISC-V"
temas: ["ac", "loop-unrolling", "pipeline", "riscv", "software-pipelining"]
claves: ["desenrollar bucle", "factor de desenrollamiento", "start-up finish-up", "CPI ideal", "latencia FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[loop-unrolling]] · [[pipeline]] · [[riscv]] · [[software-pipelining]]

Procedimiento estándar (Ej. 15b, 17b, 18b):
1. **Calcular distancia mínima entre instrucciones dependientes** (latencia efectiva con forwarding).
   - Ej: fmul.d (3 ciclos EX) → resultado listo al final de EX3. fdiv.d (4 ciclos) → final EX4.
   - fld: dato listo tras MEM (o EX si forwarding desde MEM). fsd: necesita dato en EX.
   - Salto resuelto en ID → instrucción en delay slot (siguiente a bne) se ejecuta gratis.
2. **Determinar factor de desenrollamiento N** = techo( latencia_crítica / ciclos_entre_instrucciones_independientes ).
   - Latencia crítica = ciclos desde que se produce un valor hasta que se consume sin stall.
   - Ciclos entre instrucciones = 1 (ideal, 1 instr/ciclo en estado estacionario).
   - N = latencia_crítica (en ciclos) para la cadena más larga de dependencias loop-carried.
3. **Copiar cuerpo del bucle N veces**, renombrando registros temporales (f0, f2, f4... → f0, f6, f10... o usar más registros FP) para romper WAW/WAR *entre copias*.
   - Registros de índice (x1, x2, x3): actualizar *una sola vez* al final del cuerpo desenrollado (addi x1, x1, 8*N).
   - Comparación de salto (bne): comparar con límite ajustado (x3 - N) o usar contador separado.
4. **Planificar (schedule)** las N×instrucciones reordenándolas para llenar huecos (software pipelining sobre el cuerpo desenrollado).
5. **Añadir start-up** (instrucciones iniciales de las primeras iteraciones) y **finish-up** (instrucciones finales de las últimas iteraciones) para que código sea funcional equivalente.
6. **Verificar CPI**: estado estacionario = (ciclos_cuerpo_desenrollado) / (N * instrucciones_originales_por_iter). Ideal = 1.0 si no hay stalls.

> Desenrolla el bucle el mínimo número de veces para evitar todas las detenciones. Asume que hay salto retardado.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[parametros-estandar-para-ejercicios-de-segmentacion-software]] · [[dependencias-en-bucles-risc-v-clasificacion-intra-iteracion]] · [[segmentacion-software-software-pipelining-para-bucle-conteo]] · [[desenrollado-de-bucle-minimo-para-planificacion-sin-detencio]]
