---
tipo: "dato"
titulo: "Inicialización del selector y bits de predicción en predictor híbrido"
temas: ["ac", "prediccion-saltos"]
claves: ["inicialización", "selector=1", "bits predicción=1"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Tanto el selector (contador de 2 bits) como los bits de predicción de ambos predictores comienzan con valor 1. Esto implica que inicialmente el selector está en el punto medio (1 de 0-3), por lo que Predictor 2 se usaría primero (ya que selector < 2).

> Selector and prediction bits are initialized to 1.
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[selector-de-2-bits-para-predictor-hibrido-de-saltos]]
