---
tipo: "dato"
titulo: "Latencias de ejecución FP en superescalar MIPS64 del examen Enero 2015"
temas: ["ac", "latencias", "mips64", "superescalar"]
claves: ["ADD.D 2 ciclos", "MUL.D 3 ciclos", "L.D 1 ciclo", "S.D 1 ciclo", "DADDUI 1 ciclo", "BNE 1 ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[latencias]] · [[mips64]] · [[superescalar]]

Latencias de la etapa de ejecución (EX) para el superescalar MIPS64 del problema:
- **ADD.D (suma PF):** 2 ciclos en EX.
- **MUL.D (multiplicación PF):** 3 ciclos en EX.
- **L.D (carga PF):** 1 ciclo en EX (cálculo dirección + acceso caché).
- **S.D (almacenamiento PF):** 1 ciclo en EX (cálculo dirección + acceso caché).
- **DADDUI (suma entera inmediata sin signo):** 1 ciclo en EX.
- **BNE (salto condicional):** 1 ciclo en EX (evaluación condición + cálculo objetivo).
Todas las unidades funcionales están segmentadas (pipelined), por lo que pueden aceptar una nueva operación cada ciclo. El adelantamiento (forwarding) permite usar el resultado al ciclo siguiente de terminar EX.

> Además, las sumas en PF requieren 2 ciclos para la etapa de ejecución, las multiplicaciones en PF 3 ciclos y el resto de operaciones 1 ciclo.
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[planificacion-superescalar-mips64-4-vias-con-latencias-pf-pr]]
