---
tipo: "concepto"
titulo: "Qué hace la técnica de segmentación software (software pipelining)"
temas: ["ac", "bucles", "pipeline", "software-pipelining"]
claves: ["segmentación software", "software pipelining", "iteraciones independientes", "saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[pipeline]] · [[software-pipelining]]

La segmentación software (software pipelining) reorganiza instrucciones de **distintas iteraciones** para ejecutarlas en paralelo, creando un "kernel" donde iteraciones se solapan. Requiere que no haya dependencias entre iteraciones (o que se puedan romper). Respuesta correcta: b).

> La técnica de segmentación software: a) Reduce el número de saltos b) Transforma un bucle con iteraciones dependientes en un bucle con iteraciones independientes c) Transforma un bucle con instrucciones dependientes en un bucle con instrucciones independientes
> — `repo:datos/temarios/AC/examenes/Noviembre2011.pdf`

Relacionado: [[segmentacion-software-software-pipelining-transforma-bucles]] · [[segmentacion-software-software-pipelining-modifica-codigo-pa]] · [[que-busca-conseguir-la-segmentacion-software-software-pipeli]]
