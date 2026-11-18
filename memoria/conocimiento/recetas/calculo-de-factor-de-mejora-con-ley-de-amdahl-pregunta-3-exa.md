---
tipo: "receta"
titulo: "Cálculo de factor de mejora con ley de Amdahl (pregunta 3 examen)"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["ley de Amdahl", "speedup", "fracción mejorada", "factor mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Datos: T_original = 135 s, T_mejorada_objetivo = 67,5 s (mitad). Tiempo en sumas = 110 s (fracción f = 110/135 ≈ 0,8148). Tiempo resto = 25 s (invariable). Ley de Amdahl: T_mejorada = (1-f)*T_original + f*T_original/k = 25 + 110/k. Igualando a 67,5: 25 + 110/k = 67,5 → 110/k = 42,5 → k = 110/42,5 ≈ 2,588. Respuesta correcta: b) 2,59.

> A program is run in 135 s in a computer, from which 110 s are devoted to addition operations. We want to reduce the program execution time by half, by improving the addition speed. Then, the factor of enhancement for this part of the computer should be… a) 1,59 b) 2,59 c) 3,59 d) It is not possible
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[calculo-de-mejora-necesaria-con-ley-de-amdahl-fraccion-mejor]] · [[aplicacion-de-la-ley-de-amdahl-para-speedup-global-mejorando]] · [[aplicacion-de-la-ley-de-amdahl-para-acelerar-una-fraccion-de]]
