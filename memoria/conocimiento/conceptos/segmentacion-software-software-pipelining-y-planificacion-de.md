---
tipo: "concepto"
titulo: "Segmentación software (software pipelining) y planificación de trazas (trace scheduling)"
temas: ["ac", "ilp", "planificacion-estatica", "software-pipelining", "trace-scheduling"]
claves: ["segmentación software", "software pipelining", "planificación de trazas", "trace scheduling", "reordenación instrucciones dependientes"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[planificacion-estatica]] · [[software-pipelining]] · [[trace-scheduling]]

Dos técnicas de planificación estática además del desenrollamiento:
- **Segmentación software (software pipelining)**: Reordena instrucciones de distintas iteraciones de un bucle para solapar su ejecución, como una pipeline por software. Busca iniciar una nueva iteración cada ciclo (II=1) rellenando las latencias con instrucciones de otras iteraciones. Requiere prólogo, kernel estable y epílogo.
- **Planificación de trazas (trace scheduling)**: Optimiza el camino de ejecución más frecuente (traza) tratando bloques básicos concatenados como una unidad. Mueve instrucciones especulativamente fuera de la traza con código de compensación (fix-up) en las salidas laterales. Base de arquitecturas VLIW/EPIC (IA-64/Itanium).
Ambas reordenan instrucciones dependientes para aumentar ILP; la primera enfocada en bucles, la segunda en flujo de control general.

> Segmentación software (software pipelining) reordenación de instrucciones dependientes • Planificación de trazas (trace scheduling) reordenación de instrucciones dependientes
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[arquitectura-epic-ia64-y-procesadores-itanium]] · [[comparacion-de-tecnicas-de-planificacion-estatica-desenrolla]] · [[planificacion-de-trazas-trace-scheduling-para-condicionales]] · [[planificacion-software-software-pipelining-transforma-iterac]]
