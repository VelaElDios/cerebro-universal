---
tipo: "concepto"
titulo: "Tipos de dependencias en bucles: loop-independent vs loop-carried"
temas: ["ac", "bucles", "dependencias", "paralelismo-instruccion", "vectorizacion"]
claves: ["loop-independent", "loop-carried", "distance vector", "direction vector", "dependencia entre iteraciones", "dependencia misma iteración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[paralelismo-instruccion]] · [[vectorizacion]]

Clasificación fundamental para paralelismo de bucles:
- **Loop-independent (misma iteración)**: dependencia entre instrucciones dentro de una misma iteración `i`. No impide ejecución paralela de distintas iteraciones. Ej: Ej.3 I1 `a[i]=b[i]+a[i]` → I2 `c[i+1]=a[i]+d[i]` (RAW en `a[i]` misma `i`).
- **Loop-carried (entre iteraciones)**: dependencia entre instrucción en iteración `i` e instrucción en iteración `j ≠ i`. Impide paralelismo entre esas iteraciones (o requiere sincronización). Se caracteriza por **vector distancia** `d = j - i` (positivo = flujo hacia adelante).
  - Ej.3: I3 `a[i-1]=2*b[i]` escribe `a[i-1]`; I1 iteración `i+1` lee `a[i+1]`? No. I1 iteración `i` lee `a[i]`. I3 iteración `i` escribe `a[i-1]`. I1 iteración `i-1` escribe `a[i-1]` → WAW loop-carried distancia 1 en `a`.
  - Ej.8 RISC-V: no hay dependencias de memoria loop-carried porque `addi x1,x1,8` y `addi x2,x2,8` avanzan punteros a elementos distintos cada iteración.
La dirección (`<`, `>`, `=`) y distancia determinan si se puede vectorizar, desenrollar o paralelizar el bucle.

> Indica para cada una de ellas si se trata de una dependencia entre diferentes iteraciones del bucle.
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf`

Relacionado: [[identificacion-de-dependencias-loop-carried-en-bucles-c-styl]]
