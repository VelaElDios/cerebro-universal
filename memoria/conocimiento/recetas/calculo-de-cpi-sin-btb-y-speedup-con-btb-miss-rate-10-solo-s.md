---
tipo: "receta"
titulo: "Cálculo de CPI sin BTB y speedup con BTB (miss rate 10%, solo saltos tomados, actualización con penalidad)"
temas: ["ac", "btb", "cpi", "prediccion-saltos", "speedup"]
claves: ["CPI sin BTB", "mejora prestaciones BTB", "miss rate 10%", "saltos condicionales 25% (75% tomados)", "incondicionales 8%", "penalidad actualizacion 1 ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[btb]] · [[cpi]] · [[prediccion-saltos]] · [[speedup]]

Sin BTB: Penalidad por salto tomado = ciclos perdidos. Dirección fin ID, sentido fin EX. Si se fetchea secuencial, al detectar tomado en EX, se flush IF, ID (2 burbujas). Penalidad = 2 ciclos por salto tomado. Frecuencia saltos tomados = condicionales_tomados + incondicionales = 0.25*0.75 + 0.08 = 0.1875 + 0.08 = 0.2675 (26.75% instrucciones). CPI = 1 + 0.2675 * 2 = 1.535. Con BTB: Miss rate 10% (solo en saltos tomados, pues BTB solo guarda tomados). Hit 90%: 0 penalidad. Miss 10%: 1 ciclo penalidad (actualización en MEM/EX). Además, si hit pero condicional no tomado: elimina entrada, 0 penalidad. CPI_con = 1 + (freq_saltos_tomados * miss_rate * 1) = 1 + 0.2675 * 0.1 = 1.02675. Speedup = 1.535 / 1.02675 ≈ 1.495.

> a) Calcula el CPI del sistema sin BTB b) ¿Cuál es la mejora de prestaciones al usar la BTB?
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[evaluacion-de-rendimiento-de-btb-con-politica-de-solo-saltos]] · [[mejora-prestaciones-btb-con-politica-solo-saltos-tomados-y-a]] · [[calculo-de-cpi-con-btb-que-almacena-solo-saltos-tomados-y-pr]]
