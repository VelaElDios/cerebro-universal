---
tipo: "concepto"
titulo: "Predictor híbrido con selectores por salto (1-bit vs 2-bit) y contadores de 2 bits saturados"
temas: ["ac", "hybrid predictor", "prediccion-saltos"]
claves: ["hybrid predictor", "local predictor", "1-bit predictor", "2-bit saturating counter", "selector counter", "Predictor 1", "Predictor 2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[hybrid predictor]] · [[prediccion-saltos]]

Mecánica del predictor híbrido del examen:
- **Predictor 1 (P1)**: 1 bit por salto (B1, B2). Valor 0 = not taken, 1 = taken. Se actualiza con el resultado real: si taken → 1, si not taken → 0.
- **Predictor 2 (P2)**: 2 bits saturados por salto (estados 00, 01, 10, 11). 00/01 = not taken, 10/11 = taken. Se actualiza como predictor de 2 bits estándar: taken → incrementa (saturando en 11), not taken → decrementa (saturando en 00).
- **Tabla Counters (selectores)**: 2 bits saturados por salto. MSB=1 → usa P1; MSB=0 → usa P2.
- **Actualización de Counters tras cada predicción** (según tabla del enunciado):
  - P1 Hit, P2 Hit → contador no cambia.
  - P1 Hit, P2 Miss → contador +1 (incrementa).
  - P1 Miss, P2 Hit → contador -1 (decrementa).
  - P1 Miss, P2 Miss → contador no cambia.
- **Estado inicial dado**: Counters B1=00, B2=00 (MSB=0 → empiezan usando P2). P1: B1=0, B2=0. P2: B1=11, B2=11 (ambos predicen taken inicialmente).
- **Simulación**: para cada ejecución de salto (en orden dinámico), se mira outcome real, se evalúa hit/miss de P1 y P2, se actualiza el predictor usado y el otro, y se actualiza el Counter según la regla. El predictor usado para la siguiente vez que aparezca ese salto depende del nuevo MSB del Counter.

> Detail the behavior of a hybrid predictor combining two local predictors (called Predictor 1 and Predictor 2). Predictor 1 associates a 1-bit predictor to each branch instruction (B1 and B2) and Predictor 2 associates a 2-bit predictor to each branch. To select the predictor to employ in each case there is a table (called Counters) storing a 2-bit saturating counter for each branch. If the most-significant bit of the counter is 1, then Predictor 1 is selected; otherwise, Predictor 2 is selected.
> — `repo:datos/temarios/AC/examenes/January2020.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]] · [[ejecucion-multicamino-multi-path-execution-como-alternativa]] · [[predictor-hibrido-con-selector-de-2-bits-entre-predictor-de]] · [[simulacion-paso-a-paso-del-predictor-hibrido-con-contadores]] · [[predictor-hibrido-de-saltos-con-selectores-de-2-bits-entre-p]]
