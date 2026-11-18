---
tipo: "receta"
titulo: "Selección de mejoras mutuamente excluyentes con ley de Amdahl (ejercicio 10)"
temas: ["ac", "arquitectura-computadores", "decision-diseno", "ley-amdahl"]
claves: ["speedup", "memoria", "multiplicación", "otras instrucciones", "factor 2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[decision-diseno]] · [[ley-amdahl]]

Comparar speedup de cada opción: speedup = 1 / ((1-f) + f/k). Datos: memoria 30% (f=0.3), mult 20% (f=0.2), otras 50% (f=0.5), k=2 para todas. Resultados: mem → 1/0.85=1.176 (17.6%); mult → 1/0.9=1.111 (11.1%); otras → 1/0.75=1.333 (33.3%). Ganar: mejorar lo que más tiempo consume (mayor f).

> Teniendo en cuenta la ley de Amdahl es preferible elegir la mejora en la ejecución de otras instrucciones puesto que dedica el mayor porcentaje de todos en la ejecución del programa.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[seleccion-de-mejora-hardware-multiplicacion-vs-memoria-ejerc]] · [[calculo-de-speedup-con-ley-de-amdahl-mejora-de-una-fraccion]] · [[speedup-combinado-de-mejoras-independientes-en-fracciones-di]]
