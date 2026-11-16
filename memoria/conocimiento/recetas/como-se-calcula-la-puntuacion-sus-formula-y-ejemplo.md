---
tipo: "receta"
titulo: "Cómo se calcula la puntuación SUS (fórmula y ejemplo)"
temas: ["calculo", "formula", "latex", "sus", "usabilidad"]
claves: ["items impares", "items pares", "puntuación 0-100", "factor 2.5"]
proyectos: ["plantilla-sus"]
fuentes: ["../plantilla-sus/spec.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[calculo]] · [[formula]] · [[latex]] · [[sus]] · [[usabilidad]]

Cálculo estándar SUS por participante:
1. Para cada ítem impar (1,3,5,7,9): contribución = respuesta - 1
2. Para cada ítem par (2,4,6,8,10): contribución = 5 - respuesta
3. Sumar las 10 contribuciones
4. Multiplicar por 2.5 → puntuación final 0-100

Ejemplo con participante U1 (5,1,5,1,4,2,5,1,5,1):
- Impares: (5-1)+(5-1)+(4-1)+(5-1)+(5-1) = 4+4+3+4+4 = 19
- Pares: (5-1)+(5-1)+(5-2)+(5-1)+(5-1) = 4+4+3+4+4 = 19
- Total: 38 × 2.5 = 95.0

La plantilla debe incluir la fórmula en notación matemática y este ejemplo resuelto.

> Ítems impares: respuesta − 1 · Ítems pares: 5 − respuesta · Suma de las 10 contribuciones × 2,5 → puntuación de 0 a 100
> — `../plantilla-sus/spec.md` (cita sin comprobar)

Origen: [[proyectos/plantilla-sus/estado|plantilla-sus]]
