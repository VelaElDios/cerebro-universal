---
tipo: "receta"
titulo: "Planificación en superescalar 3-vías (entero/salto, memoria, FP) con ranura de retardo"
temas: ["ac", "loop unrolling", "pipeline", "scheduling", "superscalar"]
claves: ["3-way superscalar", "issue slots", "integer/branch", "memory", "floating-point", "ADD.D latency 2", "MUL.D latency 4", "delayed branch 1 slot", "forwarding"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop unrolling]] · [[pipeline]] · [[scheduling]] · [[superscalar]]

Restricciones del procesador:
- **Ancho de emisión**: 3 instrucciones/ciclo máx, una por tubería: Entero/Salto, Memoria, Punto Flotante.
- **Latencias FP**: ADD.D = 2 ciclos ejecución, MUL.D = 4 ciclos ejecución. (DIV.D no aparece en este ejercicio, pero en el anterior sí).
- **Forwarding**: resultados FP disponibles para instrucciones posteriores tras finalizar ejecución (sin esperar write-back).
- **Ranura de retardo (delay slot) = 1**: la instrucción inmediatamente después de un salto se ejecuta siempre, independientemente de si el salto se toma o no. El compilador debe rellenarla con instrucción útil o NOP.
- **Riesgos**: RAW resueltos por forwarding; WAW/WAR en FP evitados si hay renombrado (no se especifica, asumir que no hay renombrado en registros FP → hay que respetar dependencias de nombre).
- **Bucle del Ejercicio 1** (no mostrado en este trozo, pero referenciado): hay que planificarlo reordenando instrucciones sin cambiar semántica.
Pasos para planificar:
1. Identificar dependencias (RAW, WAW, WAR) entre instrucciones del bucle.
2. Asignar cada instrucción a su tubería (Entero: BEQZ, DADDUI, J; Memoria: L.D, S.D; FP: ADD.D, MUL.D, DIV.D, SUB.D).
3. Construir diagrama de precedencia con latencias.
4. Rellenar ciclos: en cada ciclo, meter hasta 1 instrucción por tubería respetando dependencias y latencias (con forwarding, consumidor puede emitirse en el ciclo siguiente al final de ejecución del productor si misma tubería, o mismo ciclo si tubería distinta y forwarding cruza).
5. Para el salto de fin de bucle (BEQZ/BNEZ), colocar instrucción útil en delay slot (ej. primera instrucción de la siguiente iteración o instrucción de restauración).
6. Calcular CPI = ciclos totales / instrucciones útiles.
**Desenrollado (unroll) 2 iteraciones**: replicar cuerpo del bucle 2 veces, renombrar registros para evitar WAW/WAR falsos, eliminar salto de la 1ª iteración (o convertir en salto condicional al final del 2º cuerpo), y planificar el bloque resultante como código lineal. Esto aumenta ILP y permite ocultar latencias.

> Assume that we have a 3-way superscalar processor capable of issuing an integer instruction (including branches), a memory instruction, and a floating-point instruction per clock cycle. Consider that the execution step of ADD.D and MUL.D takes, respectively, 2 and 4 clock cycles. As usual, assume that this processor supports forwarding and delayed branch (with 1 delay slot).
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]] · [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]] · [[desenrollado-de-bucle-8-veces-para-superscalar-con-latencias]] · [[problema-de-desenrollado-y-planificacion-de-bucle-superescal]] · [[como-desenrollar-8x-y-planificar-en-superescalar-4-issue-2-i]]
