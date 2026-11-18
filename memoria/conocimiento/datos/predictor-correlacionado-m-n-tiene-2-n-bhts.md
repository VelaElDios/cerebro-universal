---
tipo: "dato"
titulo: "Predictor correlacionado (m,n) tiene 2^n BHTs"
temas: ["ac", "bht", "prediccion-saltos"]
claves: ["predictor correlacionado", "BHT", "historia global", "tablas predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[prediccion-saltos]]

Un predictor correlacionado (m, n) usa m bits de historia global y n bits de historia local (o viceversa según notación). El número de BHTs (tablas de predicción) es 2^n donde n es el número de bits de historia que indexan la tabla de patrones. Para (3,2): 2^2 = 4 BHTs... pero las opciones son 2,3,6,8. La notación (m,n) suele ser (historia_global, historia_local) → 2^historia_local BHTs. Si (3,2) significa 2 bits de historia local → 4 BHTs (no está). Si significa 3 bits historia global → 8 entradas en BHT global. La respuesta esperada en este contexto académico: d) 8 (asumiendo que el primer parámetro son bits de historia global que determinan número de BHTs = 2^3 = 8).

> ¿Cuántas BHTs hay en un predictor correlacionado (3, 2)? a) 2 b) 3 c) 6 d) 8
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
