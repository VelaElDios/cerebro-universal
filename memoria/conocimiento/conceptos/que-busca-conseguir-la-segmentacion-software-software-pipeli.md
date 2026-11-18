---
tipo: "concepto"
titulo: "Qué busca conseguir la segmentación software (software pipelining) en el código del bucle"
temas: ["ac", "ilp", "planificacion-estatica", "segmentacion-software"]
claves: ["software pipelining", "iteraciones independientes", "instrucciones dependientes"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[planificacion-estatica]] · [[segmentacion-software]]

La segmentación software (software pipelining) reorganiza el código del bucle para superponer la ejecución de varias iteraciones, de forma que en el estado estable (kernel) las instrucciones de diferentes iteraciones se ejecutan en paralelo. El objetivo es obtener un bucle donde las instrucciones *dentro* de una iteración pueden tener dependencias, pero las *iteraciones* en vuelo son independientes entre sí (se solapan). Por tanto, la descripción correcta es: «Un bucle con instrucciones dependientes e iteraciones independientes» (opción b).

> La técnica de segmentación software modifica el código original para obtener: a) Un bucle con instrucciones independientes e iteraciones dependientes b) Un bucle con instrucciones dependientes e iteraciones independientes c) Una estructuras condicional con instrucciones independiente d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
