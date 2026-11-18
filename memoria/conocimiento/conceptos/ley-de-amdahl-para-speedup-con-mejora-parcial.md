---
tipo: "concepto"
titulo: "Ley de Amdahl para speedup con mejora parcial"
temas: ["ac", "arquitectura-computadores", "ley-amdahl", "speedup"]
claves: ["speedup", "mejora", "fracción mejorada", "fracción no mejorada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[ley-amdahl]] · [[speedup]]

La ley de Amdahl expresa el speedup global cuando solo una fracción del código se optimiza. Si una fracción `f` del tiempo original se acelera `k` veces, el speedup total es `1 / ((1-f) + f/k)`. El documento muestra la formulación aditiva: tiempo total = tiempo parte no mejorada + tiempo parte mejorada. Es clave para decidir si vale la pena optimizar un subsistema (vectorización, caché, paralelismo) y predecir el techo de ganancia.

> 𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎𝑎ó𝑛 𝑑𝑑𝑑𝑑𝑑𝑑 𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟 = 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛 𝑠𝑠𝑠𝑠𝑠𝑠 𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢 𝑙𝑙 𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 + 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛 𝑐𝑒𝑐𝑐 𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚
> — `repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf` (cita sin comprobar)

Relacionado: [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[ley-de-amdahl-la-aceleracion-maxima-viene-determinada-por-la]] · [[ley-de-amdahl-aplicada-a-speedup-con-mejora-parcial-de-un-su]] · [[calculo-de-speedup-con-ley-de-amdahl-mejora-de-una-fraccion]]
