---
tipo: "receta"
titulo: "Cálculo de CPI a partir de tiempos por tipo de instrucción y frecuencia"
temas: ["ac", "cpi", "rendimiento", "tipos-instruccion"]
claves: ["CPI", "tiempo ejecución", "frecuencia", "instrucciones FP/Int/Load/Store/Saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[rendimiento]] · [[tipos-instruccion]]

Dado tiempo total por tipo de instrucción, frecuencia y cuenta de instrucciones por tipo: CPI = (Tiempo_total × Frecuencia) / Total_instrucciones. Ejercicio 22: Prog A: 200s, 2GHz, 560M+200M+1280M+256M=2296M instr → CPI=200×2e9/2296e6=174.22. Prog B: 210s, misma cuenta instr → CPI=210×2e9/2296e6=182.93. Nota: CPI muy alto sugiere ciclos de espera memoria.

> Tiempo de ejecución = Número de Instrucciones × CPI / Frecuencia de reloj
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]] · [[calculo-de-cpi-dado-frecuencia-de-reloj-y-conteo-de-instrucc]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-y-frecuencia]] · [[ejercicios-de-cpi-mips-y-tiempo-de-ejecucion-con-mezcla-de-i]]
