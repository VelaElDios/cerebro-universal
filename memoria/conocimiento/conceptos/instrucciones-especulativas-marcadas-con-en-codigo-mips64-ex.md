---
tipo: "concepto"
titulo: "Instrucciones especulativas marcadas con * en código MIPS64 (examen June 2025)"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["speculative instructions", "L.D*", "ADD.D*", "BNEZ", "branch prediction"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

En el fragmento de código del examen, las instrucciones marcadas con asterisco (L.D* F2,0(R2) y ADD.D* F6,F0,F2) son las que el procesador ejecuta de forma especulativa tras predecir el salto BNEZ R1,jump. Si la predicción es correcta (salto tomado cuando R1≠0), sus resultados se confirman; si es incorrecta (no salto cuando R1=0), se descartan y se ejecutan las instrucciones del camino no especulativo (ADD.D F6,F0,F4). Esta marcación explícita permite al alumno identificar qué instrucciones llevan bits venenosos en planificación estática o entran en ROB/estaciones de reserva en Tomasulo con especulación.

> Instructions marked with * are speculative.
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[planificacion-estatica-con-bits-venenosos-convencion-dirty-p]] · [[instrucciones-especulativas-marcadas-con-asterisco-en-codigo]] · [[especulacion-estatica-con-cargas-especulativas-lw-en-mips64]] · [[especulacion-estatica-con-poison-bits-en-mips64-lw]]
