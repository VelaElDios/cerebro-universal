---
tipo: "concepto"
titulo: "Definición de MIPS (Millones de Instrucciones Por Segundo)"
temas: ["ac", "arquitectura-computadores", "metricas-rendimiento", "mips", "métricas"]
claves: ["MIPS", "instrucciones", "tiempo ejecución", "millón"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf", "repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[metricas-rendimiento]] · [[mips]]

MIPS = (número de instrucciones ejecutadas) / (tiempo de ejecución en segundos × 10⁶). Mide throughput de instrucciones enteras/simples. Útil para comparar procesadores con ISA similar, pero no captura complejidad de instrucciones ni trabajo real (punto flotante, memoria). El documento incluye la fórmula invertida errónea (MIPS = tiempo × 10⁶); la correcta divide instrucciones entre tiempo.

> 𝑀𝑀𝑀𝑀𝑀𝑀𝑀𝑀 = 𝑛𝑛ú𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 𝑑𝑑𝑑𝑑 𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖 × 106 / 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛
> — `repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]

## Ampliación (2026-11-17, )
MIPS mide la tasa de ejecución de instrucciones. El temario da cuatro formas equivalentes: (1) MIPS = IC / (t_ejec × 10^6); (2) MIPS = IC / (ciclos × t_ciclo × 10^6); (3) MIPS = (IC × f_reloj) / (IC × CPI × 10^6); (4) MIPS = f_reloj / (CPI × 10^6). Donde IC = instruction count, CPI = ciclos por instrucción, f_reloj = frecuencia. La última forma muestra que MIPS depende solo de frecuencia y CPI medio.
