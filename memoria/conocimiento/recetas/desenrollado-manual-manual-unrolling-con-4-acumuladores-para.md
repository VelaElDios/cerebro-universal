---
tipo: "receta"
titulo: "Desenrollado manual (Manual Unrolling) con 4 acumuladores para romper cadena de dependencia y subir IPC"
temas: ["ac", "ilp", "optimizacion", "pipeline"]
claves: ["manual unrolling", "ILP", "dependency chain", "accumulator", "IPC", "-O1", "tarea4_1_ilp.cpp", "acc1 acc2 acc3 acc4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[optimizacion]] · [[pipeline]]

Problema: `sumA += v[i]` crea dependencia RAW (Read-After-Write) en `sumA`; latencia de ADD (~3-4 ciclos) frena pipeline → IPC bajo. Solución: desenrollar bucle 4× con 4 acumuladores independientes:
```cpp
float acc1=0, acc2=0, acc3=0, acc4=0;
for (size_t i=0; i<N; i+=4) {
    acc1 += v[i];
    acc2 += v[i+1];
    acc3 += v[i+2];
    acc4 += v[i+3];
}
float sum = acc1 + acc2 + acc3 + acc4;
```
Compilar con `-O1` para que el compilador NO haga auto-unrolling. Esperado: IPC ~2-4× mayor, cycles ~½, mismo instructions. N debe ser múltiplo de 4.

> Una solución es reestructurar el código repartiendo el cálculo en varias variables independientes (por ejemplo: acc1, acc2, acc3 y acc4).
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf`

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[formula-del-techo-roofline-mononucleo]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
