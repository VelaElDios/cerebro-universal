---
tipo: "receta"
titulo: "Selección de mejora hardware: multiplicación vs memoria (ejercicio 14)"
temas: ["ac", "arquitectura-computadores", "decision-diseno", "ley-amdahl", "reduccion-tiempo"]
claves: ["speedup", "multiplicación", "acceso memoria", "reducción porcentaje tiempo", "mutuamente excluyentes"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[decision-diseno]] · [[ley-amdahl]] · [[reduccion-tiempo]]

Comparar speedup de dos mejoras exclusivas. Mejora mult: reduce tiempo 25% → k=1/0.75=1.333, f=0.10 → speedup=1/(0.1/1.333+0.9)=1/0.975=1.0256. Mejora mem: reduce tiempo 15% → k=1/0.85=1.176, f=0.35 → speedup=1/(0.35/1.176+0.65)=1/0.9475=1.055. Elegir la de mayor speedup (memoria 1.055 > mult 1.026). Nota: "reducir tiempo un X%" equivale a factor k = 1/(1-X/100).

> Por lo tanto, debería optarse por mejorar el acceso a memoria.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[seleccion-de-mejoras-mutuamente-excluyentes-con-ley-de-amdah]] · [[speedup-combinado-de-mejoras-independientes-en-fracciones-di]] · [[speedup-combinando-multiples-mejoras-independientes]]
