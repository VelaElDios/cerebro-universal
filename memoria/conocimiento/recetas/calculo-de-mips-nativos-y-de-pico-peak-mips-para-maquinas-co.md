---
tipo: "receta"
titulo: "Cálculo de MIPS nativos y de pico (peak MIPS) para máquinas con CPI variable"
temas: ["ac", "arquitectura-computadores", "cpi", "mips", "rendimiento"]
claves: ["MIPS", "peak MIPS", "CPI medio", "frecuencia reloj", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[cpi]] · [[mips]] · [[rendimiento]]

MIPS_nativos = Freq_Hz / (CPI_medio * 1e6). CPI_medio = Σ (CPI_i * %_i). M1: CPI_medio = 2*0.4 + 6*0.5 + 4*0.1 = 4.2 → MIPS = 400e6/(4.2e6)=95.24. M2: CPI=3 constante → MIPS=750e6/(3e6)=250. Peak MIPS: usa CPI_mínimo (mejor caso). M1: CPI_min=2 (tipo A) → Peak=400e6/(2e6)=200. M2: CPI constante → Peak = Nativos = 250.

> MIPS = Frecuencia / (CPI × 10^6). Los MIPS de pico para M1 se calculan considerando únicamente instrucciones de tipo A.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
