---
tipo: "receta"
titulo: "Parámetros estándar para ejercicios de segmentación software en RISC-V (Tema 3)"
temas: ["ac", "pipeline", "riscv", "software-pipelining"]
claves: ["adelantamiento", "salto retardado", "IF ID EX MEM WB", "fld fsd fmul.d fadd.d fdiv.d", "latencia FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[pipeline]] · [[riscv]] · [[software-pipelining]]

Configuración base asumida en la mayoría de ejercicios del temario:
- Pipeline 5 etapas: IF, ID, EX, MEM, WB (1 ciclo cada una salvo EX de FP).
- Adelantamiento (forwarding) completo entre etapas EX/MEM/WB → ID/EX.
- Lectura/escritura de registro en mismo ciclo (WB escribe en flanco subida, ID lee en flanco bajada).
- Salto retardado (delayed branch): la instrucción en el *delay slot* (siguiente al branch) se ejecuta siempre.
- Resolución de salto en ID (comparación y cálculo de target).
- Unidades funcionales FP segmentadas (pipelined) con latencias variables:
  * Suma/resta FP: 2-4 ciclos (según ejercicio).
  * Multiplicación FP: 3-5 ciclos.
  * División FP: 4-7 ciclos.
  * Carga/almacenamiento FP (fld/fsd): EX toma 1-2 ciclos.
- Sin riesgos estructurales en MEM/WB entre instrucciones aritméticas y carga/salto (salvo ejercicio 12 que lo menciona explícito).
- Dependencias se detectan en ID.
Pasos típicos para resolver:
1. Identificar dependencias RAW, WAR, WAW dentro de la iteración y entre iteraciones (loop-carried).
2. Dibujar diagrama de espacio-tiempo (pipeline timing) para ver burbujas (stalls).
3. Calcular CPI = ciclos_totales / instrucciones_útiles (o ciclos/iteración en estado estacionario).
4. Aplicar segmentación software: reordenar instrucciones, insertar *start-up* (prologo) y *finish-up* (epilogo) para llenar huecos.
5. Si no basta, desenrollar bucle (loop unrolling) N veces y volver a planificar.
6. Verificar que el código transformado produce mismos resultados (mismas direcciones, mismos registros finales).

> El procesador segmentado usa para la ejecución del Código las características típicas: es posible escribir y leer a/desde un registro en el mismo ciclo de reloj, hay adelantamiento de operandos, los saltos se resuelven en la etapa ID, se aplica salto retardado, etc.
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf`

Relacionado: [[desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e]] · [[segmentacion-software-software-pipelining-para-bucle-conteo]] · [[salto-retardado-delayed-branch-en-risc-v-implicaciones-en-pl]]
