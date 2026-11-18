---
tipo: "concepto"
titulo: "Predictores n bits y optimalidad de n=2 en la práctica"
temas: ["ac", "arquitectura-computadores", "contador-saturado", "prediccion-saltos"]
claves: ["predictor n bits", "contador saturado", "n=2 óptimo", "decrementa no salto", "predice no salto si cuenta < 2^(n-1)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[contador-saturado]] · [[prediccion-saltos]]

La generalización usa un contador saturado de n bits por salto. El contador decrementa cuando el salto no se toma. La predicción es "no saltar" si el valor del contador es menor que 2^(n-1) (es decir, el bit más significativo es 0). Sin embargo, en la práctica n=2 ofrece el mejor equilibrio: predictores con n>2 no mejoran la precisión y aumentan el coste de hardware y latencia.

> Generalización: predictor n bits • Hace uso de un contador saturado por salto • Decrementa cuando no salta • Predice no saltar si cuenta < 2n-1 • En la práctica, n=2 es tan efectivo como n>2 o incluso mejor
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[predictor-dinamico-de-un-bit-funcionamiento-y-limitacion-en]] · [[como-el-predictor-de-2-bits-resuelve-el-problema-de-bucles-a]] · [[predictor-dinamico-de-2-bits-jim-smith-1981-maquina-de-4-est]]
