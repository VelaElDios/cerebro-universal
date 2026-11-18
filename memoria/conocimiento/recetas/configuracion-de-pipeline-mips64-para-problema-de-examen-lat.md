---
tipo: "receta"
titulo: "Configuración de pipeline MIPS64 para problema de examen (latencias FP, salto retardado, forwarding)"
temas: ["ac", "forwarding", "latencias", "mips64", "pipeline", "salto-retardado"]
claves: ["MIPS64", "L.S", "S.S", "ADD.S", "MUL.S", "latencia 2", "latencia 4", "salto retardado", "forwarding", "detección ID", "riesgo estructural MEM", "riesgo estructural WB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[forwarding]] · [[latencias]] · [[mips64]] · [[pipeline]] · [[salto-retardado]]

Parámetros clave para resolver el Problema 1: pipeline MIPS64 de 5 etapas (IF, ID, EX, MEM, WB) con forwarding completo, detección de riesgos en ID, salto resuelto en ID con **un slot de retardo** (la instrucción tras BNE se ejecuta siempre). Latencias de EX: FP add/sub = 2 ciclos (segmentada), FP mul = 4 ciclos (segmentada), L.S/S.S EX = 1 ciclo, entero = 1 ciclo. Riesgo estructural en MEM si dos accesos memoria simultáneos; en WB si dos escrituras al mismo banco (entero o FP). El bucle procesa un vector de simple precisión (4 bytes/elemento): S0 inicializa R4=R1+48 (12 elementos), S1 carga, S2 suma, S3 multiplica, S4 almacena, S5/S6 incrementan punteros, S8 BNE.

> Las características del computador empleado son: • Un dato se puede escribir y leer de un registro en el mismo ciclo de reloj • Se usa adelantamiento de operandos • Todas las dependencias se detectan y se resuelven en la etapa ID • Los saltos se resuelven completamente en la etapa ID. Se aplica salto retardado • La fase de ejecución de las instrucciones L.D y S.D requiere 1 ciclo • Todas las unidades funcionales (UF) están segmentadas • La UF para la Suma/Resta en PF emplea 2 ciclos, la UF para multiplicación en PF usa 4 ciclos y el resto de las UF emplean 1 ciclo. • Sólo hay riesgo estructural en la etapa MEM si se trata de dos instrucciones de acceso a memoria • Sólo hay riesgo estructura en la etapa WB si las dos instrucciones intentan escribir en el mismo banco de registros (entero o en punto flotante)
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]]
