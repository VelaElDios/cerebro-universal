---
tipo: "concepto"
titulo: "Salto retardado (delayed branch) en RISC-V: implicaciones en planificación"
temas: ["ac", "control-hazard", "delayed-branch", "pipeline", "riscv"]
claves: ["delay slot", "bne", "salto retardado", "instrucción en delay slot", "planificación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[control-hazard]] · [[delayed-branch]] · [[pipeline]] · [[riscv]]

Regla en todos los ejercicios: **La instrucción inmediatamente posterior a la instrucción de salto (bne, beq, etc.) se ejecuta *siempre*, independientemente de si el salto se toma o no.** Esa posición se llama *delay slot*.
Consecuencias para ejercicios:
1. **En diagrama de pipeline**: El branch resuelve en ID. La instrucción en delay slot ya está en IF/ID. No hay burbuja de control *si* el delay slot se llena con instrucción útil.
2. **En segmentación software / desenrollado**: El delay slot es una oportunidad gratis. Se coloca una instrucción que *deba ejecutarse* tanto en camino taken como not-taken (ej. una instrucción de la siguiente iteración, o una operación independiente).
3. **En start-up / finish-up**: El código debe respetar la semántica del delay slot. Al salir del bucle (última iteración, salto no tomado), la instrucción en delay slot *todavía se ejecuta*. Por tanto, finish-up debe compensar si esa instrucción no debía ejecutarse en la iteración extra.
4. **En cálculo de CPI**: El branch "cuesta" 0 ciclos extra si el delay slot está lleno de trabajo útil; 1 ciclo (burbuja) si hay que meter NOP.
5. **En Tomasulo/Scoreboard**: El branch es una instrucción más que compite por recursos; su resolución en ID libera fetch siguiente.

> Sabiendo que se usa salto retardado y adelantamiento" / "se aplica salto retardado" / "hacemos uso del salto retardado" / "Soporta la técnica de salto retardado
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf` (cita sin comprobar)

Relacionado: [[parametros-estandar-para-ejercicios-de-segmentacion-software]] · [[desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e]] · [[saltos-retardados-delayed-branches-en-planificacion-estatica]] · [[uso-de-ranura-de-retardo-de-1-ciclo-en-superescalar-para-ocu]]
