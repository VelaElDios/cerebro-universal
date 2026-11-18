---
tipo: "receta"
titulo: "Cálculo de speedup con ley de Amdahl (mejora de una fracción del tiempo)"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["speedup", "Amdahl", "fracción tiempo", "factor mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Para calcular el speedup al mejorar un componente que ocupa una fracción f del tiempo de ejecución original con un factor de mejora k: speedup = 1 / ((f/k) + (1-f)). En el ejercicio 16: memoria 35% (f=0.35, k=3) → speedup=1.30; multiplicación 15% (f=0.15, k=3) → speedup=1.11; otras instrucciones 50% (f=0.50, k=3) → speedup=1.50. La mayor ganancia se obtiene mejorando la fracción más grande.

> speedup = Tiempo ejecución sin utilizar la mejora / Tiempo ejecución utilizando la mejora
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[ley-de-amdahl-aplicada-a-speedup-con-mejora-parcial-de-un-su]] · [[calculo-de-speedup-maximo-con-ley-de-amdahl-fraccion-mejorab]] · [[calculo-de-ganancia-de-velocidad-speedup-con-la-ley-de-amdah]]
