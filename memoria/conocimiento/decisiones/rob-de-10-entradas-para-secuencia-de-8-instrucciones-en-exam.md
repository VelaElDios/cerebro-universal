---
tipo: "decision"
titulo: "ROB de 10 entradas para secuencia de 8 instrucciones en examen"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB", "reorder buffer", "10 entradas", "estado emisión primera S.D"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

El ejercicio pide capturar el estado del ROB (10 entradas) exactamente en el ciclo donde se emite la primera S.D (instrucción 7). Esto implica que las 6 instrucciones previas (3 loads, 2 ADD.D, 1 MUL.D) ya han sido emitidas y ocupan entradas del ROB. La 7ª (S.D F8) se está emitiendo en ese ciclo. La 8ª (S.D F10) aún no. Cada entrada ROB registra: ocupada (S/N), instrucción, estado (emitida/ejecutando/escritura/terminada/commit), destino (registro o dirección memoria), valor (resultado o dirección calculada). Con especulación, los stores esperan en ROB hasta commit para escribir memoria.

> Indica en la siguiente tabla el estado del ROB (suponiendo que tiene 10 entradas) en el ciclo en el que la primera instrucción S.D es emitida.
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf`

Relacionado: [[buffer-de-carga-en-tomasulo-especulativo-pregunta-18]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]] · [[estado-rob-en-ciclo-de-emision-del-primer-s-d-tomasulo-espec]] · [[como-resolver-tabla-de-estado-en-tomasulo-con-rob-y-especula]] · [[como-simular-tomasulo-especulativo-con-rob-de-4-entradas-y-l]]
