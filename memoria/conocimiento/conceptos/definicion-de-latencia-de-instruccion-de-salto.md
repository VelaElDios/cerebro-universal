---
tipo: "concepto"
titulo: "Definición de latencia de instrucción de salto"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["latencia salto", "IF stage", "condición", "resolución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

La latencia de una instrucción de salto se define como el número de ciclos adicionales entre la etapa IF (Instruction Fetch) y el ciclo en el que se computa su condición. No es el tiempo hasta su resolución completa, ni hasta la etapa ID o MEM, sino específicamente hasta que la condición está disponible para decidir si el salto se toma.

> The number of additional cycles between the IF stage and the cycle where its condition is computed
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
