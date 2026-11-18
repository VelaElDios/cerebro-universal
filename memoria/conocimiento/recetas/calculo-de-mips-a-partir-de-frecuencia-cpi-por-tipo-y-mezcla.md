---
tipo: "receta"
titulo: "Cálculo de MIPS a partir de frecuencia, CPI por tipo y mezcla de instrucciones"
temas: ["ac", "mips", "rendimiento"]
claves: ["MIPS", "CPI", "frecuencia", "mezcla instrucciones", "promedio ponderado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[rendimiento]]

Para calcular MIPS: 1) Calcular CPI medio = Σ (CPI_i × %_i / 100). 2) MIPS = (Frecuencia en MHz) / CPI_medio. En el ejemplo: CPI_medio = 2×0.4 + 3×0.25 + 4×0.25 + 5×0.1 = 0.8 + 0.75 + 1.0 + 0.5 = 3.05. MIPS = 500 / 3.05 ≈ 163.9 MIPS (opción b).

> Assuming the following instruction mix for a given test program: Type % A 40 B 25 C 25 D 10 What would be the MIPS value for this computer?
> — `repo:datos/temarios/AC/examenes/January2018.pdf`
