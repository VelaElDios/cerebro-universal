---
tipo: "concepto"
titulo: "Ejecución multicamino (multi-path execution) frente a predicción de saltos"
temas: ["ac", "ejecucion-multicamino", "prediccion-saltos"]
claves: ["multi-path execution", "predicción saltos", "registro predicado", "ambas ramas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ejecucion-multicamino]] · [[prediccion-saltos]]

La ejecución multicamino (multi-path execution) ejecuta **ambas ramas** de un salto condicional simultáneamente, sin predicción, y luego selecciona el resultado correcto (p.ej., mediante registros predicados o commit condicional). Es una alternativa a la predicción para evitar penalización por fallos. Opción correcta: c. "Se ejecutan las dos ramas de un salto condicional sin hacer uso de predicción".

> Indica la respuesta correcta para la ejecución multicamino: a. Se ejecutan las dos ramas del salto condicional y la instrucción se ejecuta dependiendo del valor de un registro predicado b. Se escoge usando predicción uno de los dos caminos de un salto condicional para ser ejecutado c. Se ejecutan las dos ramas de un salto condicional sin hacer uso de predicción d. Se escoge al azar uno de los dos caminos de un salto condicional para ser ejecutado
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]] · [[especulacion-estatica-con-cargas-especulativas-lw-en-mips64]]
