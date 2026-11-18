---
tipo: "receta"
titulo: "Cálculo de factor de mejora en multiplicación según ley de Amdahl (pregunta 3)"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["Amdahl", "speedup", "multiplicación", "300 segundos", "250 segundos", "5 veces más rápido"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Tiempo original T=300 s, tiempo en multiplicación T_mul=250 s (fracción f=250/300=5/6). Speedup global deseado S=5. Ley de Amdahl: S = 1 / ((1-f) + f/k) donde k es factor de mejora en multiplicación. 5 = 1 / (1/6 + (5/6)/k) → 1/5 = 1/6 + 5/(6k) → 1/30 = 5/(6k) → k = 25. Respuesta: factor 25 (opción b).

> A given program takes 300 seconds to run on a machine, of which 250 seconds correspond to multiplication operations. How much do I have to improve the multiplication speed if I want the program to run five times faster?
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-en-pregunta-de-examen]] · [[calculo-de-mejora-necesaria-con-la-ley-de-amdahl-test-ac-q3]] · [[calculo-de-mejora-necesaria-con-ley-de-amdahl-ejemplo-multip]]
