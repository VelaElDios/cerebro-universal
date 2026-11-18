---
tipo: "receta"
titulo: "Planificación VLIW de bucle con 6 unidades funcionales (examen Enero 2017)"
temas: ["ac", "planificacion", "software-pipelining", "vliw"]
claves: ["VLIW", "INT", "MEM", "FP ADD", "FP MUL", "latencia", "slot", "BNEZ", "delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[planificacion]] · [[software-pipelining]] · [[vliw]]

Especificación completa para resolver a mano o con herramienta:
- Unidades y latencias:
  * INT1, INT2: ALU enteras + salto, latencia 1.
  * MEM1, MEM2: load/store segmentados, latencia 3.
  * FP ADD: suma FP segmentada, latencia 4.
  * FP MUL: multiplicación FP segmentada, latencia 4.
- Procesador implementa adelantamiento (forwarding) y salto retardado (delayed branch) con un hueco (delay slot).
- Bucle (12 instrucciones):
  Loop: L.S    F1, 0(R1)
        L.S    F2, 0(R2)
        MUL.S F4, F2, F1
        S.S    F4, 0(R1)
        L.S    F3, 0(R3)
        ADD.S F5, F4, F3
        S.S    F5, 0(R3)
        DADDUI R1, R1, #4
        DADDUI R2, R2, #4
        DADDUI R3, R3, #4
        DADDUI R4, R4, #-1
        BNEZ   R4, Loop
- Tarea a): Rellenar tabla de planificación por ciclos (columnas: INT1, INT2, MEM1, MEM2, FP ADD, FP MUL) mostrando qué instrucción ocupa cada unidad en cada ciclo. No necesariamente todas las filas.
- Tarea b): Calcular operaciones por ciclo (throughput) conseguido.
- Dependencias clave: MUL.S usa F1,F2 de loads; S.S usa F4 de MUL.S; ADD.S usa F4 y F3; S.S usa F5; DADDUI actualizan punteros; BNEZ depende de R4.

> El siguiente programa se ejecuta en un procesador VLIW con 6 unidades de ejecución: 2 unidades enteras (para operaciones ALU enteras y de salto), con una latencia de 1 ciclo; 2 unidades de memoria completamente segmentadas (para loads y stores), con una latencia de 3 ciclos; 2 unidades de punto flotante completamente segmentadas (una para suma y otra para multiplicación), con una latencia de 4 ciclos
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf` (cita sin comprobar)

Relacionado: [[benchmarks-sinteticos-dhrystone-y-whetstone-proposito-y-orig]] · [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]] · [[codigo-del-bucle-a-planificar-en-vliw-examen-ac-enero-2017]] · [[planificacion-vliw-para-bucle-con-latencias-mem-2-add-d-1-mu]]
