---
tipo: "dato"
titulo: "Limitaciones del paralelismo en bloques básicos y solución a nivel de bucle"
temas: ["ac", "bloque-basico", "ilp", "paralelismo-bucle"]
claves: ["bloque básico", "basic block", "15% saltos", "5-7 instrucciones", "paralelismo a nivel de bucle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bloque-basico]] · [[ilp]] · [[paralelismo-bucle]]

Datos empíricos que justifican ir más allá del bloque básico: los saltos son frecuentes (15 %) y los bloques son cortos (5-7 instrucciones), por lo que el ILP intra-bloque es bajo. La solución estándar es explotar paralelismo entre iteraciones de bucles (loop-level parallelism) mediante técnicas como desenrollamiento, segmentación software o planificación de trazas.

> Estadísticas:            el 15% del código son instrucciones de salto  hay 5, 6 o 7 instrucciones en un bloque básico  Conclusión: el paralelismo con bloques básicos está limitado  Solución: Explotar el ILP a lo largo de varios bloques básicos  Aumentar el ILP solapando varios bloques básicos  Conseguir independencia entre iteraciones de un bucle  Apoyarse en el paralelismo a nivel de bucle
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[relacion-ilp-y-cpi-en-procesadores-segmentados]] · [[tecnicas-avanzadas-estaticas-y-dinamicas-para-reducir-detenc]] · [[impacto-de-la-frecuencia-de-saltos-en-el-ilp-y-tamano-de-blo]] · [[que-es-un-bloque-basico-basic-block-en-ilp]]
