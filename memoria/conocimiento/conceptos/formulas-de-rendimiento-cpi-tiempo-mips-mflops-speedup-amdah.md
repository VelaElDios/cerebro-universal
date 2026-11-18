---
tipo: "concepto"
titulo: "Fórmulas de rendimiento (CPI, tiempo, MIPS, MFLOPS, speedup, Amdahl) referencia examen AC"
temas: ["ac", "formulas", "rendimiento"]
claves: ["CPI", "tiempo ejecución", "frecuencia reloj", "MIPS", "MFLOPS", "speedup", "ley Amdahl"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[formulas]] · [[rendimiento]]

Resumen de fórmulas estándar que aparecen al final del examen (texto parcialmente corrupto en PDF): 1) CPI = ciclos_reloj / instrucciones_ejecutadas. 2) Tiempo_ejecución = instrucciones × CPI / frecuencia_reloj = instrucciones × CPI × período_reloj. 3) MIPS = instrucciones_ejecutadas / (tiempo_ejecución × 10^6) = frecuencia_reloj / (CPI × 10^6). 4) MFLOPS = ops_flotantes / (tiempo_ejecución × 10^6). 5) Speedup = tiempo_sin_mejora / tiempo_con_mejora. 6) Amdahl: speedup_global = 1 / ((1-fracción_mejorada) + fracción_mejorada/mejora_parcial). Útiles para apartados de análisis de rendimiento.

> 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛 = 𝑛𝑛ú𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 𝑑𝑑𝑑𝑑 𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖 × 𝐶𝐶𝐶𝐶𝐶𝐶 × 𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑ó𝑛𝑛 𝑑𝑑𝑑𝑑 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑑𝑑𝑑𝑑 𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

Relacionado: [[calculo-speedup-vliw-vs-escalar-para-examen-enero-2026-probl]] · [[calculo-de-cpi-medio-mips-y-speedup-entre-dos-maquinas]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-y-frecuencia]] · [[speedup-con-cambio-simultaneo-de-cpi-y-frecuencia-de-reloj]]
