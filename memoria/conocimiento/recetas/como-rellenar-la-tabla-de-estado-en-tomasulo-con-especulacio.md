---
tipo: "receta"
titulo: "Cómo rellenar la tabla de estado en Tomasulo con especulación y ROB"
temas: ["ac", "rob", "speculation", "tomasulo"]
claves: ["Tomasulo especulativo", "Reorder Buffer (ROB)", "commit", "speculative execution", "branch prediction"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[rob]] · [[speculation]] · [[tomasulo]]

Diferencias clave al añadir ROB de 6 entradas (misma UF, mismas estaciones/buffers):
1. **Issue**: igual que sin especulación, pero además se asigna una entrada en el ROB (orden de programa). La instrucción entra en estado "issued".
2. **Execution**: igual, pero los resultados no se escriben en registros arquitectónicos ni memoria; se guardan en la entrada del ROB (y se difunden por CDB para dependencias RAW).
3. **Write result**: ahora significa "completar ejecución y escribir resultado en el ROB + broadcast por CDB". La instrucción pasa a estado "completed" en el ROB.
4. **Commit (nueva columna)**: la instrucción sale del ROB en orden de programa (head del ROB) cuando:
   - Está en estado "completed".
   - Todas las instrucciones anteriores ya han hecho commit.
   - Para saltos: la predicción fue correcta (si no, flush del ROB y recuperación).
   - Para stores: la dirección y el dato están listos; se escribe en memoria/caché en el commit.
   - Para cargas especulativas: si hubo fallo de página/protección, se marca bit venenoso en el ROB; la excepción se lanza en el commit.
Restricción: el ROB de 6 entradas limita cuántas instrucciones pueden estar "en vuelo" (issued pero no committed). Si el ROB está lleno, Issue se detiene (riesgo estructural nuevo).

> We perform an improvement in the processor, so that it now supports the speculative version of the Tomasulo's algorithm. A 6-entry ROB is added. FU were not changed, and the number of reservation stations and load buffers is maintained the same as before.
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[buffer-de-carga-en-tomasulo-especulativo]] · [[comparativa-tomasulo-vs-marcador-scoreboard]]
