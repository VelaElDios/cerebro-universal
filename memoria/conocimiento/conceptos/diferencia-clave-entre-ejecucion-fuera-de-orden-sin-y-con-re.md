---
tipo: "concepto"
titulo: "Diferencia clave entre ejecución fuera de orden sin y con renombramiento"
temas: ["ac", "pipeline", "superscalar"]
claves: ["renombramiento de registros", "WAR", "WAW", "ROB", "estaciones de reserva", "registro físico vs arquitectónico"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

**Sin renombramiento (OOO issue/exec, registros arquitectónicos únicos)**:
- Los registros destino son los arquitectónicos (R1-R31).
- **WAW (Write After Write)**: Dos instrucciones escriben mismo registro → la segunda no puede emitir/ejecutar hasta que la primera haya escrito (commit) para no perder el valor correcto. Frena pipeline.
- **WAR (Write After Read)**: Instrucción posterior escribe registro que instrucción anterior aún no ha leído → la posterior debe esperar a que la anterior lea (en ID o via forwarding). Frena pipeline.
- **RAW**: Se resuelve con forwarding/esperar dato.
- Commit en orden (ROB o similar) para mantener estado arquitectónico preciso.
- En el examen: WAW en R5 (instr 4 y 7) y R8 (instr 3 y 6); WAR en R5 (instr 2 lee, 4 escribe) y R8 (instr 3 lee, 6 escribe). Estas dependencias de nombre obligan a serializar casi todo.

**Con renombramiento (OOO issue/exec/commit, mapeo arquitectónico→físico)**:
- Cada escritura asigna nuevo registro físico. Elimina WAW y WAR completamente.
- Solo RAW verdaderas (dependencias de datos) limitan paralelismo.
- Tabla de mapeo (RAT) + lista de libres + ROB para commit en orden y recuperación ante fallos.
- En el examen: solo RAW en R2 (1→2,6,7), R5 nuevo (4→7), R8 viejo (3→6). Permite gran solapamiento: cargas y aritméticas en paralelo, dos DADD/DSUB simultáneos si UF disponibles.

> b) Ejecución fuera de orden, sin capacidad de renombramiento. c) Ejecución fuera de orden, con capacidad de renombramiento.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffer-de-carga-en-tomasulo-especulativo]] · [[diferencias-entre-ejecucion-en-orden-fuera-de-orden-sin-reno]] · [[diferencias-clave-entre-los-tres-modelos-de-ejecucion-supers]] · [[diagrama-pipeline-superscalar-ejecucion-fuera-de-orden-con-r]]
