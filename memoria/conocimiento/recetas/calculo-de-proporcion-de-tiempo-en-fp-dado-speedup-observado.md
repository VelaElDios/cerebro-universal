---
tipo: "receta"
titulo: "Cálculo de proporción de tiempo en FP dado speedup observado y factor de mejora (Ejercicio 8b)"
temas: ["ac", "coma-flotante", "compiladores", "ley-amdahl", "speedup"]
claves: ["speedup 5", "10 veces más rápido", "50 segundos", "proporción tiempo FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[coma-flotante]] · [[compiladores]] · [[ley-amdahl]] · [[speedup]]

Dado: k = 10 (FP 10x más rápido), Speedup_observado = 5, Tiempo_original = 50s
Buscar: f (fracción de tiempo en FP con compilador C)

Ley de Amdahl: Speedup = 1 / [(1 - f) + f/k]
5 = 1 / [(1 - f) + f/10]
5 = 1 / [1 - f + 0.1f]
5 = 1 / [1 - 0.9f]
1 - 0.9f = 1/5 = 0.2
0.9f = 0.8
f = 0.8 / 0.9 = 8/9 ≈ 0.8889 = 88.89%

Verificación: Tiempo en FP = 50 * 8/9 ≈ 44.44s. Tiempo no-FP = 50/9 ≈ 5.56s.
Con M: FP tarda 4.44s, no-FP 5.56s → Total 10s. Speedup = 50/10 = 5. ✓

Respuesta: La proporción de tiempo dedicado a FP es 8/9 (88.89%).

> b) Si el código que genera el compilador M para las instrucciones de coma flotante es 10 veces más rápido, y un determinado programa necesita 50 segundos para ejecutarse usando el compilador C, indica la proporción de ese tiempo dedicado a las instrucciones de coma flotante considerando un speedup de 5.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[ley-de-amdahl-aplicada-a-optimizacion-de-compilador-para-com]] · [[determinar-si-es-posible-alcanzar-un-speedup-objetivo-mejora]] · [[como-calcular-factor-de-mejora-necesario-segun-ley-de-amdahl]] · [[despeje-de-fraccion-de-tiempo-mejorable-dado-speedup-objetiv]]
