---
tipo: "receta"
titulo: "Simulación de algoritmo Tomasulo básico y especulativo con ROB de 5 entradas"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["Tomasulo básico", "Tomasulo especulativo", "ROB", "ciclos emisión ejecución escritura terminación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

El problema proporciona 7 instrucciones: L.D F0,0(R1); L.D F2,0(R2); L.D F4,0(R3); MUL.D F6,F0,F2; ADD.D F8,F0,F4; DIV.D F10,F8,F6; S.D F10,0(R4). Para la versión básica se pide rellenar columnas: Emisión, Ejecución, Escritura res. Para la versión especulativa con ROB de 5 entradas inicialmente vacío: Emisión, Ejecución, Escritura res., Terminación. Además, se pide mostrar el contenido del ROB (5 entradas: Nº entrada, ¿Ocupada?, Instrucción, Estado, Destino, Valor) al final del ciclo 8. Las latencias típicas implícitas: carga ~2 ciclos, MUL ~10, ADD ~4, DIV ~40, store ~1; pero el examen no las declara explícitamente en el trozo.

> Detalla la ejecución del código de abajo cuando se emplea la versión básica del algoritmo de Tomasulo (sin especulación). Para ello, indica en la tabla siguiente el número de ciclo en el que se inicia y se completa cada paso.
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[como-simular-tomasulo-especulativo-con-rob-de-4-entradas-y-l]] · [[secuencia-de-instrucciones-para-simulacion-tomasulo-con-div]] · [[simulacion-tomasulo-especulativa-con-rob-de-4-entradas-exame]]
