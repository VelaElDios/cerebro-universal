---
tipo: "receta"
titulo: "Tomasulo con CDB no simultáneo 2 RS por UF buffers carga/almacen (Ejercicio 10)"
temas: ["ac", "buffer-almacen", "buffer-carga", "cdb", "planificacion-dinamica", "tabla-estado-instrucciones", "tomasulo"]
claves: ["2 RS por UF", "buffer carga 2 entradas", "buffer almacen 1 entrada", "CDB no permite escribir e iniciar ejecución mismo ciclo", "UF: add 2 (2c)", "mul 2 (6c)", "div 1 (12c)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[buffer-almacen]] · [[buffer-carga]] · [[cdb]] · [[planificacion-dinamica]] · [[tabla-estado-instrucciones]] · [[tomasulo]]

Programa: fld f2,0(x1); fld f4,8(x1); fld f6,16(x1); fadd.d f8,f2,f4; fmul.d f10,f2,f6; fdiv.d f0,f10,f8; fsd f0,32(x1). Estructura: 2 estaciones reserva por UF (add, mul, div), 2 buffers carga, 1 buffer almacen. CDB: escritura y lectura no simultáneas (si una instrucción escribe en CDB en ciclo T, otra que esperaba ese dato no puede iniciar ejecución hasta T+1). Simular ciclo a ciclo: emisión a buffers/estaciones si hueco; ejecución cuando operandos listos y UF libre; escritura en CDB al finalizar EX (1 ciclo); store espera dato en buffer almacen y dirección. Llenar tabla estado instrucciones: Emisión (inicio-fin), Ejecución (inicio-fin), Escritura resultado (inicio-fin). Detallar ciclos para cada instrucción.

> Sea un procesador dotado de planificación dinámica de instrucciones según el método de Tomasulo. Se dispone de un Bus de Datos Común y se supone que en el mismo ciclo de reloj no se puede escribir un dato en este bus e iniciar la ejecución de una operación que estuviera esperando ese dato.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[primeros-3-ciclos-tomasulo-con-2-add-1c-y-2-mul-4c-ejercicio]] · [[completar-tabla-tomasulo-con-una-estacion-por-uf-ejercicio-8]] · [[problema-examen-ac-tomasulo-con-especulacion-buffers-carga-a]]
