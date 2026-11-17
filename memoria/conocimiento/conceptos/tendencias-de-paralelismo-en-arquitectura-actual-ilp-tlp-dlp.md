---
tipo: "concepto"
titulo: "Tendencias de paralelismo en arquitectura actual (ILP, TLP, DLP, multinúcleo)"
temas: ["ac", "dlp", "ilp", "paralelismo", "tlp"]
claves: ["ILP", "TLP", "DLP", "paralelismo a nivel de CPUs", "temas 1-7", "tema 8"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dlp]] · [[ilp]] · [[paralelismo]] · [[tlp]]

Cuatro ejes de paralelismo que estructuran el temario:
- ILP (Instruction-Level Parallelism): paralelismo implícito en código secuencial/bucles (temas 1-7). Técnicas: segmentación, superescalar, VLIW, predicción de saltos, ejecución fuera de orden.
- TLP (Thread-Level Parallelism): hilos inherentemente paralelos (tema 8). Multihilo, multiprocesamiento simétrico (SMP), chip multiprocesador (CMP).
- DLP (Data-Level Parallelism): mismas operaciones sobre grandes volúmenes de datos (tema 8). SIMD, extensiones multimedia (SSE, AVX), GPUs.
- Paralelismo a nivel de CPUs: múltiples procesadores completos (tema 8). Clusters, NUMA, warehouse-scale.

> Tendencias en arquitectura de computadores  Paralelismo a nivel de instrucción (ILP) – explota el paralelismo implícito dentro de un segmento de código lineal o un bucle (temas 1-7)  Paralelismo a nivel de thread (TLP) – uso de múltiples flujos (streams) de instrucciones que son inherentemente paralelos (tema 8)  Paralelismo a nivel de datos (DLP) – realiza operaciones idénticas sobre grandes volúmenes de datos (tema 8)  Paralelismo a nivel de CPUs – uso de múltiples procesadores (tema 8)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf (trozo 3 de 5)`
