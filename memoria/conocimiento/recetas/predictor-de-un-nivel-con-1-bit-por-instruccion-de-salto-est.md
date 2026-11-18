---
tipo: "receta"
titulo: "Predictor de un nivel con 1 bit por instrucción de salto (estado inicial tomado)"
temas: ["ac", "prediccion-saltos"]
claves: ["1-bit predictor", "estado inicial 1", "actualización tras resultado real"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Para cada salto (B1, B2, B3) se mantiene un bit de predicción (1=Taken, 0=Not Taken). Estado inicial: los tres bits a 1 (predicen Taken). En cada ejecución: se usa el bit actual para predecir; se compara con resultado real (T/NT); se anota acierto (Y/N); se actualiza el bit al resultado real (1 si T, 0 si NT). Al final se calcula tasa de acierto = aciertos / total predicciones.

> Detail the behavior of a one-level predictor that assigns 1 bit to each branch instruction. Consider that the initial state of the predictor is the one shown in the first row of the table.
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad]]
