---
tipo: "receta"
titulo: "Completar tabla Tomasulo con una estación por UF (Ejercicio 8)"
temas: ["ac", "cdb", "estacion-reserva", "planificacion-dinamica", "tabla-temporizacion", "tomasulo"]
claves: ["2 UF mul 7c", "2 UF add 5c", "1 UF div 15c", "1 UF entera", "una estación reserva por UF", "consideraciones i", "ii", "iii"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cdb]] · [[estacion-reserva]] · [[planificacion-dinamica]] · [[tabla-temporizacion]] · [[tomasulo]]

Tabla Tomasulo: Instrucción, Emisión, Ejecución (inicio-fin), Escritura resultado. Estaciones de reserva: una por UF (total 2 mul, 2 add, 1 div, 1 load/store). Emisión: si estación libre, asignar; si ocupada, esperar (consideración ii permite emitir en ciclo que anterior escribe resultado). Ejecución: comienza cuando operandos disponibles (Vj/Vk o escuchando CDB). Duración EX fija. Escritura: en ciclo siguiente a fin EX, poner resultado en CDB (consideración iii: CDB leído y escrito mismo ciclo). Las estaciones que esperan ese registro capturan valor. Detenciones: estructural (estación llena), RAW (espera operando via CDB), WAW (gestión de Qi en registro destino). Rellenar filas dadas (fld ciclo 11, fadd.d, fdiv.d ciclo 30, fadd.d, fdiv.d, fdiv.d ciclo 158, fmul.d ciclo 167, fadd.d, fadd.d ciclo 182, fmul.d).

> Completa la siguiente tabla usando la técnica de Tomasulo. Explica los motivos de las detenciones, si las hay. Ten en cuenta las siguientes consideraciones: i. sólo hay una estación de reserva por unidad funcional ii. una instrucción que está esperando una unidad funcional puede ser emitida en el mismo ciclo que la instrucción que está usando dicha unidad completa su etapa de escritura de resultados. iii. el CDB puede ser escrito y leído en el mismo ciclo
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[completar-tabla-marcador-con-uf-mul-7c-add-5c-div-15c-ejerci]] · [[tomasulo-con-cdb-no-simultaneo-2-rs-por-uf-buffers-carga-alm]] · [[primeros-3-ciclos-tomasulo-con-2-add-1c-y-2-mul-4c-ejercicio]] · [[planificacion-con-algoritmo-tomasulo-issue-execution-commit]]
