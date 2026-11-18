---
tipo: "receta"
titulo: "Desenrollamiento y segmentación software con latencia fadd.d 5 ciclos (Ejercicio 5)"
temas: ["ac", "compilador-conoce-hardware", "desenrollamiento", "planificacion-estatica", "segmentacion-software"]
claves: ["fadd.d 5 ciclos", "fld->fadd 1", "fadd->fsd 2", "fld->fsd 0", "caso compilador no conoce hardware", "caso compilador conoce hardware"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilador-conoce-hardware]] · [[desenrollamiento]] · [[planificacion-estatica]] · [[segmentacion-software]]

Bucle simple: carga f0, fadd.d f4=f2+f0, store f4, decrementa x1, salta. Latencia fadd.d = 5 ciclos. (a) Compilador no conoce hardware: asume latencia genérica (p.ej. 1 o 2), desenrolla conservadoramente (factor 2-4) y planifica con NOPs o instrucciones independientes si las hay. (b) Compilador conoce hardware: sabe que fadd.d tarda 5 ciclos. Para evitar stalls sin NOPs, desenrollar factor 5 (o 6) para tener 5 sumas en vuelo. Luego aplicar segmentación software: kernel con II=1 (si UF segmentada) iniciando una fadd.d por ciclo. Prólogo: 5 primeras cargas y sumas escalonadas. Epílogo: 5 últimos stores. Renombrar registros f0,f4,f6,f8,f10,f12 para cada iteración en vuelo.

> Considerando una latencia de 5 ciclos para la instrucción fadd.d, aplica desenrollamiento al siguiente fragmento de código ... Después, aplica segmentación software y desenrollamiento de bucles (el menor número de veces) para que no haya detenciones. a) Asume que el compilador no conoce las características del hardware b) Asume que el compilador conoce las características del hardware (i.e. ciclos de las UF)
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3_Prob.pdf` (cita sin comprobar)

Relacionado: [[segmentacion-software-software-pipelining-para-bucle-con-mul]] · [[segmentacion-software-software-pipelining-en-bucles-sin-depe]] · [[desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e]]
