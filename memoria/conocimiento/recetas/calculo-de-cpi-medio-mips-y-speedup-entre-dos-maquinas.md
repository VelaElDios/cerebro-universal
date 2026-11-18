---
tipo: "receta"
titulo: "Cálculo de CPI medio, MIPS y speedup entre dos máquinas"
temas: ["ac", "cpi", "mips", "rendimiento", "speedup"]
claves: ["CPI medio", "MIPS", "speedup", "mezcla instrucciones", "frecuencia reloj"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[mips]] · [[rendimiento]] · [[speedup]]

1) CPI medio ponderado por mezcla: Σ(CPI_i × %_i). Mbase: 2×0.4+3×0.25+3×0.25+5×0.1=2.8. Mopt: 2×0.4+2×0.25+3×0.25+4×0.1=2.45. 2) MIPS = Frec(MHz)/CPI. Mbase: 500/2.8=178.57. Mopt: 600/2.45=244.9. 3) Speedup = (CPI_base × Frec_opt) / (CPI_opt × Frec_base) = (2.8×600)/(2.45×500)=1.37. Mopt 37% más rápida.

> CPI = Σ CPI_i × p_i; MIPS = Frecuencia / (CPI × 10^6); speedup = (CPI_base × Frec_opt) / (CPI_opt × Frec_base)
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[calculo-de-mips-nativos-y-de-pico-peak-mips-para-maquinas-co]] · [[calculo-de-mips-con-cpi-ponderado-y-frecuencia-de-reloj]] · [[comparativa-de-rendimiento-mips-entre-dos-implementaciones-c]]
