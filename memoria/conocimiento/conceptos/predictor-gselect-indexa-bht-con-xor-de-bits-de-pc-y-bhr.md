---
tipo: "concepto"
titulo: "Predictor gselect indexa BHT con XOR de bits de PC y BHR"
temas: ["ac", "bht", "gselect", "prediccion-saltos"]
claves: ["gselect", "predictor", "BHT", "XOR", "PC", "BHR", "indexado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[gselect]] · [[prediccion-saltos]]

El predictor **gselect** (global selection) combina historia global (BHR) y bits del PC mediante **XOR** para indexar la tabla de patrones (BHT/PHT). Opción correcta: b) XOR de algunos bits del PC y BHR. A diferencia de gshare (que usa XOR del PC con BHR completo), gselect usa solo una parte del PC.

> El predictor gselect indexa la BHT con los bits que resultan de:
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
