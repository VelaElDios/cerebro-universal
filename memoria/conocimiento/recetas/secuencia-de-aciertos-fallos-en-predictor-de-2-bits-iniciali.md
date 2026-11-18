---
tipo: "receta"
titulo: "Secuencia de aciertos/fallos en predictor de 2 bits inicializado a strongly not taken"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor 2 bits", "strongly not taken", "BNEZ", "historial"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Estados: 00=strongly NT, 01=weakly NT, 10=weakly T, 11=strongly T. Bucle: R2=6, decrementa cada iteración, salto tomado mientras R2≠0 → 5 tomados, 1 no tomado. Transiciones: 1º T (pred NT)→M (01), 2º T (pred NT)→M (10), 3º T (pred T)→H (11), 4º T→H, 5º T→H, 6º NT (pred T)→M. Secuencia: MMHHHM.

> We have a one level 2-bit branch predictor initialized to strongly not taken. Indicate the correct sequence of hits (H) and misses (M) for B1 in the next code:
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[secuencia-de-aciertos-fallos-en-predictor-2-bits-inicializad]] · [[secuencia-h-m-para-predictor-2-bit-debilmente-no-tomado-en-b]] · [[predictor-de-1-bit-en-bucle-de-3-iteraciones-t-t-nt-produce]]
