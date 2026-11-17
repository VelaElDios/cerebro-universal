---
tipo: "concepto"
titulo: "Predictor Alpha 21264 (Tournament Branch Prediction) combina local y global"
temas: ["ac", "alpha-21264", "prediccion-saltos", "torneo"]
claves: ["Alpha 21264", "Tournament Branch Prediction", "Sag(10", "210)", "Gag(12)", "selector"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[alpha-21264]] · [[prediccion-saltos]] · [[torneo]]

El Alpha 21264 (1998) implementa un predictor de torneo con tres partes:
1. Predictor local (izquierda): Sag(10,210) — tabla de historia local (BHRT) de 1024 entradas (10 bits de PC) cada una con 10 bits de historia; esa historia indexa una BHT local de 1K entradas con contadores de 3 bits.
2. Predictor global (derecha): Gag(12) — BHR global de 12 bits indexa una BHT global de 4K entradas (2¹²) con contadores de 2 bits.
3. Selector (Judge): tabla de 4K entradas indexada por el BHR global (o PC), cada entrada es un contador de 2 bits que elige entre predictor local y global según cuál acierte más.
Es la materialización en hardware de la recomendación Yeh-Patt: combinar G/g y S/s.

> Alpha 21264 (Tournament Branch Prediction): combina predictores globales y locales
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[predictor-hibrido-mcfarling-con-contador-saturado-de-2-bits]] · [[yeh-y-patt-recomiendan-g-g-para-enteros-y-s-s-para-coma-flot]]
