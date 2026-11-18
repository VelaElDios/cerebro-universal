---
tipo: "concepto"
titulo: "Técnica de segmentación software (software pipelining)"
temas: ["ac", "bucles", "ilp", "planificacion"]
claves: ["software pipelining", "segmentación software", "kernel", "prologo", "epilogo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2011.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucles]] · [[ilp]] · [[planificacion]]

El software pipelining reorganiza el bucle para iniciar una nueva iteración antes de terminar la anterior (solapamiento), generando un kernel con más instrucciones por iteración pero menos iteraciones totales (prologue + kernel + epilogue).

> Transforma un bucle en otro con menos iteraciones y mas instrucciones
> — `repo:datos/temarios/AC/examenes/Enero2011.pdf`

Relacionado: [[condicion-para-solapar-iteraciones-de-un-bucle-desenrollado]] · [[proposito-de-la-segmentacion-software-software-pipelining-te]] · [[planificacion-software-software-pipelining-transforma-iterac]] · [[que-hace-la-tecnica-de-segmentacion-software-software-pipeli]]
