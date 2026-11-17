---
tipo: "receta"
titulo: "Predictor híbrido con predictores locales de 1-bit y 3-bits más selector de 2-bits saturado"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor híbrido", "predictor local 1-bit", "predictor local 3-bits", "contador saturado 2-bits", "torneo", "Fibonacci"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Ejercicio 11: bucle que procesa 6 números de Fibonacci (0,1,1,2,3,5). Saltos: B1 (beqz x3,next) salta si x3==0; B2 (bnez x2,loop) salta si x2!=0. Predictor híbrido: Predictor1 = 1-bit por salto (B1/B2), Predictor2 = 3-bits por salto (B1/B2). Tabla "Contadores": un contador de 2-bits saturado por salto (B1/B2). Inicialización: contadores y bits de predicción a 0. Regla de selección: MSB del contador = 1 → Predictor1; MSB = 0 → Predictor2. Actualización de contadores tras cada predicción: (Acierto,Acierto)→no cambia; (Acierto,Fallo)→+1; (Fallo,Acierto)→-1; (Fallo,Fallo)→no cambia. Ambos predictores se actualizan siempre según su propio esquema (1-bit o 3-bits saturado).

> Muestra el comportamiento de un predictor híbrido que combina dos predictores locales (llamados “Predictor1” y “Predictor2”). El Predictor1 asocia un predictor de 1-bit para cada instrucción de salto (B1 y B2) y el Predictor2 usa un predictor de 3-bits para cada salto. Para seleccionar el predictor a emplear en cada caso hay una tabla (llamada “Contadores”) que almacena un contador de 2-bits saturado para cada salto.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[estructura-y-funcionamiento-de-predictor-hibrido-de-torneo-c]]
