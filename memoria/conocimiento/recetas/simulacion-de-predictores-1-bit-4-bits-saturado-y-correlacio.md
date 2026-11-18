---
tipo: "receta"
titulo: "Simulación de predictores 1 bit, 4 bits saturado y correlacionado (2,1) para dos bucles anidados con conteos fijos"
temas: ["ac", "contadores-saturados", "prediccion-saltos", "predictor-correlacionado", "simulacion"]
claves: ["salto 1 (externo)", "salto 2 (interno)", "8 ejecuciones salto 2", "2 ejecuciones salto 1", "predictor 1 bit init NT", "predictor 4 bits init 7", "predictor (2", "1) historia 2 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[contadores-saturados]] · [[prediccion-saltos]] · [[predictor-correlacionado]] · [[simulacion]]

Código: L1 (externo) se ejecuta 2 veces. Dentro, L2 (interno) se ejecuta 8 veces por vuelta de L1. Salto 2 (L2): patrón T x7, NT (salida). Salto 1 (L1): patrón T (vuelta 1), NT (vuelta 2). a) 1 bit init NT: Salto2: predice NT siempre -> acierta solo en la última (NT), falla 7 T. Primera vuelta: 1 acierto. Segunda vuelta: predictor queda en NT (por último NT), mismo resultado: 1 acierto. Total 2. Salto1: init NT, primera ejecución T -> fallo, predice T; segunda NT -> fallo. 0 aciertos. b) 4 bits init 7 (111 = tomado fuerte). Contador saturado 0-15. Simular decrementos en NT. c) Predictor (2,1): 2 bits historia global (últimos 2 saltos globales), 1 bit por entrada BHT (4 entradas). Historia inicial 00 (NT, NT). Indexar BHT[historia]. Actualizar historia y entrada usada. Mostrar tabla de evolución.

> Indica el número de predicciones correctas para cada salto en los siguientes casos: a) Predictores de 1 bit, inicializados a no tomado. b) Predictores de 4 bits, contadores saturados, inicializados con el valor 7. c) Predictor del tipo (2,1), considerando que cuando comienza la ejecución del código, los dos saltos anteriores han sido no tomados, y el estado inicial de todos los predictores es no tomado fuerte.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[calculo-de-predicciones-correctas-en-bucles-anidados-con-pre]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]] · [[ejercicio-simulacion-de-predictores-de-2-bits-vs-correlacion]]
