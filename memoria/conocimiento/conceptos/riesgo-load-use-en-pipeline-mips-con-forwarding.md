---
tipo: "concepto"
titulo: "Riesgo load-use en pipeline MIPS con forwarding"
temas: ["ac", "forwarding", "mips", "pipeline", "riesgos"]
claves: ["load-use hazard", "memory access", "stall"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[forwarding]] · [[mips]] · [[pipeline]] · [[riesgos]]

Aunque el forwarding resuelve la mayoría de dependencias RAW entre instrucciones ALU consecutivas, una instrucción de carga (load) seguida de una instrucción que usa el dato cargado provoca un riesgo load-use que requiere detener el pipeline un ciclo (burbuja), porque el dato no está disponible hasta el final de la etapa MEM, mientras que la instrucción siguiente lo necesita en EX.

> In a pipelined MIPS processor supporting forwarding, when executing two consecutive integer instructions: If the first instruction is a memory access, sometimes it is necessary to stop.
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)` (cita sin comprobar)

Relacionado: [[limitacion-del-adelantamiento-hazard-load-use-load-use-penal]] · [[adelantamiento-forwarding-para-riesgos-raw]] · [[dependencia-de-datos-en-pipeline-riesgo-solo-si-instruccione]]
