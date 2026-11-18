---
tipo: "receta"
titulo: "Fórmula del tiempo de ejecución de CPU y sus tres factores"
temas: ["ac", "cpi", "cpu-time", "frecuencia-reloj", "rendimiento"]
claves: ["tiempo de ejecución", "CPU time", "instrucciones", "CPI", "ciclos por instrucción", "duración ciclo reloj", "frecuencia reloj"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[cpu-time]] · [[frecuencia-reloj]] · [[rendimiento]]

**Tiempo de ejecución CPU** = Instrucciones × CPI × Duración ciclo reloj
- **Instrucciones**: depende del compilador y de la ISA; una ISA más rica reduce el número de instrucciones.
- **CPI** (Ciclos Por Instrucción promedio): depende de la ISA y la organización de la CPU; una ISA más simple o una organización más elaborada reducen el CPI. Para *n* tipos de instrucción: Σ(CPIᵢ × NIᵢ).
- **Duración ciclo reloj** (o 1/frecuencia): depende de la organización y tecnología; organización sencilla → período menor.
Esta descomposición permite analizar *trade-offs*: p. ej., añadir instrucciones complejas reduce "Instrucciones" pero puede subir CPI y duración de ciclo.

> 𝑡𝑒𝑗𝑒𝑐𝑢𝑐𝑖ó𝑛 = 𝑛ú𝑚𝑒𝑟𝑜 𝑑𝑒 𝑖𝑛𝑠𝑡𝑟𝑢𝑐𝑐𝑖𝑜𝑛𝑒𝑠 × 𝐶𝑃𝐼 × 𝑑𝑢𝑟𝑎𝑐𝑖ó𝑛 𝑑𝑒𝑙 𝑐𝑖𝑐𝑙𝑜 𝑑𝑒 𝑟𝑒𝑙𝑜𝑗
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1 2026-27.pdf`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[definicion-de-mflops-millones-de-operaciones-de-punto-flotan]] · [[ecuacion-fundamental-del-tiempo-de-ejecucion-en-arquitectura]] · [[calculo-de-tiempo-de-ejecucion-con-cpi-y-frecuencia]] · [[como-calcular-ciclos-de-reloj-de-cpu-a-partir-de-instruccion]]
