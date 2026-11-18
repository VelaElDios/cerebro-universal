---
tipo: "receta"
titulo: "Cálculo de mejora necesaria con Ley de Amdahl (fracción mejorable y speedup global)"
temas: ["ac"]
claves: ["Amdahl", "speedup", "fracción mejorable", "tiempo ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Fracción mejorable f = 110/135 ≈ 0.8148. Speedup global deseado S = 2. Ley de Amdahl: S = 1 / ((1-f) + f/k) → 2 = 1 / (0.1852 + 0.8148/k) → 0.1852 + 0.8148/k = 0.5 → 0.8148/k = 0.3148 → k = 0.8148/0.3148 ≈ 2.59. Respuesta: 2,59 (opción b).

> Supongamos que un programa tarda en ejecutarse 135 segundos de los cuales 110 los utilizo en operaciones de suma, ¿cuánto tengo que mejorar la velocidad de la suma para que el programa se ejecute al doble de velocidad?
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[aplicacion-de-la-ley-de-amdahl-para-acelerar-una-fraccion-de]] · [[calculo-de-factor-de-mejora-con-ley-de-amdahl-pregunta-3-exa]] · [[aplicacion-de-la-ley-de-amdahl-para-speedup-global-mejorando]]
