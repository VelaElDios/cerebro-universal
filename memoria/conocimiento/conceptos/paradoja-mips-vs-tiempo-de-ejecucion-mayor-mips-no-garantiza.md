---
tipo: "concepto"
titulo: "Paradoja MIPS vs tiempo de ejecución: mayor MIPS no garantiza menor tiempo"
temas: ["ac", "compiladores", "evaluacion-rendimiento", "mips", "tiempo-ejecucion"]
claves: ["MIPS", "tiempo ejecución", "compilador", "CPI", "frecuencia reloj", "instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compiladores]] · [[evaluacion-rendimiento]] · [[mips]] · [[tiempo-ejecucion]]

MIPS = Instrucciones / (Tiempo × 10^6). Tiempo = Ciclos_totales / Frecuencia.
- Compilador 1: 7M instrucciones, 10M ciclos → Tiempo = 12.5s → MIPS = 560.
- Compilador 2: 12M instrucciones, 15M ciclos → Tiempo = 18.75s → MIPS = 640.
El compilador 2 genera más instrucciones (mayor cuenta) pero con CPI medio menor (1.25 vs 1.43), subiendo MIPS; sin embargo, el aumento de instrucciones supera la ganancia en CPI, resultando en más ciclos totales y mayor tiempo real.
Conclusión: MIPS es métrica engañosa para comparar código real; el tiempo de ejecución (o ciclos totales) es la métrica correcta.

> Lo que quiere decir que el código obtenido por el compilador 2 tiene un mayor MIPS.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[ejercicios-de-cpi-mips-y-tiempo-de-ejecucion-con-mezcla-de-i]] · [[definicion-de-mips-millones-de-instrucciones-por-segundo]] · [[mejor-medida-de-rendimiento-de-un-computador]]
