---
tipo: "receta"
titulo: "Cómo leer la tabla de estado de instrucciones en el marcador de Tomasulo"
temas: ["ac", "estado-instrucciones", "pipeline", "scoreboard", "tomasulo"]
claves: ["Emisión", "Lectura Operandos", "Ejecución completa", "Escritura resultado", "ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[estado-instrucciones]] · [[pipeline]] · [[scoreboard]] · [[tomasulo]]

La tabla muestra para cada instrucción el ciclo en que ocurre cada fase: Emisión (se asigna UF y se renombra destino), Lectura Operandos (espera a Qj=Qk=0), Ejecución completa (fin de cómputo en UF), Escritura resultado (broadcast en CDB y actualización de registro destino). Una instrucción "Bloqueada" (como fadd.d en ciclo 10) no ha podido emitirse por peligro estructural (UF ocupada) o WAW (registro destino ya reservado por otra instrucción en vuelo).

> Estado de las instrucciones                                                                              Lectura           Ejecución    Escritura   ciclo 10                     Instrucción               Emisión              Operandos         completa     resultado
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]] · [[como-leer-la-tabla-de-estado-de-instrucciones-en-simulacion]] · [[como-rellenar-la-tabla-de-estado-de-instrucciones-en-tomasul]] · [[pasos-para-rellenar-tabla-de-estado-de-instrucciones-emision]]
