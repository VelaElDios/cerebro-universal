---
tipo: "receta"
titulo: "Cálculo de MIPS con CPI ponderado y frecuencia de reloj"
temas: ["ac", "mips", "rendimiento"]
claves: ["MIPS", "CPI", "frecuencia", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[rendimiento]]

Para calcular MIPS (Millones de Instrucciones Por Segundo) dado frecuencia (Hz) y CPI medio: 1) Calcular CPI ponderado = Σ (CPI_i × %_i). 2) MIPS = Frecuencia (MHz) / CPI_ponderado. En el ejemplo: CPI_ponderado = 2×0.4 + 3×0.25 + 4×0.25 + 5×0.1 = 0.8 + 0.75 + 1.0 + 0.5 = 3.05. MIPS = 500 / 3.05 ≈ 163.93 → respuesta b) 163,9.

> Sea una máquina con una frecuencia de reloj de 500 MHz y con los siguientes CPI para cada uno de los cuatro tipos de instrucción soportados: Tipo CPI A 2 B 3 C 4 D 5 Asumiendo la siguiente mezcla de instrucciones para un programa de prueba determinado: Tipo % A 40% B 25% C 25% D 10% ¿Cuál es el valor de MIPS para dicha máquina?
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[benchmarks-sinteticos-dhrystone-y-whetstone-proposito-y-orig]]
