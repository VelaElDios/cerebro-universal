---
tipo: "concepto"
titulo: "Planteamiento general de predicción de saltos con ejecución especulativa"
temas: ["ac", "arquitectura", "prediccion-saltos"]
claves: ["predicción saltos", "ejecución especulativa", "fallo predicción", "recuperación", "camino tomado no tomado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[prediccion-saltos]]

Cuando el procesador detecta un salto condicional sin resolver, predice si será tomado o no tomado y, si es tomado, también predice la dirección destino. La ejecución continúa especulativamente por el camino predicho. Al resolverse la condición: si la predicción fue correcta, la secuencia se confirma; si fue incorrecta (fallo de predicción), se descartan todas las instrucciones ejecutadas especulativamente y se reanuda la ejecución por el camino correcto. Las cuestiones clave son: detección de la instrucción de salto, predicción del camino y dirección destino, y recuperación en caso de fallo.

> Cuando se detecta una instrucción de salto condicional sin resolver – se supone o predice el camino del salto: tomado o no tomado – si el salto se predice tomado se predice la dirección destino del salto – la ejecución continúa especulativamente a lo largo del camino supuesto
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[mecanismos-de-recuperacion-ante-fallos-de-prediccion-de-salt]] · [[recuperacion-ante-fallo-de-prediccion-de-salto-misprediction]] · [[recuperacion-ante-fallo-de-prediccion-descartar-resultados-e]]
