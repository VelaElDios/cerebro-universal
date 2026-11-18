---
tipo: "receta"
titulo: "Análisis en estado estable de predictor 2 bits vs correlacionado (1,1) para bucle RISC-V con patrón complejo"
temas: ["ac", "estado-estable", "prediccion-saltos", "predictor-2-bits", "predictor-correlacionado", "risc-v"]
claves: ["B1", "B2", "B3", "bucle while(1)", "secuencia a/b", "predictor 2 bits", "predictor (1", "1)", "historia global 1 bit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[estado-estable]] · [[prediccion-saltos]] · [[predictor-2-bits]] · [[predictor-correlacionado]] · [[risc-v]]

El código alterna a y b. Iteración 1: a=1->0 (B1 NT, B2 T, B3 T), Iteración 2: a=0->1 (B1 T, B2 NT, B3 NT). Patrón de 2 iteraciones. Predictor 2 bits por salto (local): cada salto ve patrón periódico. B1: NT, T, NT, T... -> predictor 2 bits oscila entre 01 y 10, falla siempre en cambios? Ver simulación. Predictor (1,1): usa 1 bit de historia global para indexar BHT de 2 entradas. Historia global = resultado salto anterior. Simular transiciones de estado en estado estable (tras calentamiento). Contar aciertos por iteración completa (3 saltos).

> Indica cuál es el rendimiento de un predictor de saltos de 2 bits, en términos de predicciones correctas por iteración, cuando la ejecución de este código se encuentra en un estado estable. b) Indica cuál es el rendimiento de un predictor de saltos correlacionado (1,1), en términos de predicciones correctas por iteración, cuando la ejecución de este código se encuentra en un estado estable.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[predictor-de-2-bits-por-instruccion-y-predictor-correlaciona]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]] · [[predictor-correlacionado-2-1-para-bucle-de-conteo-de-caracte]]
