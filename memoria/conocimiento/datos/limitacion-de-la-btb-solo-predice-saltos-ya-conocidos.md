---
tipo: "dato"
titulo: "Limitación de la BTB: solo predice saltos ya conocidos"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["BTB", "predicción", "saltos conocidos", "limitación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

La BTB solo puede predecir saltos que ya tienen una entrada en el buffer. Los saltos que se ejecutan por primera vez (cold start) no están en la BTB y, bajo predicción implícita, se predicen como no tomados. Esto causa fallos de predicción en la primera ejecución de cada salto.

> Sólo se pueden predecir aquellas instrucciones de salto que están en la BTB
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[prediccion-implicita-sin-bits-de-prediccion-en-btb]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]]
