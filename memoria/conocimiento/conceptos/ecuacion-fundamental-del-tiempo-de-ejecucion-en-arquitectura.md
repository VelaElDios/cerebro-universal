---
tipo: "concepto"
titulo: "Ecuación fundamental del tiempo de ejecución en arquitectura de computadores"
temas: ["ac", "arquitectura-computadores", "rendimiento"]
claves: ["tiempo de ejecución", "CPI", "frecuencia reloj", "instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[rendimiento]]

La ecuación fundamental relaciona el tiempo de ejecución de un programa con tres factores: número de instrucciones ejecutadas (IC), ciclos por instrucción promedio (CPI) y duración del ciclo de reloj (1/frecuencia). Es la base para cualquier análisis de rendimiento y optimización: reducir cualquiera de los tres factores mejora el tiempo total. Se usa para comparar arquitecturas, evaluar optimizaciones de compilador y estimar speedup teórico.

> 𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 𝑑𝑑𝑑𝑑 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒ó𝑛𝑛 = 𝑛𝑛ú𝑚𝑚𝑚𝑚𝑚𝑚𝑚𝑚 𝑑𝑑𝑑𝑑 𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖𝑖 × 𝐶𝐶𝐶𝐶𝐶𝐶 × 𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑ó𝑛 𝑑𝑑𝑑𝑑 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑑𝑑𝑑𝑑 𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟
> — `repo:datos/temarios/AC/Tema1-Introduccion/Formulas.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[formula-del-techo-roofline-mononucleo]]
