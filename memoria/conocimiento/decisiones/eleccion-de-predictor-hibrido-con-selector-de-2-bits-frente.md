---
tipo: "decision"
titulo: "Elección de predictor híbrido con selector de 2 bits frente a predictor único"
temas: ["ac", "prediccion-saltos"]
claves: ["diseño predictor híbrido", "trade-off complejidad precisión", "selector 2 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

La decisión de diseño combina un predictor simple y barato (1 bit, buena para patrones estables o alternantes simples) con uno más sofisticado (3 bits, mejor para patrones con sesgo fuerte), usando un selector adaptativo de 2 bits por salto. Ventajas: bajo coste (solo 6 bits por salto: 1+3+2), adaptabilidad dinámica. En este ejercicio, el selector no llega a cambiar (se queda en 00) porque los aciertos/fallos de P1 y P2 se compensan en B1 y P2 acierta casi siempre en B2. Esto muestra que la efectividad depende de la correlación entre predictores y la regla de actualización del selector.

> Detail the behavior of a hybrid predictor combining two local predictors (called “Predictor 1” and “Predictor 2”). Predictor 1 associates a 1-bit predictor to each branch instruction (B1 and B2) and Predictor 2 associates a 3-bit predictor to each branch. To select the predictor to employ in each case there is a table (called “Counters”) storing a 2-bit saturating counter for each branch.
> — `repo:datos/temarios/AC/examenes/June2017.pdf`

Relacionado: [[predictor-hibrido-con-selector-de-2-bits-entre-predictor-de]] · [[comparativa-tomasulo-vs-marcador-scoreboard]]
