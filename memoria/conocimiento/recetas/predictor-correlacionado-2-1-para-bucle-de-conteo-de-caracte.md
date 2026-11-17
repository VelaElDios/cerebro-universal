---
tipo: "receta"
titulo: "Predictor correlacionado (2,1) para bucle de conteo de caracteres en cadena \"exam18"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor correlacionado", "(2", "1)", "BHR", "BHT", "bne", "bnez", "exam18"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Ejercicio 10: código RISC-V que recorre la cadena "exam18" (6 chars + NULL = 7 iteraciones). Saltos: B1 (bne x2,x4,not_a) salta si el char no es 'a'; B2 (bnez x3,loop) salta si el char leído no es NULL. El predictor correlacionado (2,1) usa un BHR global de 2 bits y 4 entradas BHT (índice = BHR). Estado inicial: todos los bits de predicción a 0. Hay que simular iteración a iteración actualizando BHR tras cada salto y consultando/actualizando la BHT correspondiente.

> Completa la siguiente tabla sabiendo que se usa un predictor correlacionado (2,1) para predecir el comportamiento de los saltos y que en memoria se ha almacenado la cadena “exam18”
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
