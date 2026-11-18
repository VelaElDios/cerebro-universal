---
tipo: "concepto"
titulo: "Punto de inflexión (knee) del modelo Roofline mononúcleo"
temas: ["ac", "rendimiento", "roofline"]
claves: ["punto de inflexión", "intensidad aritmética", "techo de cómputo", "ancho de banda memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[rendimiento]] · [[roofline]]

El **punto de inflexión (knee)** del Roofline es la intensidad aritmética 𝐼ₖ donde la recta de ancho de banda (pendiente = BW máximo) intersecta el techo plano de cómputo (peak FLOPs/s). Fórmula: 𝐼ₖ = Peak_GFLOPs/s ÷ Peak_GB/s. A la izquierda del knee: **memory-bound** (rendimiento limitado por BW); a la derecha: **compute-bound** (limitado por peak FLOPs/s).

> El punto de inflexión es el valor de Intensidad Aritmética (𝐼𝐼𝑘𝑘𝑘𝑘𝑘𝑘𝑘𝑘 ) en el Eje X donde la pendiente del ancho de banda de la memoria se cruza con la meseta horizontal del techo de la CPU. Se calcula dividiendo el Techo de Cómputo entre el Ancho de Banda de la Memoria: 𝐼𝐼𝑘𝑘𝑘𝑘𝑘𝑘𝑘𝑘 = Techo de Cómputo Máximo (GFLOPs/s) / Ancho de Banda de la Memoria Máximo (GB/s)
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf` (cita sin comprobar)

Relacionado: [[formula-del-techo-roofline-mononucleo]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[punto-de-inflexion-knee-del-modelo-roofline-i-knee-gflops-ma]] · [[punto-de-inflexion-ridge-point-en-el-modelo-roofline]]
