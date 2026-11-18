---
tipo: "receta"
titulo: "Configuración superscalar 4-issue para diagramas de pipeline (examen AC enero 2022)"
temas: ["ac", "pipeline", "superscalar"]
claves: ["4-way", "superscalar", "decode", "execute", "write", "functional units", "in-order", "out-of-order", "renaming"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Parámetros fijos para los tres apartados del Ejercicio 3:
- Ancho de issue/decoder: 4 instrucciones/ciclo (cualquier tipo)
- Unidades funcionales: 5 (F1..F5), cada una 1 ciclo de ejecución
- Pipeline: 3 etapas fijas (Decode 1c, Execute 1c, Write 1c)
- Forwarding: resultado disponible para consumidores en el ciclo **siguiente** al Write (no en el mismo ciclo)
- Código de 7 instrucciones con dependencias:
  I1: LW      R1, 0(R2)
  I2: DADD R4, R1, R3        # RAW con I1 (R1)
  I3: DSUB R6, R7, R8
  I4: LW      R3, 0(R9)
  I5: DSUB R10, R10, R12
  I6: DADD R8, R8, R1        # RAW con I1 (R1), WAW con I3 (R8)
  I7: DSUB R3, R3, R1        # RAW con I4 (R3) e I1 (R1), WAW con I4 (R3)
- Tres modelos a dibujar en tablas ciclo a ciclo (Decode / Execute / Write, máx 4/5/4):
  a) In-order execution + in-order write
  b) Out-of-order execution, **sin renombrado**, in-order write
  c) Out-of-order execution, **con renombrado** (registros ilimitados), out-of-order write

> Consider a 4-way superscalar processor capable of issuing four instructions of any type per cycle, with five functional units (F1, F2, F3, F4, and F5). Assume that instructions require one cycle for the decode stage, one cycle for the execute stage and one cycle for the write stage. The result of an instruction is available to other instructions at the next cycle in which that result is written.
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
