---
tipo: "receta"
titulo: "Ejemplo comparativo predictores 1 bit vs 2 bits vs correlacionado (1,1) con código if(d==0)/if(d==1)"
temas: ["ac", "arquitectura-computadores", "ejemplo-comparativo", "prediccion-saltos", "tasas-fallo"]
claves: ["predictor 1 bit 100% fallos", "predictor 2 bits 50% fallos", "predictor correlacionado (1", "1)", "d alterna 2 y 0", "b1 b2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[ejemplo-comparativo]] · [[prediccion-saltos]] · [[tasas-fallo]]

Código: if(d==0) {d=1;} if(d==1) {...} con d alternando 2 y 0. Comportamiento real: d=2 → b1:T, b2:T; d=0 → b1:NT, b2:NT. a) Predictor 1 bit por salto (inicial NT): d=2 predice (NT,NT) → falla ambos; actualiza a (T,T). d=0 predice (T,T) → falla ambos; actualiza a (NT,NT). Ciclo infinito: 100% fallos. b) Predictor 2 bits por salto (inicial NT=01): d=2 predice (NT,NT) → falla ambos; b1 pasa a DT(10), b2 a DT(10). d=0 predice (T,T) → falla b1 (pasa a NT), acierta b2 (pasa a NT). Siguiente d=2: predice (NT,NT) → falla b1 (pasa a DT), acierta b2 (pasa a DT). Patrón: 50% fallos (solo falla el primer salto de cada par). c) Predictor (1,1): BHR 1 bit selecciona entre 2 BHTs de 1 bit. La historia del salto anterior (b1) permite predecir b2 correctamente tras calentamiento.

> a) Predictor de un bit para cada salto inicializado a NT  100% de fallos • b) Predictor de 2 bits para cada salto inicializado a NT  50% de fallos • c) Predictor correlacionado (1,1) • Implementación más simple: predictor (1,1):  1 bit en la BHR, que selecciona la BHT  2 tablas BHT de 1 bit
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[como-el-predictor-de-2-bits-resuelve-el-problema-de-bucles-a]]
