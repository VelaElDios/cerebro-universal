---
tipo: "receta"
titulo: "Tasa de fallos de predictor dinámico de 2 bits (inicializado WNT) en bucle de 25 iteraciones"
temas: ["ac", "prediccion-saltos", "predictor-2-bits", "tasa-fallos"]
claves: ["predictor 2 bits", "Weakly Not Taken", "bucle", "tasa fallos", "mispredictions"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictor-2-bits]] · [[tasa-fallos]]

Estados 2-bit: 00=Strong NT, 01=Weak NT, 10=Weak T, 11=Strong T. Inicio: 01 (WNT). Iter 1: predice NT, real T → fallo → estado 10. Iter 2: predice T, real T → acierto → estado 11. Iter 3-24: predice T, real T → aciertos (estado 11). Iter 25: predice T, real NT → fallo → estado 10. Total fallos = 2. Tasa = 2/25 = 0.08 (8%). Opción correcta: "2/25=0,08 → un 8%".

> El siguiente bucle se ejecuta 25 veces, es decir, en las 24 primeras ejecuciones el salto bnez es TOMADO y la última NO TOMADO ... Si se utiliza un predictor dinámico de 2 bit inicializado a Débilmente No Tomado, ¿Cuál es la tasa de fallos (número de fallos/número de saltos) del predictor al finalizar todas iteraciones?
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[predictor-de-1-bit-en-bucle-de-3-iteraciones-t-t-nt-produce]] · [[calculo-de-tasa-de-acierto-con-predictor-de-1-bit-inicializa]] · [[secuencia-de-aciertos-fallos-en-predictor-2-bits-inicializad]]
