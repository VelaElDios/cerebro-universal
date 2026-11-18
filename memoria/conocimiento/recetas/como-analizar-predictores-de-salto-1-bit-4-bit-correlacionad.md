---
tipo: "receta"
titulo: "Cómo analizar predictores de salto (1-bit, 4-bit, correlacionado) sobre secuencia conocida"
temas: ["ac", "branch-prediction", "correlacionado", "prediccion-saltos"]
claves: ["predictor 1-bit", "predictor 4-bit", "predictor correlacionado (1", "2)", "BHR", "BHT", "tasa acierto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[branch-prediction]] · [[correlacionado]] · [[prediccion-saltos]]

El bucle recorre secuencia 0,1,0,2,0,3,0,4,0,5 (10 elementos). Saltos: B1 (BEQZ R2, next) y B2 (BEQ R1, R3, fin). a) Sentido real: B1 tomado cuando R2==0 (elementos pares: 0,0,0,0,0 → 5 veces tomado, 5 no tomado alternando). B2 tomado solo en última iteración (1 tomado, 9 no tomado). b) Predictor 1-bit init=1 (tomado): B1 acierta 5/10 (alterna T/NT, predictor cambia cada vez → 50%). B2 acierta 9/10 (predice T, 9 NT → falla 1, acierta 9 → 90%). Predictor 4-bit init=0111 (tomado débil): máquina de estados 0000=NT fuerte ... 1111=T fuerte. Simular transiciones. c) Correlacionado (1,2): 1 bit historia global (BHR), 2 bits por entrada en BHT (4 entradas). BHR init=1 (tomado). BHTs init=00 (NT fuerte). Para cada salto, usar BHR como índice a BHT, predecir, actualizar BHT[BHR] y BHR=sentido_real. Detallar ciclo a ciclo.

> ¿Qué tasa de acierto obtendríamos si asociamos a cada salto un predictor de 1 bit inicializado a 1? ¿Y si asociamos a cada salto un predictor de 4 bits inicializado a 0111? Justifica las respuestas. ¿Cómo quedarían los predictores una vez finalizado el recorrido?
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf`

Relacionado: [[estado-inicial-de-predictores-en-ejercicio-12-predictor-2-bi]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]]
