---
tipo: "concepto"
titulo: "Penalización de fallo de predicción de salto en pipeline"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["branch misprediction", "pipeline flush", "penalty cycles", "branch predictor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Un fallo de predicción de salto (branch misprediction) obliga al procesador a vaciar el pipeline (pipeline flush) porque se han ejecutado instrucciones por el camino equivocado. La penalización típica es de 10-20 ciclos en procesadores modernos, ya que hay que descartar el trabajo especulativo y reanudar la ejecución desde la dirección correcta. En el código, esto se manifiesta como una diferencia drástica de rendimiento entre datos ordenados (predictor acierta casi siempre) y desordenados (predictor falla ~50%).

> Con datos desordenados, las bifurcaciones impredecibles provocan fallos de predicción que obligan a vaciar el pipeline (penalización de 10-20 ciclos).
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp` (cita sin comprobar)

Relacionado: [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
