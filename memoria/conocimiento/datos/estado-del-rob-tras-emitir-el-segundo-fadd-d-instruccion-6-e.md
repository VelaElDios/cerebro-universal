---
tipo: "dato"
titulo: "Estado del ROB tras emitir el segundo fadd.d (instrucción 6) en Problema 2"
temas: ["ac", "reorder-buffer", "rob", "snapshot", "tomasulo"]
claves: ["ROB 6 entradas", "fld f0", "fld f2", "fadd.d f4", "fsub.d f10", "fmul.d f16", "fadd.d f18", "fsd f16"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[reorder-buffer]] · [[rob]] · [[snapshot]] · [[tomasulo]]

En el ciclo en que se emite 'fadd.d f18, f4, f10' (6ª instrucción), el ROB tiene 6 entradas ocupadas (0 a 5). Entrada 0: fld f0, 1: fld f2, 2: fadd.d f4, 3: fsub.d f10, 4: fmul.d f16, 5: fadd.d f18. Estado: todas en 'Emisión' o 'Ejecutando' según hayan pasado ciclos. Destino: registro destino (f0, f2, f4, f10, f16, f18). Valor: aún no calculado (pendiente). La 7ª instrucción (fsd) aún no emitida.

> Completa la siguiente tabla para mostrar el contenido del buffer de reordenamiento (ROB) justo al finalizar el ciclo de emisión del segundo fadd.d.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[buffer-de-carga-en-tomasulo-especulativo-pregunta-18]] · [[rob-de-10-entradas-para-secuencia-de-8-instrucciones-en-exam]] · [[estado-rob-en-ciclo-de-emision-del-primer-s-d-tomasulo-espec]] · [[como-resolver-tabla-de-estado-en-tomasulo-con-rob-y-especula]]
