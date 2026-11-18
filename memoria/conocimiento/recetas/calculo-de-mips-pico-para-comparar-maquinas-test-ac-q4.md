---
tipo: "receta"
titulo: "Cálculo de MIPS pico para comparar máquinas (test AC Q4)"
temas: ["ac", "cpi", "mips", "rendimiento"]
claves: ["MIPS-pico", "CPI-medio", "frecuencia-reloj", "mezcla-instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[mips]] · [[rendimiento]]

Pasos para obtener MIPS pico (máximo teórico, sin stalls):
1. Calcular CPI medio ponderado: `CPI_medio = Σ (fracción_tipo_i × CPI_tipo_i)`.
   - M1: `0.4×2 + 0.5×8 + 0.1×4 = 5.2` ciclos/inst.
   - M2: `4` ciclos/inst (uniforme).
2. MIPS = `frecuencia_MHz / CPI_medio`.
   - M1: `600 / 5.2 ≈ 115.4` MIPS.
   - M2: `1000 / 4 = 250` MIPS.
3. Comparar: M2 tiene mayor MIPS pico. La frecuencia alta compensa el CPI fijo.

> Queremos analizar el rendimiento de dos máquinas, M1 y M2, que soportan el mismo repertorio de instrucciones. En dicho repertorio hay tres tipos de instrucciones, A, B, y C. M1 necesita 2, 8 y 4 ciclos de reloj para ejecutar las instrucciones de tipo A, B y C, respectivamente. Por su parte, M2 emplea 4 ciclos para todos los tipos. M1 tiene una frecuencia de reloj de 600 MHz y M2 una frecuencia de 1 GHz. El programa de prueba que vamos a emplear tiene la siguiente mezcla de instrucciones: 40% de tipo A, 50% de tipo B, y 10% de tipo C. Cual de las dos máquinas tiene mayor MIPS máximo (de pico).
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf`

Relacionado: [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-f]] · [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-c]] · [[comparativa-de-rendimiento-mips-entre-dos-implementaciones-c]]
