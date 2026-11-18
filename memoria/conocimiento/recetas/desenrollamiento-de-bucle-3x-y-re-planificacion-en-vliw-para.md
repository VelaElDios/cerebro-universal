---
tipo: "receta"
titulo: "Desenrollamiento de bucle 3x y re-planificación en VLIW para aumentar operaciones por ciclo"
temas: ["ac", "pipeline", "vliw"]
claves: ["loop unrolling", "desenrollamiento", "scheduling", "operaciones por ciclo", "ILP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

Procedimiento: 1) Replicar el cuerpo del bucle 3 veces, renombrando registros para evitar dependencias falsas (WAR/WAW) entre iteraciones (p.ej., usar F1,F2,F4,F3,F5 para iteración 1; F6,F7,F8,F9,F10 para iteración 2; etc., o rotar registros). Ajustar los DADDUI: los incrementos de punteros (R1,R2,R3) y decremento de contador (R4) se hacen una sola vez por cada 3 iteraciones originales (sumar 12 a punteros, restar 3 a R4). 2) Planificar el bucle desenrollado (ahora con ~3*11 - overhead instrucciones) en la misma tabla VLIW. 3) El desenrollamiento expone más paralelismo a nivel de instrucción (ILP): permite rellenar huecos de latencia de FP MUL (6 ciclos) y FP ADD (4 ciclos) con instrucciones de otras iteraciones, saturando mejor las 6 unidades. 4) Calcular operaciones por ciclo = instrucciones útiles del kernel desenrollado / ciclos del kernel. Justificar mejora: reducción de overhead de salto, mejor ocupación de unidades FP y MEM, amortización de latencias.

> Unroll the original loop three times and then schedule it again for the same VLIW processor (use as many rows as necessary in the table below). How many operations per cycle are reached now? Justify the solution.
> — `repo:datos/temarios/AC/examenes/January2019.pdf`

Relacionado: [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]] · [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]]
