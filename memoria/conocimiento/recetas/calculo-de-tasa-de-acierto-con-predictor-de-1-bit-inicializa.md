---
tipo: "receta"
titulo: "Cálculo de tasa de acierto con predictor de 1 bit inicializado a tomado y predictor de 3 bits inicializado a 011"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor 1 bit", "predictor 3 bits", "contador saturación", "inicialización", "tasa acierto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Para cada salto (B1 y B2 por separado): Predictor 1 bit: estado inicial T (tomado). En cada ocurrencia, predecir según estado; si acierto, estado unchanged; si fallo, invertir estado. Tasa acierto = aciertos / total ocurrencias. Predictor 3 bits (contador saturación 0-7): inicial 011 (3, débilmente tomado). Predicción: tomado si contador >= 4 (100), no tomado si < 4. Actualización: tomado -> incrementar (max 7); no tomado -> decrementar (min 0). Al final, mostrar estado final de cada predictor (1 bit: T/NT; 3 bits: valor 0-7).

> b) ¿Qué tasa de acierto tendríamos si asociamos a cada salto un predictor de 1 bit inicializado a tomado? ¿Y si asociamos a cada salto un predictor de 3 bits inicializado a 011? Justifica las respuestas. ¿Cómo quedarían los predictores una vez finalizado el recorrido?
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]] · [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]]
