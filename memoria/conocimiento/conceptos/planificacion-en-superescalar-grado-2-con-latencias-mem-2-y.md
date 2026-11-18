---
tipo: "concepto"
titulo: "Planificación en superescalar grado 2 con latencias MEM=2 y EX=2"
temas: ["ac", "hazards", "pipeline", "planificacion-instrucciones", "superescalar"]
claves: ["superescalar grado 2", "latencia MEM", "latencia EX", "adelantamiento", "hazard RAW", "hazard WAR", "hazard WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[hazards]] · [[pipeline]] · [[planificacion-instrucciones]] · [[superescalar]]

En un superescalar de grado 2 se pueden emitir hasta 2 instrucciones por ciclo. Las cargas (LW) tardan 2 ciclos en MEM (acceso a memoria), las aritméticas (ADD/SUB) tardan 2 ciclos en EX. El adelantamiento (forwarding) permite resolver hazards RAW enviando resultados directamente desde EX/MEM a etapas anteriores sin esperar a WB. Los hazards WAR y WAW solo aparecen en ejecución fuera de orden y se resuelven con renombramiento de registros (caso c) o causan paradas en caso b.

> El procesador invierte 2 ciclos para la etapa MEM en las cargas y 2 ciclos para completar la etapa EX de las operaciones aritméticas. Además, implementa adelantamiento.
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
