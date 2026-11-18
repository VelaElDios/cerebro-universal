---
tipo: "receta"
titulo: "Cálculo de predicciones correctas en bucles anidados con predictores de 1, 2 y 3 bits"
temas: ["ac", "bucles-anidados", "contadores-saturados", "prediccion-saltos"]
claves: ["B1 salto interno", "B2 salto externo", "predictor 1 bit", "predictor 2 bits", "predictor 3 bits", "inicialización"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucles-anidados]] · [[contadores-saturados]] · [[prediccion-saltos]]

Bucle interno (B1): 10 iteraciones por vuelta externa, 100 vueltas externas = 1000 ejecuciones. B1 se toma 9 veces y no se toma 1 vez por vuelta externa (salida del bucle). Patrón: T T T T T T T T T NT repetido 100 veces. Bucle externo (B2): 100 iteraciones, se toma 99 veces, no tomado 1 vez al final. Patrón: 99 T seguidos, luego NT. Para cada predictor, simular la máquina de estados (contador saturado) con la inicialización dada y contar aciertos. Ejemplo: predictor 1 bit init tomado -> acierta las 9 T, falla en NT, luego predice NT (porque falló), falla en la siguiente T, predice T, acierta las 8 T restantes... Total aciertos = 9 (primeras T) + 8*99 (resto de vueltas) = 801? Ver simulación exacta en clase.

> Considera que B1 y B2 son las instrucciones de salto correspondientes al bucle interno y externo, respectivamente. a) Para B1, indica el número de predicciones correctas que habrá para cada uno de los siguientes esquemas: i. predictor de 1 bit inicializado a tomado ii. predictor de 1 bit inicializado a no tomado iii. predictor de 2 bits inicializado a 10 tomado débil iv. predictor de 2 bits inicializado a 01 no tomado débil v. predictor de 3 bits inicializado a 100 vi. predictor de 3 bits inicializado a 000
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[simulacion-de-predictores-1-bit-4-bits-saturado-y-correlacio]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]] · [[ejercicio-simulacion-de-predictores-de-2-bits-vs-correlacion]]
