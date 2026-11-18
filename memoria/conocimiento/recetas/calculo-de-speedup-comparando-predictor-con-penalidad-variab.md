---
tipo: "receta"
titulo: "Cálculo de speedup comparando predictor con penalidad variable vs penalidad fija"
temas: ["ac", "cpi", "penalidad-salto", "prediccion-saltos", "speedup"]
claves: ["penalidad 4 ciclos", "frecuencia saltos 10%", "CPI base 1", "predictor caso iii (2 bits init 10)", "penalidad fija 2 ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[penalidad-salto]] · [[prediccion-saltos]] · [[speedup]]

1) Calcular CPI con predictor: CPI = 1 + (frecuencia_saltos * tasa_fallo * penalidad_fallo). Tasa_fallo = 1 - (predicciones_correctas_B1 + predicciones_correctas_B2) / total_saltos. Total saltos = ejecuciones_B1 + ejecuciones_B2 = 1000 + 100 = 1100. Usar aciertos del ejercicio 2.a.iii. 2) CPI con penalidad fija 2 ciclos: CPI_fijo = 1 + 0.10 * 2 = 1.2 (asumiendo que la penalidad fija se paga en cada salto). 3) Speedup = CPI_fijo / CPI_predictor.

> Asume que la penalidad por fallo en la predicción es siempre de 4 ciclos, que sólo hay saltos del tipo B1 y B2, y que la frecuencia de saltos es del 10%. ¿Cuánto más rápido es un procesador que usa el predictor del caso iii, que otro procesador que tiene una penalidad por saltos fija e igual a 2 ciclos? Supón un CPI de 1 sin detenciones por los saltos.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[calculo-de-cpi-sin-btb-y-speedup-con-btb-miss-rate-10-solo-s]] · [[calculo-de-cpi-con-predictor-de-salto-tomado-y-penalizacion]] · [[evaluacion-de-rendimiento-de-btb-con-politica-de-solo-saltos]]
