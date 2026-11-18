---
tipo: "concepto"
titulo: "Predictor gselect: índice mediante XOR de bits de PC y BHR"
temas: ["ac", "prediccion-saltos"]
claves: ["gselect", "XOR", "PC", "BHR", "índice", "BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

El predictor gselect (global select) combina información global (BHR) y local (bits del PC) mediante XOR para indexar la tabla de patrones (BHT). Esto reduce aliasing frente a usar solo BHR (ghistory) o solo PC.

> El predictor gselect indexa la BHT con los bits que resultan de: c) XOR de algunos bits del PC y BHR
> — `repo:datos/temarios/AC/examenes/Junio2016.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[predictor-gselect-indexa-bht-con-xor-de-bits-de-pc-y-bhr]] · [[predictor-gselect-concatenacion-vs-gshare-xor-para-indexar-b]] · [[seleccion-de-entrada-en-bht-branch-history-table]]
