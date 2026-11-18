---
tipo: "receta"
titulo: "Cálculo de ganancia de velocidad (speedup) con la ley de Amdahl"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["speedup", "ley de Amdahl", "fracción mejorada", "factor mejora"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Speedup = 1 / ((1 - fracción_mejorada) + (fracción_mejorada / factor_mejora)). Ejemplo: fracción=0.2, factor=4 → Speedup = 1 / (0.8 + 0.05) = 1/0.85 ≈ 1.1765. Ganancia porcentual = (Speedup - 1) * 100% ≈ 17.6%. La opción correcta es "17,6 %".

> Supongamos que mejoramos una máquina de modo que las instrucciones de suma de coma flotante se ejecuten 4 veces más rápido. Si el tiempo de ejecución de un benchmark sin la mejora era de 100 segundos, ¿cuál será la ganancia en velocidad si el 20% del tiempo de ejecución se emplea en ejecutar instrucciones de suma en coma flotante?
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[speedup-por-ley-de-amdahl-con-mejora-10x-usada-20-del-tiempo]] · [[calculo-de-speedup-con-ley-de-amdahl-mejora-de-una-fraccion]] · [[calculo-de-speedup-con-ley-de-amdahl-mejora-10x-en-punto-flo]]
