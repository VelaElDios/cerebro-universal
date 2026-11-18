---
tipo: "concepto"
titulo: "Buffer de Reordenamiento (ROB) en Tomasulo con especulación: campos y funcionamiento"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB", "buffer de reordenamiento", "entrada ROB", "destino", "valor", "terminada", "commit", "especulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Estructura y uso del ROB (6 entradas, índices 0-5) en Tomasulo especulativo:
- **Campos por entrada**:
  * **Instrucción**: tipo y operandos (ej. "MUL.D F8, F2, F4")
  * **Destino**: registro arquitectónico (F8) o dirección memoria efectiva (para S.D)
  * **Valor**: dato resultante (una vez ejecutado) o tag de otra entrada ROB (mientras espera)
  * **¿Terminada? (s/n)**: 's' cuando la instrucción ha completado Escritura (resultado en CDB y capturado en ROB), 'n' en caso contrario.
- **Asignación**: En **Emisión** (en orden), se reserva la siguiente entrada libre (cola circular). El destino arquitectónico de la instrucción se mapea a esta entrada ROB (renombramiento implícito).
- **Actualización Valor**: En **Escritura/CDB**, cuando la instrucción publica resultado, se copia el dato al campo Valor de su entrada ROB y se pone ¿Terminada? = s. Las estaciones de reserva que esperaban ese tag (ROB#) ven el dato en CDB y capturan el valor.
- **Commit (Terminación)**: En orden de programa, una por ciclo (cabeza de cola ROB). Si ¿Terminada?=s → escribe Valor en registro arquitectónico (o memoria para stores), libera entrada ROB. Si ¿Terminada?=n → stall hasta que sea 's'.
- **Excepciones/Especulación**: Si instrucción causa excepción, se marca en ROB; no se hace commit hasta que sea cabeza; entonces se vacía pipeline y salta a handler. Permite especulación en saltos (instrucciones tras salto predicho entran en ROB pero no hacen commit hasta que salto resuelto).
- **En el problema**: Rellenar tabla ROB **en el ciclo en que finaliza MUL.D** (i.e., termina su Escritura/CDB). Eso implica simular hasta ese ciclo y volcar estado de las 6 entradas.

> buffer de reordenamiento (ROB). El sistema dispone de un buffer de carga y un buffer de almacenamiento con 1 entrada.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[buffer-de-carga-en-tomasulo-especulativo]]
