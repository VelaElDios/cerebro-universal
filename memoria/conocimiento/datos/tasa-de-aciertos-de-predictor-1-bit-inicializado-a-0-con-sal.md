---
tipo: "dato"
titulo: "Tasa de aciertos de predictor 1-bit inicializado a 0 con salto siempre tomado ejecutado 100 veces"
temas: ["ac", "prediccion-saltos", "predictor-1-bit", "tasa-aciertos"]
claves: ["predictor 1 bit", "inicializado 0", "siempre tomado", "100 ejecuciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictor-1-bit]] · [[tasa-aciertos]]

Predictor 1-bit: estado 0 = no tomado, 1 = tomado. Inicializado a 0. Salto siempre tomado (T). 1ª ejecución: predice NT → fallo, actualiza a 1. Ejecuciones 2-100: predice T → acierto. Total aciertos = 99, total ejecuciones = 100. Tasa = 0.99 (opción b).

> Se usa un predictor de 1 nivel de 1 bit para predecir un salto que se ha ejecutado 100 veces. ¿Cuál es la tasa de aciertos si está inicializado a 0?
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[accion-del-procesador-ante-fallo-de-prediccion-de-salto]] · [[calculo-de-tasa-de-acierto-con-predictor-de-1-bit-inicializa]] · [[predictor-de-1-bit-en-bucle-de-3-iteraciones-t-t-nt-produce]] · [[predictor-de-un-nivel-con-1-bit-por-instruccion-de-salto-est]]
