---
tipo: "receta"
titulo: "Desenrollado de bucle mínimo para planificación sin detenciones con salto retardado"
temas: ["ac", "bucles", "optimizacion", "pipeline", "salto-retardado"]
claves: ["desenrollado", "loop unrolling", "delayed branch", "planificación sin stalls", "preservar comportamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[optimizacion]] · [[pipeline]] · [[salto-retardado]]

Procedimiento: 1) Determinar el número mínimo de desenrollados (k) tal que las instrucciones de k iteraciones puedan reordenarse para llenar todos los slots de latencia sin burbujas. 2) Reordenar instrucciones respetando dependencias verdaderas (RAW). 3) Colocar la instrucción de salto en el slot de retardo (delayed branch) con una instrucción útil o NOP. 4) Verificar que la semántica se mantiene (mismos resultados, mismo número de iteraciones efectivas). 5) Calcular nuevo CPI = ciclos_totales_desenrollado / (k * instrucciones_originales).

> Desenrolla el bucle el mínimo número de veces que permita obtener una planificación sin detenciones. Considera salto retardado. Ten en cuenta que el comportamiento del programa debe preservarse.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[analisis-de-detenciones-stalls-en-bucle-con-media-ponderada]] · [[cpi-tras-desenrollado-y-planificacion-de-bucle]] · [[desenrollado-de-bucle-4x-con-salto-retardado-para-eliminar-s]] · [[desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e]]
