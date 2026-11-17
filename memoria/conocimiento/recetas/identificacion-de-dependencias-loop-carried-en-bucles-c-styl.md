---
tipo: "receta"
titulo: "Identificación de dependencias loop-carried en bucles (C-style y RISC-V)"
temas: ["ac", "bucles", "dependencias-entre-iteraciones", "loop-carried", "paralelismo-instruccion"]
claves: ["loop-carried", "dependencia entre iteraciones", "vectorización", "paralelismo de bucles", "distance vector"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucles]] · [[dependencias-entre-iteraciones]] · [[loop-carried]] · [[paralelismo-instruccion]]

Metodología para detectar dependencias entre iteraciones (loop-carried):
1. Representa cada acceso a array como `array[índice]` donde el índice depende de `i`.
2. Compara accesos a mismo array entre instrucciones Sx (iteración i) y Sy (iteración j).
3. Hay dependencia loop-carried si existe solución entera a `índice_x(i) = índice_y(j)` con `i ≠ j` y `i,j` en rango del bucle.
4. La distancia es `j - i` (positiva = dependencia hacia adelante).
Ejemplos del trozo:
- Ej.3: `a[i] = b[i] + a[i]` (I1) y `a[i-1] = 2*b[i]` (I3) → `a[i]` (escritura I1 iter i) vs `a[i-1]` (escritura I3 iter i) → mismo i, no loop-carried. Pero `a[i]` (I1 iter i) vs `a[i-1]` (I3 iter i+1) → `i = (i+1)-1` → dependencia loop-carried distancia 1 (WAW en a).
- Ej.4: `c[i] = a[i+1]+b[i+1]` (S1) y `c[i+1] = a[i-1]` (S4) → `c[i]` (S1 iter i) vs `c[i+1]` (S4 iter i) → mismo i. `c[i]` (S1 iter i) vs `c[i+1]` (S4 iter i-1) → `i = (i-1)+1` → loop-carried distancia 1 (RAW en c).
- Ej.8 (RISC-V): `fld f0,0(x1)` (i1) y `fsd f0,0(x1)` (i5) misma iteración → RAW en memoria. Entre iteraciones: `addi x1,x1,8` (i6) cambia dirección → no hay dependencia de memoria entre iteraciones (distintas direcciones).

> Indica para cada una de ellas si se trata de una dependencia entre diferentes iteraciones del bucle.
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2_Prob_RISCV_rev.pdf`
