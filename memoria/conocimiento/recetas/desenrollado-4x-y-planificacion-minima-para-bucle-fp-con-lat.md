---
tipo: "receta"
titulo: "Desenrollado 4x y planificación mínima para bucle FP con latencias dadas"
temas: ["ac", "loop-unrolling", "pipeline", "scheduling", "software-pipelining"]
claves: ["unroll 4 times", "minimum cycles", "schedule table", "FP units", "integer units"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[pipeline]] · [[scheduling]] · [[software-pipelining]]

Pasos para planificación óptima desenrollando 4×: 1) Replicar el cuerpo del bucle 4 veces renombrando registros (F2,F4,F6 → F2,F4,F6,F8,F10,F12,F14,F16,F18,F20,F22,F24) y ajustar punteros (R1,R2 decrementados 4×8=32 bytes al final). 2) Eliminar instrucciones de control de bucle internas (SLTI, BEQZ) salvo una comprobación final. 3) Planificar instrucciones en tabla de ciclos respetando: una emisión por ciclo por tipo de unidad (1 FP add, 1 FP mul, 2 INT), latencias de la tabla, y dependencias entre instrucciones. 4) Intercalar cargas, multiplicaciones, sumas y almacenamientos de las 4 iteraciones para ocultar latencias: p.ej. emitir L.D iter1, L.D iter2, L.D iter3, L.D iter4 en ciclos consecutivos (latencia L.D→ALU FP=1), luego MUL.D iter1 (ciclo 2), MUL.D iter2 (ciclo 3), etc., ADD.D iter1 (ciclo 5 tras MUL.D iter1 +3), etc. 5) La longitud mínima del schedule para 4 iteraciones determina ciclos totales; speedup = (4 × CPI_original) / ciclos_totales_desenrollado.

> A) Unroll the loop 4 times and schedule it so that it uses the minimum number of cycles. Write the solution in the table provided on the other side (use as many rows as you need).
> — `repo:datos/temarios/AC/examenes/June2018.pdf`

Relacionado: [[configuracion-del-procesador-para-el-ejercicio-de-desenrolla]] · [[tabla-de-latencias-entre-instrucciones-productoras-y-consumi]] · [[desenrollamiento-de-bucle-3x-y-re-planificacion-en-vliw-para]] · [[desenrollado-de-bucle-8-veces-para-superscalar-con-latencias]] · [[desenrollar-bucle-2x-y-planificar-para-latencias-fp-dadas-ej]]
