---
tipo: "receta"
titulo: "Cálculo de MIPS pico a partir de mezcla de instrucciones y frecuencias"
temas: ["ac", "mips", "rendimiento"]
claves: ["MIPS pico", "frecuencia reloj", "ciclos por instrucción", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[rendimiento]]

Para calcular MIPS pico: 1) Hallar CPI medio ponderado = Σ(%tipo_i × ciclos_tipo_i). 2) MIPS = (Frecuencia_MHz) / CPI_medio. Ejemplo M1: CPI = 0.4×3 + 0.5×6 + 0.1×4 = 1.2+3.0+0.4 = 4.6 ciclos. MIPS = 400/4.6 ≈ 86.96 ≈ 87. M2: CPI = 4 ciclos (uniforme). MIPS = 750/4 = 187.5. La opción correcta es "Para M1 es 87 y para M2 es 187.5".

> M1 necesita 3, 6, y 4 ciclos de reloj para ejecutar las instrucciones de tipo A, B y C, respectivamente. Por su parte, M2 emplea 4 ciclos para todos los tipos. M1 tiene una frecuencia de reloj de 400 MHz y M2 una frecuencia de 750 MHz. El programa de prueba que vamos a emplear tiene la siguiente mezcla de instrucciones: 40% de tipo A, 50% de tipo B, y 10% de tipo C.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`
