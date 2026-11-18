---
tipo: "receta"
titulo: "Primeros 3 ciclos Tomasulo con 2 add 1c y 2 mul 4c (Ejercicio 9)"
temas: ["ac", "cdb", "ciclos-iniciales", "estaciones-reserva", "planificacion-dinamica", "tomasulo"]
claves: ["fadd.d f0", "f2", "f4 (S1)", "fmul.d f2", "f6", "f8 (S2)", "fadd.d f8", "f2", "f4 (S3)", "2 UF add 1 ciclo", "2 UF mul 4 ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cdb]] · [[ciclos-iniciales]] · [[estaciones-reserva]] · [[planificacion-dinamica]] · [[tomasulo]]

Ciclo 1: Emisión S1 (fadd.d) a Add1 (operandos f2,f4 disponibles -> Vj,Vk), Emisión S2 (fmul.d) a Mul1 (f6,f8 disponibles), Emisión S3 (fadd.d) a Add2 (f2 disponible, f4 disponible). S1 y S3 inician ejecución en ciclo 1 (latencia 1). S2 inicia en ciclo 1 (latencia 4). Ciclo 2: S1 y S3 terminan ejecución, escriben resultado en CDB (f0 y f8). S2 continúa. Estaciones Add1 y Add2 libres. Ciclo 3: S2 continúa (ciclo 3 de 4). No hay más instrucciones. Mostrar estado de estaciones (Op, Qj, Qk, Vj, Vk, Busy), registro resultado (Qi), y CDB cada ciclo.

> Muestra lo que sucede en los tres primeros ciclos de su ejecución aplicando Tomasulo. Considera dos unidades de suma y multiplicación en coma flotante, que requieren 1 y 4 ciclos para su ejecución, respectivamente.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[completar-tabla-tomasulo-con-una-estacion-por-uf-ejercicio-8]] · [[tomasulo-con-cdb-no-simultaneo-2-rs-por-uf-buffers-carga-alm]] · [[ejecucion-ciclo-a-ciclo-del-ejemplo-tomasulo-fld-fmul-d-fsub]]
