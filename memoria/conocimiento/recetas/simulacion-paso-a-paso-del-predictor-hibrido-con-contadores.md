---
tipo: "receta"
titulo: "Simulación paso a paso del predictor híbrido con contadores selectores"
temas: ["ac", "hybrid predictor", "prediccion-saltos", "simulation"]
claves: ["predictor simulation", "1-bit predictor", "2-bit predictor", "selector counter", "saturating counter", "hit/miss"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[hybrid predictor]] · [[prediccion-saltos]] · [[simulation]]

Algoritmo de simulación para cada ejecución dinámica de salto (B1 o B2):
1. **Leer estado actual**:
   - P1[salto] ∈ {0,1} (predicción: 0=NT, 1=T)
   - P2[salto] ∈ {00,01,10,11} (predicción: 00/01=NT, 10/11=T)
   - Counter[salto] ∈ {00,01,10,11} (selector: MSB=1 → usa P1; MSB=0 → usa P2)
2. **Determinar predictor usado**: `used = P1 si Counter[MSB]==1 else P2`.
3. **Predicción del predictor usado**: `pred = predicción(used)`.
4. **Outcome real** (del trazo de ejecución): `actual ∈ {T, NT}`.
5. **Hit/Miss de cada predictor**:
   - `hit1 = (predicción(P1) == actual)`
   - `hit2 = (predicción(P2) == actual)`
6. **Actualizar P1**: si `actual==T` → P1=1; else P1=0.
7. **Actualizar P2**: saturating 2-bit: si `actual==T` → incrementa (max 11); else decrementa (min 00).
8. **Actualizar Counter** según tabla:
   - hit1 ∧ hit2 → sin cambio.
   - hit1 ∧ ¬hit2 → Counter = saturating_increment(Counter).
   - ¬hit1 ∧ hit2 → Counter = saturating_decrement(Counter).
   - ¬hit1 ∧ ¬hit2 → sin cambio.
9. **Registrar**: salto, outcome, predictor usado, predicted outcome (T/NT), hit/miss del usado, nuevos estados P1, P2, Counter.
10. **Repetir** para siguiente ejecución dinámica del mismo u otro salto.

Estado inicial dado en examen:
- Counter: B1=00, B2=00 (MSB=0 → empiezan con P2).
- P1: B1=0 (NT), B2=0 (NT).
- P2: B1=11 (T), B2=11 (T).

> After each prediction, apart from updating both predictors, the corresponding counter must be updated according to the next table: Predictor 1 behavior Hit, Predictor 2 behavior Hit → The counter value does not change; Predictor 1 behavior Hit, Predictor 2 behavior Miss → Increment the counter (+1); Predictor 1 behavior Miss, Predictor 2 behavior Hit → Decrement the counter (-1); Predictor 1 behavior Miss, Predictor 2 behavior Miss → The counter value does not change
> — `repo:datos/temarios/AC/examenes/January2020.pdf` (cita sin comprobar)

Relacionado: [[predictor-hibrido-con-selectores-por-salto-1-bit-vs-2-bit-y]] · [[resultados-reales-de-saltos-b1-y-b2-en-bucles-anidados-con-r]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
