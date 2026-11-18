---
tipo: "receta"
titulo: "Cómo calcular efectividad en coste (rendimiento/coste) entre dos sistemas"
temas: ["ac", "coste-efectividad", "evaluacion-rendimiento"]
claves: ["efectividad en coste", "rendimiento/coste", "tiempo ejecución", "coste sistema"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[coste-efectividad]] · [[evaluacion-rendimiento]]

Pasos:
1. Calcular el rendimiento de cada sistema para la carga de trabajo: rendimiento = 1 / tiempo_total_ejecución (en ejecuciones/segundo).
2. Dividir el rendimiento por el coste del sistema (€) → efectividad = rendimiento / coste (ejecuciones/segundo/€).
3. Comparar: la mayor efectividad gana.

Ejemplo del texto (Ejercicio 1):
- S1: coste 10000 €, tiempos 10s (P1) + 3s (P2) = 13s total → rendimiento = 1/13 ejec/s → efectividad = (1/13)/10000 = 1/130000.
- S2: coste 15000 €, tiempos 5s + 4s = 9s total → rendimiento = 1/9 ejec/s → efectividad = (1/9)/15000 = 1/135000.
- S1 es ligeramente más efectiva en coste para la carga mixta (1/130000 > 1/135000).

> Decimos que una máquina es más efectiva en coste que otra si la razón de rendimiento dividida por el coste es mayor.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[ejercicio-de-coste-efectividad-comparacion-de-sistemas-por-r]] · [[como-comparar-efectividad-en-coste-entre-dos-sistemas]] · [[calculo-de-cost-effectiveness-entre-dos-sistemas-con-cargas]]
