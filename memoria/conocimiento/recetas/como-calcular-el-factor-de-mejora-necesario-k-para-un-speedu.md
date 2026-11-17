---
tipo: "receta"
titulo: "Cómo calcular el factor de mejora necesario (k) para un speedup objetivo dado (ley de Amdahl inversa)"
temas: ["ac", "evaluacion-rendimiento", "factor-mejora", "ley-amdahl", "speedup-objetivo"]
claves: ["factor mejora", "speedup objetivo", "fracción tiempo", "ley Amdahl inversa"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[evaluacion-rendimiento]] · [[factor-mejora]] · [[ley-amdahl]] · [[speedup-objetivo]]

Dado: speedup_objetivo (n), fracción no mejorada (1-f), fracción mejorada (f).
Fórmula: n = T_original / (T_no_mejorado + T_mejorado/k) = 1 / ((1-f) + f/k).
Despejar k: k = f / (1/n - (1-f)).

Ejemplo (Ejercicio 7): T_original = 5s, f = 0.8 (80% FP), n = 1.5 (50% ganancia).
T_no_mejorado = 1s (20%), T_mejorado_original = 4s.
1.5 = 5 / (1 + 4/k) → 1 + 4/k = 5/1.5 = 3.33 → 4/k = 2.33 → k = 4/2.33 = 1.71.
Se necesita mejorar la unidad FP 1.71× (≈ 71% más rápida).

> Por lo tanto, 5 / (1 + x) = 1.5 → x = 1.71
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[ley-de-amdahl-aplicada-a-speedup-con-mejora-parcial-de-un-su]]
