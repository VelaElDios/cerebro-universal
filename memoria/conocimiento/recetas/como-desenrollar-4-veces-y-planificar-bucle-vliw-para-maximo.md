---
tipo: "receta"
titulo: "Cómo desenrollar 4 veces y planificar bucle VLIW para máximo aprovechamiento (examen enero 2023)"
temas: ["ac", "pipeline", "vliw"]
claves: ["loop unrolling", "VLIW scheduling", "static scheduling", "effectiveness", "desenrollamiento", "planificación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

Pasos para resolver el ejercicio 3b: 1) Identificar las latencias de cada unidad funcional (parte 3a). 2) Desenrollar el bucle 4 veces: replicar el cuerpo del bucle 4 veces, renombrando registros para evitar dependencias falsas (WAR/WAW) entre iteraciones (p.ej., usar F1_1, F2_1, F3_1, F4_1 para iteración 1; F1_2... para iteración 2, etc.). 3) Eliminar las instrucciones de control de bucle (DADDUI R4, BNEZ) de las 3 primeras iteraciones y dejar solo una al final. 4) Planificar estáticamente todas las instrucciones resultantes en las 4 ranuras (slots) de cada ciclo VLIW, respetando las latencias (RAW) y aprovechando que no hay restricciones de tipo de operación por slot. 5) Rellenar la tabla de instrucciones 1..N con las operaciones por slot y ciclo, minimizando NOPs.

> Unroll the program loop 4 times and then schedule it for the VLIW processor. Assume that the processor imposes no restrictions on the type of operations that can be issued, and the static scheduling is as aggressive and efficient as possible to optimize the resulting code as much as possible.
> — `repo:datos/temarios/AC/examenes/January2023.pdf`

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]] · [[desenrollamiento-de-bucle-3x-y-re-planificacion-en-vliw-para]] · [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]] · [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]]
