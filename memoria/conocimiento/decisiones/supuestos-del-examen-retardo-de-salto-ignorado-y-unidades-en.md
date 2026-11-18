---
tipo: "decision"
titulo: "Supuestos del examen: retardo de salto ignorado y unidades enteras latencia 0"
temas: ["ac", "examen", "pipeline", "supuestos"]
claves: ["retardo salto ignorado", "unidades enteras latencia 0", "predicción perfecta"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[pipeline]] · [[supuestos]]

Dos simplificaciones importantes en el enunciado: 1) Las instrucciones enteras (DADDUI, SLTI, BEQZ) tienen latencia 0: su resultado está disponible en el mismo ciclo de ejecución (ejecución combinacional). 2) El retardo del salto (branch delay) se ignora: se asume que la predicción es perfecta o que la penalidad por fallo es 0, por lo que BEQZ no introduce burbujas en el pipeline. Esto elimina la necesidad de considerar slots de retraso o penalidades de predicción en la planificación.

> 2 unidades funcionales enteras con latencia 0 • Se ignora el retardo del salto
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
