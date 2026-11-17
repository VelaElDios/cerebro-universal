---
tipo: "concepto"
titulo: "Definición de MFLOPS (Millones de Operaciones de Punto Flotante Por Segundo)"
temas: ["ac", "arquitectura-computadores", "metricas-rendimiento", "mflops", "métricas"]
claves: ["MFLOPS", "punto flotante", "FLOPS", "tiempo ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf", "repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[metricas-rendimiento]] · [[mflops]]

MFLOPS = (operaciones de punto flotante realizadas) / (tiempo de ejecución en segundos × 10⁶). Métrica estándar para cargas científicas/HPC. El documento también muestra una forma alternativa vía frecuencia y CPI: MFLOPS = (frecuencia en MHz) / CPI, asumiendo 1 FLOP/ciclo; para SIMD/FMA hay que multiplicar por ancho de vector y ops por instrucción (ej. AVX2 FMA = 2 FLOPs/ciclo por lane).

> 𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 = 𝑛𝑛ú𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 𝑑𝑑𝑑𝑑 𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜 𝑑𝑑𝑑𝑑 𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓 / (𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛 × 106)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[formula-del-techo-roofline-mononucleo]]

## Ampliación (2026-11-17, )
MFLOPS cuenta operaciones de punto flotante (suma, multiplicación, división, etc.) por segundo. El temario advierte que MFLOPS «Cambia con la mezcla de: operaciones rápidas y lentas de punto flotante; operaciones de enteros y de punto flotante». Por tanto, no es una métrica portable entre cargas de trabajo distintas; sirve para comparar un mismo kernel en distintas máquinas.
