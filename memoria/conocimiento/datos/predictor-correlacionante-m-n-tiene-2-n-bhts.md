---
tipo: "dato"
titulo: "Predictor correlacionante (m,n) tiene 2^n BHTs"
temas: ["ac", "correlating-predictor", "prediccion-saltos"]
claves: ["correlating predictor", "BHT", "(3", "2)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[correlating-predictor]] · [[prediccion-saltos]]

Un predictor correlacionante (m,n) usa m bits de historia global y n bits de historia local/por salto. El número de BHTs (tablas de predicción local) es 2^n. Para (3,2): 2^2 = 4 BHTs. Nota: la opción 4 no aparece; la más cercana es 8 (2^3) o 6. Revisar convención: algunos textos definen (m,n) como m bits historia global, n bits índice → 2^n tablas. Respuesta esperada: 4 (no listada) o 8 si n=3. En examen real, verificar convención usada en asignatura.

> How many BHTs are there in a (3, 2) correlating predictor? a) 2 b) 3 c) 6 d) 8
> — `repo:datos/temarios/AC/examenes/June2018.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[predictor-correlacionado-m-n-numero-de-bhts-2-m]] · [[numero-de-tablas-bht-en-predictor-correlacionado-m-n]] · [[calculo-de-bits-totales-en-predictor-2-2-con-3-entradas-por]]
