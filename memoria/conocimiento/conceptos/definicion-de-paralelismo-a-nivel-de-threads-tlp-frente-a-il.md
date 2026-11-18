---
tipo: "concepto"
titulo: "Definición de paralelismo a nivel de threads (TLP) frente a ILP y DLP"
temas: ["ac", "paralelismo"]
claves: ["TLP", "ILP", "DLP", "Flynn", "streams instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2011.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[paralelismo]]

El TLP (Thread-Level Parallelism) explota hilos de control independientes (múltiples instruction streams), a diferencia del ILP (paralelismo implícito en código lineal/bucles) y el DLP (misma operación sobre grandes volúmenes de datos, tipo SIMD).

> Se usan múltiples streams de instrucciones que son inherentemente paralelos
> — `repo:datos/temarios/AC/examenes/Enero2011.pdf`

Relacionado: [[tendencias-de-paralelismo-en-arquitectura-actual-ilp-tlp-dlp]] · [[tecnica-de-mejora-de-rendimiento-en-sisd]] · [[paralelismo-a-nivel-de-bucle-lp-solapamiento-de-iteraciones]]
