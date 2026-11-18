---
tipo: "dato"
titulo: "Problema 3 examen AC Junio 2011: código y parámetros de planificación superescalar"
temas: ["ac", "pipeline", "planificacion-instrucciones", "superescalar"]
claves: ["LW", "SUB", "ADD", "superescalar grado 2", "MEM 2 ciclos", "EX 2 ciclos", "adelantamiento", "ventana instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[planificacion-instrucciones]] · [[superescalar]]

Secuencia de 8 instrucciones: LW R3,0(R1); LW R4,0(R2); SUB R6,R7,R8; ADD R4,R3,R11; LW R11,0(R4); SUB R9,R9,R13; ADD R8,R8,R3; SUB R11,R11,R3. Procesador superescalar grado 2 (emite 2 instrucciones/ciclo). Latencias: MEM=2 ciclos para cargas, EX=2 ciclos para aritméticas. Adelantamiento activado. Tres escenarios: a) en orden, b) fuera de orden sin renombramiento, c) fuera de orden con renombramiento. Ventana de instrucciones ilimitada para b y c.

> El procesador invierte 2 ciclos para la etapa MEM en las cargas y 2 ciclos para completar la etapa EX de las operaciones aritméticas. Además, implementa adelantamiento.
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[planificacion-en-superescalar-grado-2-con-sin-renombramiento]] · [[planificacion-en-superescalar-grado-2-en-orden-fuera-de-orde]] · [[codigo-y-parametros-superescalar-examen-ac-junio-2013-p3]]
