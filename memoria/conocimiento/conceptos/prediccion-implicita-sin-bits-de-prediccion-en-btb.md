---
tipo: "concepto"
titulo: "Predicción implícita sin bits de predicción en BTB"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["predicción implícita", "bit único", "BTB", "tomado", "no tomado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

Esquema de predicción simplificado que no requiere bits de predicción explícitos:
- Si la instrucción de salto tiene entrada en la BTB → se predice TOMADO.
- Si no tiene entrada en la BTB → se predice NO TOMADO.
Solo se pueden predecir saltos que ya están en la BTB; los nuevos saltos se asumen no tomados hasta que se insertan tras su primera ejecución.

> Predicción implícita (sin bits de predicción) Aplicable con un único bit de predicción – si la instrucción de salto está en la BTB, el salto se predice como tomado – si la instrucción de salto no está en la BTB, el salto se predice como no tomado
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
