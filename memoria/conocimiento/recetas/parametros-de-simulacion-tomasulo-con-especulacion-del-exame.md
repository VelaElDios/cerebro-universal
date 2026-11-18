---
tipo: "receta"
titulo: "Parámetros de simulación Tomasulo con especulación del examen Junio 2011 (Problema 2)"
temas: ["ac", "buffers", "especulacion", "simulacion", "tomasulo", "unidades-funcionales"]
claves: ["Tomasulo especulativo", "buffer carga 2 entradas", "buffer almacenamiento 1 entrada", "UF FP", "estaciones reserva", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[buffers]] · [[especulacion]] · [[simulacion]] · [[tomasulo]] · [[unidades-funcionales]]

Configuración completa para simular Tomasulo con especulación (ROB, renombramiento, emisión en orden, ejecución/escritura fuera de orden, commit en orden):
- Buffers: Load Buffer (2 entradas, 2 ciclos ejecución), Store Buffer (1 entrada, 2 ciclos ejecución).
- Unidades funcionales FP: 2 Adders (3 ciclos, 2 estaciones cada una), 2 Multipliers (8 ciclos, 2 estaciones cada una), 1 Divider (10 ciclos, 2 estaciones).
- CDB: escritura y lectura en mismo ciclo no permitidas (riesgo estructural en bus).
- Instrucciones a simular: LD F2,0(R1); LD F4,8(R1); ADDD F8,F2,F4; LD F6,16(R1); MULTD F10,F2,F6; DIVD F12,F10,F8; SUBD F14,F16,F14; SD 32(R1),F12.
- Rellenar tabla: Emisión, Ejecución (inicio-fin), Escritura resultado, Terminación (commit).

> Tenemos un procesador con especulación hardware según el método de Tomasulo con especulación. Se dispone de un Bus de Datos Común y se supone que en el mismo ciclo de reloj no se puede escribir un dato en este bus e iniciar la ejecución de una operación que estuviera esperando ese dato. El sistema dispone de un buffer de carga con 2 entradas y un buffer de almacenamiento con 1 entrada. La etapa de ejecución de ambas operaciones requiere 2 ciclos. Además, dispone de varias UF en coma flotante con 2 estaciones de reserva por UF y las siguientes características: UF Sumador/Restador PF Cantidad 2 Ciclos 3; Multiplicador PF 2 8; Divisor PF 1 10
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
