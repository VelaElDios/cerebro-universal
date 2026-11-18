---
tipo: "decision"
titulo: "Bloqueo de fadd.d por peligro WAW en registro f6 hasta ciclo 13"
temas: ["ac", "bloqueo-emision", "peligros", "scoreboard", "tomasulo", "waw"]
claves: ["fadd.d", "f6", "WAW", "bloqueada", "ciclo 13", "emisión"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bloqueo-emision]] · [[peligros]] · [[scoreboard]] · [[tomasulo]] · [[waw]]

La instrucción fadd.d f6, f8, f2 no puede emitirse en los ciclos 10-12 porque el registro destino f6 ya está reservado como destino de la fld f6, 34(x2) (que escribe en ciclo 4) y luego será destino de la propia fadd.d. En el marcador clásico sin renombrado completo, la emisión se bloquea hasta que la instrucción previa que escribe f6 (la carga) ha escrito su resultado y el registro está libre para ser renombrado. En ciclo 13, tras completarse la escritura de la carga, fadd.d emite y procede a leer operandos en ciclo 14 (esperando a que f8 esté listo tras fsub.d que escribe en ciclo 12).

> Bloqueada              fadd.d     f6, f8, f2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]] · [[como-leer-la-tabla-de-estado-de-instrucciones-en-el-marcador]] · [[deteccion-de-riesgos-war-y-waw-en-marcador-y-bloqueo-de-escr]] · [[deteccion-y-resolucion-de-riesgo-war-en-el-marcador-ciclos-1]] · [[marcador-scoreboard-distingue-riesgos-raw-y-war-con-detencio]]
