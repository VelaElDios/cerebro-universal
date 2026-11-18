---
tipo: "receta"
titulo: "Planificación (scheduling) de bucle en VLIW con forwarding y delayed branch"
temas: ["ac", "pipeline", "vliw"]
claves: ["scheduling", "VLIW", "forwarding", "delay slot", "dependencias RAW", "latencias"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

Pasos para planificar el bucle original: 1) Listar instrucciones con sus tipos y dependencias (RAW). 2) Construir diagrama de precedencia considerando latencias: carga (MEM, 2 ciclos MEM) → uso en FP MUL/ADD (latencia EX 6/4) → almacenamiento (MEM). Enteros DADDUI (INT, 1 ciclo) actualizan punteros y contador. BNEZ (INT, 1 ciclo) con 1 delay slot: la instrucción inmediatamente posterior al salto en código original se coloca en el delay slot (aquí no hay instrucción explícita tras BNEZ, pero en VLIW se puede mover una instrucción independiente al slot). 3) Asignar instrucciones a ciclos y unidades en la tabla, explotando paralelismo: dos cargas iniciales en MEM1/MEM2 mismo ciclo; MUL.S en FP MUL (6 ciclos EX); mientras tanto, otras cargas/enteros en unidades libres; ADD.S en FP ADD (4 ciclos EX) tras MUL.S; stores tras resultados; enteros en INT1/INT2. 4) Calcular operaciones por ciclo = total instrucciones ejecutadas / ciclos del steady-state (o del kernel planificado). Justificar cuellos de botella (unidad FP MUL única con 6 ciclos, FP ADD única con 4 ciclos, dos MEM con 2 ciclos).

> As usual, assume that this processor supports forwarding and delayed branch (with 1 delay slot). Loop: L.S F1, 0(R1); L.S F2, 0(R2); MUL.S F4, F2, F1; S.S F4, 0(R1); L.S F3, 0(R3); ADD.S F5, F4, F3; S.S F5, 0(R3); DADDUI R1, R1, #4; DADDUI R2, R2, #4; DADDUI R3, R3, #4; DADDUI R4, R4, #-1; BNEZ R4, Loop
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]] · [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[desenrollamiento-de-bucle-3x-y-re-planificacion-en-vliw-para]] · [[codigo-del-bucle-vliw-para-planificacion-cargas-fp-mul-s-add]] · [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]]
