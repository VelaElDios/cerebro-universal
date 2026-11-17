---
tipo: "concepto"
titulo: "Definición de speedup como razón de tiempos de ejecución"
temas: ["ac", "arquitectura-computadores", "metricas-rendimiento", "speedup"]
claves: ["speedup", "tiempo ejecución", "razón", "aceleración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[metricas-rendimiento]] · [[speedup]]

Speedup de X respecto a Y = Tiempo_Ejecución_X / Tiempo_Ejecución_Y. Si speedup > 1, X es más rápido. Es la métrica universal de mejora de rendimiento. Combinada con la ecuación fundamental permite descomponer el speedup en mejoras de IC, CPI o frecuencia. Base de la ley de Amdahl y del modelo Roofline (speedup teórico = techo / rendimiento actual).

> 𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑅𝑋𝑋 = 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛 𝑑𝑑𝑑𝑑 𝑋𝑋 / 𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇𝑇 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛 𝑑𝑑𝑑𝑑 𝑌𝑌
> — `repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf` (cita sin comprobar)

Relacionado: [[ley-de-amdahl-para-speedup-con-mejora-parcial]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
