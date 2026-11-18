---
tipo: "concepto"
titulo: "Dependencias en bucles RISC-V: clasificación intra-iteración vs loop-carried"
temas: ["ac", "dependencias-datos", "pipeline", "riscv"]
claves: ["RAW WAR WAW", "dependencia de datos antidependencia dependencia de salida", "loop-carried", "distancia"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias-datos]] · [[pipeline]] · [[riscv]]

Tipología que piden identificar en *todos* los ejercicios de bucles (Ej. 11, 12, 13, 15, 17, 18):
1. **Dependencia de datos (RAW / True)**: Instr A escribe registro/memoria que B lee.
   - *Intra-iteración*: misma iteración (ej. I1 fld f0 → I3 fmul f0).
   - *Loop-carried*: A en iteración i, B en iteración i+1 (ej. I6 addi x1 → I1 fld 0(x1) siguiente iteración). Distancia = 1 normalmente.
2. **Antidependencia (WAR)**: A lee registro que B escribe después.
   - Común en registros de índice (x1, x2, x3) actualizados al final del bucle y usados al principio.
   - Ej: I1 fld f0, 0(x1) lee x1; I6 addi x1, x1, 8 escribe x1 (siguiente iteración o misma).
3. **Dependencia de salida (WAW)**: A y B escriben mismo registro/memoria.
   - Ej: I5 fsd f4, 0(x1) escribe memoria; I1 fld 0(x1) siguiente iteración lee misma dirección → RAW memoria, pero WAW si dos stores a misma dir.
   - En registros: I3 fmul f4, f0, f2 escribe f4; I3 siguiente iteración vuelve a escribir f4 → WAW en f4 (distancia 1).
Clave: Con renombrado (Tomasulo) WAW/WAR se eliminan; en pipeline estático / Scoreboard causan stalls.

> Indica las dependencias de datos, antidependencias y dependencias de salida. Indica si son entre iteraciones.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[parametros-estandar-para-ejercicios-de-segmentacion-software]] · [[tipos-de-dependencias-en-bucles-loop-independent-vs-loop-car]] · [[identificacion-de-dependencias-loop-carried-en-bucles-c-styl]] · [[analisis-de-dependencias-en-codigo-risc-v-raw-war-waw]]
