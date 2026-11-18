---
tipo: "concepto"
titulo: "Predictor correlacionado general mejora a predictores no correlacionados"
temas: ["ac", "correlacionado", "prediccion-saltos"]
claves: ["predictor correlacionado", "mispredicciones", "benchmarks SPEC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[correlacionado]] · [[prediccion-saltos]]

En la gráfica de la página 39 se comparan tres predictores con 4,096 entradas (2 bits/entrada): predictor no correlacionado, predictor no correlacionado con capacidad infinita, y predictor correlacionado. Este último reduce consistentemente la frecuencia de mispredicciones (6% frente a 11-18%) en benchmarks como doduc, gcc, nasa7, eqntott, espresso, spice, fpppp, tomcatv, li y matrix300. La cita literal "El predictor correlacionado mejora a los otros dos predictores" resume la conclusión experimental.

> El predictor correlacionado mejora a los otros dos predictores
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[ejemplo-comparativo-predictores-1-bit-vs-2-bits-vs-correlaci]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]] · [[calculo-de-speedup-comparando-predictor-con-penalidad-variab]]
