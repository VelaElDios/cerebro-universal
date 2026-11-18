---
tipo: "concepto"
titulo: "Planificación software (software pipelining) transforma iteraciones dependientes en independientes"
temas: ["ac", "ilp", "planificacion software", "software pipelining"]
claves: ["planificación software", "software pipelining", "iteraciones dependientes", "independientes", "saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[planificacion software]] · [[software pipelining]]

El software pipelining (planificación software / segmentación software) reorganiza instrucciones de diferentes iteraciones para solaparlas, creando un kernel donde las iteraciones en vuelo son independientes entre sí, eliminando las dependencias entre iteraciones (loop-carried dependencies) en el código programado.

> La técnica de segmentación software: Transforma un bucle con iteraciones dependientes en un bucle con iteraciones independientes
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[condicion-para-solapar-iteraciones-de-un-bucle-desenrollado]] · [[tecnica-de-segmentacion-software-software-pipelining]] · [[que-busca-conseguir-la-segmentacion-software-software-pipeli]]
