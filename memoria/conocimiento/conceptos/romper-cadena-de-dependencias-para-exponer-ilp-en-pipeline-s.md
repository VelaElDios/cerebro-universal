---
tipo: "concepto"
titulo: "Romper cadena de dependencias para exponer ILP en pipeline superscalar"
temas: ["ac", "dependency-chain", "ilp", "pipeline", "superscalar"]
claves: ["dependency chain", "ILP", "pipeline stall", "superscalar", "ALU", "instruction-level parallelism"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependency-chain]] · [[ilp]] · [[pipeline]] · [[superscalar]]

**Problema fundamental**: En un pipeline superscalar moderno (ej. Intel Skylake: 4 ALUs, 2 puertos FP add), una cadena de dependencia serial `sum += v[i]` fuerza:

```
Ciclo 1:  LOAD v[0]  →  ADD sum+v[0]  (latencia ~4 ciclos)
Ciclo 2:  LOAD v[1]  →  WAIT (depende de sum anterior)
Ciclo 3:  LOAD v[2]  →  WAIT
Ciclo 4:  LOAD v[3]  →  WAIT
Ciclo 5:  ADD sum+v[1]  →  ...
```

**Resultado**: Solo 1 ADD cada 4 ciclos → **IPC ~0.25** para la parte FP, desperdiciando 3 ALUs.

**Solución (unrolling + múltiples acumuladores)**: Crea 4 cadenas independientes:
```
acc1 += v[i]     acc2 += v[i+1]     acc3 += v[i+2]     acc4 += v[i+3]
```
Ahora el scheduler puede emitir 4 ADDs en paralelo (uno por ciclo si hay puertos) → **IPC ~1-4** según puertos FP add disponibles.

**Límite real**: Latencia FP add (3-4 ciclos) + puertos de ejecución (2 FP add en Skylake) → máx teórico 2 ADDs/ciclo = 2 FLOPs/ciclo (sin vectorizar). Con AVX2/FMA se llega a 32 FLOPs/ciclo (ver nota "Cálculo de FLOPS por ciclo en x86 con AVX2/FMA").

> // - Cada iteración depende estrictamente del resultado de la anterior, // generando parones (stalls) y desaprovechando las múltiples ALUs de la CPU.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache]] · [[desenrollado-manual-manual-unrolling-con-4-acumuladores-para]] · [[optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul]] · [[problema-de-desenrollado-y-planificacion-de-bucle-superescal]]
