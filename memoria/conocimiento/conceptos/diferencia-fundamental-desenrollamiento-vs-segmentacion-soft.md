---
tipo: "concepto"
titulo: "Diferencia fundamental: desenrollamiento vs segmentación software"
temas: ["ac", "comparativa", "loop-unrolling", "planificacion-estatica", "software-pipelining"]
claves: ["iteraciones-independientes", "instrucciones-dependientes", "kernel", "prologue", "epilogue"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[comparativa]] · [[loop-unrolling]] · [[planificacion-estatica]] · [[software-pipelining]]

Desenrollamiento: replica el cuerpo del bucle N veces, ejecuta N iteraciones originales por iteración desenrollada; las iteraciones siguen siendo independientes entre sí, pero se exponen más instrucciones para planificar. Segmentación software: reorganiza instrucciones de DIFERENTES iteraciones en una sola tubería (pipeline) superpuesta; el kernel ejecuta una etapa de cada una de varias iteraciones concurrentes (carga iteración i+2, suma iteración i+1, store iteración i). Requiere código de arranque (llenar tubería) y finalización (vaciar tubería). El desenrollamiento aumenta presión de registros linealmente con N; la segmentación software usa registros fijos (3 en el ejemplo) independientemente de la longitud del array.

> Consiste en transformar un bucle con instrucciones dependientes e iteraciones independientes en un bucle con instrucciones independientes e iteraciones dependientes
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]] · [[segmentacion-software-software-pipelining-en-bucles-sin-depe]] · [[tecnica-de-segmentacion-software-software-pipelining]] · [[planificacion-software-software-pipelining-transforma-iterac]]
