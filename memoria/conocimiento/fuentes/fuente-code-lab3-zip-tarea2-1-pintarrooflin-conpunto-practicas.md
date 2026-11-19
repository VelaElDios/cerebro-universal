---
tipo: "fuente"
titulo: "Code Lab3.zip!tarea2 1 pintarRoofLin conPunto (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_pintarRoofLin_conPunto.py`.

## Resumen
Script de Python para visualizar el modelo Roofline mononúcleo: calcula el techo de cómputo (GFLOPS máx) a partir de la frecuencia de CPU y FLOPS/ciclo (32 con AVX2+FMA), el punto de inflexión (I_KNEE = GFLOPS_MAX / BW_DRAM), dibuja la curva techo (mínimo entre BW_DRAM·intensidad y GFLOPS_MAX), colorea zonas memory-bound (intensidad ≤ I_KNEE) y compute-bound (intensidad > I_KNEE), y superpone tres puntos medidos (Temporal, Secuencial, Aleatorio) con sus coordenadas (intensidad aritmética, rendimiento).

## Lo que se sacó de él (6)
- [[clasificacion-memory-bound-vs-compute-bound-en-el-modelo-roo]]
- [[como-calcular-el-techo-de-computo-gflops-max-y-el-punto-de-i]]
- [[como-trazar-el-modelo-roofline-con-matplotlib-escala-log-log]]
- [[derivacion-de-flopspercycle-32-para-x86-con-avx2-y-fma]]
- [[uso-de-todo1-y-todo2-como-puntos-de-personalizacion-obligato]]
- [[valores-de-ejemplo-de-intensidad-y-rendimiento-para-tres-pat]]
