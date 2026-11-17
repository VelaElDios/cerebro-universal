---
tipo: "receta"
titulo: "Cómo leer la evolución ciclo a ciclo de un marcador con cargas y operaciones FP"
temas: ["ac", "arquitectura", "punto-flotante", "scoreboard", "simulacion"]
claves: ["fld", "fmul.d", "fsub.d", "fdiv.d", "fadd.d", "ciclo", "emisión", "lectura operandos", "escritura resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[punto-flotante]] · [[scoreboard]] · [[simulacion]]

Pasos para interpretar la tabla ciclo a ciclo:

1. **Identificar la instrucción emitida en cada ciclo** (columna Emisión). En el ejemplo:
   - Ciclo 1: `fld f6, 34(x2)` → UF Entera (carga)
   - Ciclo 5: `fld f2, 45(x3)` → UF Entera
   - Ciclo 6: `fmul.d f0, f2, f4` → UF Mult1 (espera f2 de UF 1 → Qj=1)
   - Ciclo 7: `fsub.d f8, f6, f2` → UF Suma (espera f6 y f2 de UF 1 → Qj=1, Qk=1)
   - Ciclo 8: `fdiv.d f10, f0, f6` → UF Divide (espera f0 de UF 2 y f6 de UF 1 → Qj=2, Qk=1)

2. **Ver la lectura de operandos** (columna Lectura Operandos): ocurre cuando Rj=Rk=SI. En ciclo 6, `fmul.d` lee f2 (Rj=SI) porque la carga terminó en ciclo 4 y el registro está listo. En ciclo 8b, `fmul.d` y `fsub.d` pasan a Rj=Rk=SI.

3. **Seguir la ejecución** (columna Ejecución completa): cada UF tiene latencia distinta. Mult1 tarda 3 ciclos (emite en 6, completa en 9). Suma tarda 2 ciclos (emite en 7, completa en 9). Divide no completa en el rango mostrado.

4. **Escritura resultado** (columna Escritura resultado): solo ocurre si no hay riesgo WAW/WAR. `fadd.d` se bloquea en ciclo 9 («Bloqueada») porque su destino f6 es leído por `fsub.d` y `fdiv.d` (riesgo WAR) y también escrito por la primera `fld` (riesgo WAW si no se renombra).

> ciclo 6 Instrucción Emisión Operandos completa resultado fld f6, 34(x2) 1 2 3 4 fld f2, 45(x3) 5 6 fmul.d f0, f2, f4 6
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]] · [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
