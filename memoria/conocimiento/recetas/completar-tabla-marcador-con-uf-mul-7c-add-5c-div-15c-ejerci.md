---
tipo: "receta"
titulo: "Completar tabla Marcador con UF mul 7c add 5c div 15c (Ejercicio 7)"
temas: ["ac", "marcador", "planificacion-dinamica", "scoreboard", "tabla-temporizacion"]
claves: ["2 UF mul 7 ciclos EX", "2 UF add 5 ciclos EX", "1 UF div 15 ciclos EX", "1 UF entera memoria", "un puerto escritura registros", "consideraciones i", "ii", "iii"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[marcador]] · [[planificacion-dinamica]] · [[scoreboard]] · [[tabla-temporizacion]]

La tabla tiene columnas: Instrucción, Emisión, Lectura operandos, Ejecución (inicio-fin), Escritura resultado. Se rellena ciclo a ciclo. Reglas: Emisión: si UF libre y no hay riesgo estructural (puerto escritura), se emite; si UF ocupada, espera (consideración ii permite emitir en ciclo que la anterior escribe). Lectura operandos: si operandos listos (Qi=0), leer; si esperan resultado, esperar hasta que se escribe (consideración i permite leer en mismo ciclo que escritura). Ejecución: dura latencia EX (mul 7, add 5, div 15, load/store 1). Escritura: si puerto escritura libre, escribir y limpiar Qi de registros que esperaban; si ocupado, esperar. Detenciones por: RAW (espera operando), WAR (espera lectura previa), WAW (espera escritura previa), conflicto UF, conflicto puerto escritura. Rellenar filas dadas (fld ciclo 11, fadd.d, fdiv.d ciclo 29, fadd.d, fdiv.d, fdiv.d ciclo 157, fmul.d ciclo 166, fadd.d, fadd.d ciclo 181, fmul.d).

> Completa la siguiente tabla usando la técnica de Marcador. Explica los motivos de las detenciones, si las hay. Ten en cuenta las siguientes consideraciones: i. una instrucción que está esperando un resultado de otra unidad funcional puede pasar a través de la etapa de lectura de operandos al mismo tiempo que el resultado esperado es escrito ii. una instrucción que está esperando una unidad funcional puede ser emitida en el mismo ciclo que la instrucción que está usando dicha unidad completa su etapa de escritura de resultados iii. el fichero de registros sólo tiene un puerto de escritura
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[marcador-scoreboard-distingue-riesgos-raw-y-war-con-detencio]]
