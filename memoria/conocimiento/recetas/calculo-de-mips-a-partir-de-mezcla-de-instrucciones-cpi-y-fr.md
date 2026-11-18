---
tipo: "receta"
titulo: "Cálculo de MIPS a partir de mezcla de instrucciones, CPI y frecuencia"
temas: ["ac", "cpi", "mips", "rendimiento"]
claves: ["MIPS", "CPI medio", "frecuencia reloj", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[mips]] · [[rendimiento]]

CPI_medio = Σ(frecuencia_i × ciclos_i) = 0.4×2 + 0.3×4 + 0.3×6 = 3.8 ciclos/instr. MIPS = Frecuencia(MHz) / CPI_medio = 1000 / 3.8 ≈ 263.15 MIPS. Respuesta correcta: 263,15 (opción b).

> Tenemos una máquina que su repertorio de instrucciones tiene tres tipos de instrucciones A, B y C, que necesitan 2, 4 y 6 ciclos respectivamente para ejecutarse, la máquina tiene una frecuencia de reloj de 1 GHz. El programa de prueba que vemos a emplear tiene la siguiente mezcla de instrucciones: 40% tipo A, 30% tipo B y 30% tipo C. Indica la velocidad en MIPS.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[calculo-de-mips-a-partir-de-frecuencia-cpi-por-tipo-y-mezcla]] · [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-f]] · [[calculo-de-mips-con-cpi-ponderado-y-frecuencia-de-reloj]]
