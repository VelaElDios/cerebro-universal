---
tipo: "receta"
titulo: "Algoritmo de Marcador (Scoreboard): pasos de simulación para ejercicios"
temas: ["ac", "planificacion-dinamica", "punto-flotante", "scoreboard"]
claves: ["emisión", "lectura operandos", "ejecución", "escritura resultado", "FU status", "registro status", "WAW RAW WAR"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[planificacion-dinamica]] · [[punto-flotante]] · [[scoreboard]]

Diferencias clave vs Tomasulo (Ej. 16a):
- **Sin renombrado de registros**: Riesgos WAW y WAR *sí* detienen emisión (stall).
- **Control centralizado**: Tabla *Functional Unit Status* (Busy, Op, Fi, Fj, Fk, Qj, Qk, Rj, Rk) y *Register Result Status* (Qi por registro).
- **Cuatro fases por instrucción** (en orden, pueden solaparse entre instrucciones distintas):
  1. **Emisión (Issue)**: Si FU libre *y* no hay WAW (Qi[Fi]==0) → ocupa FU, pone Qi[Fi]=FU, copia Qj=Qi[Fj], Qk=Qi[Fk], Rj=Rk=Yes si Q==0.
  2. **Lectura operandos (Read Operands)**: Cuando Qj=Qk=0 (operandos listos en registros) → lee valores, pone Rj=Rk=No. **Espera aquí si hay RAW**.
  3. **Ejecución (Execution)**: Tras leer operandos, empieza en siguiente ciclo. Latencia fija por FU. Al terminar → avisa a control.
  4. **Escritura resultado (Write Result)**: Si no hay WAR (ninguna instrucción *pendiente de leer* ese registro, i.e., ∃ otra instr con Qj==FU o Qk==FU para ese registro) → escribe en registro, pone Qi[registro]=0, avisa a FUs esperando (Qj/Qk→0, Rj/Rk→Yes). Si hay WAR → espera.
- **Prioridad escritura**: Si varias FU terminan mismo ciclo, elige una (suelen dar prioridad a la más antigua).
- **Liberación FU**: Tras Write Result → FU libre en siguiente ciclo.
Tabla de control: Ciclo | Instrucción | Fase completada | Estado FU / Registros.

> Detalla la ejecución del código que se muestra en la tabla cuando se ejecuta según el algoritmo de Marcador. Para ello, indica en la tabla siguiente los pasos realizados en la ejecución y el número de ciclo en el que se completa cada paso.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[algoritmo-de-tomasulo-reglas-de-simulacion-para-ejercicios-d]] · [[simulacion-scoreboard-vs-tomasulo-basico-pasos-de-ejecucion]] · [[pasos-de-ejecucion-en-el-algoritmo-del-marcador-scoreboard]] · [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]]
