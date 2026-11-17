---
tipo: "receta"
titulo: "Comparación de dos implementaciones de la misma ISA (CPI y frecuencia distintos)"
temas: ["ac", "cpi", "frecuencia-reloj", "rendimiento", "tiempo-ejecucion"]
claves: ["máquina A", "máquina B", "ciclo reloj 1 ns", "CPI 2", "ciclo reloj 2 ns", "CPI 1.2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[frecuencia-reloj]] · [[rendimiento]] · [[tiempo-ejecucion]]

**Problema**: Misma ISA, mismo programa → mismo nº de instrucciones (I).
- Máquina A: ciclo = 1 ns, CPI = 2 → T_A = I × 2 × 1 ns = 2I ns.
- Máquina B: ciclo = 2 ns, CPI = 1.2 → T_B = I × 1.2 × 2 ns = 2.4I ns.
**Resultado**: A es más rápida. Speedup = T_B / T_A = 2.4I / 2I = 1.2× (A es 20 % más rápida).
Lección: **frecuencia más alta no garantiza mejor rendimiento**; el CPI (organización) compensa.

> La máquina A tiene un ciclo de reloj de 1 ns y un CPI de 2 para un programa concreto, mientras que la máquina B tiene un tiempo de ciclo de 2 ns y un CPI de 1.2 para el mismo programa
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[formula-del-tiempo-de-ejecucion-de-cpu-y-sus-tres-factores]] · [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
