---
tipo: "concepto"
titulo: "Configuración Tomasulo con especulación para examen Enero 2012 Problema 3"
temas: ["ac", "especulacion", "rob", "tomasulo", "examen"]
claves: ["CDB", "buffer carga 2 entradas", "buffer almacenamiento 1 entrada", "UF FP", "ROB 10 entradas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf", "repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[rob]] · [[tomasulo]]

Parámetros clave para simulación: CDB con restricción de no escritura y lectura simultánea (efecto: una instrucción que recibe dato en ciclo N no puede empezar ejecución hasta N+1). Buffers: Load Buffer (2 entradas, 2 ciclos EX), Store Buffer (1 entrada, 2 ciclos EX). Estaciones de reserva: 2 por cada UF FP. UF FP: 2 Add/Sub (latencia 2), 2 Mul (latencia 6), 1 Div (latencia 12). ROB: 10 entradas. Instrucciones: 2 L.D, 2 ADD.D, 1 MUL.D, 2 S.D. La simulación requiere tabla de estados (Emisión, Ejecución, Escritura, Terminación) y detenciones por: dependencias RAW (esperar operandos), conflictos estructurales (buffers/estaciones llenos), restricción CDB, orden de memoria (loads/stores a misma dirección).

> Tenemos un procesador MIPS64 con especulación hardware según el método de Tomasulo con especulación. Se dispone de un Bus de Datos Común y se supone que en el mismo ciclo de reloj no se puede escribir un dato en este bus e iniciar la ejecución de una operación que estuviera esperando ese dato. El sistema dispone de un buffer de carga con 2 entradas y un buffer de almacenamiento con 1 entrada. La etapa de ejecución de ambas operaciones requiere 2 ciclos. Además, dispone de varias UF en coma flotante con 2 estaciones de reserva por UF y las siguientes características: Sumador/Restador 2 UF 2 ciclos, Multiplicador 2 UF 6 ciclos, Divisor 1 UF 12 ciclos.
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf` (cita sin comprobar)

## Ampliación (2026-11-18, )
Especificación exacta del procesador para el Problema 2. Puntos clave: ROB pequeño (4 entradas) limita instrucciones en vuelo; 2 RS por unidad FP (adder, multiplier, divider) permite hasta 2 ops simultáneas por tipo; 2 load buffers; latencias asimétricas (div 10c es cuello de botella); CDB de puerto único serializa escrituras; recursos liberados en ciclo N solo disponibles en N+1 (burbuja implícita). Para simular: emitir en orden, ejecutar fuera de orden cuando operandos listos y RS libre, escribir CDB si libre, confirmar en orden desde ROB head.
