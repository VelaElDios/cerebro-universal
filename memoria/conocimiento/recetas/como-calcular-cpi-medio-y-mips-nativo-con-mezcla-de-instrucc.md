---
tipo: "receta"
titulo: "Cómo calcular CPI medio y MIPS nativo con mezcla de instrucciones"
temas: ["ac", "cpi", "evaluacion-rendimiento", "mezcla-instrucciones", "mips-nativo"]
claves: ["CPI medio", "MIPS nativo", "mezcla instrucciones", "frecuencia reloj"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[evaluacion-rendimiento]] · [[mezcla-instrucciones]] · [[mips-nativo]]

1. CPI_medio = Σ (fracción_i × CPI_i) para cada clase de instrucción i.
2. MIPS_nativo = Frecuencia_Hz / (CPI_medio × 10^6).
3. Si una máquina solo tiene un tipo de instrucción (ej. MNFP solo enteras con CPI=2), CPI_medio = ese CPI fijo.

Ejemplo (Ejercicio 3):
- MFP (con FP hardware): mezcla 10% mult FP (6 ciclos), 15% add FP (4), 5% div FP (20), 70% enteras (2) → CPI = 3.6 → MIPS = 1000/3.6 = 277.78.
- MNFP (sin FP, todo entero CPI=2): CPI = 2 → MIPS = 1000/2 = 500.

> Calculamos en primer lugar el CPI para MFP, teniendo en cuenta la mezcla de instrucciones en el programa de prueba y los ciclos requeridos para cada tipo de instrucción: CPI_MFP = Σ p_i × CPI_i = 0.1 × 6 + 0.15 × 4 + 0.05 × 20 + 0.7 × 2 = 3.6 ciclos/instrucción
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[calculo-de-mips-nativos-y-de-pico-peak-mips-para-maquinas-co]] · [[calculo-de-mips-nativo-a-partir-de-mezcla-de-instrucciones-y]] · [[calculo-de-mips-con-cpi-ponderado-y-frecuencia-de-reloj]]
