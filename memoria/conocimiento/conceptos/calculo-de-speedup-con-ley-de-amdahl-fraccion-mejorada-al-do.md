---
tipo: "concepto"
titulo: "Cálculo de speedup con ley de Amdahl: fracción mejorada al doble de velocidad"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["speedup", "Amdahl", "instrucciones enteras", "fracción mejorada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Ejemplo clásico de ley de Amdahl: speedup = 1 / ((1 - f) + f/k) donde f = 0.5 (mitad del tiempo en enteros) y k = 2 (doble velocidad). Speedup = 1 / (0.5 + 0.5/2) = 1 / 0.75 = 1.33. La respuesta correcta es a) 1.33.

> Let’s assume that we improve a computer by making all integer instructions run twice as fast. If a test program runs for 20 seconds before the improvement, what will be the speedup if half of this time is spent executing integer instructions?
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-para-instrucciones-de-p]] · [[speedup-por-ley-de-amdahl-con-mejora-10x-usada-20-del-tiempo]] · [[calculo-de-speedup-con-ley-de-amdahl-mejora-10x-en-punto-flo]]
