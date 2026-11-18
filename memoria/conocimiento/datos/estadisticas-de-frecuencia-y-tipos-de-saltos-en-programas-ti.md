---
tipo: "dato"
titulo: "Estadísticas de frecuencia y tipos de saltos en programas típicos"
temas: ["ac", "benchmarks", "saltos"]
claves: ["1 de cada 6", "1 de cada 8", "1 de cada 10", "85% hacia atrás", "60% hacia delante"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarks]] · [[saltos]]

Datos estadísticos clave para dimensionar el impacto de los saltos: (1) Frecuencia global: ~16,7% de instrucciones son saltos tomados. (2) Saltos condicionales: ~12,5% del total; de ellos, ~10% son tomados. (3) Direccionalidad: los saltos condicionales hacia adelante (forward) son 3,7x más frecuentes que hacia atrás (backward), pero los backward se toman el 85% de las veces (bucles) frente al 60% de los forward. (4) Desglose: 1/3 llamadas, 1/3 retornos, 1/3 bucles y resto; en bucles, las n-1 primeras iteraciones se toman, la última no.

> En promedio: 1 de cada 6 instrucciones es un salto tomado; 1 de cada 8 instrucciones es un salto condicional; 1 de cada 10 instrucciones es un salto condicional y tomado. Saltos condicionales hacia delante 3,7 veces más que hacia atrás. Hacia atrás tomados: 85%. Hacia delante tomados: 60%.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[impacto-de-la-frecuencia-de-saltos-en-el-ilp-y-tamano-de-blo]] · [[frecuencias-de-saltos-en-el-examen-condicionales-30-75-tomad]] · [[taxonomia-de-tecnicas-de-prediccion-de-saltos]]
