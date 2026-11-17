---
tipo: "receta"
titulo: "Algoritmo de Tomasulo: reglas de simulación para ejercicios de examen"
temas: ["ac", "planificacion-dinamica", "punto-flotante", "tomasulo"]
claves: ["estaciones de reserva", "BDC", "emisión", "ejecución", "escritura resultado", "Qj Qk Vj Vk", "buffer carga almacenamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[planificacion-dinamica]] · [[punto-flotante]] · [[tomasulo]]

Reglas críticas para simular a mano en examen (Ej. 14, 16):
1. **Emisión (Issue)**: En orden de programa. Si hay estación de reserva libre *y* buffer de carga/almacenamiento libre (para fld/fsd), se emite. Se renombra registro destino → etiqueta de estación (Qi). Se copian operandos disponibles (Vj, Vk) o se ponen etiquetas productoras (Qj, Qk).
2. **Ejecución (Execute)**: Empieza cuando *ambos* operandos están listos (Qj=Qk=0) *y* UF libre. **Regla clave**: si el operando llega por BDC en ciclo T, la ejecución empieza en T+1 (no mismo ciclo). Latencia fija por UF (suma 2, mul 4, etc.). Para fld/fsd: ejecución = cálculo dirección + acceso memoria (2 ciclos en ej. 14).
3. **Escritura resultado (Write Result)**: Al terminar latencia, se pone en BDC si libre. **Regla clave**: solo 1 escritura por ciclo en BDC. Prioridad: suele ser por orden de llegada a "listo para escribir" o por tipo UF (ej. carga antes que FP). Al escribir: broadcast valor + etiqueta → actualiza Vj/Vk y pone Qj/Qk=0 en *todas* estaciones y buffers que esperaban esa etiqueta. Libera estación/buffer.
4. **Buffers de carga/almacenamiento**: Tratados como estaciones de reserva dedicadas. fld: emite a buffer carga, ejecuta (2 ciclos), escribe en BDC. fsd: emite a buffer almacenamiento, espera dato (Qk) y dirección (Qj), cuando ambos listos escribe memoria (no usa BDC para dato, pero ocupa buffer).
5. **Liberación de recursos**: Estación/buffer/U.F. liberados en ciclo T → disponibles en T+1.
Tabla de estado típica: Instrucción | Emisión | Inicio Ejecución | Fin Ejecución | Escritura BDC.

> En el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que esté esperando ese dato. Un recurso que se libera en un ciclo no se puede usar hasta el ciclo siguiente. La etapa de ejecución de fld y fsd consume 2 ciclos de reloj.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf` (cita sin comprobar)

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]]
