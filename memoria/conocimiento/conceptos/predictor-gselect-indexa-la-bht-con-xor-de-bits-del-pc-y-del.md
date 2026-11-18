---
tipo: "concepto"
titulo: "Predictor gselect indexa la BHT con XOR de bits del PC y del BHR"
temas: ["ac", "gselect", "prediccion-saltos"]
claves: ["gselect", "BHT", "BHR", "XOR", "predictor correlacionado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[gselect]] · [[prediccion-saltos]]

El predictor gselect (global select) combina el historial global de saltos (BHR) con bits del PC mediante una operación XOR para indexar la tabla de patrones (BHT). Esto permite distinguir contextos de salto diferentes que compartan el mismo historial global.

> El predictor gselect indexa la BHT con los bits que resultan de: a) AND de algunos bits del PC y BHR b) XOR de algunos bits del PC y BHR c) Concatenar algunos bits de PC y BHR d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
