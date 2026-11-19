---
tipo: "concepto"
titulo: "Efecto del orden de datos en predicción de saltos condicionales"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["sorted data", "unsorted data", "branch predictor accuracy", "data dependency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Cuando los datos están ordenados, la condición `x >= 128` crea un patrón predecible: primero muchos falsos (x < 128), luego muchos verdaderos (x >= 128). Los predictores de saltos modernos (basados en historia local/global) aprenden este patrón y aciertan casi siempre. Con datos desordenados, el patrón es aleatorio y el predictor falla ~50% de las veces, causando vaciados de pipeline constantes. El código branchless elimina esta dependencia del orden.

> Sumar elementos que superan un umbral es drásticamente más rápido con datos ordenados porque el predictor de saltos casi siempre acierta.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp` (cita sin comprobar)

Relacionado: [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline]]
