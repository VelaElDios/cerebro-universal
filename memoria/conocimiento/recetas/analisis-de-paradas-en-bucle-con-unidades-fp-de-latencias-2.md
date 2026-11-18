---
tipo: "receta"
titulo: "Análisis de paradas en bucle con unidades FP de latencias 2/3/5 y forwarding"
temas: ["ac", "desenrollado bucles", "pipeline", "punto flotante"]
claves: ["L.D", "MUL.D", "ADD.D", "DIV.D", "S.D", "latencias", "forwarding", "parada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollado bucles]] · [[pipeline]] · [[punto flotante]]

Pasos para calcular paradas (stalls) por iteración: 1) Dibujar diagrama de temporización (pipeline) con etapas IF, ID, EX (FP: 2/3/5 ciclos), MEM, WB. 2) Detectar dependencias RAW entre instrucciones consecutivas (ej. L.D → MUL.D, MUL.D → ADD.D, ADD.D → DIV.D, DIV.D → S.D). 3) Aplicar forwarding: resultado disponible al final de EX, usable en siguiente ciclo en EX de instrucción dependiente. 4) Calcular ciclos de espera = latencia - 1 (si forwarding completo). 5) Sumar paradas totales y obtener CPI = (ciclos útiles + paradas) / instrucciones por iteración. 6) Desenrollar bucle mínimo para ocultar latencias: replicar cuerpo, renombrar registros, planificar instrucciones de distintas iteraciones en huecos. 7) Verificar que no queden paradas y recalcular CPI.

> The processor exhibits the usual characteristics: a value can be written and read from a register in the same clock cycle, dependences are detected and solved in the ID stage, operand forwarding is supported, branches are completely solved in the ID stage, the integer functional unit requires 1 cycle, and the execution step of L.D and S.D requires 1 cycle. Functional units for floating-point addition, multiplication, and division are fully pipelined, and require, respectively, 2, 3, and 5 cycles.
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]]
